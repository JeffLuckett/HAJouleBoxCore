import sys
from pathlib import Path

# Add project root to PYTHONPATH so `adapters` and `hajouleboxcore` can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
