package cards;

import java.util.ArrayList;
import java.util.Random;

public class Deck {
    private ArrayList<Card> cards = new ArrayList<Card>();

    public Deck(){
        for(Suit suit : Suit.values()){
            for(int i = 1; i < 14; i++) {
                cards.add(new Card(i, suit));
            }
        }
    }

    public ArrayList<Card> shuffle(){
        Random rand = new Random();
        for(int i = 0; i < cards.size(); i++){
            int j = rand.nextInt(cards.size());
            swap(i, j);
        }
        return cards;
    }

    private void swap(int i, int j){
        Card temp;

        temp = cards.get(i);
        cards.set(i, cards.get(j));
        cards.set(j, temp);
    }
}
