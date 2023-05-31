from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, uploadN, newsOut, competitionOut
urlpatterns = [
    path('competition/', competitionOut, name="competition"),
    path('news', newsOut, name="news"),
    path('upload/', uploadN, name="upload"),
    path('', home, name="home"),
]+static(settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)