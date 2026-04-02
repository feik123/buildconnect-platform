from django.urls import path

from api.views import JobListAPIView, JobDetailAPIView

urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='api-jobs'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='api-job-detail')
]