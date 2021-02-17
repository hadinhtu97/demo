// Selection sort works by selecting the minimum value in a list
// and swapping it with the first value in the list.
// It then starts at the second position, selects the smallest value in the remaining list,
// and swaps it with the second element.
// It continues iterating through the list and swapping elements until it reaches the end of the list. 
// Now the list is sorted. Selection sort has quadratic time complexity in all cases.

const selectionSort = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        let min = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[min] > arr[j]) min = j
        }
        let tmp = arr[min]
        arr[i] = arr[min]
        arr[min] = tmp
    }
    return arr
}