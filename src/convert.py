# Path to the original dataset

import supervisely as sly
import gdown
import os
from dataset_tools.convert import unpack_if_archive
import src.settings as s

def download_dataset():
    archive_path = os.path.join(sly.app.get_data_dir(), 'archive.zip')

    if not os.path.exists(archive_path):
        if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
            gdown.download(s.DOWNLOAD_ORIGINAL_URL, archive_path, quiet=False)
        if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
            for name, url in s.DOWNLOAD_ORIGINAL_URL:
                gdown.download(url, os.path.join(archive_path, name), quiet=False)
    else:
        sly.logger.info(f"Path '{archive_path}' already exists.")
    return unpack_if_archive(archive_path)    


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    raise NotImplementedError(f'Use "Convert YOLO v5 to Supervisely format" app to upload the dataset.')
