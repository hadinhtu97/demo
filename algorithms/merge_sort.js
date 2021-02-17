// Merge sort also uses a divide - and - conquer, recursive methodology to sort an array.
// Recursively split the input array in half until a sub-array with only one element is produced.
// Merge each sorted sub-array together to produce the final sorted array.

// Merge sort is an efficient sorting method, with time complexity of O(nlog(n)). 
// This algorithm is popular because it is performant and relatively easy to implement.

const mergeSort = (arr) => {

    const merge = (arr1, arr2) => {
        let merged = [];
        while (arr1.length && arr2.length) {
            arr1[0] < arr2[0] ? merged.push(arr1.shift()) : arr1[0] > arr2[0] ? merged.push(arr2.shift()) : merged.push(arr1.shift(), arr2.shift())
        }
        return [...merged, ...arr1, ...arr2]
    }

    if (arr.length == 1) {
        return arr;
    } else {
        let splitIndex = Math.floor(arr.length / 2);
        return merge(mergeSort(arr.slice(0, splitIndex)), mergeSort(arr.slice(splitIndex)))
    }
}