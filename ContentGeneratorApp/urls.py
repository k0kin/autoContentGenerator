from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create_article/', views.create_article, name='create_article'),
    path('save_article/', views.save_article, name='save_article'),
    path('article/<int:article_id>/', views.display_article, name='display_article'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)