
function rangeArray(start, end) {
    let result = [];

    for (let i = start; i <= end; i++) {
        result.push(i);
    }

    return result;
}

let start = 4;
let end = 10;
let numbersInRange = rangeArray(start, end);
console.log(numbersInRange);
