from django.urls import path

from .views import add_comment, delete_comment

urlpatterns = [
    path('<int:id>/add-comment/', add_comment, name='add_comment'),
    path('delete-comment/<int:id>/', delete_comment, name='delete_comment'),
]