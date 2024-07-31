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


from src.part_3 import (
    get_teamfavourateGame_player,
    get_top_calification,
    get_player_from_review,
    delete_worst_game,
    patch_update_game_calification,
)

from data import GAMES_A, REVIEWS_A, PLAYERS_A


def test_3A():
    games = deepcopy(GAMES_A[0:4])
    reviews = deepcopy(REVIEWS_A[0:6])
    players = deepcopy(PLAYERS_A[0:9])

    results = {
        0: delete_all_players(),
        1: delete_all_games(),
        2: post_games(games[0]),
        3: post_games(games[1]),
        4: post_games(games[2]),
        5: post_games(games[3]),
        6: post_players(players[0], games[0]),
        7: post_players(players[1], games[0]),
        8: post_players(players[2], games[0]),
        9: post_review(games[0],players[2] , reviews[1]),
        10: post_review(games[0], players[2], reviews[2]),
        11: post_review(games[0], players[0], reviews[3]),
        12: post_review(games[0], players[0], reviews[4]),
        13: post_review(games[0], players[1], reviews[5]),
        14: get_teamfavourateGame_player(players[0],games),
        15: get_teamfavourateGame_player(players[1],games),
        16: get_top_calification(games,3),
        17: get_player_from_review(reviews[1], players),
        18: delete_worst_game(games, reviews),
        19: get_all_games(games),
        20: patch_update_game_calification(games[0]),
    }

    return results


if __name__ == '__main__':
    results = test_3A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
