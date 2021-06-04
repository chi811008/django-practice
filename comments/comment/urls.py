from django.urls import path
from comment import views

urlpatterns = [
    path('', views.comment_list, name="comments"),
    path('detail/<str:pk>', views.comment_detail, name="detail"),
]