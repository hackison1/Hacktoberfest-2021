function selectionSort(arr) {
    let n = arr.length 
    for (let index = 0; index < n - 1; index++) { 
        let smallestNum = index;
        for (let newSmallestNumber = index + 1; newSmallestNumber < n; newSmallestNumber++) { 
                if(arr[newSmallestNumber] < arr[smallestNum]){ 
                    smallestNum = newSmallestNumber;
                }
        }
        if (smallestNum != index) {
            let _ = arr[index]
            arr[index] = arr[smallestNum]
            arr[smallestNum] = _ 
        }
    }
    return arr;
}

let testArr=[6,5,4,3,2,1]
selectionSort(testArr)
console.log(testArr)
