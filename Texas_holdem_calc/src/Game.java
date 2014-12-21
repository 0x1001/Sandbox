import java.util.ArrayList;

public class Game {
    private Deck deck;
    private ArrayList<Player> players;
    private Board board;

    public Game(int players_num){
        deck = new Deck();
        players = new ArrayList<Player>();
        board = new Board();

        for(int player = 0; player < players_num; player++)
            players.add(new Player(player));

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

    }
}
