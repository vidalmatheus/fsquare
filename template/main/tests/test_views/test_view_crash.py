import pytest

from commons.utils import error_str


def test_whoami_not_authenticated(client):
    with pytest.raises(Exception) as ex:
        client.get('/api/crash')
    assert 'Break on purpose' in error_str(ex)
