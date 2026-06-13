import random

songs = [
    {"title": "Billie Jean", "album": "Thriller", "year": 1982, "genre": "pop"},
    {"title": "Beat It", "album": "Thriller", "year": 1982, "genre": "rock"},
    {"title": "Thriller", "album": "Thriller", "year": 1982, "genre": "pop"},
    {"title": "Smooth Criminal", "album": "Bad", "year": 1987, "genre": "pop"},
    {"title": "Man in the Mirror", "album": "Bad", "year": 1987, "genre": "ballad"},
    {"title": "Don't Stop 'Til You Get Enough", "album": "Off the Wall", "year": 1979, "genre": "funk"},
]

def generate_playlist(year=None, number=3):
    if year:
        filtered = [s for s in songs if s["year"] == year]
    else:
        filtered = songs
    
    return random.sample(filtered, min(number, len(filtered)))

playlist = generate_playlist(year=1982, number=2)
print("Your Michael Jackson playlist:")
for s in playlist:
    print(f"- {s['title']} ({s['album']}, {s['year']})")
