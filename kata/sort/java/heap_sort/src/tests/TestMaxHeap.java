package tests;

import heap_sort.MaxHeap;
import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class TestMaxHeap {
    @Test
    public void test_empty_Heap(){
        MaxHeap heap = new MaxHeap(new int[]{});
    }

    @Test
    public void test_one_element_Heap(){
        MaxHeap heap = new MaxHeap(new int[]{1});
    }

    @Test
    public void test_small_heap(){
        MaxHeap heap = new MaxHeap(new int[] {3, 2, 1});
        assertArrayEquals(new int[] {3, 2, 1}, heap.getHeap());

        heap = new MaxHeap(new int[] {1, 2, 3});
        assertArrayEquals(new int[] {3, 2, 1}, heap.getHeap());

        heap = new MaxHeap(new int[] {1, 2, 4, 3, 5});
        assertArrayEquals(new int[] {5, 3, 4, 1, 2}, heap.getHeap());

        heap = new MaxHeap(new int[] {1, 1, 1, 1, 1});
        assertArrayEquals(new int[] {1, 1, 1, 1, 1}, heap.getHeap());

        heap = new MaxHeap(new int[] {1, 2});
        assertArrayEquals(new int[] {2, 1}, heap.getHeap());
    }
}
