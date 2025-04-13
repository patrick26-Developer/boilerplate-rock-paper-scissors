# main.py

from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

# Exécute les matchs contre les 4 bots
play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Pour jouer manuellement (facultatif)
# play(human, abbey, 20, verbose=True)

# Pour tester contre un bot aléatoire (facultatif)
# play(human, random_player, 1000)

# Active les tests unitaires
main(module='test_module', exit=False)