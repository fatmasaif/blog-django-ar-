from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
   path('register/', views.register, name='register'),
  
   # login logout by django auth
   # path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
   # path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
 
   #  login logout by forms
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),

   # login logout by HTML

]