package heap_sort;

public class MaxHeap {
    int[] array = null;
    int size = 0;

    public MaxHeap(int[] array){
        this.array = array;
        size = array.length;

        build();
    }

    public void heapify(int idx){
        int left = 2*idx + 1;
        int right = 2*idx + 2;
        int largest = idx;

        if (idx >= size)
            return;

        if (left < size && array[idx] < array[left])
            largest = left;

        if (right < size && array[left] < array[right])
            largest = right;

        if (largest != idx){
            swap(idx, largest);
            heapify(largest);
        }
    }

    public int[] getHeap(){ return array; }
    public int getSize() { return size; }
    public void setSize(int size) { this.size = size; }

    private void swap(int idx1, int idx2){
        int temp = array[idx2];

        array[idx2] = array[idx1];
        array[idx1] = temp;
    }

    private void build(){
        if (size == 0)
            return;

        for(int i = size/2; i >= 0; i--)
            heapify(i);
    }
}
