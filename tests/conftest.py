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

    with ZipFile(archive, "a") as zip_file:
        zip_file.write(os.path.join(TMP_DIR, 'file_csv.csv'), arcname='file_csv.csv')
        zip_file.write(os.path.join(TMP_DIR, 'file_pdf.pdf'), arcname='file_pdf.pdf')
        zip_file.write(os.path.join(TMP_DIR, 'file_xlsx.xlsx'), arcname='file_xlsx.xlsx')

    yield

    shutil.rmtree(RESOURCE_DIR)
