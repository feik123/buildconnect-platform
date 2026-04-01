from django.urls import path

from reviews.views import ReviewCreateView

app_name = 'reviews'

urlpatterns = [
    path('create/<int:pk>/', ReviewCreateView.as_view(), name='create')
]