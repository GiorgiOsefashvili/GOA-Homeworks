function getRandomNumber() {
    return Math.floor(Math.random() * 1001);
}

function handleButtonClick() {
    const button = document.getElementById('generateBtn');
    
    button.onclick = function() {
        const randomNumber = getRandomNumber();
        
        const newParagraph = document.createElement('p');
        
        newParagraph.textContent = "Random Number: " + randomNumber;

        document.body.appendChild(newParagraph);
    };
}

handleButtonClick();
