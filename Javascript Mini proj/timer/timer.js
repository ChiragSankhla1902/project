function myfunction(){
    console.log("Timer started");
    timer();
    start();
    // restart();
}

function restart(){
    // document.getElementById("day").value=" ";
    // document.getElementById("month").value=" ";
    // document.getElementById("year").value=" ";
}

function start() {
    var countdownTimer = setInterval(timer, 1000);
}


function timer(){
    
    const day= document.getElementById("day").value
    const month= document.getElementById("month").value
    const year= document.getElementById("year").value
    
    const usertime = day+" "+month+" "+year;

    const newYearsDate = new Date(usertime);
    const currentDate = new Date();
    const totalSeconds = (newYearsDate - currentDate) / 1000;

    var days = Math.floor(totalSeconds / 3600 / 24);
    var hours = Math.floor(totalSeconds / 3600) % 24;
    var mins = Math.floor(totalSeconds / 60) % 60;
    var seconds = Math.floor(totalSeconds) % 60;

    document.getElementById("days").innerText = days;
    document.getElementById("hours").innerText = hours;
    document.getElementById("mins").innerText = mins;
    document.getElementById("secs").innerText = seconds;
    if(totalSeconds<0){
        document.getElementById("days").innerText = "Donw";
        document.getElementById("hours").innerText = "Done";
        document.getElementById("mins").innerText = "Done";
        document.getElementById("secs").innerText = "Done";
    }
}

