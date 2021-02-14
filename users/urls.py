from django.conf.urls import url
from users import views
# from admini import views
app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    #
    url(r'more$', views.more, name = 'more'),
    #
    # url(r'some_view$', views.some_view, name = 'some_view'),

    url(r'formations$', views.formations, name = 'formations'),
    ]
