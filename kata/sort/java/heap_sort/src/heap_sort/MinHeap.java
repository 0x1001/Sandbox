package heap_sort;

public class MinHeap {
    int[] array = null;

    public void build(int[] array){
        this.array = array;

        if (array.length == 0)
            return;

        for(int i = array.length/2; i >= 0; i--)
            heapify(i);
    }

    public void heapify(int idx){
        int left = 2*idx + 1;
        int right = 2*idx + 2;

        if (left >= array.length || right >= array.length || idx >= array.length)
            return;

        if (array[idx] <= array[left] && array[idx] <= array[right])
            return;
        else if (array[left] < array[right]){
            swap(idx, left);
            heapify(left);
        } else if (array[left] > array[right]) {
            swap(idx, right);
            heapify(right);
        }
    }

    public int[] getHeap(){
        return array;
    }

    private void swap(int idx1, int idx2){
        int temp = array[idx2];

        array[idx2] = array[idx1];
        array[idx1] = temp;
    }
}
