import java.util.ArrayList;

import static java.util.Collections.max;

public class LongestSeq {
    private ArrayList<Integer> ints;

    public LongestSeq(ArrayList<Integer> ints){
        this.ints = ints;
    }

    public int get() {
        ArrayList<Integer> longest = new ArrayList<Integer>();

        Integer prev = Integer.MIN_VALUE;
        int c = 0;
        for (Integer val: ints){
            if (val >= prev){
                c++;
            } else {
                longest.add(c);
                c = 0;
            }
            prev = val;
        }
        longest.add(c);

        return max(longest);
    }
}
