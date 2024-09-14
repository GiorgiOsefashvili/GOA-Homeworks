function handleForm() {
    const form = document.getElementById('dataForm');
    const nameInput = document.getElementById('name');
    const ageInput = document.getElementById('age');
    const emailInput = document.getElementById('email');
    const submitBtn = document.getElementById('submitBtn');

    submitBtn.onclick = function() {

        if (validateForm(nameInput, ageInput, emailInput)) {

            const formData = {
                name: nameInput.value,
                age: ageInput.value,
                email: emailInput.value
            };

            addRowToTable(formData);

            form.reset();
        } else {
            alert("Please fill in all fields correctly.");
        }
    };
}

function validateForm(name, age, email) {
    return name.value.trim() !== "" && age.value.trim() !== "" && email.value.trim() !== "";
}

function addRowToTable(data) {
    const table = document.getElementById('dataTable').getElementsByTagName('tbody')[0];

    const newRow = table.insertRow();
    const nameCell = newRow.insertCell(0);
    const ageCell = newRow.insertCell(1);
    const emailCell = newRow.insertCell(2);

    nameCell.textContent = data.name;
    ageCell.textContent = data.age;
    emailCell.textContent = data.email;
}

handleForm();
