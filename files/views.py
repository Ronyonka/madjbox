from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

from .models import Files

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Files(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})