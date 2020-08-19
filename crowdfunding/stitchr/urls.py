from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('stitchr/', views.StitchrList.as_view()),
    path('stitchr/<int:pk>/', views.StitchrDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)