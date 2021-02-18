// This method works by building up a sorted array at the beginning of the list.
// It begins the sorted array with the first element.
// Then it inspects the next element and 
// swaps it backwards into the sorted array until it is in sorted position. 
// It continues iterating through the list and 
// swapping new items backwards into the sorted portion until it reaches the end.
// This algorithm has quadratic time complexity in the average and worst cases.

const insertionSort = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        let curr = arr[i];
        for (var j = i - 1; j >= 0 && arr[j] > curr; j--) {
            arr[j + 1] = arr[j]
        }
        arr[j + 1] = curr
    }
    return arr
}