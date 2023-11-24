from django.urls import path
from .import views

urlpatterns = [
    path('update-profile/', views.update_user_profile),
    # 필요에 따라 URL을 변경하여 사용합니다.
    path('user-info/<int:user_pk>/', views.user_info),
]