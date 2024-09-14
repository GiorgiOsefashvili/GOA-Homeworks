document.getElementById('manipulateBtn').onclick = function() {

    let paragraphs = document.getElementsByTagName('p');
    console.log(paragraphs); 

    let textElements = document.getElementsByClassName('text');
    console.log(textElements);

    let firstParagraph = textElements[0];
    console.log(firstParagraph.parentElement); 
    firstParagraph.parentElement.style.border = "2px solid red";

    let containerDiv = firstParagraph.parentElement;
    console.log(containerDiv.children);
    containerDiv.children[1].style.color = "blue"; 

    console.log(containerDiv.firstElementChild);
    containerDiv.firstElementChild.style.fontSize = "40px";

    console.log(containerDiv.lastElementChild); 
    containerDiv.lastElementChild.style.backgroundColor = "yellow";

    let secondParagraph = textElements[1];
    console.log(secondParagraph.previousElementSibling); 
    secondParagraph.previousElementSibling.style.fontStyle = "italic";

    console.log(secondParagraph.nextElementSibling); 
    secondParagraph.nextElementSibling.style.fontWeight = "bold"; 
};
