package rules;

import cards.Card;
import game.Board;
import game.Player;
import rules.SpecialK.SpecialKEval.SevenEval;

import java.util.ArrayList;

public class Rules {
    Translator translator = new Translator();

    public int evaluate(Player player, Board board) {
        ArrayList<Card> cards = new ArrayList<Card>();
        cards.addAll(board.getCards());
        cards.addAll(player.getCards());

        int[] translated_cards = translator.translate(cards);

        SevenEval sevenEval = new SevenEval();
        return sevenEval.getRankOf( translated_cards[0],
                                    translated_cards[1],
                                    translated_cards[2],
                                    translated_cards[3],
                                    translated_cards[4],
                                    translated_cards[5],
                                    translated_cards[6]);
    }
}