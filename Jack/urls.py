from django.urls import path
from .views import (
    HomeView,
    ProjectListView,
    ProjectDetailView,
    contact_view,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('contact/', contact_view, name='contact'),
]