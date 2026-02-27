from django.urls import path, include
from watchlist_app.api import views

urlpatterns = [
    path('media/list/', views.WatchList.as_view(), name='media-list'),
    path('media/<int:pk>/', views.WatchDetail.as_view(), name='media-detail'),
    path('platform/list/', views.PlatformList.as_view(), name='platform-list'),
    path('platform/<int:pk>/', views.PlatformDetail.as_view(), name='platform-detail'),
]
