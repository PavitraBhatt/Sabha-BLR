from django.urls import path
from .views import LoginView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import MyTokenObtainPairView, MyProtectedView
from .views import KaryakartaCreateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('login/',views.LoginView),
    #  path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/protected/', MyProtectedView.as_view(), name='protected'),
    # path('getkk/',views.kk_get),
    path('create_karyakarta/', KaryakartaCreateView.as_view(), name='create_karyakarta'),
]
