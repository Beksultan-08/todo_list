from django.urls import path
from blog.views import post, category

app_name = 'blog'

urlpatterns = [
path('categories/<int:pk>/', category.category_detail, name='category-detail'),
    # Посты
    path('posts/', post.post_list, name='post-list'),
    path('posts/<int:pk>/', post.post_detail, name='post-detail'),
    path('post/create/', post.post_create, name='post-create'),
    path('post/<int:pk>/edit/', post.post_edit, name='post-edit'),
    path('post/<int:pk>/delete/', post.post_delete, name='post-delete') ]


