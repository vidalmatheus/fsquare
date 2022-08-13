from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from main.models.models_auth import Profile


class DeleteNotAllowedAdmin(admin.ModelAdmin):
    """
        Django admin for blocking a model record deletion
    """

    def get_actions(self, request):
        actions = super(DeleteNotAllowedAdmin, self).get_actions(request)
        actions.pop('delete_selected', None)
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def delete_model(self, request, obj):
        raise PermissionDenied("You can't delete a model on django-admin")


class UserProfileInline(admin.StackedInline):
    model = Profile
    fk_name = "user"
    can_delete = False
    fields = ('photo_url', 'is_blocked', 'block_reason')


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_joined']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
