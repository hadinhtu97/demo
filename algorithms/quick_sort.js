// Quick sort is an efficient, recursive divide-and-conquer approach to sorting an array.
// In this method, a pivot value is chosen in the original array.
// The array is then partitioned into two subarrays of values less than and greater than the pivot value. 
// We then combine the result of recursively calling the quick sort algorithm on both sub-arrays.
// This continues until the base case of an empty or single-item array is reached, which we return
// The unwinding of the recursive calls return us the sorted array.

// Quick sort is a very efficient sorting method, providing O(nlog(n)) performance on average.
// It is also relatively easy to implement. 
// These attributes make it a popular and useful sorting method.

const quickSort = (arr) => {
    if (arr.length == 0) {
        return []
    } else {
        let pivot = arr[0]
        let lesser = []
        let equal = []
        let greater = []
        for (let i = 0; i < arr.length; i++) {
            arr[i] < pivot ? lesser.push(arr[i]) : arr[i] == pivot ? equal.push(arr[i]) : greater.push(arr[i])
        }
        return [...quickSort(lesser), ...equal, ...quickSort(greater)]
    }
}