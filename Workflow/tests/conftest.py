import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Ensure local packages are importable during tests
root_str = str(ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)
