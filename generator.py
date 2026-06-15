import random, requests

def generate_playlist(genre=None, era=None, number=3):
    response = requests.get("https://douglasdboliveira.pythonanywhere.com/songs")

    filtered = response.json()

    if genre:
        filtered = [s for s in filtered if genre.lower() in s["genre"].lower()]
    if era:
        filtered = [s for s in filtered if era.lower() in s["era"].lower()]

    return random.sample(filtered, min(number, len(filtered)))

playlist = generate_playlist(genre="pop", era="2000s", number=2)

print("Your Michael Jackson playlist:")
for s in playlist:
    print(f"- {s['title']} ({s['album']}, {s['era']})")
