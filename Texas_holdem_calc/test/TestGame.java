import game.Game;
import org.junit.Test;

public class TestGame {
    @Test
    public void test_game(){
        Game game = new Game(4);

        game.deal();
        game.verify();
    }
}
