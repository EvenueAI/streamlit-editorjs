type StreamlitRenderData = {
  args: Record<string, any>;
  disabled?: boolean;
  theme?: Record<string, any>;
};

const COMPONENT_READY = "streamlit:componentReady";
const SET_COMPONENT_VALUE = "streamlit:setComponentValue";
const SET_FRAME_HEIGHT = "streamlit:setFrameHeight";
const RENDER_EVENT = "streamlit:render";
const API_VERSION = 1;

function postToParent(message: Record<string, any>): void {
  window.parent.postMessage(
    {
      isStreamlitMessage: true,
      ...message,
    },
    "*"
  );
}

export function initStreamlit(
  onRender: (data: StreamlitRenderData) => void
): void {
  window.addEventListener("message", (event: MessageEvent<StreamlitRenderData>) => {
    if (!event.data || event.data.type !== RENDER_EVENT) {
      return;
    }

    onRender(event.data);
  });

  postToParent({
    type: COMPONENT_READY,
    apiVersion: API_VERSION,
  });
  setFrameHeight();
}

export function setComponentValue(value: any): void {
  postToParent({
    type: SET_COMPONENT_VALUE,
    value,
  });
}

export function setFrameHeight(height?: number): void {
  postToParent({
    type: SET_FRAME_HEIGHT,
    height: height ?? document.body.scrollHeight,
  });
}
