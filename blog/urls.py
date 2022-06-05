from django.urls import path
from .views import post_list, post_add, post_detail, post_delete, post_update

urlpatterns = [
    
    path('list/', post_list, name='list'),
    path('add/', post_add, name='add'),
    path('update/<int:id>', post_update, name='update'),
    path('delete/<int:id>', post_delete, name='delete'),
    path('detail/<int:id>', post_detail, name="detail"),
]