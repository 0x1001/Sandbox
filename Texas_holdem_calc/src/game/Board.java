package game;

import cards.Card;

import java.util.ArrayList;

public class Board {
    private ArrayList<Card> cards;

    public Board(){
        cards = new ArrayList<Card>();
    }

    public void addCard(Card card){
        cards.add(card);
    }

    public ArrayList<Card> getCards() {
        return cards;
    }
}
