# Pipeline material class for static integrity calculation

## Installation

```bash
pip install pipeline-material
```

## Usage

```python
from pipeline_material import PipelineMaterial

material = PipeMaterial("Steel", 20000)

assert material.smys == 20000
assert str(material) == 'xxx'
```

## Development

```
$ git clone git@github.com:vb64/pipeline.material.git
$ cd pipeline.material
```
With Python 3:
```
$ make setup PYTHON_BIN=/path/to/python3
$ make tests
```
With Python 2:
```
$ make setup2 PYTHON_BIN=/path/to/python2
$ make tests2
```
