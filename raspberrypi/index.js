const got = require('got');
var fs = require("fs");
const {spawn} = require('child_process');
const FormData = require('form-data');

const freq = 60 * 1000; // secs en millis
const ws_server = "https://kinotools.kinoki.fr";
const ws_port = 3000;

var socket = require('socket.io-client')( ws_server + ':' + ws_port );

function poll_python( response ){
    var python = spawn('python', ['sensors.py']);

    python.stdout.on('data', function (data) {
       console.log('Pipe data from python script ...');
       dataToSend = data.toString();
    });

    python.on('close', (code) => {
        var resp = JSON.parse( dataToSend );
        resp.data.timestamp = new Date().getTime();
        resp.data.user = "rafa226@gmail.com";
        socket.emit('environment_data', resp.data);
    });    
}

socket.on('connect', function(){
    console.log("connected");
});

socket.on('event', function(data){
    
});

socket.on('disconnect', function(){
    
});



var interval = setInterval(function() {
    poll_python();
}, freq);

//clearInterval(interval);