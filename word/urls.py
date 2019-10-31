from django.urls import path, include
from . import views
app_name = 'word'
urlpatterns = [
    path('home',views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('blog_single',views.about, name = 'blog_single'),
    path('category', views.about, name = 'category'),
    path('contact',views.about, name = 'contact'),
]