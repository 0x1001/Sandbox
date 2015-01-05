package tests;

import heap_sort.Sort;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;

public class TestSort {
    @Test
    public void testSort(){
        //check(new int[] {4, 2, 1});
        check(new int[]{4, 5, 10, 1, 3, 15, 6, 8});
    }

    private void check(int[] array){
        int[] array_copy = Arrays.copyOf(array, array.length);
        Sort.sort(array);

        Arrays.sort(array_copy);

        printArray(array);
        printArray(array_copy);
        assertArrayEquals(array_copy, array);
    }

    private void printArray(int[] array){
        System.out.print("[");
        for(int element: array){
            System.out.print(element + ", ");
        }
        System.out.print("]\n");
    }
}
