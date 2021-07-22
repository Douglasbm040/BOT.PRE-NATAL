import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';

FirebaseFirestore firestore = FirebaseFirestore.instance;

class Firestore {
  void criardocumento(String collection, String document, Map<String,dynamic> data) async {
    firestore.collection(collection)
    .doc(document)
    .set(data); //instanciando o obj firestore para acessar a colecao
  }
}

































































//class GetUserName extends StatelessWidget {
//  final String documentId;
//
//  GetUserName(this.documentId);
//
//  @override
//  Widget build(BuildContext context) {
//    CollectionReference users = FirebaseFirestore.instance.collection('respostas');
//
//    return FutureBuilder<DocumentSnapshot>(
//      future: users.doc(documentId).get(),
//      builder:
//          (BuildContext context, AsyncSnapshot<DocumentSnapshot> snapshot) {
//
//        if (snapshot.hasError) {
//          return Text("Something went wrong");
//        }
//
//        if (snapshot.hasData && !snapshot.data!.exists) {
//          return Text("Document does not exist");
//        }
//
//        if (snapshot.connectionState == ConnectionState.done) {
//          Map<String, dynamic> data = snapshot.data!.data() as Map<String, dynamic>;
//          return Text("Full Name: ${data['conteudo']} ${data['dia']}");
//        }
//
//        return Text("loading");
//      },
//    );
//  }
//}