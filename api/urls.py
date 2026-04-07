from django.urls import path

from api.views import JobListAPIView, JobDetailAPIView, MyJobsAPIView, JobCreateAPIView

urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='api-jobs'),
    path('jobs/create/', JobCreateAPIView.as_view(), name='api-create'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='api-job-detail'),
    path('jobs/my/', MyJobsAPIView.as_view(), name='api-my-jobs')
]