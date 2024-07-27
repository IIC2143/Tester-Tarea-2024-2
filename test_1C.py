from copy import deepcopy

from src.part_1 import (
    get_all_games,
    post_games,
    get_game,
    delete_game,
    delete_all_games,
)

from data import GAMES_B, WRONG_GAMES


def test_1C():
    games = deepcopy(GAMES_B[0:3])
    bad_games = deepcopy(WRONG_GAMES[0:3])

    results = {
        1: delete_all_games(),
        2: post_games(games[0]),
        3: post_games(games[1]),
        4: post_games(games[2]),
        5: not post_games(bad_games[0]),
        6: not post_games(bad_games[1]),
        7: not post_games(bad_games[2]),
        8: get_all_games(games),
        9: get_game(games[0]),
        10: get_game(games[1]),
        11: not get_game(bad_games[0]),
        12: delete_game(games, games[0]),
        13: delete_game(games, games[1]),
        14: not delete_game(games, bad_games[0]),
        15: get_all_games(games),
        16: not post_games(bad_games[0]),
        17: not post_games(bad_games[1]),
        18: not post_games(bad_games[2]),
        19: not get_game(bad_games[0]),
        20: delete_all_games(),
    }

    return results


if __name__ == '__main__':
    results = test_1C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
