# myapp/urls.py

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import ItemList,AirdropDetailView,AirdropCreateOrUpdate

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('user', AirdropCreateOrUpdate.as_view(), name='item-list'),
    path('<int:id>/', AirdropDetailView.as_view(), name='airdrop-detail'),  

]
if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)