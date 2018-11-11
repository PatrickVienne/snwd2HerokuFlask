// Client Side Javascript to receive numbers.

var socket = io.connect('wss://' + document.domain + ':' + location.port + '/test');
var logElement = document.getElementById("log");
var inputElement = document.getElementById("message");
var nameElement = document.getElementById("name");

window.onload = function(){
    myFunction();
};

function writeToMessageBox(message){
    var numberElement = document.createTextNode(message);
    var paragraph = document.createElement("p");
    paragraph.appendChild(numberElement);
    logElement.appendChild(paragraph);
}

function myFunction(){
    // start up the SocketIO connection to the server - the namespace 'test' is also included here if necessary
        //receive details from server
    socket.on('newMessage', function(msg) {
        console.log("Received message" + msg.message);
        writeToMessageBox(msg.message);
    });
}

function sendText(){


    let newName = nameElement.value;
    let newMessage = inputElement.value;

    console.log("Emitting message: ", newName, newMessage);
    socket.emit('newChatMessage', newName+": "+newMessage);
    inputElement.value = "";
}
