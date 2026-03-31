from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    is_contractor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
