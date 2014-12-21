public class Card implements Comparable<Card> {
    private Suit suite;
    private int value;

    public Suit getSuite() {
        return suite;
    }

    public void setSuite(Suit suite) {
        this.suite = suite;
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
