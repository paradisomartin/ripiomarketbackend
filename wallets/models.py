from django.db import models

# Model de la Wallet
# Por ahora solo indica quien es el dueño y un JSON con balances de cada moneda
class Wallet(models.Model):
    owner = models.EmailField(unique=True)
    balance = models.JSONField(null=True)
