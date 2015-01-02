import game.Game;
import game.Player;
import org.junit.Test;

public class TestGame {
    @Test
    public void test_game(){
        Game game = new Game(4);

        game.deal();
        Player winner = game.winner();
        winner.getCards();
    }

    @Test
    public void test_multiple_games(){
        for(int i=0; i < 10; i++) {
            Game game = new Game(4);
            game.deal();
            game.winner().getCards();
        }
    }
}
