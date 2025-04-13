import random

def player(prev_play, opponent_history=[]):
    # Ajout du coup de l'adversaire à l'historique
    opponent_history.append(prev_play)

    # Si l'historique est trop court, on joue de manière aléatoire
    if len(opponent_history) < 3:
        return "R"

    # Si l'historique est suffisant, on essaie de prédire le prochain coup de l'adversaire
    guess = predict_next_move(opponent_history)
    move = counter_move(guess)
    
    # Mémorisation du dernier coup joué
    player.prev_player_move = move
    return move

# Mémorise le dernier coup joué par le bot
player.prev_player_move = "R"

def counter_move(move):
    """
    Cette fonction retourne le coup gagnant contre le coup de l'adversaire.
    """
    return {"R": "P", "P": "S", "S": "R"}[move]

def predict_next_move(history):
    """
    Prédit le prochain coup de l'adversaire en fonction de son historique.
    Analyser des séquences plus longues peut rendre la prédiction plus robuste.
    """
    # On analyse les séquences de 3 coups pour deviner le suivant
    pattern = "".join(history[-3:])
    options = ["R", "P", "S"]
    freq = {"R": 0, "P": 0, "S": 0}

    # Recherche des motifs dans l'historique de l'adversaire
    for i in range(len(history) - 3):
        if history[i:i+3] == list(pattern):
            next_move = history[i+3]
            if next_move in freq:
                freq[next_move] += 1

    # Si aucune prédiction fiable, choix aléatoire
    prediction = max(freq, key=freq.get) if any(freq.values()) else random.choice(options)
    return prediction