from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup , name="signup"),
    path('idcheck/', views.idCheck , name="idcheck"),
    path('nicknamecheck/', views.nicknameCheck , name="nicknameCheck"),
    path('store_register/' , views.store_register , name="store_register"),
]
