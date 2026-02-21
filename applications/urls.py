
from django.urls import path, include
from applications.views import ApplicationCreateView
from jobs.views import JobUpdateView

app_name = 'applications'

urlpatterns = [
    path('<int:pk>/', include([
        path('apply/', ApplicationCreateView.as_view(), name='create'),
    ])),
]
