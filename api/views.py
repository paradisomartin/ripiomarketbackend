from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, serializers, permissions

from wallets.models import Wallet

# Creo serializers y views para registro y login de usuario, y ver usuarios para las transferencias
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # Permiso de GET para solo authenticados

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    # Permiso de registro para cualquiera


# Creo serializers y views para wallets
class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class UserWallet(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = UserWalletSerializer
    # Permiso para ver solo si tiene mismo ID/Usuario/Email


# Transferencias y movimimentos

# Metodo POST y PUT para ingreso de dinero
# Metodo DELETE y PUT para retiro de dinero
# Metodo PUT para transferencia de un JSON a otro
