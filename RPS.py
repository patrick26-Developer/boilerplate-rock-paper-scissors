# RPS.py — version finale optimisée

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return "R"

    guess = predict_next_move(opponent_history)
    move = counter_move(guess)
    player.prev_player_move = move
    return move

# Mémorise le dernier coup joué par le bot
player.prev_player_move = "R"

def counter_move(move):
    return {"R": "P", "P": "S", "S": "R"}[move]

def predict_next_move(history):
    # On analyse les séquences de 2 coups pour deviner le suivant
    pattern = "".join(history[-2:])
    options = ["R", "P", "S"]
    freq = {"R": 0, "P": 0, "S": 0}

    for i in range(len(history) - 2):
        if history[i] + history[i+1] == pattern:
            next_move = history[i+2]
            if next_move in freq:
                freq[next_move] += 1

    # Si aucune prédiction fiable, choix aléatoire
    prediction = max(freq, key=freq.get) if any(freq.values()) else random.choice(options)
    return prediction