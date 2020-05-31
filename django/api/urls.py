from django.urls import path

from .views import (
    AppointmentsListView,
    AppointmentsCreateView,
    HealthView
)

app_name = 'api'
urlpatterns = [
    path('appointments/list', AppointmentsListView.as_view(), name='appointments-list'),
    path('appointments/create', AppointmentsCreateView.as_view(), name='appointments-create'),
    path('', HealthView.as_view(), name='health'),
]