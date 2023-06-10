ML-Ops Course App

Testing (test_Multiply.py & test_app.py)
```
python -m pytest -vv
```
Deploy:
```
uvicorn app:app --reload
```
URL Example (2*3):
```
http://127.0.0.1:8000/Multi/2/3
```
