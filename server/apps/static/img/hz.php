document.writeln("<div class=\"mod-common clearfix\"><div class=\"mod-channel\"><div class=\"channel-title\"><h2>美女推荐</h2><div class=\"in-more clearfix\"><a href=\"/index-hot.html\">更多+</a></div></div><div class=\"channel-ctn\"><div class=\"cnt hz-list clearfix\"id=\"hz-list\"style=\"width:1000px;\"></div></div></div></div>");
$(document).ready(function() {
	var linkArray = [{
		id: 0,
		name: '酒店援交女抚胸弄乳自拍',
		url: 'http://cnrdn.com/XKb6',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q20933230-L.jpg'
	},
	{
		id: 1,
		name: '赤裸尤物爆乳撩人大胆诱惑',
		url: 'http://cnrdn.com/eeIC',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q20936090-L.jpg'
	},
	{
		id: 2,
		name: '婀娜的身段销魂写真秀嫩姿',
		url: 'http://cnrdn.com/nUh5',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q2093J90-L.jpg'
	},
	{
		id: 3,
		name: '豪乳美女美胸嫩白写真',
		url: 'http://cnrdn.com/XKb6',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q20939480-L.jpg'
	},
	{
		id: 4,
		name: '绝色美女深沟热裤惹诱惑',
		url: 'http://cnrdn.com/nUh5',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q2145T90-L.jpg'
	},
	{
		id: 5,
		name: '丰满性感尤物湿身诱惑',
		url: 'http://cnrdn.com/XKb6',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q21503230-L.jpg'
	},
	{
		id: 6,
		name: '少妇半裸写真让人心跳加速',
		url: 'http://cnrdn.com/XKb6',
		img: 'http://p.aimm-img.com/uploads/allimg/130812/2-130Q21506220-L.jpg'
	}]
	var $ = function(id) {
		return document.getElementById(id);
	}
	var addLoadEvent = function(func, obj) {
		var obj = obj ? obj: window;
		if (typeof obj.onload != 'function') obj.onload = func;
		else obj.onload = function() {
			obj.onload();
			func();
		};
	}
	var is_array = function(object) {
		return object != null && typeof object == "object" && 'splice' in object && 'join' in object;
	}
	var in_array = function(value, array) {
		for (var x in array) {
			if (array[x] == value) return true;
		}
		return false;
	}
	var array_push = function(array, value) {
		array[array.length] = value;
		return array;
	}
	var array_rand = function(array) {
		if (!is_array(array)) return;
		var array_length = array.length;
		var rand_seed; // = Math.random().toString().substr(2,array_length.toString().length);
		function getRandomSeed(array_length) {
			var seed;
			var result = true;
			do seed = parseInt(Math.random().toString().substr(2, array_length.toString().length));
			while (seed >= array_length);
			return seed;
		}
		var rand_seed = getRandomSeed(array_length);
		for (var i in array) {
			if (i == rand_seed) return array[i];
		}
	}
	function init() {
		var adlist = $('hz-list');
		var tempArr = [];
		do {
			temp1 = array_rand(linkArray);
			if (!in_array(temp1['id'], tempArr)) {
				array_push(tempArr, temp1['id']);
				var oA = document.createElement("a");
				var oImg = document.createElement("img");
				var oSp = document.createElement("span");
				oA.setAttribute('href', temp1['url']);
				oA.setAttribute('target', '_blank');
				oImg.setAttribute('src', temp1['img']);
				oSp.setAttribute('class', 'writing');
				oSp.innerHTML = temp1['name'];
				oA.appendChild(oImg);
				oA.appendChild(oSp);
				adlist.appendChild(oA);
			}
		} while ( tempArr . length < 5 );
	}
	addLoadEvent(init);
});