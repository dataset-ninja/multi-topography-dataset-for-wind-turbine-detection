Dataset **Multi-topography Dataset for Wind Turbine Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTQ3M19NdWx0aS10b3BvZ3JhcGh5IERhdGFzZXQgZm9yIFdpbmQgVHVyYmluZSBEZXRlY3Rpb24vbXVsdGktdG9wb2dyYXBoeS1kYXRhc2V0LWZvci13aW5kLXR1cmJpbmUtZGV0ZWN0aW9uLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIlJ0aytER0dUZ3RHMlR5VEQ3MlpnL1pvdzhoTStnV2ZHV2VGZ2luNmhscEU9In0=?response-content-disposition=attachment%3B%20filename%3D%22multi-topography-dataset-for-wind-turbine-detection-DatasetNinja.tar%22)

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