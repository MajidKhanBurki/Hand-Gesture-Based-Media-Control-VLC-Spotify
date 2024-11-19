import spotipy
from spotipy.oauth2 import SpotifyOAuth

from utils import spotify_credentials

# Initialize Spotify client with Spotipy
scope = "user-read-playback-state user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_credentials.SPOTIPY_CLIENT_ID,
    client_secret=spotify_credentials.SPOTIPY_CLIENT_SECRET,
    redirect_uri=spotify_credentials.SPOTIPY_REDIRECT_URI,
    scope=scope
))

# Spotify control functions
def play_spotify():
    try:
        sp.start_playback()
        print("Playing on Spotify")
    except Exception as e:
        print("Error playing on Spotify:", e)

def pause_spotify():
    try:
        sp.pause_playback()
        print("Paused on Spotify")
    except Exception as e:
        print("Error pausing on Spotify:", e)

def next_track():
    try:
        sp.next_track()
        print("Next track on Spotify")
    except Exception as e:
        print("Error skipping track:", e)

def previous_track():
    try:
        sp.previous_track()
        print("Previous track on Spotify")
    except Exception as e:
        print("Error going back to previous track:", e)

def volume_up():
    try:
        current_volume = sp.current_playback()["device"]["volume_percent"]
        new_volume = min(100, current_volume + 10)
        sp.volume(new_volume)
        print(f"Volume up: {new_volume}%")
    except Exception as e:
        print("Error adjusting volume up:", e)

def volume_down():
    try:
        current_volume = sp.current_playback()["device"]["volume_percent"]
        new_volume = max(0, current_volume - 10)
        sp.volume(new_volume)
        print(f"Volume down: {new_volume}%")
    except Exception as e:
        print("Error adjusting volume down:", e)

def handle_gesture(gesture):
    """Handle gestures for Spotify control."""
    if gesture == "Open Hand":  # Play
        play_spotify()
    elif gesture == "Closed Fist":  # Pause
        pause_spotify()
    elif gesture == "Two Fingers Up":  # Next Track
        next_track()
    elif gesture == "One Finger Up":  # Volume Up
        volume_up()
    elif gesture == "Pinky Finger Up":  # Volume Down
        volume_down()