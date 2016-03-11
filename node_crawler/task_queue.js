
TaskQueue = function(){
	this._array = [];
	this._callback = {};
}

TaskQueue.prototype.add = function(ele){
	this._array.push(ele);
	return this;
}

TaskQueue.prototype.size = function(){
	return this._array.length
}