import java.util.ArrayList;
import java.util.Collections;

public class Rules {
    public int evaluate(Player player, Board board) {
        int value = straightFlush(player, board);
        if (value != 0)
            return value;

        return 0;
    }

    private ArrayList<ArrayList<Card>> generateCardsCombinations(Player player, Board board) {
        ArrayList<ArrayList<Card>> combinations = new ArrayList<ArrayList<Card>>();

        combinations.add(board.getCards());

        for(Card player_card: player.getCards()){
            for(int card_idx = 0; card_idx < board.getCards().size(); card_idx++) {
                ArrayList<Card> cards = new ArrayList<Card>(board.getCards());
                cards.set(card_idx, player_card);

                cards.addAll(player.getCards());
                cards.remove(player_card);

                combinations.add(cards);
            }
        }

        for(int first_card = 0; first_card < board.getCards().size(); first_card++) {
            for(int second_card = 0; second_card < board.getCards().size(); second_card++) {
                if (first_card != second_card){
                    ArrayList<Card> cards = new ArrayList<Card>(board.getCards());
                    cards.set(first_card, player.getCards().get(0));
                    cards.set(second_card, player.getCards().get(1));
                    combinations.add(cards);
                }
            }
        }

        return combinations;
    }

    private int straightFlush(Player player, Board board) {
        int max_board_value = 0;
        int max_player_value = 0;

        for(ArrayList<Card> combination: generateCardsCombinations(player, board)){
            ArrayList<Card> board_cards = new ArrayList<Card>(combination.subList(0, board.getCards().size() - 1));
            ArrayList<Card> player_cards = new ArrayList<Card>(combination.subList(board.getCards().size() - 1, combination.size() - 1));

            boolean suit_ok = checkSuit(board_cards);
            int board_value;
            int player_value;

            if (suit_ok) {
                board_value = checkStraight(board_cards);
                player_value = checkHighCard(player_cards);

                if (board_value > max_board_value) {
                    max_board_value = board_value;
                    max_player_value = player_value;
                }
            }
        }

        return 8 * max_board_value + max_player_value;
    }

    private boolean checkSuit(ArrayList<Card> cards) {
        Suit suit = null;
        boolean suit_ok = true;

        for (Card card : cards) {
            if (suit == null)
                suit = card.getSuite();
            else if (suit != card.getSuite())
                suit_ok = false;
        }
        return suit_ok;
    }

    private int checkStraight(ArrayList<Card> cards) {
        boolean straight = true;

        Collections.sort(cards);

        Integer card_value = cards.get(0).getValue();
        for (Card card : cards) {
            if (card.getValue() != card_value)
                straight = false;
            card_value++;
        }
        if (straight)
            return cards.get(0).getValue();
        else
            return 0;
    }

    private int checkHighCard(ArrayList<Card> cards){
        if (cards.size() == 0)
            return 0;

        Collections.sort(cards);
        return cards.get(cards.size() - 1).getValue();
    }
}