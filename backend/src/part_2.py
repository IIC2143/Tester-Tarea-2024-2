from requests import get, post, patch, delete
from .utils import __show, __skip_exception
from copy import deepcopy

BASE_URL = 'http://localhost:3000'

@__skip_exception
def post_players(player, game, *, show=False):
    url = f'{BASE_URL}/players/{game.id}'
    player.favourite_game_id = game.id
    data = player.data()
    response = post(url, json=data)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, player)

    if response.status_code >= 400:
        return False, f"Error en la petición: {response.status_code}"
    
    if not player.is_valid(body, is_new=True):
        return False, "La respuesta de la request no coincide con lo esperado"
    
    player.id = body['id']
    return True, "Operación exitosa"

@__skip_exception
def delete_all_players(*, show=False):
    url = f'{BASE_URL}/players'
    response = delete(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, [])

    if body != []:
        return False, "No se pudieron eliminar todos los jugadores"

    return True, "Operación exitosa"

@__skip_exception
def get_player(player, *, show=False):
    url = f'{BASE_URL}/players/{player.id}'
    response = get(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, player)

    if not player.is_valid(body):
        return False, "La respuesta de la request no coincide con lo esperado"

    return True, "Operación exitosa"

@__skip_exception
def get_game_reviews(game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}/reviews'
    response = get(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, game.reviews)

    if len(body) != len(game.reviews):
        return False, "La cantidad de reseñas no coincide"

    content_match = all(
        match.is_valid(body[i])
        for i, match in enumerate(game.reviews)
    )

    if not content_match:
        return False, "La respuesta de la request no coincide con lo esperado"

    return True, "Operación exitosa"

@__skip_exception
def post_review(game, player, review, *, show=False):
    url = f'{BASE_URL}/reviews'
    review.game_id = game.id
    review.player_id = player.id
    data = review.data()
    response = post(url, json=data)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if show:
        __show(body, review)

    if response.status_code >= 400:
        return False, f"Error en la petición: {response.status_code}"
    
    if not review.is_valid(body, is_new=True):
        return False, "La respuesta de la request no coincide con lo esperado"
    
    game.reviews.append(review)
    review.id = body['id']
    return True, "Operación exitosa"

@__skip_exception
def patch_review(review, new_review_data, *, show=False):
    review.data()

    url = f'{BASE_URL}/reviews/{review.id}'
    data = new_review_data
    response = patch(url, json=data)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    if response.status_code >= 400:
        return False, f"Error en la petición: {response.status_code}"

    review_copy = deepcopy(review)
    review_copy.update(new_review_data)

    if show:
        __show(body, review_copy)

    if not review_copy.is_valid(body):
        return False, "La respuesta de la request no coincide con lo esperado"

    review.update(new_review_data)
    return True, "Operación exitosa"

@__skip_exception
def get_review_by_game(reviews, game, *, show=False):
    url = f'{BASE_URL}/reviews/{game.name}'
    response = get(url)
    
    try:
        body = response.json()
    except ValueError:
        return False, "Respuesta no es JSON"

    filtered_reviews = [
        review
        for review in reviews
        if game.id == review.game_id
    ]

    if show:
        __show(body, filtered_reviews)

    if len(body) != len(filtered_reviews):
        return False, "La cantidad de reseñas filtradas no coincide"

    content_match = all(
        review.is_valid(body[i])
        for i, review in enumerate(filtered_reviews)
    )

    if not content_match:
        return False, "La respuesta de la request no coincide con lo esperado"

    return True, "Operación exitosa"
