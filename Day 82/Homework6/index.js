let dataBase = [];

document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    let accountExists = false;
    for (let i = 0; i < dataBase.length; i++) {
        if (dataBase[i].email === email) {
            accountExists = true;
            break;
        }
    }

    if (accountExists) {
        alert('Account with this email already exists.');
    } else {
        let newUser = {
            name: name,
            email: email,
            password: password
        };

        dataBase.push(newUser);

        alert('Account created successfully!');
    }

    document.getElementById('registrationForm').reset();
});
