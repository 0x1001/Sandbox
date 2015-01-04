package tests;

import heap_sort.MinHeap;
import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

public class TestMinHeap {
    @Test
    public void test_empty_Heap(){
        MinHeap heap = new MinHeap();

        int[] array = {};

        heap.build(array);
    }

    @Test
    public void test_one_element_Heap(){
        MinHeap heap = new MinHeap();

        int[] array = {1};

        heap.build(array);
    }

    @Test
    public void test_small_heap(){
        MinHeap heap = new MinHeap();

        heap.build(new int[] {1, 2, 3});
        assertArrayEquals(new int[] {1, 2, 3}, heap.getHeap());

        heap.build(new int[] {3, 2, 1});
        assertArrayEquals(new int[] {1, 2, 3}, heap.getHeap());

        heap.build(new int[] {5, 4, 3, 2, 1});
        assertArrayEquals(new int[] {1, 2, 3, 5, 4}, heap.getHeap());

        heap.build(new int[] {1, 1, 1, 1, 1});
        assertArrayEquals(new int[] {1, 1, 1, 1, 1}, heap.getHeap());
    }
}
