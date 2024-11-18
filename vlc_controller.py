import vlc
import os

# Setup VLC instance
media_folder = "media"
media_files = [os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith('.mp3')]

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
current_track_index = 0

def play_track(index):
    media = vlc_instance.media_new(media_files[index])
    player.set_media(media)
    player.play()

def handle_gesture(gesture):
    global current_track_index

    if gesture == "Open Hand":  # Play
        if not player.is_playing():
            play_track(current_track_index)
            print("Playing track")
    elif gesture == "Closed Fist":  # Pause
        if player.is_playing():
            player.pause()
            print("Paused")
    elif gesture == "One Finger Up":  # Volume Up
        volume = player.audio_get_volume()
        player.audio_set_volume(min(100, volume + 10))
        print("Volume Up")
    elif gesture == "Two Fingers Up":  # Next Track
        current_track_index = (current_track_index + 1) % len(media_files)
        play_track(current_track_index)
        print("Next Track")
    elif gesture == "Pinky Finger Up":  # Volume Down
        volume = player.audio_get_volume()
        player.audio_set_volume(max(0, volume - 10))
        print("Volume Down")
