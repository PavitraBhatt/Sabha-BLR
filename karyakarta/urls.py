from django.urls import path
from .views import LoginView
from . import views
from .views import KaryakartaCreateView

urlpatterns = [
    path('getkk/',views.kk_get),
    path('login/', LoginView.as_view(), name='login'),
    path('create_karyakarta/', KaryakartaCreateView.as_view(), name='create_karyakarta'),
]
