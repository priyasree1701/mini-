from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi,name='unused medicine'),
    path('hi.html', views.hi),
    path('signup.html', views.signUp),
    path('signin.html', views.signin),
    path('contact.html', views.contact),
    path('registerationSuccess', views.registrationSuccess),
    path('home.html', views.home),
    path('loginvalidation', views.loginsucess),

    path('medilist', views.medilist),

    ]
