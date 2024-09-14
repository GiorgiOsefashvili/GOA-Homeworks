function Car(brand, model, year, color) {
    this.brand = brand; 
    this.model = model; 
    this.year = year;   
    this.color = color; 
}

let myCar = new Car('Bmw', 'M5', 2015, 'Silver');

console.log(myCar)