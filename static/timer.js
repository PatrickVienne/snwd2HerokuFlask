function setTime(){
    var myDate = new Date();
    document.getElementById("time").innerHTML = myDate.toLocaleString();
    console.log(myDate.toISOString());
}
setInterval(setTime, 1000);
