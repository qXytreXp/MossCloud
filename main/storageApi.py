import requests
from django.conf import settings
       

session = requests.Session()  


def add_document(username, document):
    add_doc = session.post(f'{settings.STORAGE_API_URL}/api/main/add-doc/', data={'username':username, 'token':settings.STORAGE_API_TOKEN}, files={'document':document})

    return add_doc


def download_doc(username, document):
    download_doc_url = session.get(f'{settings.STORAGE_API_URL}/api/main/download-doc/{username}/{settings.STORAGE_API_TOKEN}/{document}')

    return download_doc_url


def get_my_document(username):
    get_doc = session.post(f'{settings.STORAGE_API_URL}/api/main/storage/', json={'username':username, 'token':settings.STORAGE_API_TOKEN})

    return get_doc.json()
    
    
def delete_document(username, document):
    del_doc = session.post(f'{settings.STORAGE_API_URL}/api/main/delete-doc/', json={'username':username, 'token':settings.STORAGE_API_TOKEN, 'document':document})

    return del_doc.json()

