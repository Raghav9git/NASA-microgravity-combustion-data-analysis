"""
Root conftest for the backend test suite.

Adds the backend/ directory to sys.path so that
'from app.main import app' resolves correctly
regardless of which directory pytest is invoked from.
"""
import sys
from pathlib import Path

# Ensure backend/ is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))
