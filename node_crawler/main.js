/*
*	@Author: Cheng@NJU
*/

var request = require("request");
var cheerio = require("cheerio");
var iconv = require("iconv-lite");
var querystring = require("querystring");

var home_seed = "http://www.zhihu.com/explore";

var main_page = function(url, callback){
	request.get({url: home_seed, encoding: null}, function(error, response, body){
		if(error){
			console.log("抓取首页失败");
		}

		if(response.statusCode != 200){
			console.log("响应状态错误");
		}

		callback(cheerio.load(iconv.decode(body, "utf-8"), {decodeEntities: false}));
	});
}

var login_func = function(url, form_data, callback){
	request.post({uri: url, body: querystring.stringify(form_data)}, function(error, response, body){
		if(error){
			console.log("提交失败");
		}

		if(response.statusCode != 200){
			console.log("status code invalid");
		}

		//console.log(response.cookies);
		callback(response);
	});
}


var main_func = function(){
	//爬取首页
	main_page(home_seed, function(dom){
		var $ = dom;

		$("div[class='explore-feed feed-item']").each(function(i, e){
			console.log($(e).find("h2>a").attr('href'));

			//问题页面提取 爬取

		});
	})
}
/*
login_func('http://www.zhihu.com/login', {'email': 'cchain0615@gmail.com', 'password': 'kgbfbi'}, 
	function(data){
		console.log(data);
})*/

main_func()