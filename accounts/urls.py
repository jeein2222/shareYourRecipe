from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# 이게 있어야 {% url 'accounts:~' %} 사용 가능
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]