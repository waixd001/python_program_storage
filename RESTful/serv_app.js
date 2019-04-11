var express = require('express');
var fs = require("fs");

var app = express();
app.use(express.static('public'));


var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

let data = fs.readFileSync('users.json');
users = JSON.parse( data );
console.log(users);


app.get('/', function (req, res) {
   res.sendFile( __dirname + "/" + "testpost.html" );
})
 

app.get('/listUsers', function (req, res) {
   fs.readFile("./" + "users.json", 'utf8', function (err, data) {
       console.log( data );
       res.end( data );
   });
})

app.get('/listUser/:uuid', function (req, res) {
   // First read existing users.
   fs.readFile( "./" + "users.json", 'utf8', function (err, data) {
       users = JSON.parse( data );
       var user = users["user" + req.params.uuid];
       console.log( user );
       res.end( JSON.stringify(user));
   });
})


app.post('/addUser', function (req, res) {
     var uuid  = req.body.uuid;
     var uname = req.body.uname;
     var prof  = req.body.prof;
     var passwd = req.body.passwd;
     var str = 'UPDATE: Name: '+ uname +', PROF: '+prof+' UUID: '+uuid+' PASS: '+ passwd;
     // json data
     var response = {
      "name":uname,
      "password":passwd,
      "profession":prof,
      "id": uuid
     };
     // name in json
     var user = "user" + uuid;
     users[user] = response;
     // stringify to a good looking table
     var input_data = JSON.stringify(users,null,4)

     console.log(users); //console log checking

     // write in
     fs.writeFile('users.json', input_data , 'utf8',function (err) {
      if (err)
          console.log(err);
      else
          console.log('Write operation complete. ( ' + str + ' )');
     });

     res.end(str);
});

app.put('/updateUser', function (req, res) {
     var uuid  = req.body.uuid;
     var uname = req.body.uname;
     var prof  = req.body.prof;
     var passwd = req.body.passwd;
     var str = 'UPDATE: Name: '+ uname +', PROF: '+prof+' UUID: '+uuid+' PASS: '+ passwd;

     users = JSON.parse( data );
     var user = users["user" + uuid];
     console.log( user );
     
     if (user == NULL){
        console.log('User not found');
     }else{
        console.log(str);
     }

     console.log( str );
     res.end(str);
})

app.delete('/deleteUser/:id', function (req, res) {

})

var server = app.listen(8081, function () {

   var host = server.address().address
   var port = server.address().port
 
   console.log("Example app listening at http://%s:%s", host, port)
 
 })