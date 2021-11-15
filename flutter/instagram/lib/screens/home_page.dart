import 'package:flutter/material.dart';
import 'package:instagram/models/post.dart';
import 'package:instagram/screens/pages/home.dart';
import 'package:instagram/services/database_service.dart';
import 'package:provider/provider.dart';

final db = DatabaseService();

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  void _navigateBottomNavBar(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  final List<Widget> _children = [
    StreamProvider<List<Post>>.value(
      value: db.streamPosts(),
      initialData: const [],
      builder: (context, snapshot) {
        return Feed();
      },
    ),
    const Center(
      child: Text("Search"),
    ),
    const Center(
      child: Text("Reels"),
    ),
    const Center(
      child: Text("Shop"),
    ),
    const Center(
      child: Text("Profile"),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _children[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: _navigateBottomNavBar,
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.video_call), label: 'Reels'),
          BottomNavigationBarItem(icon: Icon(Icons.shop), label: 'Shop'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  }
}
