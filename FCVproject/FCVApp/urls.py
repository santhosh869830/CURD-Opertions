from django.urls import path
from . import views


urlpatterns=[
    path('wel/',views.welcome),
    path('form/',views.create_view),
    path('list/',views.list_view),
    path('detail/<int:id>',views.Detail_view),
    path('update/<int:id>',views.update_view),
    path('delete/<int:id>',views.delete_view),
    path('detailC/<int:pk>',views.Detail_views.as_view(),name='detailC'),
    path('createC/',views.Create_view.as_view()),
    path('updateC/<int:pk>',views.Update_view.as_view()),
    path('deleteC/<int:pk>',views.Delete_view.as_view()),
    path('listC/',views.List_view.as_view(),name='list'),
]