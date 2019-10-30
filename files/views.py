from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .forms import UploadFileForm, FileUploadForm
from utils import upload

from .models import Files


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # instance = Files(file_field=request.FILES['file'])
            form.save()
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def test_view(request):

    def do_this(file_object):
        upload.upload_dataset(upload.auth_client, file_object)
    if request.method == 'POST' and 'run_script' in request.POST:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_object = form.cleaned_data['file_source']
            # form.save()
            # return HttpResponseRedirect('/success/url/')
            do_this(file_object)
            return redirect('home')
    else:
        form = FileUploadForm()
        # import function to run
        # from path_to_script import function_to_run

        # call function

        
        # return user to required page

    return render(request, 'test.html', {'form': form})
