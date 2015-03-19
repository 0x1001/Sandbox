package coins;

import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;

public class CoinsTest {

    @Test
    public void testCoins(){
        ArrayList<Integer> coins = new ArrayList<Integer>();
        coins.add(1);
        coins.add(2);
        coins.add(5);
        coins.add(10);
        coins.add(20);
        coins.add(50);

        Coins c = new Coins(coins);
        Assert.assertEquals(c.minNum(10), new Integer(1));
        Assert.assertEquals(c.minNum(50), new Integer(1));
        Assert.assertEquals(c.minNum(100), new Integer(2));
        Assert.assertEquals(c.minNum(4), new Integer(2));
    }
}