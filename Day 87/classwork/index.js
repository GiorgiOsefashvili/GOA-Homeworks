function checkMinute() {
    const intervalId = setInterval(function() {
        let currentDate = new Date(); 
        let currentMinute = currentDate.getMinutes(); 

        console.log("Current minute: " + currentMinute); 

        
        if (currentMinute === 35) {
            console.log("Minute is 35. Stopping the interval.");
            clearInterval(intervalId); 
        }
    }, 1000); 
}

checkMinute();