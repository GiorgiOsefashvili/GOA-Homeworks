const box = document.getElementById('box');
const boxSize = 50; // Box width and height
const speed = 5;    // Speed of movement in pixels
let direction = 'right';

// Function to get window dimensions
function getWindowDimensions() {
    return {
        width: window.innerWidth,
        height: window.innerHeight
    };
}

// Initial setup for movement
let posX = 0;
let posY = 0;

// Function to move the box
function moveBox() {
    const windowWidth = getWindowDimensions().width;
    const windowHeight = getWindowDimensions().height;

    if (direction === 'right') {
        posX += speed;
        if (posX + boxSize >= windowWidth) {
            direction = 'down';
        }
    } else if (direction === 'down') {
        posY += speed;
        if (posY + boxSize >= windowHeight) {
            direction = 'left';
        }
    } else if (direction === 'left') {
        posX -= speed;
        if (posX <= 0) {
            direction = 'up';
        }
    } else if (direction === 'up') {
        posY -= speed;
        if (posY <= 0) {
            direction = 'right';
        }
    }

    // Apply new positions to the box
    box.style.left = `${posX}px`;
    box.style.top = `${posY}px`;
}

// Set the interval for movement
setInterval(moveBox, 10);
