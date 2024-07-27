from requests import get, post, delete
from copy import deepcopy
from .utils import __show, __skip_exception


BASE_URL = 'http://localhost:3000'


@__skip_exception
def get_teamfavourateGame_player(player,games ,*, show=False):
    url = f'{BASE_URL}/players/{player.id}/game'
    response = get(url)
    body = response.json()

    if show:
        __show(body, player.favourite_game_id)


    if body['id'] == player.favourite_game_id:
        for game in games:
            if game.is_valid(body):
                return True

    return False


@__skip_exception
def get_top_calification(games, quantity, *, show=False):
    url = f'{BASE_URL}/games/top/{quantity}'
    response = get(url)
    body = response.json()

    games_copy = deepcopy(games)

    sorted_games = sorted(games_copy, key=lambda game: game.calification, reverse=True)
    selected = sorted_games[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
        return all(
            game.is_valid(body[i])
            for i, game in enumerate(selected)
        )

    return False

'''@__skip_exception
def get_player_top_cards(player, quantity, *, show=False):
    url = f'{BASE_URL}/players/topCards/{quantity}'
    response = get(url)
    body = response.json()
    players_copy = deepcopy(player)

    sorted_player = sorted(players_copy, key=lambda player: player.card, reverse=False)

    selected = sorted_player[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
    
        return all(
            player.is_valid(body[i])
            for i, player in enumerate(selected)
        )

    return False'''

'''@__skip_exception
def get_player_top_assists(player, quantity, *, show=False):
    url = f'{BASE_URL}/players/topAssists/{quantity}'
    response = get(url)
    body = response.json()

    players_copy = deepcopy(player)

    sorted_player = sorted(players_copy, key=lambda player: player.assist/(player.assist+player.goal), reverse=True)
    selected = sorted_player[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
        return all(
            player.is_valid(body[i])
            for i, player in enumerate(selected)
        )

    return False'''


@__skip_exception
def get_player_from_review(review, players, *, show=False): 
    url = f'{BASE_URL}/reviews/{review.id}/player'
    response = get(url)
    body = response.json()

    if show:
        __show(body, review.player_id)

    
    if body['id'] == review.player_id:
        for player in players:
            if player.is_valid(body):
                return True

    return False


@__skip_exception
def delete_worst_game(games, reviews, players, *, show=False): #B
    url = f'{BASE_URL}/games/low'
    response = delete(url)
    body = response.json()


    lowest_game = min(games, key=lambda game: (game.calculate_points(), 1 - len(game.reviews)))


    if show:
        __show(body, lowest_game)

    if lowest_game.is_valid(body):

        reviews.remove(lowest_game.reviews)

        lowest_game.destroy()

        games.remove(lowest_game)


        return True

    return False
        

@__skip_exception
def patch_update_game_calification(game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}'
    game.calification = game.calculate_points()
    data = game.data()
    response = post(url, json=data)
    body = response.json()


    if response.status_code >= 400:
        return False

    if show:
        __show(body, game)


    if game.is_valid(body):
        game.update(data)

        return True

    return False