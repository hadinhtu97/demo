// The bubble sort method starts at the beginning of an unsorted array
// and 'bubbles up' unsorted values towards the end,
// iterating through the array until it is completely sorted.
// It does this by comparing adjacent items and swapping them if they are out of order.
// The method continues looping through the array until no swaps occur at which point the array is sorted.
// This method requires multiple iterations through the array and for average 
// and worst cases has quadratic time complexity. 

const bubleSort = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                let tmp = arr[j];
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
            }
        }
    }
    return arr
}

bubbleSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);