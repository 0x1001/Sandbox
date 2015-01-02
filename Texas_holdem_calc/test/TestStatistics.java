import calc.Statistics;
import org.junit.Test;

public class TestStatistics {

    @Test
    public void test_statistics(){
        Statistics stats = new Statistics();

        stats.run();
        stats.save("output.txt");
    }
}

