
def check(game_arr):
    # Sjekker for vannrett seier
    for i in range(3):
        if game_arr[i][0] == game_arr[i][1] == game_arr[i][2] == "O":
            return "Jebb"

    # Sjekker for loddrett seier
    for j in range(3):
        if game_arr[0][j] == game_arr[1][j] == game_arr[2][j] == "O":
            return "Jebb"

    # Sjekker for diagonal seier (fra øverste venstre til nedre høyre)
    if game_arr[0][0] == game_arr[1][1] == game_arr[2][2] == "O":
        return "Jebb"

    # Sjekker for diagonal seier (fra øverste høyre til nedre venstre)
    if game_arr[0][2] == game_arr[1][1] == game_arr[2][0] == "O":
        return "Jebb"

    # Hvis ingen seier er funnet, returnerer vi False
    return "Neibb"



rad1 = [f for f in input()]
rad2 = [f for f in input()]
rad3 = [f for f in input()]

game_arr = [[rad1[0],rad1[1],rad1[2]],
                [rad2[0],rad2[1],rad2[2]],
                [rad3[0],rad3[1],rad3[2]]
]

print(check(game_arr))
