import pytest

from constants import EMAIL, JSON, KEY


@pytest.mark.django_db
def test_registration(client, signup_payload, User):
    res = client.post('/api/register/', signup_payload, format=JSON)
    assert res.status_code == 204

    # Check if the user was created in the database
    user = User.objects.filter(email=signup_payload[EMAIL]).first()
    assert user is not None
    assert user.email == signup_payload[EMAIL]


@pytest.mark.django_db
def test_login(client, signup_payload, signin_payload, User):
    resgister_res = client.post('/api/register/', signup_payload, format='json')
    assert resgister_res.status_code == 204

    # Check if the user was created in the database
    user = User.objects.filter(email=signup_payload[EMAIL]).first()
    assert user is not None
    assert user.email == signup_payload[EMAIL]

    login_res = client.post('/api/login/', signin_payload, format=JSON)
    assert login_res.status_code == 200

    assert login_res.json()[KEY] is not None
