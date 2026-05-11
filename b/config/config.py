import json
from pathlib import Path


_app_config_path = Path(__file__).parent / 'app.json'


APP_CONFIG = json.load(open(_app_config_path, 'r'))
DATABASE_PATH = Path(__file__).parent.parent / APP_CONFIG['db']['db_path']


