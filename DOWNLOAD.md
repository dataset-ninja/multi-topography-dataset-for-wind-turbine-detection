Dataset **Wind Turbines 6** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/u/B/dB/HtpVOF7YPOLV3oEOtRSRh9m62GDUtAV8pWgJIjeCcqRGThWtJt3LvpgXM0nXb5fyRHZVm8aP5RtNhAInY4OcBg8PvQVxeQ3L2MgWoxdPmgFdzy87bTlDiU6HjW5k.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines 6', dst_path='~/dtools/datasets/Wind Turbines 6.tar')
```
The data in original format can be 🔗[downloaded here](https://zenodo.org/record/7808269/files/windTurbineDataSet.zip?download=1)