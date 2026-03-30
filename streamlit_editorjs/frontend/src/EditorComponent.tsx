import React, { useEffect, useRef, useState } from "react";
import EditorJS, { OutputData } from "@editorjs/editorjs";
import Header from "@editorjs/header";
import List from "@editorjs/list";
import Quote from "@editorjs/quote";
import { initStreamlit, setComponentValue, setFrameHeight } from "./streamlit";

type RenderArgs = {
  value?: OutputData;
  height?: number;
  placeholder?: string;
  read_only?: boolean;
  tools?: Record<string, any>;
  debounce_ms?: number;
};

function stableStringify(obj: unknown): string {
  return JSON.stringify(obj);
}

const DEFAULT_DOC: OutputData = {
  time: 0,
  blocks: [],
  version: "2.30.0",
};

function buildTools(customTools: Record<string, any> = {}): Record<string, any> {
  return {
    header: {
      class: Header,
      inlineToolbar: true,
      config: {
        levels: [2, 3, 4],
        defaultLevel: 2,
      },
      ...customTools.header,
    },
    list: {
      class: List,
      inlineToolbar: true,
      ...customTools.list,
    },
    quote: {
      class: Quote,
      inlineToolbar: true,
      ...customTools.quote,
    },
    ...customTools,
  };
}

export default function EditorComponent() {
  const editorRef = useRef<EditorJS | null>(null);
  const holderRef = useRef<HTMLDivElement | null>(null);
  const debounceRef = useRef<number | null>(null);
  const lastSentRef = useRef<string>("");
  const lastLoadedRef = useRef<string>("");
  const initializedRef = useRef<boolean>(false);

  const [args, setArgs] = useState<RenderArgs>({
    value: DEFAULT_DOC,
    height: 500,
    placeholder: "Start writing...",
    read_only: false,
    tools: {},
    debounce_ms: 500,
  });
  const toolsSignature = stableStringify(args.tools ?? {});

  useEffect(() => {
    initStreamlit((data) => {
      const nextArgs = data.args as RenderArgs;
      setArgs({
        value: nextArgs.value ?? DEFAULT_DOC,
        height: nextArgs.height ?? 500,
        placeholder: nextArgs.placeholder ?? "Start writing...",
        read_only: nextArgs.read_only ?? false,
        tools: nextArgs.tools ?? {},
        debounce_ms: nextArgs.debounce_ms ?? 500,
      });
    });
  }, []);

  useEffect(() => {
    if (!holderRef.current || initializedRef.current) {
      return;
    }

    const initialDoc = args.value ?? DEFAULT_DOC;
    lastLoadedRef.current = stableStringify(initialDoc);
    const mergedTools = buildTools(args.tools);

    const editor = new EditorJS({
      holder: holderRef.current,
      readOnly: !!args.read_only,
      data: initialDoc,
      tools: mergedTools,
      async onReady() {
        setTimeout(() => setFrameHeight(), 50);
      },
      async onChange() {
        if (!editorRef.current) return;

        if (debounceRef.current) {
          window.clearTimeout(debounceRef.current);
        }

        debounceRef.current = window.setTimeout(async () => {
          try {
            const saved = await editorRef.current!.save();
            const serialized = stableStringify(saved);

            if (serialized !== lastSentRef.current) {
              lastSentRef.current = serialized;
              setComponentValue(saved);
              setTimeout(() => setFrameHeight(), 10);
            }
          } catch (error) {
            console.error("Editor save failed", error);
          }
        }, args.debounce_ms ?? 500);
      },
    });

    editorRef.current = editor;
    initializedRef.current = true;

    return () => {
      if (debounceRef.current) {
        window.clearTimeout(debounceRef.current);
      }
      if (editorRef.current && typeof editorRef.current.destroy === "function") {
        editorRef.current.destroy();
      }
      editorRef.current = null;
      initializedRef.current = false;
    };
  }, [args.debounce_ms, args.placeholder, args.read_only, toolsSignature]);

  useEffect(() => {
    const incoming = args.value ?? DEFAULT_DOC;
    const incomingSerialized = stableStringify(incoming);

    if (!editorRef.current) return;
    if (incomingSerialized === lastLoadedRef.current) return;
    if (incomingSerialized === lastSentRef.current) return;

    const reload = async () => {
      try {
        await editorRef.current!.isReady;
        await editorRef.current!.render(incoming);
        lastLoadedRef.current = incomingSerialized;
        setTimeout(() => setFrameHeight(), 20);
      } catch (error) {
        console.error("Editor render failed", error);
      }
    };

    reload();
  }, [args.value]);

  return (
    <div
      style={{
        minHeight: `${args.height ?? 500}px`,
        padding: "8px",
        background: "white",
      }}
    >
      <style>{`
        .ce-toolbar__plus {
          display: none;
        }

        .codex-editor .codex-editor__redactor {
          padding-top: 16px !important;
          padding-bottom: 16px !important;
        }

        .codex-editor .ce-block__content,
        .codex-editor .ce-toolbar__content {
          max-width: none;
          margin-left: 32px;
          margin-right: 32px;
        }
      `}</style>
      <div ref={holderRef} className="codex-editor" />
    </div>
  );
}
