from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_editorjs",
        url="http://localhost:5173",
    )
else:
    build_dir = Path(__file__).parent / "frontend" / "dist"
    _component_func = components.declare_component(
        "streamlit_editorjs",
        path=str(build_dir),
    )


DEFAULT_VALUE = {
    "time": 0,
    "blocks": [],
    "version": "2.30.0",
}


def st_editorjs(
    value: dict[str, Any] | None = None,
    *,
    key: str | None = None,
    height: int = 500,
    placeholder: str = "Start writing...",
    read_only: bool = False,
    tools: dict[str, Any] | None = None,
    debounce_ms: int = 500,
) -> dict[str, Any]:
    """
    Render an Editor.js instance in Streamlit and return the current document JSON.

    Parameters
    ----------
    value:
        Initial or externally controlled Editor.js JSON document.
    key:
        Streamlit widget key.
    height:
        Component height in pixels.
    placeholder:
        Editor placeholder.
    read_only:
        Whether the editor is read-only.
    tools:
        Optional tool configuration to pass through to the frontend.
        Note: the frontend must also have the corresponding JS packages installed.
    debounce_ms:
        Delay before pushing content changes back to Streamlit.

    Returns
    -------
    dict
        Current Editor.js document JSON.
    """
    doc = value if value is not None else DEFAULT_VALUE

    result = _component_func(
        value=doc,
        height=height,
        placeholder=placeholder,
        read_only=read_only,
        tools=tools or {},
        debounce_ms=debounce_ms,
        key=key,
        default=doc,
    )

    if result is None:
        return doc

    if isinstance(result, str):
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return doc

    return result