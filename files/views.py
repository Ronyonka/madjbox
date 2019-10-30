from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .forms import UploadFileForm
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

    if request.method == 'POST' and 'run_script' in request.POST:

        # import function to run
        # from path_to_script import function_to_run

        # call function
        def do_this():
            upload.upload_dataset(upload.auth_client, upload.LOCAL_FILE_OR_URL)
        do_this()
        # return user to required page

    return render(request, 'test.html')
