// curl -k https://localhost:8000/
const https = require('https');
const fs = require('fs');
var privateKey  = fs.readFileSync('ssl/key.pem');
var certificate = fs.readFileSync('ssl/cert.pem');
// import express.js
var express = require('express');
var app = express();
var credentials = {key: privateKey, cert: certificate};

app.use(express.static(__dirname + '/public'));

app.get('/', function (req, res) {
	res.sendFile( __dirname + "/" + "index.html" );
});

// Start Sever
var httpsServer = https.createServer(credentials, app);
httpsServer.listen(8000, function(){
	console.log("server running at https://localhost:8000/")
});
