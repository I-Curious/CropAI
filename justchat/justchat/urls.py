# mysite/urls.py
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
	path('', include('pwa.urls')),
    path('chat/', include('chat.urls',namespace='chat')),
    path('admin/', admin.site.urls),
]