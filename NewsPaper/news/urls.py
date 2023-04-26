from django.urls import path
from .views import News, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, Search
# from .views import index

urlpatterns = [
    path('', News.as_view()),
    # path('', index),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('search/', Search.as_view(), name='search'),
]
