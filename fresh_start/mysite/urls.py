from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('about/', views.about, name='mysite-about'),
    path('blog/', views.blog, name='mysite-blog'),
]