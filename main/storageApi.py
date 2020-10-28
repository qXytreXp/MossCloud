import requests
       

session = requests.Session()
address = 'http://127.0.0.1:8000'
token = '43880072'    


def add_document(username, document):
    add_doc = session.post(f'{address}/api/main/add-doc/', data={'username':username, 'token':token}, files={'document':document})

    return add_doc


def download_doc(username, document):
    download_doc_url = session.get(f'{address}/api/main/download-doc/{username}/{token}/{document}')

    return download_doc_url


def get_my_document(username):
    get_doc = session.post(f'{address}/api/main/storage/', json={'username':username, 'token':token})

    return get_doc.json()
    
    
def delete_document(username, document):
    del_doc = session.post(f'{address}/api/main/delete-doc/', json={'username':username, 'token':token, 'document':document})

    return del_doc.json()
