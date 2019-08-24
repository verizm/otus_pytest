## Otus_pytes

My training in automated testing.


### Working with `virtualenv`

python3 -m venv env
pip3 install -r requirements.txt

### Run tests

./main.py

### Run pylint

pylint --ignore=env -rn *.py 0_math/*.py 1_fixture/*.py 2_api/*.py 3_data_driven/*.py