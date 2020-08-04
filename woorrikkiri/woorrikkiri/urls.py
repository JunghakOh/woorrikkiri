"""woorrikkiri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('main/new/', main.views.new, name="new"),
    path('main/ask/', main.views.ask, name="ask"),
    path('main/detail/<int:pk>', main.views.detail, name="detail"),
    path('main/edit/<int:index>', main.views.edit, name="edit"),
    path('main/detail/<int:pk>/delete', main.views.delete, name="delete"),
    path('main/detail/<int:pk>/comment/<int:comment_pk>/delete/',main.views.delete_comment, name="delete_comment"),
    path('main/mypage/', main.views.mypage, name="mypage"),
    path('main/about/', main.views.about, name="about"),
    path('main/faq/', main.views.faq, name="faq"),
    path('accounts/signup/', accounts.views.signup, name="signup"),
    path('accounts/signin/', accounts.views.signin, name="signin"),
    path('accounts/signout/', accounts.views.signout, name="signout"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)