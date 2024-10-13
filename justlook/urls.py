from django.urls import path, include

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('airdrops.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),

]
