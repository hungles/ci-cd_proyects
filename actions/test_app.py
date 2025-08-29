import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello CI/CD World!"

def test_sum():
    client = app.test_client()
    response = client.post("/sum", 
                           data=json.dumps({"a": 2, "b": 3}),
                           content_type="application/json")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5
