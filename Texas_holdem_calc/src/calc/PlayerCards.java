package calc;

import cards.Card;

import java.util.ArrayList;

public class PlayerCards implements Comparable<PlayerCards> {
    private ArrayList<Card> cards;
    private int hits = 0;

    public PlayerCards(ArrayList<Card> cards){
        this.cards = cards;
    }

    public boolean equal(PlayerCards player_cards){
        boolean equal = true;

        if (player_cards.getCards().size() != this.cards.size())
            return false;

        for(Card card: player_cards.getCards())
            if (!is_in_cards(card))
                equal = false;

        return equal;
    }

    private boolean is_in_cards(Card card){
        for(Card player_card: this.cards)
            if (card.getSuit() == player_card.getSuit() && card.getValue() == player_card.getValue())
                return true;
        return false;
    }

    public void incrementHits(){
        hits++;
    }

    public int getHits(){
        return hits;
    }

    public ArrayList<Card> getCards(){
        return cards;
    }

    public int compareTo(PlayerCards compare_card){
        if (hits > compare_card.getHits())
            return 1;
        else if (hits < compare_card.getHits())
            return -1;
        else
            return 0;
    }
}
