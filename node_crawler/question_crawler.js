/**
* Author: Cheng@NJU
*/

var fs = require("fs");
var request = require("request");
var cheerio = require("cheerio");
var iconv = require("iconv-lite");

var question_crawl = function(url, callback){
	//爬取问题页面
	request.get({url: url, encoding: null}, function(error, response, body){
		if(error){
			console.log("抓取问题页面失败");
		}

		if (response.statusCode != 200){
			console.log("网页状态错误， Status: " + response.statusCode);
		}

		console.log(response.headers);

		callback(cheerio.load(iconv.decode(body, "utf-8"), {decodeEntities: false}));
	});
}

var url = "https://www.zhihu.com/question/20351507";

question_crawl(url, function(dom){
	//console.log(dom("title").html());
	var title = dom("title").html();
	console.log(title);
	fs.writeFile("dom.html", dom.html(), function(error){
		if(error){
			throw error;
		}
	});
})