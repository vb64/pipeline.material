# Pipeline material class for static integrity calculation

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/pipeline.material/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/vb64/pipeline.material/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/pipeline.material/py2.yml?label=Python%202.7&style=plastic&branch=main)](https://github.com/vb64/pipeline.material/actions?query=workflow%3Apy2)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/pipeline.material/py3.yml?label=Python%203.8-3.13&style=plastic&branch=main)](https://github.com/vb64/pipeline.material/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4b1898433899465b870ed7ecc4f0fd02)](https://app.codacy.com/gh/vb64/pipeline.material/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/4b1898433899465b870ed7ecc4f0fd02)](https://app.codacy.com/gh/vb64/pipeline.material/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

## Installation

```bash
pip install pipeline-material
```

## Usage

```python
from pipeline_material import PipelineMaterial

material = PipeMaterial("Steel", 20000)

assert material.smys == 20000
assert "smys 20000" in str(material)
```

## Development

```bash
git clone git@github.com:vb64/pipeline.material.git
cd pipeline.material
```

With Python 3:

```bash
make setup PYTHON_BIN=/path/to/python3
make tests
```

With Python 2:

```bash
make setup2 PYTHON_BIN=/path/to/python2
make tests2
```
