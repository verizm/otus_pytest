## Otus_pytes

My training in automated testing.


### Working with `virtualenv`

python3 -m venv env
pip3 install -r requirements.txt

### Run tests

./main.py

### Run pylint

pylint --ignore=env -rn *.py 0_math/*.py 1_fixture/*.py 2_api/*.py 3_data_driven/*.py 4_opencart/*.py 5_opencart_locators/*.py 6_opencart_products/*.py 7_action_chains/*.py
