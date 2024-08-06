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
from data import GAMES_B, REVIEWS_B, WRONG_REVIEWS, PLAYERS_B


def test_2B():
    games = deepcopy(GAMES_B[0:3])
    reviews = deepcopy(REVIEWS_B[0:6])
    players = deepcopy(PLAYERS_B[0:3])
    bad_reviews = deepcopy(WRONG_REVIEWS[0:3])

    results = {
        1: delete_all_games(),
        2: delete_all_players(),
        3: post_games(games[0]),
        4: post_games(games[1]),
        5: post_games(games[2]),
        6: get_all_games(games),
        7: post_players(players[0], games[0]),
        8: post_players(players[1], games[1]),
        9: post_players(players[2], games[2]),
        10: post_review(games[0],players[0], reviews[0]),
        11: post_review(games[1],players[1], reviews[1]),
        12: post_review(games[2], players[2], reviews[2]),
        13: get_game_reviews(games[0]),
        14: get_game_reviews(games[1]),
        15: get_game_reviews(games[2]),
        16: get_review_by_game(reviews, games[0]),
        17: get_review_by_game(reviews, games[1]),
        18: get_review_by_game(reviews, games[2]),
        19: patch_review(reviews[0], {'review': {'title': 'New Title'}}),
        20: get_game(games[0]),
        21: get_game(games[1]),
    }

    return results


if __name__ == '__main__':
    results = test_2B()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
