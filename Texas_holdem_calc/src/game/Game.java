package game;

import cards.Card;
import cards.Deck;
import rules.Rules;

import java.util.ArrayList;

public class Game {
    private Deck deck = new Deck();
    private ArrayList<Player> players = new ArrayList<Player>();
    private Board board = new Board();
    private Rules rules = new Rules();

    public Game(int players_num){
        for(int player = 0; player < players_num; player++)
            players.add(new Player());
    }

    public void deal() {
        ArrayList<Card> cards = deck.shuffle();

        for(int card_number = 0; card_number < 2; card_number++)
            for(Player player: players)
                player.addCard(cards.remove(0));


        for(int card_number = 0; card_number < 5; card_number++)
            board.addCard(cards.remove(0));
    }

    public void verify() {
        for(Player player: players){
            System.out.println(rules.evaluate(player, board));
        }
    }
}
