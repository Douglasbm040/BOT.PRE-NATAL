
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"C:\Users\dougl\Downloads\florence-30632-firebase-adminsdk-zloyg-ca1547373c.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# adicionar dados ao banco

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1816
})

#ler dados 

users_ref = db.collection(u'users')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


