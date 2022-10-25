from django.urls import path
from .views import view_news, add, get, edit

urlpatterns = [
    path('', view_news, name='view_news'),
    path('add/', add, name='add'),
    path('<int:id>/', get, name='get'),
    path('<int:id>/edit/', edit, name='edit'),
]
