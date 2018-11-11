var myVar;

window.onload = function(){
    myFunction();
};

function myFunction() {
    console.log("Called myFunction, will load in 3 seconds");
    myVar = setTimeout(showPage, 3000);
}

function showPage() {
    console.log("Called showPage");
    document.getElementById("loader").style.display = "none";
    document.getElementById("myDiv").style.display = "block";
}
