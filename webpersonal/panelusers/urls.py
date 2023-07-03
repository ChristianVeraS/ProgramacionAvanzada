from django.urls import path
from . import views
from .views import LoginPagueView, PanelHomePagueView, UserChangePasswordView, UserProfileView

 
urlpatterns = [
    path('iniciar_sesion/', LoginPagueView.as_view(), name="login"),
    path('panel_usuario/', PanelHomePagueView.as_view(), name="panel_home"),
    path('cambiar_contraseña/', UserChangePasswordView.as_view(), name="change_password"),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
