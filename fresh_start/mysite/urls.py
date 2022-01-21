from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('about/', views.about, name='mysite-about'),
    path('blog/', views.blog, name='mysite-blog'),
    path('resources/', views.resources, name='mysite-resources'),
    path('register/', user_views.register, name='register')
]