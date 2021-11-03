from django_qserializer import BaseSerializer


class UserSerializer(BaseSerializer):
    def serialize_object(self, user):
        data = {
            'id': user.id,
            'name': user.get_full_name(),
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'avatar': user.profile.photo_url,
            'permissions': {
                'ADMIN': user.is_superuser,
                'STAFF': user.is_staff,
            }
        }

        return data
