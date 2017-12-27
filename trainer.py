from SpadesAI import *
import pyCardDeck


def main():
    print("...Initialize State")
    state = GameState()

    # order 
    order = [0, 1, 2, 3]
    for i in range(0, 1):
        print("...Round " + str(i))

        # initialize in initial order
        ai_list = [SpadesAI(x) for x in range(0, 4)]

        # initialize deck
        deck = pyCardDeck.Deck()
        deck.load_standard_deck()
        
        print("...Loading and Shuffling Deck")
        # shuffle
        deck.shuffle()

        # deal hands
        print("...Dealing Hands")
        for ai in ai_list:
            # 12 cards in each hand
            for counter in range(0, 13):
                ai.hand.append(deck.draw())
       
        # from here on out, we follow the order
        # get bets
        for p_number in order:
            print("...Player " + str(p_number) + " betting")
            state.bets[p_number] = ai_list[p_number].bet(state)


        # 7 plays per player in a round
        for play in range(0, 13):
            print("...Play " + str(play))

            # every player does a play
            for counter in range(0, 4):
                to_play_num = order[counter]
                print("...Player " + str(to_play_num) + " playing")
                card_played = ai_list[to_play_num].play(state)
                print("...Played " + str(card_played))

                # if this is the first play, we set the trump
                if counter == 0:
                    state.trump_card = card_played
                    print("...Trump is " + str(state.trump_card.suit))

                # update the state based on the card played
                state.played_cards.append(card_played)
                state.played[to_play_num] = card_played

            # figure out who won
            # rotate order to the winner
            winner_num = state.find_play_winner()

            # reset the round
            state.reset_play()

            # Rotate
            while(order[0] != winner_num):
                out_of = order.pop(0)
                order.append(out_of)

        assert len(state.played_cards) == 52

        # reset the play
        state.reset_round()

if __name__ == "__main__":
    main()