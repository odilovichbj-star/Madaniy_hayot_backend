"""
Madaniy Hayot — Core App URL Configuration
"""

from django.urls import path
from .views import (
    ServiceListView,
    ProjectListView,
    TeamMemberListView,
    NewsListView,
    NewsDetailView,
    ContactMessageCreateView,
    CompanyInfoView,
    HeroBannerListView,
)

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('team/', TeamMemberListView.as_view(), name='team-list'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-create'),
    path('company-info/', CompanyInfoView.as_view(), name='company-info'),
    path('banners/', HeroBannerListView.as_view(), name='banner-list'),
]
