package heap_sort;


public class Sort {
    public static void sort(int[] array){
        MaxHeap heap = new MaxHeap(array);

        for(int i = array.length - 1; i > 0; i--) {
            heap.setSize(heap.getSize() - 1);
            swap(heap.getHeap(), 0, i);
            heap.heapify(0);
        }
    }

    private static void swap(int[] array, int idx1,int idx2){
        int temp = array[idx1];

        array[idx1] = array[idx2];
        array[idx2] = temp;
    }
}
