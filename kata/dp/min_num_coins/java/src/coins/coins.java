package coins;

import java.util.ArrayList;

public class Coins {
    private ArrayList<Integer> coins;

    public Coins(ArrayList<Integer> coins){
        this.coins = coins;
    }

    public Integer minNum(Integer sum) {
        ArrayList<Integer> mins = new ArrayList<Integer>();

        for (int i=0; i <= sum; i++){
            mins.add(Integer.MAX_VALUE);
        }

        mins.set(0, 0);

        for (int i=0; i <= sum; i++){
            for (Integer coin : coins){
                if (coin <= i && mins.get(i - coin) + 1 < mins.get(i)){
                    mins.set(i, mins.get(i - coin) + 1);
                }

            }
        }
        return mins.get(sum);
    }
}
