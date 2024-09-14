let fruits = ['Apple', 'Banana'];

fruits.push('Orange'); 
console.log(fruits); 

fruits.push('Pear');
console.log(fruits);






let colors = ['Red', 'Blue', 'Green'];

let lastColor = colors.pop(); 
console.log(colors); 
console.log(lastColor); 

let anotherColor = colors.pop(); 
console.log(colors);
console.log(anotherColor); 








let numbers = [2, 3, 4];

numbers.unshift(1); 
console.log(numbers); 

numbers.unshift(0);
console.log(numbers);








let animals = ['Dog', 'Cat', 'lion'];

let firstAnimal = animals.shift(); 
console.log(animals);
console.log(firstAnimal);

let anotherAnimal = animals.shift(); 
console.log(animals); 
console.log(anotherAnimal); 





let letters = ['A', 'B', 'C', 'D', 'E'];

let subset = letters.slice(1, 3); 
console.log(subset); 

let anotherSubset = letters.slice(2);
console.log(anotherSubset);






let cities = ['New York', 'Los Angeles', 'Chicago', 'Houston'];


cities.splice(2, 1, 'San Francisco', 'Austin'); 
console.log(cities); 


let removedCities = cities.splice(1, 2); 
console.log(cities); 
console.log(removedCities);











