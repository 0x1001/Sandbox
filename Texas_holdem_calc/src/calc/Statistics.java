package calc;

import cards.Card;
import game.Game;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;

public class Statistics {
    ArrayList<PlayerCards> player_cards = new ArrayList<PlayerCards>();

    public void run(){
        for(int i=0; i < 10000; i++) {
            Game game = new Game(4);
            game.deal();
            addPlayerCards(new PlayerCards(game.winner().getCards()));
        }
    }

    public void display(){
        Collections.sort(player_cards);

        print_cards(player_cards.get(0).getCards());
        print_cards(player_cards.get(1).getCards());
        print_cards(player_cards.get(2).getCards());
    }

    public void save(String path){
        try {
            PrintWriter out = new PrintWriter(path);
            for (int i=0; i < 100; i++) {
                if (this.player_cards.size() == i)
                    break;

                out.println("###");
                for (Card card : this.player_cards.get(i).getCards())
                    out.println(card.getValue() + " " + card.getSuit());
            }
            out.close();
        } catch (FileNotFoundException error){
            System.out.println("Can't write to file: " + path);
            return;
        }
    }

    private void addPlayerCards(PlayerCards player_cards){
        boolean not_found = true;

        for(PlayerCards player: this.player_cards)
            if (player.equal(player_cards)) {
                player.incrementHits();
                not_found = false;
                break;
            }

        if (not_found)
            this.player_cards.add(player_cards);
    }

    private void print_cards(ArrayList<Card> cards){
        System.out.println("###");
        for(Card card: cards){
            System.out.println(card.getValue() + " " + card.getSuit());
        }
    }
}
