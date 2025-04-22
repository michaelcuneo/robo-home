
import json
from pathlib import Path

# Get the path to the config file
CONFIG_PATH = Path(__file__).resolve().parent.parent / 'config.json'

# Load the config once
with open(CONFIG_PATH, 'r') as f:
    _config = json.load(f)

get_config = lambda: _config