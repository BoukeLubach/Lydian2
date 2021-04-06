from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UploadForm, CsvProcessSettingsForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Tagmodel, Datafile, Batch
import pandas as pd

# function to handle an uploaded file.
from .process_uploaded_files import handle_uploaded_file, process_dataframe


# @login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('csvfile')

            for f in files:
                handle_uploaded_file(f)

            return redirect('home')

    else:
        form = UploadForm()
    return render(request, 'file_upload/upload_form.html', {'form': form})


def upload_failed_view(request):

    return render(request, 'file_upload/upload_failed.html')


# @login_required
def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            # csvfile_instance = request.FILES['csvfile']       
        
            csvfile_instance = form.save()

            return redirect('dataframe_preview', pk=csvfile_instance.id)

    else:
        form = UploadForm()
    return render(request, 'file_upload/upload_csvfile.html', {'form': form})



def dataframe_preview(request, pk):

    file_object = Datafile.objects.get(id=pk)
    df = pd.read_csv(file_object.csvfile.path, encoding='UTF-8', sep=';')

    if request.method=="POST":
        form = CsvProcessSettingsForm(request.POST, request.FILES)

        if form.is_valid():
            batch = Batch(
                skiprows = form.cleaned_data.get("rowsToSkip"),
                dayfirst = form.cleaned_data.get("dayfirst"),
                datafile = file_object,
                tagsIdentified = df.shape[1],
            )
            batch.save()
            batchId = batch.id

            for tagname in df.columns:

                tag_instance = Tagmodel(name=tagname, 
                                        batch = batch)
                tag_instance.save()

            return redirect('select_tags_to_store', pk=batchId)

    else:
        form = CsvProcessSettingsForm()
        dftable = df.head().to_html()

    
    context = {
        "dftable" : dftable,
        "form": form,
    }
    return render(request, 'file_upload/dataframe_preview.html', context = context)

def select_tags_to_store(request, pk):
    context = {}
    tagsToSave = []
    batch = Batch.objects.get(id=pk)
    identified_tags = Tagmodel.objects.filter(batch=Batch.objects.get(id=pk))
    if request.method =="POST":
        for i in range(batch.tagsIdentified):
            tagsToSave.append(request.POST.get(f'tag{i}'))
            # Tagmodel.objects.get(id=pk, )
        tagsToSave = [False if v is None else True for v in tagsToSave]

        for index, tag in enumerate(identified_tags):
            print(tagsToSave[index])
            if not tagsToSave[index]:
                tag.delete()
    else:
        
        context = {
            'identified_tags': identified_tags
        }
    return render(request, 'file_upload/select_tags_to_store.html', context=context)