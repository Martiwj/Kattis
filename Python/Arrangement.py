def allocate_teams_to_rooms(rooms, teams):
    teams_per_room = teams // rooms
    extra_teams = teams % rooms

    allocation = [teams_per_room + 1] * extra_teams + \
        [teams_per_room] * (rooms - extra_teams)

    return allocation


def print_rooms(allocation):
    for count in allocation:
        print('*' * count)


def main():
    rooms = int(input())
    teams = int(input())

    allocation = allocate_teams_to_rooms(rooms, teams)
    print_rooms(allocation)

main()
