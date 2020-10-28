from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('download/<str:filename>/', views.DownloadDocumentView.as_view(), name='download'),
    path('delete/<str:filename>/', views.DeleteDocumentView.as_view(), name='delete'),
    path('add-file/', views.AddDocumentView.as_view(), name='add_file'),
]
