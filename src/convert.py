# Path to the original dataset

import os
import re
import xml.etree.ElementTree as ET

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # https://zenodo.org/record/7808269

    # if sly.is_development():
    # load_dotenv("local.env")
    # load_dotenv(os.path.expanduser("~/supervisely.env"))

    # api = sly.Api.from_env()
    # team_id = sly.env.team_id()
    # workspace_id = sly.env.workspace_id()

    # project_name = "Multi-topography dataset for wind turbine detection"
    dataset_path = "APP_DATA/windTurbineDataSet"
    batch_size = 30
    images_ext = ".png"
    bboxes_ext = ".xml"
    ds_name = "ds"

    images_folder = "JPEGImages"
    bboxes_folder = "Annotations"

    def create_ann(image_path):
        labels = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        # img_height = image_np.shape[0]
        # img_wight = image_np.shape[1]

        file_name = get_file_name(image_path)

        ann_path = os.path.join(bboxes_path, file_name + bboxes_ext)

        if file_exists(ann_path):
            tree = ET.parse(ann_path)
            root = tree.getroot()

            img_wight = int(root.find(".//width").text)
            img_height = int(root.find(".//height").text)

            coords_xml = root.findall(".//bndbox")
            for curr_coord in coords_xml:
                left = int(curr_coord[0].text)
                top = int(curr_coord[1].text)
                right = int(curr_coord[2].text)
                bottom = int(curr_coord[3].text)

                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class)
                labels.append(label)

        filename_stem = os.path.basename(image_path).split(".")[0]
        bname, number = re.match(r"^(\D+)(\d+)", filename_stem).groups()
        tags = [
            sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == bname2location[bname]
        ]

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("wind turbine", sly.Rectangle)

    tag_names = [
        "Baicheng",
        "Baqi",
        "Chifeng",
        "Hami",
        "Huiteng",
        "Jiamusi",
        "Mudanjiang",
        "Tieling",
        "Tongliao",
        "Wulanchabu",
        "Ürümqi",
        "Ximeng",
        "Yilan",
    ]
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]

    bname2location = {
        "baicheng": "Baicheng",
        "baqi": "Baqi",
        "Bbaicheng": "Baicheng",
        "Cchifeng": "Chifeng",
        "chifeng": "Chifeng",
        "hami": "Hami",
        "Hhami": "Hami",
        "huiteng": "Huiteng",
        "jiamusi": "Jiamusi",
        "Jjiamusi": "Jiamusi",
        "mudanjiang": "Mudanjiang",
        "tieling": "Tieling",
        "tongliao": "Tongliao",
        "Ttieling": "Tieling",
        "Ttongliao": "Tongliao",
        "wulanchabu": "Wulanchabu",
        "wulumuqi": "Ürümqi",
        "Wwulanchabu": "Wulanchabu",
        "Wwulumuqi": "Ürümqi",
        "ximeng": "Ximeng",
        "yilan": "Yilan",
        "Yyilan": "Yilan",
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    images_path = os.path.join(dataset_path, images_folder)
    bboxes_path = os.path.join(dataset_path, bboxes_folder)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = [im_name for im_name in os.listdir(images_path)]

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in images_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))

    return project
