from copy import deepcopy

from src.part_1 import (
    get_all_teams,
    post_team,
    get_team,
    delete_team,
    delete_all_teams,
)

from src.part_2 import (
    get_team_matches,
    post_match,
    patch_match,
    get_matches_by_team,
)

from src.part_3 import (
    post_player,
    get_team_player,
    get_player_top_goals,
    get_player_top_assists,
    get_player_top_cards,
    get_players_from_team,
    delete_worst_team,
)

from data import (
    TEAMS_A, MATCHES_B, PLAYERS_A,
    WRONG_MATCHES, WRONG_TEAMS, WRONG_PLAYERS,
)


def test_3C():
    teams = deepcopy(TEAMS_A[0:4])
    bad_teams = deepcopy(WRONG_TEAMS[0:3])
    matches = deepcopy(MATCHES_B[0:5])
    bad_matches = deepcopy(WRONG_MATCHES[0:2])
    players = deepcopy(PLAYERS_A[0:9])
    bad_players = deepcopy(WRONG_PLAYERS[0:2])

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: not post_team(bad_teams[0]),
        5: not post_team(bad_teams[1]),
        6: post_team(teams[2]),
        7: not post_team(bad_teams[2]),
        8: post_team(teams[3]),
        9: get_all_teams(teams),
        10: get_team(teams[0]),
        11: not get_team(bad_teams[0]),
        12: get_team(teams[1]),
        13: post_match(teams[0],teams[1], matches[0]),
        14: post_match(teams[0], teams[2], matches[1]),
        15: post_match(teams[1], teams[3], matches[4]),
        16: post_match(teams[1], teams[2], matches[2]),
        17: post_match(teams[2], teams[3], matches[3]),
        18: patch_match(matches[3], {'match': {'state': False, 'result': "--"}}),
        19: get_team_matches(teams[0]),
        20: get_team_matches(teams[1]),
        21: get_team_matches(teams[2]),
        22: get_matches_by_team(matches, teams[0]),
        23: get_matches_by_team(matches, teams[2]),
        24: not get_matches_by_team(matches, 'Unión Española'),
        25: not delete_team(teams, bad_teams[0]),
        26: not delete_team(bad_teams, bad_teams[0]),
        27: post_player(teams[0], players[0]),
        28: post_player(teams[0], players[1]),
        29: post_player(teams[0], players[2]),
        30: post_player(teams[1], players[3]),
        31: post_player(teams[1], players[4]),
        32: post_player(teams[1], players[5]),
        33: post_player(teams[2], players[6]),
        34: post_player(teams[2], players[7]),
        35: post_player(teams[2], players[8]),
        36: get_team_player(players[0]),
        37: get_team_player(players[3]),
        38: get_player_top_assists(players, 3),
        39: get_players_from_team(teams[0]),
        40: get_players_from_team(teams[1]),
        41: delete_worst_team(teams, matches, players),
        42: get_team_player(players[0]),
        43: not post_player(teams[0], bad_players[0]),
        44: not post_player(teams[0], bad_players[1]),
        45: not post_match(teams[0], bad_matches[0]),
        46: not post_match(teams[0], bad_matches[1]),
        47: not patch_match(matches[0], {'match': {'teamB': teams[2]}}),
        48: not patch_match(matches[0], {'match': {'teamA': teams[1]}}),
        49: get_all_teams(teams),
        50: delete_all_teams(),
    }

    return results


if __name__ == '__main__':
    results = test_3C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
