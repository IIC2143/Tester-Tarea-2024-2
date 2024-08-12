from requests import get, post, delete, patch
from copy import deepcopy
from .utils import __show, __skip_exception

BASE_URL = 'http://localhost:3000'

@__skip_exception
def get_teamfavouriteGame_player(player, games, *, show=False):
    url = f'{BASE_URL}/players/{player.id}/game'
    response = get(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, player.favourite_game_id)

    if body['id'] != player.favourite_game_id:
        return False, "La respuesta de la request no coincide con lo esperado"

    for game in games:
        if game.is_valid(body):
            return True, "Operación exitosa"

    return False, "La respuesta de la request no coincide con lo esperado"

@__skip_exception
def get_top_calification(games, quantity, *, show=False):
    url = f'{BASE_URL}/games/top/{quantity}'
    response = get(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    games_copy = deepcopy(games)
    sorted_games = sorted(games_copy, key=lambda game: (game.calification, game.id), reverse=True)
    selected = sorted_games[:quantity]

    if show:
        __show(body, selected)

    if len(selected) != len(body) or len(body) != quantity:
        return False, "La cantidad de juegos en la respuesta no coincide con lo esperado"

    if not all(game.is_valid(body[i]) for i, game in enumerate(selected)):
        return False, "La respuesta de la request no coincide con lo esperado"

    return True, "Operación exitosa"

@__skip_exception
def get_player_from_review(review, players, *, show=False):
    url = f'{BASE_URL}/reviews/{review.id}/player'
    response = get(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, review.player_id)

    if body['id'] != review.player_id:
        return False, "La respuesta de la request no coincide con lo esperado"

    for player in players:
        if player.is_valid(body):
            return True, "Operación exitosa"

    return False, "La respuesta de la request no coincide con lo esperado"

@__skip_exception
def delete_worst_game(games, reviews, *, show=False):
    url = f'{BASE_URL}/games/low'
    response = delete(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    lowest_game = min(games, key=lambda game: (game.calification, 1 - len(game.reviews)))

    if show:
        __show(body, lowest_game)

    if not lowest_game.is_valid(body):
        return False, "La respuesta de la request no coincide con lo esperado"

    if lowest_game.reviews:
        for review in lowest_game.reviews:
            reviews.remove(review)

    lowest_game.destroy()
    games.remove(lowest_game)

    return True, "Operación exitosa"

@__skip_exception
def patch_update_game_calification(game, *, show=False):
    url = f'{BASE_URL}/games/calification_update/{game.id}'
    game.calification = game.calculate_points()
    data = game.data()
    response = patch(url, json=data)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if response.status_code >= 400:
        return False, f"Error en la petición: {response.status_code}"

    if show:
        __show(body, game)

    if not game.is_valid(body):
        return False, "La respuesta de la request no coincide con lo esperado"

    game.update(data)
    return True, "Operación exitosa"
