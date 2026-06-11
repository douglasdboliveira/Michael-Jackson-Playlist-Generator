import random

# Biblioteca de músicas
musicas = [
    {"titulo": "Billie Jean", "album": "Thriller", "ano": 1982, "estilo": "pop"},
    {"titulo": "Beat It", "album": "Thriller", "ano": 1982, "estilo": "rock"},
    {"titulo": "Thriller", "album": "Thriller", "ano": 1982, "estilo": "pop"},
    {"titulo": "Smooth Criminal", "album": "Bad", "ano": 1987, "estilo": "pop"},
    {"titulo": "Man in the Mirror", "album": "Bad", "ano": 1987, "estilo": "balada"},
    {"titulo": "Don't Stop 'Til You Get Enough", "album": "Off the Wall", "ano": 1979, "estilo": "funk"},
]

def gerar_playlist(estilo=None, qtd=3):
    if estilo:
        filtradas = [m for m in musicas if m["estilo"] == estilo]
    else:
        filtradas = musicas
    
    return random.sample(filtradas, min(qtd, len(filtradas)))

# Exemplo de uso
playlist = gerar_playlist(estilo="pop", qtd=2)
print("Sua playlist Michael Jackson:")
for m in playlist:
    print(f"- {m['titulo']} ({m['album']}, {m['ano']})")
