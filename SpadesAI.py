import pyCardDeck

def rank_to_value(rank):
    ranks = {'A': 14,
             '2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13}
        
    return ranks[rank]
class GameState:
    def __init__(self):
        self.played_cards = []
        self.scores = [0, 0]
        self.bags = [0, 0]
        self.bets = [0, 0, 0, 0]
        self.played = [0, 0, 0, 0]
        self.trump_card = -1

    def reset_play(self):
        self.played = [0, 0, 0, 0]
        self.trump_card = -1

    def reset_round(self):
        self.played_cards = []
        self.bets = [0, 0, 0, 0]
    def a_team_bet(self):
        return self.bets[0] + self.bets[2]

    def a_total_score(self):
        return self.scores[0] - self.bags[0] % 10
    
    def b_team_bet(self):
        return self.bets[1] + self.bets[3]

    def b_total_score(self):
        return self.scores[1] - self.bags[1] % 10
    
    # Returns the player number of the current winner
    # of this play
    def find_play_winner(self):
        winning_p_num = -1
        winning_card = -1
        win_trump = self.trump_card.suit
        win_rank = -1

        for i in range(0, 4):
            card = self.played[i]
            card_rank = rank_to_value(card.rank)
            if card.suit == win_trump:
                if card_rank > win_rank:
                    winning_p_num = i
                    win_rank = card_rank
                    winning_card = card
            elif card.suit == "Spades" and win_trump != "Spades":
                # spades is now broken, change trump to spades
                win_trump = card.suit
                win_rank = card_rank
                winning_p_num = i
                winning_card = card

        print("...Winner is Player " + str(winning_p_num))
        print("...with " + str(winning_card))
        return winning_p_num
# an instance of SpadesAI
# corresponds to a single rounds of spades
# The player always considers themselves S in a NESW configuration
class SpadesAI:
    def __init__(self, abs_pos):
        self.hand = []
        self.player_number = abs_pos
    
    # return the value we want to bet
    def bet(self, state):
        return 0

    def play(self, state):
        # create a set of legally playable cards 
        # if the trump is already set
        playable_cards = []

        # if you have a trump, you have to play it
        # unless spades is broken
        if state.trump_card != -1:
            playable_cards = [card for card in self.hand if card.suit == state.trump_card.suit]

        if len(playable_cards) == 0:
                playable_cards = self.hand

        #TODO: For now just play a random card
        card_played = playable_cards[0]

        # remove the played card from the hand
        self.hand.remove(card_played)

        return card_played