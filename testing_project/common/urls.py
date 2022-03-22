
from django.contrib import admin
from django.urls import path

from testing_project.common.views import ProfileCreateView, ProfilesListView, ProfileDetailsView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('lists/', ProfilesListView.as_view(), name='profile lists'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
]
