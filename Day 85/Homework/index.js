function manualFilter(func, array) {
    let filteredArray = [];

    for (let i = 0; i < array.length; i++) {

        if (func(array[i])) {

            filteredArray.push(array[i]);
        }
    }


    return filteredArray;
}


function isEven(number) {
    return number % 2 === 0;
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8];
let evenNumbers = manualFilter(isEven, numbers);

console.log(evenNumbers); 
