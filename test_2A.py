from copy import deepcopy

from src.part_1 import (
    get_all_games,
    post_games,
    get_game,
    delete_game,
    delete_all_games,
)

from src.part_2 import (
    post_players,
    delete_all_players,
    get_player,
    get_game_reviews,
    post_review,
    patch_review,
    get_review_by_game
)

from data import GAMES_A, REVIEWS_A, PLAYERS_A


def test_2A():
    games = deepcopy(GAMES_A[0:4])
    reviews = deepcopy(REVIEWS_A[0:6])
    players = deepcopy(PLAYERS_A[0:3])

    results = {
        1: delete_all_games(),
        2: delete_all_players(),
        2: post_games(games[0]),
        3: post_games(games[1]),
        4: post_games(games[2]),
        5: post_games(games[3]),
        6: post_players(players[0], games[0]),
        7: post_players(players[1], games[1]),
        8: post_players(players[2], games[2]),
        9: get_player(players[0]),
        10: get_player(players[1]),
        11: get_player(players[2]),
        12: get_all_games(games),
        7: post_review(games[0],players[0], reviews[0]),
        8: post_review(games[1],players[1], reviews[1]),
        9: post_review(games[2],players[2], reviews[2]),
        13: get_game_reviews(games[0]),
        14: get_game_reviews(games[1]),
        15: get_game_reviews(games[2]),
        16: patch_review(reviews[0], {'review': {'rating': 5.0}}),
        17: get_game(games[0]),
        18: get_game(games[1]),
        19: get_game(games[2]),
        20: get_game(games[3]),
    }

    return results


if __name__ == '__main__':
    results = test_2A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
