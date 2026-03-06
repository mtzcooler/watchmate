from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api import views

router = DefaultRouter()
router.register('platform', views.PlatformView, basename='platform')

urlpatterns = [
    path('media/list/', views.WatchList.as_view(), name='media-list'),
    path('media/<int:pk>/', views.WatchDetail.as_view(), name='media-detail'),
    # path('platform/list/', views.PlatformList.as_view(), name='platform-list'),
    # path('platform/<int:pk>/', views.PlatformDetail.as_view(), name='platform-detail'),
    path('', include(router.urls)),
    path('media/<int:pk>/review/', views.ReviewList.as_view(), name='review-list'),
    path('media/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]
