from requests import get, post, delete
from .models import Game
from .utils import __show, __skip_exception


BASE_URL = 'http://localhost:3000'


@__skip_exception
def get_all_games(games: list[Game], *, show=False):
    url = f'{BASE_URL}/games'
    response = get(url)
    body = response.json()

    

    if show:
        __show(body, games)

    if len(body) == len(games):
        content_match = all(
            game.is_valid(body[i])
            for i, game in enumerate(games)
        )

        return content_match
    print("Error en el get_all_games")
    print("No coinciden los valores del body con los valores de games")
    return False


@__skip_exception
def post_games(game: Game, *, show=False):
    url = f'{BASE_URL}/games'
    data = game.data()
    response = post(url, json=data)
    body = response.json()


    if show:
        __show(body, game)

    if response.status_code >= 400:
        return False

    if game.is_valid(body, is_new=True):
        game.id = body['id']

        return True

    return False


@__skip_exception
def get_game(game: Game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}'
    response = get(url)
    body = response.json()

    if show:
        __show(body, game)

    return game.is_valid(body)


@__skip_exception
def delete_game(games: list[Game], game: Game, *, show=False):
    url = f'{BASE_URL}/games/{game.id}'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, {})

    if body == {}:
        games.remove(game)
        return True
    return False


@__skip_exception
def delete_all_games(*, show=False):
    url = f'{BASE_URL}/games'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, [])

    return body == []


# @__skip_exception
# def get_city(teams: list[Team], *, show=False):
#     url = f'{BASE_URL}/team/city'
#     response = get(url)
#     body = response.json()


#     if show:
#         __show(body, team.city)

#     if len(body) == len(team.city):
#         content_match = all(
#             team.city[i].is_valid(body[i])
#             for i in range(len(team.city))
#         )

#         return content_match

#     return False
