const choices = ['rock', 'paper', 'scissors'];
let playerScore = 0;
let computerScore = 0;

function getComputerChoice() {
    const randomIndex = Math.floor(Math.random() * 3);
    return choices[randomIndex];
}

function playRound(playerChoice) {
    const computerChoice = getComputerChoice();
    let resultMessage = '';

    if (playerChoice === computerChoice) {
        resultMessage = `It's a draw! You both chose ${playerChoice}`;
    } else if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        resultMessage = `You win! ${playerChoice} beats ${computerChoice}`;
        playerScore++;
    } else {
        resultMessage = `You lose! ${computerChoice} beats ${playerChoice}`;
        computerScore++;
    }

    document.getElementById('playerScore').textContent = playerScore;
    document.getElementById('computerScore').textContent = computerScore;
    document.getElementById('resultMessage').textContent = resultMessage;
}

document.getElementById('rock').onclick = () => playRound('rock');
document.getElementById('paper').onclick = () => playRound('paper');
document.getElementById('scissors').onclick = () => playRound('scissors');

document.getElementById('newGameBtn').onclick = () => {
    playerScore = 0;
    computerScore = 0;
    document.getElementById('playerScore').textContent = playerScore;
    document.getElementById('computerScore').textContent = computerScore;
    document.getElementById('resultMessage').textContent = 'Make your move!';
};
