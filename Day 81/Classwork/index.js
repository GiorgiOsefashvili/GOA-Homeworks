
const usersArray = [];


document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();


    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;

 
    const user = {
        firstName: firstName,
        lastName: lastName,
        email: email
    };
 
    usersArray.push(user);

    console.log(user);

    document.getElementById('userForm').reset();
});
