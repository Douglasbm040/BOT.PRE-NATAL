
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
class db_firebase():
    cred = credentials.Certificate(r"C:\Users\dougl\Downloads\florence-30632-firebase-adminsdk-zloyg-ca1547373c.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()


    # adicionar dados ao banco
    #doc_ref = db.collection(u'users').document(u'alovelace')
    #doc_ref.set({
    #    u'first': u'Ada',
    #    u'last': u'Lovelace',
    #    u'born': 1816
    #})
    def add_dados(obj_firestore,nomedacolecao,document,set_dados):
        doc_ref = obj_firestore.collection(nomedacolecao).document(document)
        doc_ref.set(set_dados)
        print('adicionado com sucesso')
        


    #ler dados 
    def acessar_firebase(nomedacolecao):
        colecao = db.collection(nomedacolecao) #u'xpath_whats_app'
        docs = colecao.stream()
        for doc in docs:
            registros = doc.to_dict()
        return registros 

    print(registros['nome da função']['click_box_contact'])



