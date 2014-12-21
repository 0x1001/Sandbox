package rules;

import cards.Card;
import cards.Suit;

import java.util.ArrayList;

public class Translator {
    private final int[][] TRANSLATION_TABLE = new int[][]{  {0, 1, 2, 3},
                                                            {48, 49, 50, 51},
                                                            {44, 45, 46, 47},
                                                            {40, 41, 42, 43},
                                                            {36 , 37, 38, 39},
                                                            {32, 33, 34, 35},
                                                            {28, 29, 30, 31},
                                                            {24, 25, 26, 27},
                                                            {20, 21, 22, 23},
                                                            {16, 17, 18, 19},
                                                            {12, 13, 14, 15},
                                                            {8, 9, 10, 11},
                                                            {4, 5, 6, 7},
    };

    public int[] translate(ArrayList<Card> cards){
        int[] translated = new int[7];
        int card_idx = 0;

        for(Card card: cards){
            translated[card_idx] = translate(card);
            card_idx++;
        }

        return translated;
    }

    public int translate(Card card){
        int card_value = card.getValue() - 1;
        int suite_value = 0;

        if (card.getSuit() == Suit.SPADES)
            suite_value = 0;
        else if (card.getSuit() == Suit.HEARTS)
            suite_value = 1;
        else if (card.getSuit() == Suit.DIAMONDS)
            suite_value = 2;
        else if (card.getSuit() == Suit.CLUBS)
            suite_value = 3;

        return TRANSLATION_TABLE[card_value][suite_value];
    }
}
