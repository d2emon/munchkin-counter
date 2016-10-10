class Player:
    dead = True
    fighting = False
    hand = []

    def __init__(self, title="<<UNNAMED>>"):
        self.title = title
        self.birth()

    def __repr__(self):
        return self.title

    def turn(self):
        print("{}'s turn".format(self.title))
        if self.dead:
            self.birth()

        self.play_cards()

    def end_turn(self):
        self.fighting = False
        self.play_cards()

    def birth(self):
        self.dead = False
        print("{}'s birth".format(self.title))

        print("Get 4 treasures")
        self.hand = self.hand + treasures.get_cards(4)

        print("Get 4 doors")
        self.hand = self.hand + doors.get_cards(4)

        print("Hand is {}".format([c.title for c in self.hand]))

    def play_cards(self):
        print("{} show cloth".format(self.title))
        print("{} play our cards".format(self.title))

    def hand_monster(self):
        print("Have monster in hand?")
        print("Want to fight?")
        return False

    def fight(self):
        self.fighting = True
        print("Battle")

    def low_level(self):
        return True

    def give_cards(self):
        print("Give cards")

        if len(self.hand) > 5:
            print("Too many cards")
        else:
            return

        if self.low_level():
            print("Discard cards")
        else:
            print("Give cards to low level")


class Card:
    def __init__(self, title="<<UNTITLED>>"):
        self.title = title

    def __str__(self):
        return self.title


class Deck:
    cards = []
    card_id = 0

    def __init__(self):
        # self.doors.shuffle()
        pass

    def get_card(self):
        card = self.cards[self.card_id]
        self.card_id += 1
        print("\t>\t{}".format(card.title))
        return card

    def get_cards(self, count=1):
        grab = [self.get_card() for i in range(0, count)]
        print("\t>>\t{}".format([c.title for c in grab]))
        return grab


class Treasure(Card):
    pass


class Door(Card):
    monster = False
    curse = False


class DoorDeck(Deck):
    cards = [Door("Door {}".format(i)) for i in range(0, 50)]


class TreasureDeck(Deck):
    cards = [Treasure("Treasure {}".format(i)) for i in range(0, 50)]


doors = DoorDeck()
treasures = TreasureDeck()
players = []


def ask_players():
    n = int(input("How many players? "))
    players = []
    for i in range(n):
        title = input("Player {}: ".format(i + 1))
        players.append(Player(title=title))
    return players


def play_cards(player):
    answer = ""
    while answer != "y":
        answer = input("Ready? ")


def open_door(player):
    print("Open door")
    print("Get 1 door")
    d = doors.get_card()
    print("Door is {}".format(d.title))

    if input("Is monster? ") == "y":
        d.monster = True
    elif input("Is curse? ") == "y":
        d.curse = True

    play_cards(player)
    return d


def fight(player, monster):
    player.fight()
    winner = player
    wait = 3

    while True:
        if input("Do you kill monster? ") == "y":
            if wait > 0:
                print("Wait {}".format(wait))
                wait -= 1
                continue

            print("Get levels")
            if input("Are you winner? ") == "y":
                print("You win!!!")
                return
            print("Get treasures")
            return
        else:
            if input("Want to run? ") == "y":
                if input("Run? ") != "y":
                    print("Get monster")
                    if input("Dead? ") == "y":
                        print("Dead")
                return
            else:
                if input("Got some help? ") == "y":
                    continue


def run():
    players = ask_players()
    print("Players are: {}".format(players))

    print("New turn")
    for p in players:
        p.turn()

        play_cards(p)
        d = open_door(p)

        if d.monster:
            fight(p, d)
        elif d.curse:
            print("Curse")
        else:
            print("Got door")
            p.hand.append(d)
            print("Hand is {}".format([c.title for c in p.hand]))

        if not p.fighting:
            print("Search for encounter")
            if p.hand_monster():
                fight(p, None)
            else:
                print("Search for loot")
                print("Get door")
                d = doors.get_card()
                p.hand.append(d)
                print("Hand is {}".format([c.title for c in p.hand]))

        p.end_turn()
        print("Give cards")
        if len(p.hand) > 5:
            print("Too many cards")

        print("End turn")


if __name__ == "__main__":
    run()
