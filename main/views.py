from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from . import storageApi
from django.conf import settings


class MainView(View):
    def get(self, request):
        if request.user.is_authenticated:
            json = storageApi.get_my_document(request.user.username)
            for doc in json:
                try:
                    doc['document'] = doc['document'].replace('media', '').replace(request.user.username, '').replace('/', '')
                except TypeError:
                    return render(request, 'login.html', {'errors': ['Sorry, Error!']})

            return render(request, 'main.html', {'files':json})
        return redirect('login')


class DeleteDocumentView(View):
    def get(self, request, filename):
        if request.user.is_authenticated:
            storageApi.delete_document(request.user.username, filename)

            return redirect('main')
        return redirect('login')


class DownloadDocumentView(View):
    def get(self, request, filename):
        if request.user.is_authenticated:
            username = request.user.username
            
            return redirect(f'http://127.0.0.1:8000/api/main/download-doc/{username}/{settings.STORAGE_API_TOKEN}/{filename}')
        return redirect('login')


class AddDocumentView(View):
    def post(self, request):
        if request.user.is_authenticated:
            doc = request.FILES['file']

            storageApi.add_document(request.user.username, doc)
            return redirect('main')
        return redirect('login')

        


        
