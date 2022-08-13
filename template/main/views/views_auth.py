from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

from template.main.serializers.serializers_auth import UserSerializer


@require_GET
def whoami(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({'authenticated': False})

    i_am = {
        'user': UserSerializer().serialize_object(user),
        'authenticated': True,
    }
    return JsonResponse(i_am)


@csrf_exempt
@require_POST
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.select_related('profile').get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    if (hasattr(user, 'profile') and user.profile.is_blocked) or not user.check_password(password):
        return JsonResponse({'error': 'Wrong password'}, status=401)
    if not user.is_active:
        user.is_active = True
    auth.login(request, user)
    user_dict = UserSerializer().serialize_object(user)
    return JsonResponse(user_dict, safe=False)


@require_POST
def logout(request):
    auth.logout(request)
    return JsonResponse({}, safe=False)
