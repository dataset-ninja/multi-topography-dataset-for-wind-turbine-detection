Dataset **Multi-topography Dataset for Wind Turbine Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE0NzNfTXVsdGktdG9wb2dyYXBoeSBEYXRhc2V0IGZvciBXaW5kIFR1cmJpbmUgRGV0ZWN0aW9uL211bHRpLXRvcG9ncmFwaHktZGF0YXNldC1mb3Itd2luZC10dXJiaW5lLWRldGVjdGlvbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICIySXBhMVdPazhsc0R2TVAzYmdEWU1DS2ZObzc0YW9yb2o2U1VqQkdnL3FrPSJ9)

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