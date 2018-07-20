from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        verbose_name="업체 이름",
    )
    contact = models.CharField(
        max_length=50,
        verbose_name="전화 번호",
    )
    address = models.CharField(
        max_length=200,
        verbose_name="주소",
    )
    description = models.TextField(
        verbose_name="상세 정보",
    )
