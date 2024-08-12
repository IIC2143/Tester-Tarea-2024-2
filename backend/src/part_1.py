from requests import get, post, delete
from .models import Game
from .utils import __show, __skip_exception

BASE_URL = 'http://localhost:3000'

@__skip_exception
def get_all_games(games: list[Game], *, show=False):
    url = f'{BASE_URL}/games'
    response = get(url)

    try:
        body = response.json()
    except ValueError:
        return False, "La respuesta no contiene un JSON"

    if show:
        __show(body, games)

    if len(body) != len(games):
        return False, "La cantidad de juegos no coincide"

    content_match = all(
        game.is_valid(body[i])
        for i, game in enumerate(games)
    )

    if not content_match:
        return False, "El contenido de los juegos no coincide"

    return True, "Operación exitosa"

@__skip_exception
def post_games(game: Game, *, show=False):
    url = f'{BASE_URL}/games'
    data = game.data()
    response = post(url, json=data)

    try:
        body = response.json()
    except ValueError:
        return False, "La respuesta no contiene un JSON"

    if show:
        __show(body, game)

    if response.status_code >= 400:
        return False, f"Error en la petición: {response.status_code}"

    if not game.is_valid(body, is_new=True):
        return False, "Los datos del juego no son válidos"

    game.id = body['id']
    return True, "Operación exitosa"

@__skip_exception
def get_game(game: Game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}'
    response = get(url)

    try:
        body = response.json()
    except ValueError:
        return False, "La respuesta no contiene un JSON"

    if show:
        __show(body, game)

    if not game.is_valid(body):
        return False, "Los datos del juego no coinciden"

    return True, "Operación exitosa"

@__skip_exception
def delete_game(games: list[Game], game: Game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}'
    response = delete(url)

    try:
        body = response.json()
    except ValueError:
        return False, "La respuesta no contiene un JSON"

    if show:
        __show(body, {})

    if body != {}:
        return False, "No se pudo eliminar el juego"

    games.remove(game)
    return True, "Operación exitosa"

@__skip_exception
def delete_all_games(*, show=False):
    url = f'{BASE_URL}/games'
    response = delete(url)

    try:
        body = response.json()
    except ValueError:
        return False, "La respuesta no contiene un JSON"

    if show:
        __show(body, [])

    if body != []:
        return False, "No se pudieron eliminar todos los juegos"

    return True, "Operación exitosa"
