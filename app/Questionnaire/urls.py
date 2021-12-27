"""Questionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.api.urls')),
    path('api/', include('post.api.urls')),
    path('', include('post.urls')),


    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('signup/', views.registrer, name='signup'),
    path('profile/', views.userprofile, name='profile'),
    path('profile/update/', views.userupdateprofile, name='profileupdate'),

    # password reset
    path('reset_password/',
         auth_views.PasswordResetView.as_view(),         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),     name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),  name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
