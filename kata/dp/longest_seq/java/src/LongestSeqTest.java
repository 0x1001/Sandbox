import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;

public class LongestSeqTest {
    @Test
    public void test_longest_seq(){
        ArrayList<Integer> ints;

        ints = new ArrayList<Integer>();
        ints.add(1);
        ints.add(2);
        ints.add(3);
        ints.add(4);
        ints.add(3);
        Assert.assertEquals(new LongestSeq(ints).get(), 4);

        ints = new ArrayList<Integer>();
        ints.add(1);
        ints.add(2);
        ints.add(3);
        ints.add(4);
        ints.add(5);
        ints.add(6);
        Assert.assertEquals(new LongestSeq(ints).get(), 6);

        ints = new ArrayList<Integer>();
        ints.add(6);
        ints.add(5);
        ints.add(4);
        ints.add(3);
        ints.add(2);
        ints.add(1);
        Assert.assertEquals(new LongestSeq(ints).get(), 1);

        ints = new ArrayList<Integer>();
        ints.add(1);
        ints.add(2);
        ints.add(1);
        ints.add(2);
        ints.add(1);
        ints.add(2);
        Assert.assertEquals(new LongestSeq(ints).get(), 2);

        ints = new ArrayList<Integer>();
        Assert.assertEquals(new LongestSeq(ints).get(), 0);

        ints = new ArrayList<Integer>();
        ints.add(1);
        Assert.assertEquals(new LongestSeq(ints).get(), 1);
    }
}