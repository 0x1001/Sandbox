import cards.Card;
import cards.Suit;
import game.Board;
import game.Player;
import org.junit.Test;
import rules.Rules;

import static org.junit.Assert.assertTrue;

public class TestRules {
    @Test
    public void test_rules_straight_flush(){
        Rules rules = new Rules();

        Player player1 = new Player();
        player1.addCard(new Card(1, Suit.SPADES));
        player1.addCard(new Card(2, Suit.SPADES));

        Player player2 = new Player();
        player2.addCard(new Card(11, Suit.HEARTS));
        player2.addCard(new Card(11, Suit.SPADES));

        Board board = new Board();
        board.addCard(new Card(3, Suit.SPADES));
        board.addCard(new Card(4, Suit.SPADES));
        board.addCard(new Card(5, Suit.SPADES));
        board.addCard(new Card(11, Suit.CLUBS));
        board.addCard(new Card(10, Suit.HEARTS));

        assertTrue(rules.evaluate(player1, board) > rules.evaluate(player2, board));
    }

    @Test
    public void test_rules_pair(){
        Rules rules = new Rules();

        Player player1 = new Player();
        player1.addCard(new Card(3, Suit.HEARTS));
        player1.addCard(new Card(2, Suit.DIAMONDS));

        Player player2 = new Player();
        player2.addCard(new Card(12, Suit.HEARTS));
        player2.addCard(new Card(2, Suit.SPADES));

        Board board = new Board();
        board.addCard(new Card(3, Suit.SPADES));
        board.addCard(new Card(4, Suit.HEARTS));
        board.addCard(new Card(6, Suit.SPADES));
        board.addCard(new Card(11, Suit.CLUBS));
        board.addCard(new Card(10, Suit.HEARTS));

        assertTrue(rules.evaluate(player1, board) > rules.evaluate(player2, board));
    }

    @Test
    public void test_rules_two_pair(){
        Rules rules = new Rules();

        Player player1 = new Player();
        player1.addCard(new Card(3, Suit.HEARTS));
        player1.addCard(new Card(4, Suit.DIAMONDS));

        Player player2 = new Player();
        player2.addCard(new Card(11, Suit.HEARTS));
        player2.addCard(new Card(2, Suit.SPADES));

        Board board = new Board();
        board.addCard(new Card(3, Suit.SPADES));
        board.addCard(new Card(4, Suit.HEARTS));
        board.addCard(new Card(6, Suit.SPADES));
        board.addCard(new Card(11, Suit.CLUBS));
        board.addCard(new Card(10, Suit.HEARTS));

        assertTrue(rules.evaluate(player1, board) > rules.evaluate(player2, board));
    }

    @Test
    public void test_rules_straight_flush_with_ace(){
        Rules rules = new Rules();

        Player player1 = new Player();
        player1.addCard(new Card(6, Suit.SPADES));
        player1.addCard(new Card(7, Suit.SPADES));

        Player player2 = new Player();
        player2.addCard(new Card(2, Suit.SPADES));
        player2.addCard(new Card(1, Suit.SPADES));

        Board board = new Board();
        board.addCard(new Card(3, Suit.SPADES));
        board.addCard(new Card(4, Suit.SPADES));
        board.addCard(new Card(5, Suit.SPADES));
        board.addCard(new Card(11, Suit.CLUBS));
        board.addCard(new Card(10, Suit.HEARTS));

        assertTrue(rules.evaluate(player1, board) > rules.evaluate(player2, board));
    }
}
