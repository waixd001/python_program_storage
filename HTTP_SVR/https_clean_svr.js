// curl -k https://localhost:8000/
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

https.createServer(options, (req, res) => {
	fs.readFile('index.html', function(err, data) {
		console.log("Request received.");
		res.writeHead(200, {"Content-Type": "text/html"});     
		res.write(data);
		res.end();
	});
}).listen(8000);
