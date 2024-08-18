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
        5: (False, "validación incorrecta") if isinstance(post_games(bad_games[0]), tuple) and post_games(bad_games[0])[0] else (True, "validación correcta"),
        6: (False, "validación incorrecta") if isinstance(post_games(bad_games[1]), tuple) and post_games(bad_games[1])[0] else (True, "validación correcta"),
        7: (False, "validación incorrecta") if isinstance(post_games(bad_games[2]), tuple) and post_games(bad_games[2])[0] else (True, "validación correcta"),
        8: get_all_games(games),
        9: get_game(games[0]),
        10: get_game(games[1]),
        11: (False, "validación incorrecta") if isinstance(get_game(bad_games[0]), tuple) and get_game(bad_games[0])[0] else (True, "validación correcta"),
        12: delete_game(games, games[0]),
        13: delete_game(games, games[1]),
        14: (False, "validación incorrecta") if isinstance(delete_game(games, bad_games[0]), tuple) and delete_game(games, bad_games[0])[0] else (True, "validación correcta"),
        15: get_all_games(games),
        16: (False, "validación incorrecta") if isinstance(post_games(bad_games[0]), tuple) and post_games(bad_games[0])[0] else (True, "validación correcta"),
        17: delete_all_games(),
    }

    return results


if __name__ == '__main__':
    results = test_1C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
