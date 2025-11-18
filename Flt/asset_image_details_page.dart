add in yaml file 
dependencies:
  flutter:
    sdk: flutter
  google_fonts: ^6.1.0


then : 
flutter pub get


import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AssetImageDetailsPage extends StatelessWidget {
  final String assetPath = "assets/images/sample.jpg";
  final String title = "Image from Assets";
  final String description =
      "This image is loaded from the local assets folder in Flutter.";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Asset Image Details",
          style: GoogleFonts.poppins(),
        ),
        backgroundColor: Colors.blueAccent,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              // ---------- ASSET IMAGE ----------
              ClipRRect(
                borderRadius: BorderRadius.circular(12),
                child: Image.asset(
                  assetPath,
                  height: 250,
                  width: double.infinity,
                  fit: BoxFit.cover,
                ),
              ),

              SizedBox(height: 20),

              // ---------- TITLE ----------
              Text(
                title,
                style: GoogleFonts.poppins(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                ),
              ),

              SizedBox(height: 10),

              // ---------- ASSET PATH ----------
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Path: ",
                    style: GoogleFonts.poppins(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Expanded(
                    child: Text(
                      assetPath,
                      style: GoogleFonts.robotoMono(
                        color: Colors.blueGrey,
                      ),
                    ),
                  ),
                ],
              ),

              SizedBox(height: 15),

              // ---------- DESCRIPTION ----------
              Text(
                description,
                style: GoogleFonts.robotoMono(
                  fontSize: 16,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
