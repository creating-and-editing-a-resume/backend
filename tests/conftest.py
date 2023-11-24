import pytest
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
root_dir_content = os.listdir(BASE_DIR)

PROJECT_DIR_NAME = 'creating_and_editing_a_resume'

MANAGE_PATH = os.path.join(BASE_DIR, PROJECT_DIR_NAME)
project_dir_content = os.listdir(MANAGE_PATH)
FILENAME = 'manage.py'

pytest_plugins = [
    'tests.fixtures.fixture_user',
]

@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()
