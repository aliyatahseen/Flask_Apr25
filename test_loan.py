import pytest
from loan_app import app


# client -> simulate a live server.
@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/') # send a get request /
    assert resp.status_code == 200
    assert resp.text == "<h1>Loan Approval Application !!!!</h1>"

def test_predict(client):
    test_data= {
                "applicant_income":10,
                "consumer_credit_history":1.0,
                "gender":"Male",
                "loan_amount":111111,
                "married":"Yes"
                }
    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status":'Approved'}