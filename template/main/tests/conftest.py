import pytest
from model_bakery import baker
from django.contrib.auth.models import User


@pytest.fixture
def zuck(db):
    user = baker.make(
        User,
        username='zuck',
        first_name='Mark',
        last_name='Zuckerberg',
        email='mark.zuckerberg@facebook.com',
        profile__photo_url='http://zuck.png',
        is_superuser=True,
        is_staff=True
    )
    yield user
    user.delete()
