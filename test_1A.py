from copy import deepcopy

from src.part_1 import (
   delete_all_games,
    delete_game,
    get_game,
    post_games,
    get_all_games

)

from data import GAMES_A


def test_1A():
    games = deepcopy(GAMES_A[0:3])

    results = {
        1: delete_all_games(), 
        2: post_games(games[0]),
        3: post_games(games[1]),
        4: post_games(games[2]),
        5: get_all_games(games),
        6: get_game(games[0]),
        7: get_game(games[1]),
        8: get_game(games[2]),
        9: delete_game(games, games[0]),
        10: get_all_games(games),
    }

    return results


if __name__ == '__main__':
    results = test_1A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
