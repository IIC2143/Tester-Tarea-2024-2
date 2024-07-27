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

from data import GAMES_A, REVIEWS_B, WRONG_GAMES, WRONG_REVIEWS, PLAYERS_A


def test_2C():
    players = deepcopy(PLAYERS_A[0:3])
    games = deepcopy(GAMES_A[0:7])
    bad_games = deepcopy(WRONG_GAMES[0:4])
    reviews = deepcopy(REVIEWS_B[0:6])
    bad_reviews = deepcopy(WRONG_REVIEWS)

    results = {
        1: delete_all_games(),
        2: delete_all_players(),
        3: post_games(games[0]),
        4: post_games(games[1]),
        5: post_games(games[2]),
        6: get_all_games(games[0:3]),
        7: post_players(players[0], games[0]),
        8: post_players(players[1], games[1]),
        9: post_players(players[2], games[2]),
        10: post_review(games[0],players[0], reviews[0]),
        11: post_review(games[1], players[1], reviews[1]),
        12: get_game_reviews(games[0]),
        13: get_game_reviews(games[1]),
        14: get_game_reviews(games[2]),
        15: get_review_by_game(reviews, games[0]),
        16: get_review_by_game(reviews, games[1]),
        17: delete_game(games, games[0]),
        18: not post_review(games[1], games[5], bad_reviews[0]),
        19: not patch_review(reviews[4], {'review': {'title': 'New Title'}}),
        20: not patch_review(reviews[0], {'review': {'game_id': bad_games[0]}}),
        21: not get_all_games(bad_games),
        22: not get_game(bad_games[0]),
        23: not post_review(bad_games[0], bad_games[3], bad_reviews[0]),
        24: not get_game_reviews(bad_games[0]),
        25: not get_review_by_game(bad_reviews, ''),
        26: not delete_game(bad_games, bad_games[0]),
        27: not patch_review(bad_reviews[0], {'review': {'player_id': bad_games[1]}}),
        28: not patch_review(bad_reviews[0], {'review': {'game_id': bad_games[1]}}),
        29: delete_game(games, games[1]),
        30: not get_all_games(games),
    }

    return results


if __name__ == '__main__':
    results = test_2C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
