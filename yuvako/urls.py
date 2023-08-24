from . import views
from django.urls import path

urlpatterns = [
    path('getyuvak/',views.yuvako_get),
    path('postyuvak/',views.yuvak_post),
    path('updateyuvak/<int:MobileNumber>/', views.update_yuvako),
]
