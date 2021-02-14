from django.conf.urls import url
from admini import views
from users import urls
from django.contrib.auth import views as auth_views
from . import views as user_views

app_name = 'admini'
urlpatterns = [
    url(r'^adminBase$', views.adminBase, name = 'adminBase'),

    url(r'^newMember$', views.newMember, name = 'newMember'),

    url(r'^newMeeting$', views.newMeeting, name = 'newMeeting'),

    url(r'^allMeeting$', views.allMeeting, name = 'allMeeting'),

    url(r'^allMember$', views.allMember, name = 'allMember'),

    url(r'^allPurchase$', views.allPurchase, name = 'allPurchase'),

    url(r'^newPurchase$', views.newPurchase, name = 'newPurchase'),

    url(r'^deleteMember/(?P<member_id>\d+)/$', views.deleteMember, name = 'deleteMember'),

    url(r'^editMember/(?P<member_id>\d+)/$', views.editMember, name = 'editMember'),


    ## Login and logout URL
    url(r'login/$', auth_views.LoginView.as_view(template_name='admini/login.html'),name="login"),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='admini/logout.html'),name="logout"),
    ]
