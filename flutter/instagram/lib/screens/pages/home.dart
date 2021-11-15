import 'package:flutter/material.dart';
import 'package:instagram/models/post.dart';
import 'package:instagram/widgets/bubblestories.dart';
import 'package:instagram/widgets/userposts.dart';
import 'package:provider/provider.dart';

class Feed extends StatelessWidget {
  Feed({Key? key}) : super(key: key);

  final List people = [
    'eiji.tomonari',
    'pedroigor_salvador',
    'bia_iama',
    'antonio.junior366',
    'pseudo.emily',
    'treinamento_flutter',
  ];

  @override
  Widget build(BuildContext context) {
    final posts = Provider.of<List<Post>>(context);
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        foregroundColor: Colors.black,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            const Text("Instagram"),
            Row(
              children: const [
                Icon(Icons.add, color: Colors.black),
                Icon(Icons.favorite, color: Colors.black),
                Icon(Icons.share, color: Colors.black)
              ],
            )
          ],
        ),
        elevation: 0,
      ),
      body: Column(
        children: [
          //Stories
          const Divider(
            thickness: 1.5,
          ),
          SizedBox(
            height: 130,
            child: ListView.builder(
              itemCount: people.length,
              scrollDirection: Axis.horizontal,
              itemBuilder: (context, index) {
                return BubbleStories(text: people[index]);
              },
            ),
          ),
          const Divider(
            thickness: 1.5,
          ),
          //Posts
          Expanded(
              child: ListView.builder(
            itemCount: posts.length,
            itemBuilder: (context, index) {
              return UserPosts(
                username: posts[index].username!,
                photoURL: posts[index].photoURL!,
                caption: posts[index].caption!,
                postID: posts[index].postID!,
              );
            },
          ))
        ],
      ),
    );
  }
}
