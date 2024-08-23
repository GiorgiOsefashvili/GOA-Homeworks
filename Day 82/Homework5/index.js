function rangeArray(start, end) {

    let result = [];

    for (let i = start; i <= end; i++) {
        result.push(i);
    }

    return result;
}

function calculateAverage(numbers) {
    let sum = 0;

    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }

    let average = sum / numbers.length;

    return average;
}

let start = 5;
let end = 10;


let numbersInRange = rangeArray(start, end);
console.log("Numbers in range:", numbersInRange); 

let average = calculateAverage(numbersInRange);
console.log("Average of numbers:", average);
