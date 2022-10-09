import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("COFFEE_ROOT", "~/.coffee/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("COFFEE_KEYS_ROOT", "~/.coffee_keys"))).resolve()
