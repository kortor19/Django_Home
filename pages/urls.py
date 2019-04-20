
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from . import views
#from contact.views import contact

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('portfolios/', views.portfolios, name='portfolios'),
   # path('blog/', views.blog, name='blog'),
    path('post_list/', views.post_list, name='post_list'),
    path("post/<int:pk>/", views.post_detail, name = 'post_detail'),
    path('post/new', views.new_post, name = 'new_post'),
    path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name = 'post_delete'),
    
]








