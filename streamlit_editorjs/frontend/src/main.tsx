import ReactDOM from "react-dom/client";
import EditorComponent from "./EditorComponent";

// No StrictMode: its dev double-mount creates the editor twice, leaving a
// stray empty block behind.
ReactDOM.createRoot(document.getElementById("root")!).render(<EditorComponent />);