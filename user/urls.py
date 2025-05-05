from django.urls import path
from .views import CreateUserView, LoginView, UserDetailView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]