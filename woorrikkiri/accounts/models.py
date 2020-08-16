from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(gender=self.model.GENDER_OTHER, *args, **kwargs)

class User(AbstractUser):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'
    CHOICES_GENDER = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
        (GENDER_OTHER, '기타'),
    )

    created_on = models.DateTimeField("등록일자", auto_now_add=True)
    account_num = models.CharField("계좌번호", max_length=30, null=True, blank=True)
    phone_num = models.CharField("전화번호", max_length=30, null=True, blank=True)
    name = models.CharField("이름", max_length=10)
    school = models.CharField("학교", max_length=15)
    student_num = models.CharField("학번", max_length=30, null=True, blank=True)
    is_mento = models.BooleanField("멘토인 경우 체크해주세요", default=False)
    gender = models.CharField("성별", max_length=1, choices=CHOICES_GENDER)

    objects = UserManager()

class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username =  models.CharField(max_length=40, blank =True)
    introduction = models.TextField(blank=True)
    profile_photo = models.FileField(blank=True)