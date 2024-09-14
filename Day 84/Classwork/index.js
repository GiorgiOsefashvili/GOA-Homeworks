const database = [];

function User(firstName, lastname, email) {
    this.firstName = firstName;
    this.lastname = lastname;
    this.email = email;
    this.accountActive = false;
}

function Account(firstName, lastname, email) {
    if (firstName === '' || lastname === '' || email === '') {
        alert('All fields are required!');
        return false;
    }


    return true;
}

document.getElementById('Form').addEventListener('submit', function(e) {
    e.preventDefault();

    const firstName = document.getElementById('firstName').value;
    const lastname = document.getElementById('lastname').value;
    const email = document.getElementById('email').value;

    if (Account(firstName, lastname, email)) {
        
        const newUser = new User(firstName, lastname, email);

        database.push(newUser);

        console.log('User registered:', newUser);
        alert('Registration successful!');
    }
});
