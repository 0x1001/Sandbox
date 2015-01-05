package heap_sort;

public class MaxHeap {
    int[] array = null;
    int size = 0;

    public void build(int[] array){
        this.array = array;
        size = array.length;

        if (size == 0)
            return;

        for(int i = size/2 + 1; i >= 0; i--)
            heapify(i);
    }

    public void heapify(int idx){
        int left = 2*idx + 1;
        int right = 2*idx + 2;

        if (left >= size || right >= size || idx >= size)
            return;

        if (array[idx] >= array[left] && array[idx] >= array[right])
            return;
        else if (array[left] < array[right]){
            swap(idx, right);
            heapify(right);
        } else if (array[left] > array[right]) {
            swap(idx, left);
            heapify(left);
        }
    }

    public int[] getHeap(){
        return array;
    }
    public int getSize() { return size; }
    public void setSize(int size) { this.size = size; }

    private void swap(int idx1, int idx2){
        int temp = array[idx2];

        array[idx2] = array[idx1];
        array[idx1] = temp;
    }
}
