import 'package:flutter/material.dart';

class UserPosts extends StatelessWidget {
  final String username;
  final String photoURL;
  final String caption;
  final String postID;
  const UserPosts(
      {Key? key,
      required this.username,
      required this.photoURL,
      required this.caption,
      required this.postID})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        //Header
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Container(
                    width: 40,
                    height: 40,
                    decoration: const BoxDecoration(
                      color: Colors.grey,
                      shape: BoxShape.circle,
                    ),
                  ),
                  const SizedBox(
                    width: 10,
                  ),
                  Text(
                    username,
                    style: const TextStyle(fontWeight: FontWeight.bold),
                  ),
                ],
              ),
              const Icon(Icons.menu),
            ],
          ),
        ),
        //Photo
        Container(
          height: 400,
          decoration: BoxDecoration(
              image: DecorationImage(
                  image: NetworkImage(photoURL), fit: BoxFit.cover)),
        ),
        // below the post -> buttons and comments
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: const [
                  Icon(Icons.favorite),
                  Padding(
                    padding: EdgeInsets.symmetric(horizontal: 12.0),
                    child: Icon(Icons.chat_bubble_outline),
                  ),
                  Icon(Icons.share),
                ],
              ),
              const Icon(Icons.bookmark),
            ],
          ),
        ),

        //Liked by
        Padding(
          padding: const EdgeInsets.only(left: 16.0),
          child: Row(children: const [
            Text('Curtido por '),
            Text(
              'pedroigor_salvador',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            Text(' e '),
            Text(
              '253 outros',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
          ]),
        ),
        // caption
        Padding(
          padding: const EdgeInsets.only(left: 16.0, top: 8),
          child: RichText(
            text: TextSpan(
              style: const TextStyle(color: Colors.black),
              children: [
                TextSpan(
                    text: username,
                    style: const TextStyle(fontWeight: FontWeight.bold)),
                TextSpan(text: ' ' + caption),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
