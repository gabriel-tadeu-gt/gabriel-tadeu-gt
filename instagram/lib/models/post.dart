import 'package:cloud_firestore/cloud_firestore.dart';

class Post {
  String? caption;
  String? photoURL;
  String? username;
  String? postID;

  Post({this.caption, this.photoURL, this.username, this.postID});

  factory Post.fromFirestore(DocumentSnapshot doc) {
    return Post(
        caption: doc['caption'],
        photoURL: doc['photoURL'],
        username: doc['username'],
        postID: doc['postID']);
  }
}
