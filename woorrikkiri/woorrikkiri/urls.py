from django.contrib import admin
from django.urls import path
import main.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    # path('agreement/', main.views.agreement, name="agreement"),
    # path('private_info/', main.views.private_info, name="private_info"),
    path('main/new/', main.views.new, name="new"),
    path('main/ask/', main.views.ask, name="ask"),
    path('main/detail/<int:pk>', main.views.detail, name="detail"),
    path('main/edit/<int:index>', main.views.edit, name="edit"),
    path('main/detail/<int:pk>/delete', main.views.delete, name="delete"),
    path('main/detail/<int:pk>/comment/<int:comment_pk>/delete/',main.views.delete_comment, name="delete_comment"),
    path('accounts/mypage/', accounts.views.mypage, name="mypage"),
    path('accounts/profile_update', accounts.views.profile_update, name="profile_update"),
    path('accounts/change_password', accounts.views.change_password, name="change_password"),
    path('main/about/', main.views.about, name="about"),
    path('main/about_team/', main.views.about_team, name="about_team"),
    path('main/faq/', main.views.faq, name="faq"),
    path('main/faq_datail/<int:pk>', main.views.faq_detail, name="faq_detail"),
    path('accounts/signup/', accounts.views.signup, name="signup"),
    path('accounts/signin/', accounts.views.signin, name="signin"),
    path('accounts/signout/', accounts.views.signout, name="signout"),
    path('main/payment/', main.views.payment, name="payment"),
    path('accounts/user_delete', accounts.views.user_delete, name="user_delete"),
    path('main/requestJob/', main.views.requestJob, name="requestJob"),#팝빌 결제 모듈 작동 여부 확인용  by Junghak
    path('main/getJobState/', main.views.getJobState, name="getJobState"),#팝빌 결제 모듈 시작  by Junghak
    path('main/search/', main.views.search, name="search"), #팝빌 결제 거래 내역 조회 by Junghak
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)