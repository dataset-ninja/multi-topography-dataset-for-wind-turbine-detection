Dataset **Multi-topography Dataset for Wind Turbine Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/x/d/i2/NIwPFiysSyBtwokHUnlACLk0IQddaORa5k2JGwazkgsym4jmgh9BkyHycJiuFcTgGGFjje3uKd9y7fhi33is87LriumLXLBDQ60HjofFItGmhERxvlQaktJ22WYw.tar)

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