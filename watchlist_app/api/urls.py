from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.api.views import movie_list, movie_details
import watchlist_app
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, StreamPlatformAV,
                                     StreamPlatformDetailAV, ReviewList, ReviewDetail,
                                     ReviewCreate, StreamPlatformVS, UserReview, WatchListGV)

# Routers
router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # Function Based Views, URL Structure
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie_detail'),

    # ------------------------------------------------------------------

    # Class Based View, URL Structure
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    # path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),

    # DjangoFilterBackend
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # ------------------------------------------------------------------

    # URL Using Routers
    path('', include(router.urls)),

    # ------------------------------------------------------------------

    # Concrete View Classes, URL Structure
    path('<int:pk>/reviews/create/', ReviewCreate.as_view(), name='review-create'),
    # Get All Reviews For A Particular Movie
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    # path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    # path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),

    # Access Individual Review
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # Filter: Filtering against the URL
    # path('user-reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),

    # Filter: Filtering against query parameters
    path('user-reviews/', UserReview.as_view(), name='user-review-detail'),

    # ------------------------------------------------------------------

    # GenericAPIView and Mixins, URL Structure
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]
