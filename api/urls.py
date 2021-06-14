from django.urls import path

from api import views

urlpatterns = [
    # path('users/', views.apiusers),
    path('articles/', views.ArticlesListView.as_view()),
    path('articles/<int:pk>', views.ArticlesDetailView.as_view())
]
