install:
	pip install -r requirements.txt

lint:
	pylint num_sqrt.py

test:
	python -m pytest -vv

deploy:
	uvicorn app:app --reload