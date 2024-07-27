from requests import get, post, patch, delete
from .utils import __show, __skip_exception
from copy import deepcopy


BASE_URL = 'http://localhost:3000'

@__skip_exception
def post_players(player,game ,*, show=False):
    url = f'{BASE_URL}/players/{game.id}'
    player.favorite_game = game.id
    data = player.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, player)

    if response.status_code >= 400:
        return False

    if player.is_valid(body, is_new=True):
        player.id = body['id']
        return True
    
    return False

@__skip_exception
def delete_all_players(player, *, show=False):
    url = f'{BASE_URL}/players'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, [])


    return body == []

@__skip_exception
def get_player(player, *, show=False):
    url = f'{BASE_URL}/players/{player.id}'
    response = get(url)
    body = response.json()

    if show:
        __show(body, player)

    return player.is_valid(body)


@__skip_exception
def get_game_reviews(game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}/reviews'
    response = get(url)
    body = response.json()

    if show:
        __show(body, game.reviews)

    if len(body) == len(game.reviews):
        content_match = all(
            match.is_valid(body[i])
            for i, match in enumerate(game.reviews)
        )

        return content_match

    return False


@__skip_exception
def post_review(game, player, review, *, show=False):
    url = f'{BASE_URL}/reviews'
    review.game_id = game.id
    review.player_id = player.id
    data = review.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, review)

    if response.status_code >= 400:
        return False
    

    if review.is_valid(body, is_new=True):
        game.reviews.append(review)
        review.id = body['id']

        return True

    return False


@__skip_exception
def patch_review(review, new_review_data, *, show=False):
    url = f'{BASE_URL}/matches/{review.id}'
    data = new_review_data

    response = patch(url, json=data)
    

    body = response.json()

    if response.status_code >= 400:
        return False

    review_copy = deepcopy(review)
    review_copy.update(new_review_data)

    if show:
        __show(body, review_copy)


    if review_copy.is_valid(body):
        review.update(new_review_data)

        return True

    return False


@__skip_exception
def get_review_by_game(reviews, game, *, show=False):
    url = f'{BASE_URL}/reviews/{game.name}'
    
    response = get(url)
    body = response.json()

    filtered_reviews = [
        review
        for review in reviews
        if game.id == review.game_id
    ]


    if show:
        __show(body, filtered_reviews)
    if len(body) == len(filtered_reviews):
        content_match = all(
            review.is_valid(body[i])
            for i, review in enumerate(filtered_reviews)
        )

        return content_match

    return False
