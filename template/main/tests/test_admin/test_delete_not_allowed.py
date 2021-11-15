import pytest
from django.contrib.admin.sites import AdminSite
from django.core.exceptions import PermissionDenied
from unittest.mock import MagicMock
from commons.utils import error_str

from main.admin import DeleteNotAllowedAdmin, UserAdmin


def test_delete_not_allowed_admin():
    model_admin = DeleteNotAllowedAdmin(model=MagicMock(), admin_site=AdminSite())
    request = MagicMock()
    obj = MagicMock()
    actions = model_admin.get_actions(request)
    assert 'delete_selected' not in actions
    assert model_admin.has_delete_permission(request) is False
    with pytest.raises(PermissionDenied) as ex:
        model_admin.delete_model(request=request, obj=obj)
    assert "You can't delete a model on django-admin" in error_str(ex)


def test_delete_not_allowed_user_admin():
    model_admin = UserAdmin(model=MagicMock(), admin_site=AdminSite())
    request = MagicMock()
    assert model_admin.has_delete_permission(request) is False
