image_details_page.dart

import 'package:flutter/material.dart';

class ImageDetailsPage extends StatelessWidget {
  final String imageUrl =
      "https://images.unsplash.com/photo-1506744038136-46273834b3fb"; // your image URL
  final String title = "Image from URL";
  final String description =
      "This image is loaded from the internet using Image.network().";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Network Image Details"),
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              // ---------- IMAGE ----------
              ClipRRect(
                borderRadius: BorderRadius.circular(12),
                child: Image.network(
                  imageUrl,
                  height: 250,
                  width: double.infinity,
                  fit: BoxFit.cover,
                  loadingBuilder: (context, child, progress) {
                    if (progress == null) return child;
                    return Center(
                        child: CircularProgressIndicator(
                      value: progress.expectedTotalBytes != null
                          ? progress.cumulativeBytesLoaded /
                              progress.expectedTotalBytes!
                          : null,
                    ));
                  },
                  errorBuilder: (context, error, stackTrace) =>
                      Icon(Icons.error, size: 80, color: Colors.red),
                ),
              ),

              SizedBox(height: 20),

              // ---------- TITLE ----------
              Text(
                title,
                style: TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                ),
              ),

              SizedBox(height: 10),

              // ---------- URL ----------
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "URL: ",
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  Expanded(
                    child: Text(
                      imageUrl,
                      style: TextStyle(color: Colors.blueGrey),
                    ),
                  ),
                ],
              ),

              SizedBox(height: 15),

              // ---------- DESCRIPTION ----------
              Text(
                description,
                style: TextStyle(fontSize: 16),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
