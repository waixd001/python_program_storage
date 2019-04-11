// curl -k https://localhost:8000/
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('ssl/key.pem'),
  cert: fs.readFileSync('ssl/cert.pem')
};

https.createServer(options, (req, res) => {
	fs.readFile('index.html', function(err, data) {
		res.writeHead(200, {"Content-Type": "text/html"});     
		res.write(data);
		res.end();
	});
}).listen(8000);
console.log("server running at https://localhost:8000/");
