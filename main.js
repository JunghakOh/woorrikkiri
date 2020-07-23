/*var http = require('http');
var fs = require('fs');
var index = fs.readFileSync('index.html');

http.createServer(function (req, res) {
	  res.writeHead(200, {'Content-Type': 'text/plain'});
	  res.end(index);
}).listen(8000);
*/

var http = require('http');
var fs = require('fs');
var app = http.createServer(function(request,response){
	            var url = request.url;
	            if(url == '/'){
			                              url = '/index.html';
			                            }
	            response.writeHead(200);
	            response.end(fs.readFileSync(__dirname + url));

});
app.listen(8000);

add  some
