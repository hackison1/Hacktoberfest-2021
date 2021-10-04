export function linearSearch(arr, x) {
    for (const element of arr) {
        if (element === x) {
          console.log(`linear search found ${x}`);
          return 0;
        }
    }
    console.log(`Linear search couldn't find ${x}`);
    return 1;
}

linearSearch([1,2,3,4,5,6,7,8,9,10], Math.floor(Math.random() * 10))
