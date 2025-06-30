from django.urls import path
from .views import signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),  
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        next_page='all_posts'  # ✅ redirect after login
    ), name='login'),
 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
]
