# Final-Project-MLB
> MLB modeling project with a simple Flask app and notebooks.  
> **Target runtime:** Python **3.6.x** (newer Python versions are **not supported** due to upstream deprecations and API changes).

## ✅ What works
- Running the Flask app from `app.py`
- Using the existing pickled models and CSVs in the repo
- Opening notebooks for exploration

> If you use Python 3.7+ you will likely hit import/ABI errors. Please use **Python 3.6.x**.

---

## Setup (Windows 11, Git Bash or PowerShell)

### 1) Clone
```bash
git clone https://github.com/BrianRhodes2018/Final-Project-MLB.git
cd Final-Project-MLB
```

### 2) Create a Python 3.6 environment

#### Option A — Conda (recommended on Windows)
```bash
# create and activate env with Python 3.6
conda create -y -n mlb36 python=3.6
conda activate mlb36
```

#### Option B — System Python 3.6 + venv
If you already have a **Python 3.6** interpreter installed:
```bash
python3.6 -m venv .venv
# PowerShell:
.\.venv\Scriptsctivate
# Git Bash:
source .venv/Scripts/activate
```

### 3) Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> If any legacy wheels fail to build on Windows, install the **Microsoft C++ Build Tools** (Visual Studio Build Tools). Most users won’t need this, but older packages sometimes require it.

---

## Run the app
```bash
python app.py
```
Open your browser to **http://127.0.0.1:5000**.

---

## Project contents (as used today)
```
app.py                  # Flask entrypoint
templates/              # HTML templates
static/                 # CSS/JS/assets
*.ipynb                 # Notebooks
*_model_pickle*         # Pretrained model artifacts (used by the app)
*.csv                   # Data files used by the app/notebooks
Procfile                # (Heroku-style process file; optional)
requirements.txt        # Pinned/legacy deps compatible with Python 3.6
```

---

## Notes & troubleshooting

- **“Module not found” / “ImportError”**  
  Confirm you’re in the **Python 3.6** environment:
  ```bash
  python --version
  # Should print: Python 3.6.x
  ```
- **Build errors on install**  
  - Try `pip install --only-binary=:all: -r requirements.txt` (skips building from source when wheels exist).
  - Ensure 64-bit Python matches 64-bit packages (typical on Windows).
- **Jupyter notebooks**  
  If you want to use notebooks with this env:
  ```bash
  pip install jupyter
  jupyter notebook
  ```

---

## FAQ

**Why 3.6?**  
This code relies on older package versions whose APIs changed in newer releases. Running on 3.7+ often breaks due to deprecations and binary compatibility changes.

**Can I use Docker instead (no code changes)?**  
Yes—if you prefer isolation without modifying the repo, run:
```bash
docker run --rm -it -p 5000:5000 -v "%cd%":/app -w /app python:3.6-slim   /bin/bash -lc "python -m pip install --upgrade pip && pip install -r requirements.txt && python app.py"
```
Then open **http://127.0.0.1:5000**.

---

## License
This project is for personal/educational use. If you plan to publish or share broadly, add a LICENSE file (e.g., MIT).
