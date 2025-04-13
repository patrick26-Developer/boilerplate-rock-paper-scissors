import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if not hasattr(player, "my_history"):
        player.my_history = []
    if not hasattr(player, "round"):
        player.round = 0
    player.round += 1

    if player.round < 5:
        move = "R"
    elif is_abbey(opponent_history, player.my_history):
        # Si on détecte Abbey, joue un coup qui contre ce qu'elle va probablement copier
        if len(player.my_history) >= 2:
            expected = player.my_history[-2]  # Elle va rejouer ça
            move = counter_move(expected)
        else:
            move = "R"
    else:
        guess = predict_next_move(opponent_history)
        move = counter_move(guess)

    player.my_history.append(move)
    return move

def counter_move(move):
    return {"R": "P", "P": "S", "S": "R"}[move]

def predict_next_move(history):
    pattern = "".join(history[-2:])
    options = ["R", "P", "S"]
    freq = {"R": 0, "P": 0, "S": 0}

    for i in range(len(history) - 2):
        if history[i] + history[i+1] == pattern:
            next_move = history[i+2]
            if next_move in freq:
                freq[next_move] += 1

    prediction = max(freq, key=freq.get) if any(freq.values()) else random.choice(options)
    return prediction

def is_abbey(opponent_history, my_history):
    # Si l'adversaire joue souvent ce qu'on a joué 2 tours avant
    if len(opponent_history) < 5 or len(my_history) < 3:
        return False
    matches = 0
    for i in range(2, len(opponent_history)):
        if i - 2 < len(my_history) and opponent_history[i] == my_history[i - 2]:
            matches += 1
    ratio = matches / (len(opponent_history) - 2)
    return ratio > 0.6  # Détection fiable si plus de 60% de correspondance
