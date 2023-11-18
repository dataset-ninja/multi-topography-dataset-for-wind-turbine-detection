Dataset **Multi-topography Dataset for Wind Turbine Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/7/Y/qp/ggZVjGL88t7orsQe6g5NB3H6fL51qacxHctZUFStjHoFeh9IZZYfQcW1xbbC74tmyyIrYHe2obnW2GDfcMZL3WLy7YO59Pop6To9k9d9kMwkEd5uWIMMmSFxLDxA.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Multi-topography Dataset for Wind Turbine Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/7808269/files/windTurbineDataSet.zip?download=1).