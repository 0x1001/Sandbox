package game;

import cards.Card;
import cards.Deck;
import rules.Rules;

import java.util.ArrayList;

public class Game {
    private Deck deck = new Deck();
    private ArrayList<Player> players = new ArrayList<Player>();
    private Board board = new Board();

    private class Evaluator extends Thread {
        private Player player;
        private Board board;
        private Rules rules = new Rules();
        int score = 0;

        public Evaluator(Player player, Board board){
            this.player = player;
            this.board = board;
        }

        @Override
        public void run(){
            score = rules.evaluate(player, board);
        }

        public Player getPlayer(){
            return player;
        }

        public int getScore(){
            return score;
        }
    }

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

    public Player winner(){
        ArrayList<Evaluator> evaluators = new ArrayList<Evaluator>();
        int max_score = 0;
        Player winner = new Player();

        for(Player player: players){
            Evaluator evaluator = new Evaluator(player, board);
            evaluator.start();
            evaluators.add(evaluator);
        }

        for(Evaluator evaluator: evaluators){
            try {
                evaluator.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                int score = evaluator.getScore();
                if (score > max_score) {
                    winner = evaluator.getPlayer();
                    max_score = score;
                }
            }
        }

        return winner;
    }
}
