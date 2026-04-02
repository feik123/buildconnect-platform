
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
    path('contractors/', include('contractors.urls')),
    path('reviews/', include('reviews.urls')),
    path('api/', include('api.urls'))
]
