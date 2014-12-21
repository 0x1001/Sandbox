package cards;

public class Card implements Comparable<Card> {
    private Suit suit;
    private int value;

    public Card(int value, Suit suit){
        this.value = value;
        this.suit = suit;
    }

    public Suit getSuit() {
        return suit;
    }

    public void setSuit(Suit suit) {
        this.suit = suit;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public int compareTo(Card compare_card){
        if (value > compare_card.getValue())
            return 1;
        else if (value < compare_card.getValue())
            return -1;
        else
            return 0;
    }
}
