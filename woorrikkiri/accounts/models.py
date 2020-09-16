from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager

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
    #account_num = models.CharField("계좌번호", max_length=30, null=True, blank=True)
    phone_num = models.CharField("전화번호", max_length=30, null=True, blank=True)
    name = models.CharField("이름", max_length=10)
    school = models.CharField("학교", max_length=15)
    #student_num = models.CharField("학번", max_length=30, null=True, blank=True)
    is_mento = models.BooleanField("멘토인 경우 체크해주세요", default=False)
    gender = models.CharField("성별", max_length=1, choices=CHOICES_GENDER)
    point = models.IntegerField("포인트", default = 0)
    mento_computing = models.BooleanField("컴퓨팅사고력 멘토", default=False)
    mento_basicC = models.BooleanField("C언어 기초 멘토", default=False)
    mento_GC = models.BooleanField("고급응용 C프로그래밍 멘토", default=False)
    mento_basicEngineering = models.BooleanField("기초공학설계", default=False)
    mento_univMath = models.BooleanField("대학수학", default=False)
    mento_principlesodEconomics1 = models.BooleanField("경제학원론1", default=False)
    mento_principlesodEconomics2 = models.BooleanField("경제학원론2", default=False)


    objects = UserManager()

class UserMento(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mento_computing = models.BooleanField("컴퓨팅사고력 멘토", default=False)
    mento_basicC = models.BooleanField("C언어 기초 멘토", default=False)
    mento_GC = models.BooleanField("고급응용 C프로그래밍 멘토", default=False)
    mento_basicEngineering = models.BooleanField("기초공학설계", default=False)
    mento_univMath = models.BooleanField("대학수학", default=False)
    mento_principlesodEconomics1 = models.BooleanField("경제학원론1", default=False)
    mento_principlesodEconomics2 = models.BooleanField("경제학원론2", default=False)

class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username =  models.CharField(max_length=40, blank =True)
    introduction = models.TextField(blank=True)
    profile_photo = models.FileField(blank=True)
