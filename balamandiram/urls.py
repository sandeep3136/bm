from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('library', views.library, name='library'),
    path('lib/science', views.scibooks, name='scibooks'),
    path('lib/childlit', views.childlit, name='childlit'),
    path('lib/mags', views.mags, name='mags'),
    path('lib/langs', views.langbooks, name='langbooks'),
    path('activities', views.activities, name='activities'),
]