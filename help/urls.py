from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('help/', views.helpListView.as_view()),
    path('help/<str:pk>/', views.helpDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
