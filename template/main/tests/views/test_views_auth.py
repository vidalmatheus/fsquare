def test_whoami_not_authenticated(client):
    resp = client.get('/api/whoami')
    respj = resp.json()
    assert resp.status_code == 200
    assert respj['authenticated'] is False


def test_whoami(client, zuck):
    client.force_login(zuck)
    resp = client.get('/api/whoami')
    respj = resp.json()
    assert resp.status_code == 200
    assert respj['user']['name'] == 'Mark Zuckerberg'
    assert respj['authenticated'] is True


def test_login_user_not_found(client, db):
    request_body = {
        'username': 'zuck',
        'password': 'zuck'
    }
    resp = client.post('/api/login', request_body)
    respj = resp.json()
    assert resp.status_code == 404
    assert 'User not found' in respj['error']


def test_login_wrong_password(client, zuck):
    request_body = {
        'username': zuck.username,
        'password': '123'
    }
    resp = client.post('/api/login', request_body)
    respj = resp.json()
    assert resp.status_code == 401
    assert 'Wrong password' in respj['error']


def test_login_user_inactived(client, zuck):
    password = 'zuck123'
    zuck.set_password(password)
    zuck.is_active = False
    zuck.save()
    request_body = {
        'username': zuck.username,
        'password': password
    }
    resp = client.post('/api/login', request_body)
    respj = resp.json()
    assert resp.status_code == 200
    assert respj['name'] == 'Mark Zuckerberg'


def test_login(client, zuck):
    password = 'zuck123'
    zuck.set_password(password)
    zuck.save()
    request_body = {
        'username': zuck.username,
        'password': password
    }
    resp = client.post('/api/login', request_body)
    respj = resp.json()
    assert resp.status_code == 200
    assert respj['name'] == 'Mark Zuckerberg'


def test_logout(client, zuck):
    client.force_login(zuck)
    resp = client.post('/api/logout')
    respj = resp.json()
    assert resp.status_code == 200
    assert respj == {}
