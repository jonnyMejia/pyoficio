# Django Library
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# Localfolder Library
# from ..views import (
#    ChangePasswordForm, DoChangePassword, UserCreateView, UserDeleteView,
#    UserDetailView, UserListView, UserUpdateView)
#from ..views.usercustom import (
#    ActivateUserView, AvatarUpdateView, LogOutModalView, PasswordRecoveryView,
#    ProfileView, SignUpView, cambio_clave)

app_name = 'PyUser'
urlpatterns = [
    #path('signup', SignUpView.as_view(), name='signup'),
    #path('activate/<uidb64>/<token>', ActivateUserView.as_view(), name='activar'),
    path(
        'login/',
        LoginView.as_view(
            template_name='usercustom/login.html',
            # redirect_field_name='next',
            success_url='home'
        ),
        name='login'),
]
