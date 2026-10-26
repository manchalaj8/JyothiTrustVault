from pathlib import Path
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Welcome to TrustVault</h1><p>Your secure file management application.</p>")

def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        upload_dir = Path(settings.MEDIA_ROOT) / "uploads"
        upload_dir.mkdir(parents=True, exist_ok=True)
        fs = FileSystemStorage(location=upload_dir)
        fs.save(uploaded_file.name, uploaded_file)
        return HttpResponse('File uploaded successfully! <br><br><a href="/files/">View Uploaded Files</a> | <a href="/upload/">Upload Another File</a>')
    return render(request, "vault/upload.html")

def file_list(request):
    upload_dir = Path(settings.MEDIA_ROOT) / "uploads"
    files = []
    if upload_dir.exists():
        files = [f.name for f in upload_dir.iterdir() if f.is_file()]
    return render(request, "vault/file_list.html", {"files": files})