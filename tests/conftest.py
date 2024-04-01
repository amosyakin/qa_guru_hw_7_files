import os
import shutil
import pytest
from zipfile import ZipFile


current_file = os.path.abspath(__file__)
PROJECT_DIR = os.path.dirname(os.path.dirname(current_file))
TMP_DIR = os.path.join(PROJECT_DIR, 'temp')
RESOURCE_DIR = os.path.join(PROJECT_DIR, 'resource')
archive = os.path.join(RESOURCE_DIR, 'archive.zip')


@pytest.fixture(scope="session", autouse=True)
def archive_files():
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)

    with ZipFile(archive, "w") as zip_file:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            zip_file.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(RESOURCE_DIR)
