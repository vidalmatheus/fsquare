from django.http import JsonResponse


def whoami(request):
    if not request.user.is_authenticated:
        return JsonResponse({'authenticated': False})

    # fields = request.GET.get('fields')
    # if fields:
    #     fields = fields.split(',')

    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    }
    return JsonResponse(i_am)


def login(request):
    return JsonResponse({}, safe=False)


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
