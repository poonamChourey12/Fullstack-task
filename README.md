Landing page
Visitors to the app should be able to view a livestream video played from an 
RTSP URL (use RTSP me or RTSP stream to create a temporary stream from a 
video over internet). The video should be embedded on the landing page, and 
users can click play to start watching the livestream.

App
Playing Livestream: The app should be able to play a livestream video from 
a given RTSP URL. Users should have basic controls such as play, pause, 
and volume adjustment.
1.Overlay Options: Users should have the option to add custom overlays 
(such as logos and text) on top of the livestream. These overlays can be 
positioned and resized as needed.
2.CRUD API for Overlays and Settings:
•Create: Users should be able to create and save custom overlay 
settings, including position, size, and content.
•Read: Users should be able to retrieve their saved overlay settings.
•Update: Users should be able to modify existing overlay settings.
•Delete: Users should be able to delete saved overlay settings.

Tech Stack
● Python (Flask Preferred)
● MongoDB
● React
● Video Streaming compatible with RTSP

Deliverables
● Code Repo
● API Documentation detailing the CRUD endpoints and how to interact 
with them.
● User Documentation on how to set up and use the 
