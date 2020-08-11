from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileInline(admin.StackedInline): # 로또 프로젝트에서 썼던 방식으로 유저 밑에 프로필 을 붙여서 보여주려고 이를 상속받음
    model = Profile
    con_delete = False  

class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields']+=('name', 'school', 'student_num', 'phone_num', 'gender', 'account_num', 'is_mento',)
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('account_num','student_num')}),
    )
    inlines = (ProfileInline,)

admin.site.register(User, CustomUserAdmin)