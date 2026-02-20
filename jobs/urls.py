from django.urls import path

from jobs.views import JobListView, JobCreateView, JobDetailView

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='list'),
    path('create/', JobCreateView.as_view(), name='create'),
    path('<int:pk>/', JobDetailView.as_view(), name='detail'),

]