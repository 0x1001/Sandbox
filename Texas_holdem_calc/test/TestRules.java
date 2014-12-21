import org.junit.Test;

import java.util.ArrayList;

public class TestRules {
    @Test
    public void test_rules(){
        Rules rules = new Rules();

        Player player = new Player(0);

        Card p_card1 = new Card();
        p_card1.setSuite(Suit.DIAMONDS);
        p_card1.setValue(1);
        Card p_card2 = new Card();
        p_card2.setSuite(Suit.DIAMONDS);
        p_card2.setValue(2);

        player.addCard(p_card1);
        player.addCard(p_card2);

        Board board = new Board();

        Card b_card1 = new Card();
        b_card1.setSuite(Suit.DIAMONDS);
        b_card1.setValue(3);
        Card b_card2 = new Card();
        b_card2.setSuite(Suit.DIAMONDS);
        b_card2.setValue(4);
        Card b_card3 = new Card();
        b_card3.setSuite(Suit.DIAMONDS);
        b_card3.setValue(5);
        Card b_card4 = new Card();
        b_card4.setSuite(Suit.CLUBS);
        b_card4.setValue(11);
        Card b_card5 = new Card();
        b_card5.setSuite(Suit.HEARTS);
        b_card5.setValue(10);

        board.addCard(b_card1);
        board.addCard(b_card2);
        board.addCard(b_card3);
        board.addCard(b_card4);
        board.addCard(b_card5);

        System.out.println(rules.evaluate(player, board));
    }
}
