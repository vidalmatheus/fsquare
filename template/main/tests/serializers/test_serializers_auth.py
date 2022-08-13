from main.serializers.auth import UserSerializer


def test_serialize_auth(zuck):
    resp = UserSerializer().serialize_object(zuck)
    assert resp['username'] == 'zuck'
    assert resp['name'] == 'Mark Zuckerberg'
    assert resp['permissions']['ADMIN'] is True
    assert resp['permissions']['STAFF'] is True
