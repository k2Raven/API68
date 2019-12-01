from django.urls import path
from .views import action_AB

app_name = 'api_v1'

urlpatterns = [
    path('add/', action_AB, name='add'),
    path('subtract/', action_AB, name='subtract'),
    path('multiply/', action_AB, name='multiply'),
    path('divide/', action_AB, name='divide'),
]