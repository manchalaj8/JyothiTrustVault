from vault.views import home, upload_file, file_list
from django.contrib import admin
from django.urls import path
from vault.views import home, upload_file

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("upload/", upload_file, name="upload"),
]
from django.contrib import admin
from django.urls import path
from vault.views import home, upload_file, file_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('upload/', upload_file, name='upload'),
    path('files/', file_list, name='file_list'),
]
