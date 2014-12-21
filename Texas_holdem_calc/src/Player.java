import java.util.ArrayList;

public class Player {
    private int id;
    private ArrayList<Card> cards;

    public Player(int id){
        cards = new ArrayList<Card>();
        id = id;
    }

    public void addCard(Card card) {
        cards.add(card);
    }

    public ArrayList<Card> getCards() {
        return cards;
    }
}
