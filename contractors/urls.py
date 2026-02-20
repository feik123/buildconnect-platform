
from django.urls import path, include

from contractors.views import ContractorListView, ContractorDetailView, ContractorUpdateView, ContractorCreateView, \
    ContractorDeleteView

app_name = 'contractors'

urlpatterns = [
    path('', ContractorListView.as_view(), name='list'),
    path('create/', ContractorCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('',ContractorDetailView.as_view(), name='detail'),
        path('edit/',ContractorUpdateView.as_view(), name='edit'),
        path('delete/',ContractorDeleteView.as_view(), name='delete'),
    ])),

]