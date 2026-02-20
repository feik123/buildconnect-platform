from django.urls import path
from applications.views import ApplicationCreateView

app_name = 'applications'

urlpatterns = [
    path('<int:pk>/apply/', ApplicationCreateView.as_view(), name='create'),
]
