from django.db import models
from user.models import User
from report.models import trashCans

class Declaration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trash_can = models.ForeignKey(trashCans, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)