from django.urls import path
from .views import UserProfileView, UserProfileCreate, MeasurementView, MeasurementCreate

urlpatterns = [
path('', UserProfileView.as_view(), name='home'),
path('create', UserProfileCreate.as_view(), name='user_create'),
path('messurment', MeasurementView.as_view(), name='m_list'),
path('messurment/create', MeasurementCreate.as_view(), name='m_create')
]