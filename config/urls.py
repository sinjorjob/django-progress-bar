from django.contrib import admin
from django.urls import path
from app.views import FileUploadView #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FileUploadView.as_view(), name="home"),  #追加
]
