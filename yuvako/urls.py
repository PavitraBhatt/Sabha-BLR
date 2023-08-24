from . import views
from django.urls import path

urlpatterns = [



    path('getyuvak/',views.yuvako_get),
    # path('getsite/<int:id>/',views.yuvak_get_id),
    path('postyuvak/',views.yuvak_post),
    # path("submityuvak/", views.AddYuvakAPIView.as_view(), name="add_person_api"),
    # path('updateyuvak/<int:id>/', views.yuvak_update, name='yuvak-update'),
    path('updateyuvak/<int:MobileNumber>/', views.update_yuvako),
]
