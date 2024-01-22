from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main'),
    path('my_articles', views.articles_by_user_page, name='articles_by_user'),
    path('my_articles/<int:article_id>', views.edit_article_page, name='edit_article'),
    path('my_articles/delete/<int:article_id>', views.delete_article, name='delete_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
