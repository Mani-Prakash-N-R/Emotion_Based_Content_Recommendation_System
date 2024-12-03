import base64
youtube_key = ''

client_id=''
client_secret=''
# base_64 = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

# YouTube playlist IDs for different emotions

# Spotify playlist IDs for different emotions

spotify_scopes='user-read-private user-read-email playlist-read-private playlist-modify-public'
spotify_redirect_uri=''
refresh_token=''
access_token = ''
# Encode client_id and client_secret to Base64
auth_str = f"{client_id}:{client_secret}"
base_64= base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')