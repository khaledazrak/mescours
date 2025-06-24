from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_helloworld_default():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.text == "Hello World"

def test_helloworld_with_name():
    response = client.get("/helloworld?name=khaled")
    assert response.status_code == 200
    assert response.text == "Hello Khaled"

def test_versionz():
    response = client.get("/versionz")
    assert response.status_code == 200
    assert "project" in response.json()
    assert "git_hash" in response.json()

