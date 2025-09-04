from .views import RegisterView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(next_page='task_list'), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'register'), name='logout'),
]
