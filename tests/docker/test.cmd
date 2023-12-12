python -m flake8 pipeline_material
python -m flake8 tests/test
python -m pydocstyle pipeline_material
python -m pydocstyle --match='.*\.py' tests/test
python -m pylint --rcfile .pylintrc2 pipeline_material
python -m pylint --rcfile .pylintrc2 tests/test
pytest --cov=pipeline_material --cov-report term:skip-covered --durations=5 tests
