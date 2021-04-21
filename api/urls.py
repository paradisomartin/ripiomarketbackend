from django.urls import path, include

# Agrego los views para la API
from .views import UserList, UserRegister, UserWallet

# Rutas API
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', UserList.as_view()),
    path('users/register', UserRegister.as_view()),
    path('wallet/<pk>', UserWallet.as_view())
]
