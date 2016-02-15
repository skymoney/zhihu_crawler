/*
*	@Author: Cheng@NJU
*/

var request = require("request");
var cheerio = require("cheerio");
var iconv = require("iconv-lite");

var home_seed = "http://www.zhihu.com/explore";

var main_page = function(url, callback){
	request.get({url: home_seed, encoding: null}, function(error, response, body){
		if(error){
			console.log("抓取首页失败");
		}

		callback(cheerio.load(iconv.decode(body, "utf-8"), {decodeEntities: false}));
	});
}


var main_func = function(callback){
	//爬取首页
	main_page(home_seed, function(dom){
		
	})
}