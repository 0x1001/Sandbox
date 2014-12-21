package game;

import cards.Card;

import java.util.ArrayList;

public class Player {
    private ArrayList<Card> cards = new ArrayList<Card>();;

    public void addCard(Card card) {
        cards.add(card);
    }

    public ArrayList<Card> getCards() {
        return cards;
    }
}
