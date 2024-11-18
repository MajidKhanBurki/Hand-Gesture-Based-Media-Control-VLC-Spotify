# VLC & Spotify Media Player Gesture Control

This project uses **Python**, **OpenCV**, **MediaPipe**, **Spotipy**, and **python-vlc** to control both VLC and Spotify using hand gestures detected through your webcam. The system allows you to play/pause music, change tracks, and adjust volume using intuitive hand gestures.

## 📋 Project Structure

```
project_folder/
├── gesture_recognition.py
├── vlc_controller.py
├── spotify_controller.py
├── main.py
└── media/
    ├── song1.mp3
    ├── song2.mp3
    └── ...
```

### Files:
- `gesture_recognition.py`: Handles gesture detection using MediaPipe.
- `vlc_controller.py`: Manages VLC media player actions based on gestures.
- `spotify_controller.py`: Manages Spotify playback using gestures.
- `main.py`: Orchestrates the gesture detection and controls either VLC or Spotify based on a command-line flag.
- `media/`: Folder containing your `.mp3` files for VLC playback.

## Features

- Control **VLC** or **Spotify** using hand gestures:
  - 🖐️ **Open Hand**: Play the current track.
  - ✊ **Closed Fist**: Pause the current track.
  - ☝️ **One Finger Up (Index Finger)**: Increase volume.
  - ✌️ **Two Fingers Up (Index & Middle Fingers)**: Skip to the next track.
  - 🤙 **Pinky Finger Up**: Decrease volume.

## Prerequisites

Ensure you have **Python 3** installed on your system.

### Install the required libraries:

```bash
pip install opencv-python mediapipe python-vlc spotipy
```

### Spotify Setup
1. Create a **Spotify Developer Account**:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app and get your **Client ID** and **Client Secret**.
   - Set the Redirect URI to `http://localhost:8888/callback`.

2. Update `spotify_credentials.py` with your credentials:
   ```python
   SPOTIPY_CLIENT_ID = 'your_client_id'
   SPOTIPY_CLIENT_SECRET = 'your_client_secret'
   SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
   ```

## Setup

1. Clone this repository or download the project files.
2. Add your `.mp3` music files to the `media/` folder for VLC playback.
3. Make sure your webcam is connected and accessible.

## ▶Running the Project

### Usage
The `main.py` script accepts a flag to choose between **VLC** or **Spotify** mode:

- **VLC Mode**:
  ```bash
  python main.py --mode vlc
  ```

- **Spotify Mode**:
  ```bash
  python main.py --mode spotify
  ```

### What Each Mode Does
- **VLC Mode**: Controls playback of `.mp3` files in the `media/` folder.
- **Spotify Mode**: Controls your Spotify playback on any active Spotify device.

## Usage Instructions

1. **Start Spotify Playback**:
   - For Spotify mode, you may need to **manually start playback** on any device (web player, desktop app, or mobile app) before using the gesture controls.

2. **Hand Gestures**:
   - 🖐️ **Open Hand**: Play the current track.
   - ✊ **Closed Fist**: Pause the current track.
   - ☝️ **One Finger Up (Index Finger)**: Increase volume.
   - ✌️ **Two Fingers Up (Index & Middle Fingers)**: Skip to the next track.
   - 🤙 **Pinky Finger Up**: Decrease volume.

3. **Cooldown Period**:
   - A **5-second delay** is set between consecutive gesture actions to prevent accidental triggers.

## Troubleshooting

### Spotify Issues:
- If you encounter `No active device found`, make sure to:
  - Start playback manually in your Spotify app (browser, desktop, or mobile).
  - Ensure your **Client ID**, **Client Secret**, and **Redirect URI** are correctly set.

### General Issues:
- Ensure your webcam is properly connected.
- Check if the `media/` folder contains valid `.mp3` files for VLC mode.
- If gestures aren't detected correctly, adjust your lighting conditions and try different hand positions.

## Future Improvements

- Add more gestures for additional controls (e.g., previous track, mute).
- Implement support for controlling video files.
- Add voice feedback for gesture detection.

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to fork the project, submit pull requests, or report issues.

## Contact

If you have any questions or suggestions, feel free to reach out!

---