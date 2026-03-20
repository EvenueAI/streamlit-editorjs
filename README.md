
# How to run it

From the project root:

```bash
python3.13 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\Activate.ps1  # Windows PowerShell
pip install --upgrade pip
pip install -r requirements.txt
```

```bash
pip install -e .
cd streamlit_editorjs/frontend
npm install
npm run build
cd ../..
streamlit run app.py
```
