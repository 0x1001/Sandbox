import cards.Card;
import cards.Suit;
import org.junit.Test;
import rules.Translator;

import static junit.framework.Assert.assertEquals;

public class TestTranslator {
    @Test
    public void test_translate(){
        Translator translator = new Translator();

        Card card = new Card(1, Suit.CLUBS);
        assertEquals(translator.translate(card), 3);

        card.setValue(13);
        card.setSuit(Suit.CLUBS);
        assertEquals(translator.translate(card), 7);

        card.setValue(11);
        card.setSuit(Suit.DIAMONDS);
        assertEquals(translator.translate(card), 14);

        card.setValue(12);
        card.setSuit(Suit.DIAMONDS);
        assertEquals(translator.translate(card), 10);

        card.setValue(12);
        card.setSuit(Suit.HEARTS);
        assertEquals(translator.translate(card), 9);

        card.setValue(3);
        card.setSuit(Suit.SPADES);
        assertEquals(translator.translate(card), 44);

        card.setValue(2);
        card.setSuit(Suit.SPADES);
        assertEquals(translator.translate(card), 48);

        card.setValue(6);
        card.setSuit(Suit.HEARTS);
        assertEquals(translator.translate(card), 33);
    }
}
