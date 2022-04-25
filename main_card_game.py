from DeckOfCards import DeckOfCards
from Card_Game import CardGame

new = CardGame("Natan", 20, "Gavriel", 20)

print("Bank", DeckOfCards(), "\n")
print(f"{new.player.playername}'s hand", new.player.playerdeck)
print(len(new.player.playerdeck), "cards\n")
print(f"{new.player2.playername}'s hand", new.player2.playerdeck)
print(len(new.player2.playerdeck), "cards\n")
print("Bank", DeckOfCards(), "\n")

print("Starting Game!")
for i in range(10):
    print(f"round {i+1}")
    a = new.player.get_card()
    b = new.player2.get_card()
    print(f"{new.player.playername} threw {a}")
    print(f"{new.player2.playername} threw {b}")
    if a > b:
        new.player.add_card(b)
        # p2.playerdeck.remove(b)
        print(f"{new.player.playername} won this round\n")
    else:
        new.player2.add_card(a)
        # p1.playerdeck.remove(a)
        print(f"{new.player2.playername} won this round\n")
new.get_winner()
print(f"{new.player.playername} has {len(new.player.playerdeck)} cards")
print(f"{new.player2.playername} has {len(new.player2.playerdeck)} cards")
print(new.player.playerdeck)
print(new.player2.playerdeck)
# from Card_Game import *
#
# player1 = Player('natan', 26)
# print(player1)
# player2 = Player('gavriel', 26)
# print(player2)
# print('------------------Game Starting-----------------------')
# mygame = CardGame(player1, player2)
# rounds = 0
# while rounds != 10:
#     rounds += 1
#     a = player1.get_card()
#     b = player2.get_card()
#     if a > b:
#         player1.playerdeck.append(b)
#     else:
#         player2.playerdeck.append(a)
#     print(len(player1.playerdeck))
#     print(f'Player 1 Thrown Card : {player1.get_card()},Player 2 Thrown Card: {player2.get_card()}')
#
