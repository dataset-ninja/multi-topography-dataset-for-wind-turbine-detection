Dataset **Multi-topography dataset for wind turbine detection** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/Y/9/xT/aeGBfL7UQGsZnkIKA5Mqk4OEozkDZSidv2yAsWf4OS8BlEa7bj4lIXRJREaeEds9nrd4sQc4raD0GYbXY7aLMrqdrqUJohfkg7XtC03Tmu8A9YqR4RNHh9GLr73q.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Multi-topography dataset for wind turbine detection', dst_path='~/dtools/datasets/Multi-topography dataset for wind turbine detection.tar')
```
The data in original format can be 🔗[downloaded here](https://zenodo.org/record/7808269/files/windTurbineDataSet.zip?download=1)