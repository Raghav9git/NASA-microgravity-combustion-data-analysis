# Local Setup (Windows + Git Bash / VS Code)

## 1. Open the repository folder
Open this folder in VS Code. Use the terminal at the repository root (the folder containing README.md).

## 2. Choose a compatible Python version
Python 3.14 is very recent and some packages may not have pre-built wheels for it.
Use an older stable version for the virtual environment.

Check installed versions in PowerShell:
```powershell
py -0p
```

### Currently available (as of initial audit)
| Version | Status |
|---------|--------|
| 3.14.2  | Default — too new for reliable package support |
| 3.11    | Recommended — stable, all packages have binary wheels |

### Create the virtual environment
From PowerShell at the repository root:
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

Or from Git Bash:
```bash
py -3.11 -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

If Python 3.11 is not installed, download it from https://www.python.org/downloads/ and reopen the terminal.

## 3. Start the backend
With `.venv` activated, from the repository root:
```bash
cd backend
uvicorn app.main:app --reload
```

Open in your browser:
- http://127.0.0.1:8000/ — should return `{"message": "Backend is running"}`
- http://127.0.0.1:8000/health — should return `{"status": "ok"}`
- http://127.0.0.1:8000/docs — interactive Swagger UI

## 4. Run tests
Stop the server with Ctrl+C. From the repository root:
```bash
python -m pytest backend/tests -q
```

Expected output: `2 passed`.

## 5. Environment variables
Copy `.env.example` to `.env` and edit as needed:
```bash
cp .env.example .env
```

## Notes
- SQLite is used only to make the initial setup test easy. PostgreSQL will be configured later.
- No NASA data, trained ML model, AI assistant, or frontend is included yet.
- Do not commit .env files, local databases, large datasets, or model artifacts.
- `backend/conftest.py` ensures test imports resolve correctly from any working directory.
