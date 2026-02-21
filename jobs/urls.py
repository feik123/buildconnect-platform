from django.urls import path, include

from jobs.views import JobListView, JobCreateView, JobDetailView, JobUpdateView, JobDeleteView

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='list'),
    path('create/', JobCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', JobDetailView.as_view(), name='detail'),
        path('edit/', JobUpdateView.as_view(), name='edit'),
        path('delete/', JobDeleteView.as_view(), name='delete'),
    ])),


]