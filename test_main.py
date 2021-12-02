from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_first_week_1():
    response = client.post("/week", json={"calculated_date": "2019-01-01"})
    assert response.status_code == 200
    assert response.json() == {"week_number": 1}

def test_first_week_2():
    response = client.post("/week", json={"calculated_date": "2019-01-05"})
    assert response.status_code == 200
    assert response.json() == {"week_number": 1}

def test_second_week():
    response = client.post("/week", json={"calculated_date": "2019-01-06"})
    assert response.status_code == 200
    assert response.json() == {"week_number": 2}

def test_54_week():
    response = client.post("/week", json={"calculated_date": "2020-01-05"})
    assert response.status_code == 200
    assert response.json() == {"week_number": 54}

def test_before_2019_year_1():
    response = client.post("/week", json={"calculated_date": "2018-12-31"})
    assert response.status_code == 400

def test_before_2019_year_2():
    response = client.post("/week", json={"calculated_date": "2010-11-30"})
    assert response.status_code == 400

def test_incorrect_data_1():
    response = client.post("/week", json={"date": "2020-11-30"})
    assert response.status_code == 422

def test_incorrect_data_2():
    response = client.post("/week", json={"date": "2010-11-30"})
    assert response.status_code == 422

def test_incorrect_data_3():
    response = client.post("/week", json={"calculated_date": "2020-13-30"})
    assert response.status_code == 422

def test_incorrect_data_4():
    response = client.post("/week", json={"calculated_date": "2020-13-45"})
    assert response.status_code == 422

def test_incorrect_data_5():
    response = client.post("/week", json={"calculated_date": "2019-40-50"})
    assert response.status_code == 422