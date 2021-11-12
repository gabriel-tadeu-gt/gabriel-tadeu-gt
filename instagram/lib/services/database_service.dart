import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:instagram/models/post.dart';

class DatabaseService {
  final FirebaseFirestore _db = FirebaseFirestore.instance;

  Stream<List<Post>> streamPosts() {
    var ref = _db.collection('posts');
    return ref.snapshots().map(
        (list) => list.docs.map((doc) => Post.fromFirestore(doc)).toList());
  }
}
