
from django.urls import path, include
from applications.views import ApplicationCreateView, accept_application

app_name = 'applications'

urlpatterns = [
    path('<int:pk>/', include([
        path('apply/', ApplicationCreateView.as_view(), name='create'),
        path('accept/', accept_application, name='accept'),
    ])),
]
