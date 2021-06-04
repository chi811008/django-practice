from django.urls import path
from comment import views

urlpatterns = [
    path('', views.comment_list, name="comments"),
    path('detail/<str:pk>', views.comment_detail, name="detail"),
    path('create', views.comment_create, name="create"),
    path('update/<str:pk>', views.comment_update, name="update"),
    path('delete/<str:pk>', views.comment_delete, name="delete"),
]