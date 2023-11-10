from django.contrib.auth.decorators import permission_required
from .models import User


@permission_required('add_user', True)
def user_add(request):
    data = request.POST
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    return


@permission_required('delete_user', True)
def user_delete(request, username):
    try:
        u = User.objects.get(username=username)
        u.delete()
    except:
        pass
    return
