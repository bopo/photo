var aimmPic = {
	$ : function(objName){if(document.getElementById){return eval('document.getElementById("'+objName+'")')}else{return eval('document.all.'+objName)}},
	isIE : navigator.appVersion.indexOf("MSIE")!=-1?true:false,

	//Event
	addEvent : function(obj,eventType,func){if(obj.attachEvent){obj.attachEvent("on" + eventType,func);}else{obj.addEventListener(eventType,func,false)}},
	delEvent : function(obj,eventType,func){
		if(obj.detachEvent){obj.detachEvent("on" + eventType,func)}else{obj.removeEventListener(eventType,func,false)}
	},
	//Cookie
	readCookie : function(l){var i="",I=l+"=";if(document.cookie.length>0){var offset=document.cookie.indexOf(I);if(offset!=-1){offset+=I.length;var end=document.cookie.indexOf(";",offset);if(end==-1)end=document.cookie.length;i=document.cookie.substring(offset,end)}};return i},

	writeCookie : function(O,o,l,I){var i="",c="";if(l!=null){i=new Date((new Date).getTime()+l*3600000);i="; expires="+i.toGMTString()};if(I!=null){c=";domain="+I};document.cookie=O+"="+escape(o)+i+c},
	//Style
	readStyle:function(i,I){if(i.style[I]){return i.style[I]}else if(i.currentStyle){return i.currentStyle[I]}else if(document.defaultView&&document.defaultView.getComputedStyle){var l=document.defaultView.getComputedStyle(i,null);return l.getPropertyValue(I)}else{return null}},
	absPosition : function(obj,parentObj){ //位置
		var left = 0;
		var top = 0;
		var tempObj = obj;
		try{
			do{
				left += tempObj.offsetLeft;
				top += tempObj.offsetTop;
				tempObj = tempObj.offsetParent;
			}while(tempObj.id!=document.body && tempObj.id!=document.documentElement && tempObj != parentObj && tempObj!= null);
		}catch(e){};
		return {left:left,top:top};
	},
	_getJsData : function(url,callback){
		var _script = document.createElement("script");
		_script.type = "text/javascript";
		_script.language = "javascript";

		_script[_script.onreadystatechange === null ? "onreadystatechange" : "onload"] = function(){
			if(this.onreadystatechange){
				if(this.readyState != "complete" && this.readyState != "loaded") {return;}
			};
			if(callback){callback()};
			setTimeout(function(){_script.parentNode.removeChild(_script)},1000);
		};
		_script.src = url;

		document.getElementsByTagName("head")[0].appendChild(_script);

	},
	style : {
		setOpacity : function(obj,opacity){
			if(typeof(obj.style.opacity) != 'undefined'){
				obj.style.opacity = opacity;
			}else{
				obj.style.filter = 'Alpha(Opacity=' + (opacity*100) + ')';
			};
		}
	},
	extend : {
		show : function(obj,timeLimit){
			if(aimmPic.readStyle(obj,'display') === 'none'){
				obj.style.display = 'block';
			};
			aimmPic.style.setOpacity(obj,0);
			if(!timeLimit){
				timeLimit = 200;
			};
			var opacity = 0,step = timeLimit / 20;
			clearTimeout(obj._extend_show_timeOut);
			obj._extend_show_timeOut = setTimeout(function(){
				if(opacity >= 1){
					return;
				};
				opacity += 1/step;
				aimmPic.style.setOpacity(obj,opacity);
				obj._extend_show_timeOut = setTimeout(arguments.callee,20);

			},20);
		},
		hide : function(obj,timeLimit){
			if(!timeLimit){
				timeLimit = 200;
			};
			aimmPic.style.setOpacity(obj,1);
			var opacity = 1,step = timeLimit / 20;
			clearTimeout(obj._extend_show_timeOut);
			obj._extend_show_timeOut = setTimeout(function(){
				if(opacity <= 0){
					obj.style.display = 'none';
					aimmPic.style.setOpacity(obj,1);
					return;
				};
				opacity -= 1/step;
				aimmPic.style.setOpacity(obj,opacity);
				obj._extend_show_timeOut = setTimeout(arguments.callee,20);

			},20);
		},
		actPX : function(obj,key,start,end,speed,endFn,u){
			if(typeof(u) == 'undefined'){u = 'px'};
			clearTimeout(obj['_extend_actPX' + key.replace(/\-\.\=/,'_') + '_timeOut']);
			if(start > end){
				speed = - Math.abs(speed);
			}else{
				speed = Math.abs(speed);
			};
			var now = start;
			var length = end - start;
			obj['_extend_actPX' + key.replace(/\-\.\=/,'_') + '_timeOut'] = setTimeout(function(){
				now += speed;
				//debugger;
				var space = end - now;
				if(start < end){
					if(space < length/3){
						speed = Math.ceil(space/3);
					};
					if(space <= 0){ //end
						obj[key] = end + u;
						if(endFn){endFn()};
						return;
					};
				}else{
					if(space > length/3){
						speed = Math.floor(space/3);
					};
					if(space >= 0){ //end
						obj[key] = end + u;
						if(endFn){endFn()};
						return;
					};
				};

				obj[key] = now + u;
				obj['_extend_actPX' + key.replace(/\-\.\=/,'_') + '_timeOut'] = setTimeout(arguments.callee,20);

			},20);
		}
	}
};

aimmPic.Step = function(){
	this.stepIndex = 0; //当前步数
	this.classBase = 'step_'; //class规则
	this.limit = 3; //步总数
	this.stepTime = 20; //步时长
	this.element = null; //html对象
	this._timeObj = null; //setInterval对象
	this._type = '+'; //步方向
};
aimmPic.Step.prototype.action = function(type){
	if(!this.element){return};
	var tempThis = this;
	if(type=='+'){
		this._type = '+';
	}else{
		this._type = '-';
	};
	clearInterval(this._timeObj);
	this._timeObj = setInterval(function(){tempThis.nextStep()},this.stepTime);
};
aimmPic.Step.prototype.nextStep = function(){
	if(this._type == '+'){
		this.stepIndex ++;
	}else{
		this.stepIndex --;
	};

	if(this.stepIndex <= 0){
		clearInterval(this._timeObj);
		this.stepIndex = 0;
		if(this._type == '-'){
			if(this.onfirst){this.onfirst()};
		};
	};
	if(this.stepIndex >= this.limit){
		clearInterval(this._timeObj);
		this.stepIndex = this.limit;
		if(this._type == '+'){
			if(this.onlast){this.onlast()};
		};
	};
	this.element.className = this.classBase + this.stepIndex;

	if(this.onstep){this.onstep()};
};

var getData = {
	initF:false,
	nextUrl : "",
	preUrl : "",
	curUrl : "",
	fillData : function(flagPre){	//填充数据
		epidiascope.clearData();
		var images = slide_data.images;
		var flashPic = "",flashTxt = "";
		for(var i=0;i<images.length;i++){
			var title,pic,datetime,intro,middlePic,smallPic,commUrl,imageId;
			pic = images[i].image_url;
			datetime = images[i].createtime;
			title = images[i].title;
			intro = images[i].intro;
			middlePic = images[i].thumb_160;
			smallPic = images[i].thumb_50;
			commUrl = images[i].comment;
			imageId = images[i].id;

			epidiascope.add({
				src : pic,
				date : datetime,
				title : title,
				text : intro,
				lowsrc_b : middlePic,
				lowsrc_s : smallPic,
				comment : commUrl,
				id : imageId
			});

			//for flash
			if(flashPic != ""){flashPic += "|"};
			flashPic += pic;
			if(flashTxt != ""){flashTxt += "|"};
			if(!getData.initF){
				//第一次初始化时需要转码特殊字符
				flashTxt += encodeURIComponent(title) + "#　　" + encodeURIComponent(intro.replace(/<.*?>/g,''));
			}else{
				flashTxt += title + "#　　" + intro.replace(/<.*?>/g,'');
			}
		}

		getData.nextUrl = slide_data.next_album.interface;
		getData.preUrl = slide_data.prev_album.interface;

		//设置页面上的缩略图集的上一图集、下一图集
		var efpPrePic = aimmPic.$("efpPrePic");
		var efpPreTxt = aimmPic.$("efpPreTxt");
		var efpNextPic = aimmPic.$("efpNextPic");
		var efpNextTxt = aimmPic.$("efpNextTxt");
		efpPrePic.getElementsByTagName("a")[0].href = slide_data.prev_album.url;
		efpPrePic.getElementsByTagName("img")[0].src = slide_data.prev_album.thumb_50;
		efpPrePic.getElementsByTagName("img")[0].alt = slide_data.prev_album.title;
		efpPrePic.getElementsByTagName("img")[0].title = slide_data.prev_album.title;
		efpPreTxt.getElementsByTagName("a")[0].href = slide_data.prev_album.url;
		efpPreTxt.getElementsByTagName("a")[0].title = slide_data.prev_album.title;

		efpNextPic.getElementsByTagName("a")[0].href = slide_data.next_album.url;
		efpNextPic.getElementsByTagName("img")[0].src = slide_data.next_album.thumb_50;
		efpNextPic.getElementsByTagName("img")[0].alt = slide_data.next_album.title;
		efpNextPic.getElementsByTagName("img")[0].title = slide_data.next_album.title;
		efpNextTxt.getElementsByTagName("a")[0].href = slide_data.next_album.url;
		efpNextTxt.getElementsByTagName("a")[0].title = slide_data.next_album.title;

		document.title = slide_data.slide.title;//设置文档标题

		if(!getData.initF){
			//只需要初始化一次epidiascope
			epidiascope.init();
			getData.initF = true;
		}else{
			epidiascope.initNot();
			if(flagPre){
				//如果加载的是上一组，则跳到最后一张
				epidiascope.select(images.length-1);
			}
		}
	}
};

var epidiascope = {
	//picTitleId : "d_picTit",
	picMemoId : "d_picIntro",
	picTimeId : 'd_picTime',
	picListId : "efpPicListCont",
	BigPicId : "d_BigPic",
	picArrLeftId : "efpLeftArea",
	picArrRightId : "efpRightArea",
	playButtonId : "ecbPlay",
	statusId : "ecpPlayStatus",
	mainBoxId : "efpBigPic",
	PVUrl_a : null,
	PVUrl_m : null,
	repetition : false, //循环播放
	prefetch : false, //预读图片
	autoPlay : false, //自动播放
	mode : 'player', //模式 player|list
	autoPlayTimeObj : null,
	timeSpeed : 5,
	maxWidth : 948,
	filmstrips : [],
	prefetchImg : [],
	commNum : [],
	selectedIndex : -1,
	previousPicList : {},
	nextPicList : {},
	loadTime : 0,
	PVUrl_AC : '',

	/*2012-12-13 LLL*/
	canEntryNextAlbum:false,
	canEntryPrevAlbum:false,

	isEndMsgBoxOK:false,  //2013-01-28 by lll

	add : function(s){
		this.filmstrips.push(s);
		if(this.prefetch){ //预载图片
			var tempImg = new Image();
			tempImg.src = s.src;
			this.prefetchImg.push(tempImg);
		};
	},
	clearData : function(){
		this.selectedIndex = -1;
		this.filmstrips = [];
	},
	init : function(){
		var tempThis = this;
		var tempWidth = 0;
		// edit by fanrong@ 大图显示6张，平均每张的宽度为144 参考global_function 模板使用规则
		var filmstripsLen = 116;
		if(typeof __ch_id__ != 'undefined' && (__ch_id__ == '5' || __ch_id__ == '29' || __ch_id__ == '53' )){
			filmstripsLen =144;
		}
		if(this.filmstrips.length * filmstripsLen < aimmPic.$(this.picListId).offsetWidth){
			tempWidth = Math.round(aimmPic.$(this.picListId).offsetWidth / 2 - this.filmstrips.length * filmstripsLen/2);
		};

		var commKey = "";
		var tempHTML = '<div style="width:32760px;padding-left:' + tempWidth + 'px;">',i;
		for(i=0;i<this.filmstrips.length;i++){
			//子列表
			tempHTML += '<div class="pic" id="slide_' + i + '"><table cellspacing="0"><tr><td class="picCont"><table cellspacing="0"><tr><td class="pb_01"></td><td class="pb_02"></td><td class="pb_03"></td></tr><tr><td class="pb_04"></td><td><a href="javascript:epidiascope.select(' + i + ');" onclick="this.blur();"><img src="' + this.filmstrips[i].lowsrc_s + '" alt="' + this.filmstrips[i].title + '" oncontextmenu="event.returnValue=false;return false;" /></a></td><td class="pb_05"></td></tr><tr><td class="pb_06"></td><td class="pb_07"></td><td class="pb_08"></td></tr></table></td></tr></table></div>';
		};

		aimmPic.$(this.picListId).innerHTML = tempHTML + "</div>";

		//
		aimmPic.$(this.picArrLeftId).onclick = function(){epidiascope.previous();epidiascope.stop();};
		aimmPic.$(this.picArrRightId).onclick = function(){epidiascope.next();epidiascope.stop();};

		if(window.location.href.indexOf('2010.')!=-1){
			this.autoPlay = true;
			aimmPic.$(this.picArrRightId).onclick = function(){epidiascope.next();epidiascope.play();};
		};

		//按钮
		this.buttonNext = new epidiascope.Button('ecbNext'); //下一页
		this.buttonPre = new epidiascope.Button('ecbPre'); //上一页
		this.buttonPlay = new epidiascope.Button('ecbPlay'); //播放暂停
		//this.buttonCommTop = new epidiascope.Button('ecbComm'); //评论
		this.buttonMode = new epidiascope.Button('ecbMode'); //模式切换
		//this.buttonFullScreen = new epidiascope.Button('ecbFullScreen','2'); //全屏

		this.buttonSpeed = new epidiascope.Button('ecbSpeed'); //速度
		this.buttonModeReturn = new epidiascope.Button('ecbModeReturn'); //模式切换

		this.buttonPre.element.onclick = function(){epidiascope.previous();epidiascope.stop();};
		this.buttonNext.element.onclick = function(){epidiascope.next();epidiascope.stop();};
		this.buttonMode.element.onclick = function(){epidiascope.setMode('list');};
		this.buttonModeReturn.element.onclick = function(){epidiascope.setMode('player');};
		//this.buttonFullScreen.element.onclick = function(){epidiascope.fullScreen.chk()};
		//
		this.BigImgBox = aimmPic.$(this.BigPicId);

		//禁止右键
		this.BigImgBox.oncontextmenu = function(e){
			e = e?e:event;
			e.returnValue=false;
			return false;
		};

		this._imgLoad = function(){
			if(epidiascope.maxWidth == 0 ){return};
			if(this.width > epidiascope.maxWidth){
				this.width = epidiascope.maxWidth;
			};
			if(this.width < 948){
				// aimmPic.$('d_BigPic').style.paddingTop = "15px";
				this.style.border = "1px solid #000";
			}else{
				aimmPic.$('d_BigPic').style.paddingTop = "0px";
				this.style.border = "none";
				this.style.borderBottom = "1px solid #e5e6e6";
			};
			//隐藏loading图片
			clearTimeout(tempThis._hideBgTimeObj);
			aimmPic.$('d_BigPic').className = '';
		};

		this._preLoad = function(){
			var tempTime = new Date().getTime();
			var deltaTime = tempTime - epidiascope.loadTime;
			if(deltaTime > 5000 && Math.ceil(Math.random()*1000)==1){
				var tempLoadImage = new Image().src = "/interface/slow_log.php?time="+ deltaTime +"&url=" + encodeURIComponent(this.src) + "&t=2";
			}
		}

		this.createImg(this.filmstrips[0].src);

		var page;
		var imgId = window.location.search.match(/img=(\d+)/i);
		if(imgId){
			imgId = imgId[1];
			page = 0;
			for(var i = 0, len = this.filmstrips.length; i<len; i++){
				if(parseInt(this.filmstrips[i]['id']) == parseInt(imgId)){
					page = i;
					break;
				}
			}
		}else{
			page = window.location.hash.match(/p=(\d+)/i);
			if(page){
				page = page[1] - 1;
				if(page<0 || page >= this.filmstrips.length){
					page = 0;
				};
			}else{
				page = 0;
			};
		}
		this.select(page);

		if(!aimmPic.isIE){
			this.BigImgBox.style.position = 'relative';
			this.BigImgBox.style.overflow = "hidden";

		}else{

			clearInterval(this._ieButHeiTimeObj);
			this._ieButHeiTimeObj = setInterval(function(){tempThis.setPicButtonHeight()},300);
		};
		//设置下一图集
		var nextPics = aimmPic.$('efpNextGroup').getElementsByTagName('a');
		//aimmPic.$('nextPicsBut').href = nextPics[0].href;

		if(this.autoPlay){this.play()}else{this.stop()};

		if(this.onstart){this.onstart()};
		//iPad兼容处理
		this.iPad.init();
	},
	initNot : function(){
		//不是第一次的初始化，去掉一些按钮事件的重复加载。
		var tempThis = this;
		var tempWidth = 0;
		if(this.filmstrips.length * 115 < aimmPic.$(this.picListId).offsetWidth){
			tempWidth = Math.round(aimmPic.$(this.picListId).offsetWidth / 2 - this.filmstrips.length * 110/2);
		};
		var commKey = "";
		var tempHTML = '<div style="width:32760px;padding-left:' + tempWidth + 'px;">',i;
		for(i=0;i<this.filmstrips.length;i++){
			//子列表
			tempHTML += '<div class="pic" id="slide_' + i + '"><table cellspacing="0"><tr><td class="picCont"><table cellspacing="0"><tr><td class="pb_01"></td><td class="pb_02"></td><td class="pb_03"></td></tr><tr><td class="pb_04"></td><td><a href="javascript:epidiascope.select(' + i + ');" onclick="this.blur();"><img src="' + this.filmstrips[i].lowsrc_s + '" alt="' + this.filmstrips[i].title + '"  onload="DrawImage(this);" oncontextmenu="event.returnValue=false;return false;" /></a></td><td class="pb_05"></td></tr><tr><td class="pb_06"></td><td class="pb_07"></td><td class="pb_08"></td></tr></table></td></tr></table></div>';

			//评论数据
			var commId = this.filmstrips[i].comment.match(/channel\=(.*?)\&newsid\=(.*?)(\&|$)/);
			this.filmstrips[i].commNum = 0;
			this.filmstrips[i].commId = "";
			if(commId){
				if(i>140){continue};
				commId = commId[1] + ":" + commId[2] + ":0";

				this.filmstrips[i].commId = commId;
				if(commKey!=''){commKey+=','};
				commKey += commId;
			};
		};

		aimmPic._getJsData('/count?format=js&jsvar=g_clist&newslist='+commKey,function(){tempThis.readCommNum()});

		aimmPic.$(this.picListId).innerHTML = tempHTML + "</div>";
		this.createImg(this.filmstrips[0].src);

		var page;
		var imgId = window.location.search.match(/img=(\d+)/i);
		if(imgId){
			imgId = imgId[1];
			page = 0;
			for(var i = 0, len = this.filmstrips.length; i<len; i++){
				if(parseInt(this.filmstrips[i]['id']) == parseInt(imgId)){
					page = i;
					break;
				}
			}
		}else{
			page = window.location.hash.match(/p=(\d+)/i);
			if(page){
				page = page[1] - 1;
				if(page<0 || page >= this.filmstrips.length){
					page = 0;
				};
			}else{
				page = 0;
			};
		}
		this.select(page);
		setTimeout(function(){tempThis.picList.foucsTo(page + 1)},500);

		if(!aimmPic.isIE){
			this.BigImgBox.style.position = 'relative';
			this.BigImgBox.style.overflow = "hidden";

		}else{
			clearInterval(this._ieButHeiTimeObj);
			this._ieButHeiTimeObj = setInterval(function(){tempThis.setPicButtonHeight()},300);
		};

		//列表模式初始化标志
		this.listInitStatus = false;

		//设置下一图集
		var nextPics = aimmPic.$('efpNextGroup').getElementsByTagName('a');
		aimmPic.$('nextPicsBut').href = nextPics[0].href;
		if(this.autoPlay){this.play()}else{this.stop()};
		if(this.onstart){this.onstart()};
	},
	readTry : 0,
	readCommNum : function(){
		var tempThis = this;
		try{
			for(var i in g_clist.result.count){
				for(var j=0;j<this.filmstrips.length;j++){
					if(this.filmstrips[j].commId == i){
						this.filmstrips[j].commNum = g_clist.result.count[i].total;
						break;
					};
				};
			};
			aimmPic.$('commAObjNum').innerHTML = this.filmstrips[this.selectedIndex].commNum;
		}catch(e){
			this.readTry ++;
			if(this.readTry<10){
				setTimeout(function(){tempThis.readCommNum()},1000);
			};
			return;
		};

	},
	createImg : function(src){
		if(this.ImgObj1){
			this.ImgObj1.parentNode.removeChild(this.ImgObj1);
		};
		this.ImgObj1 = document.createElement("img");
		this.ImgObj1.onmousedown = function(){return false};
		this.ImgObj1.galleryImg = false;
		this.ImgObj1.onload = this._imgLoad;
		if(src){
			this.ImgObj1.src = src;
		};
		this.BigImgBox.appendChild(this.ImgObj1);
	},
	select : function(num,type){
		var tempThis = this;
		if(this.endSelect.status == 1){
			this.endSelect.close();
		};

		if(num == this.selectedIndex){return};
		var i;
		if(num >= this.filmstrips.length || num < 0){return};

		//aimmPic.$(this.picTitleId).innerHTML = this.filmstrips[num].title;

		//如果幻灯单张图片的字数小于30则居中显示，add by fanrong at 2012-08-06
		if(this.filmstrips[num].text.length <= 30) {
			this.filmstrips[num].text = "<center>" + this.filmstrips[num].text + "</center>";
		}
		aimmPic.$(this.picMemoId).innerHTML = this.filmstrips[num].text;
		aimmPic.$(this.picTimeId).innerHTML = this.filmstrips[num].date;

		//隐藏loading图片1秒钟
		aimmPic.$('d_BigPic').className = '';
		clearTimeout(this._hideBgTimeObj);
		this._hideBgTimeObj = setTimeout("aimmPic.$('d_BigPic').className='loading'",500);

		this.createImg();

		if(this._timeOut){
			for(i=0;i<this._timeOut.length;i++){
				clearTimeout(this._timeOut[i]);
			};
		};
		this._timeOut = [];

		if(this.ImgObj1.style.opacity === undefined){
			this.ImgObj1.src = 'news_mj_005.gif';
			//this.ImgObj1.filters[0].Apply();

			this.ImgObj1.src = this.filmstrips[num].src;
			this.ImgObj1.alt = this.filmstrips[num].title;
			//this.ImgObj1.filters[0].Play();
		}else{
			this.ImgObj1.style.opacity = 0;
			this.ImgObj1.src = this.filmstrips[num].src;
			this.ImgObj1.alt = this.filmstrips[num].title;
			for(i = 0;i <= 3;i ++){
				this._timeOut[i] = setTimeout("epidiascope.ImgObj1.style.opacity = " + i * 0.3,i * 100);
			};
			this._timeOut[i] = setTimeout("epidiascope.ImgObj1.style.opacity = 1;",4 * 100);
		};

		if(aimmPic.$("slide_" + this.selectedIndex)){aimmPic.$("slide_" + this.selectedIndex).className = "pic"};
		aimmPic.$("slide_" + num).className = "picOn";
		this.selectedIndex = num;

		this.picList.foucsTo(num + 1); //滚动

		aimmPic.$("total").innerHTML = '(<span class="cC00">'+(num + 1) + "</span>/" + this.filmstrips.length + ')';
		if(this.autoPlay){this.play()};
		this.PVCount(type, this.filmstrips[num].src); //PV统计

		//预载下一张
		if(!this.prefetch && num < this.filmstrips.length - 1){ //未预载全部图片
			this.reLoad = new Image();
			this.reLoad.src = this.filmstrips[num + 1].src;
			this.loadTime = new Date().getTime();
			this.reLoad.onload = this._preLoad;
		};

		// 百度分享
		function getLintStr(str) {
			str = str.replace(/<\/?[^>]*>/g,''); //去除HTML tag
			str.value = str.replace(/[ | ]*\n/g,'\n'); //去除行尾空白
			str = str.replace(/\n[\s| | ]*\r/g,'\n'); //去除多余空行
			return str;
		}
		var bdshare = aimmPic.$('bdshare');
		var selectedPic = epidiascope.filmstrips[epidiascope.selectedIndex];
		if(bdshare&&selectedPic){
			bdshare.setAttribute('data', '{"pic":"'+selectedPic.src+'","url":"'+location.href+'","text":"'+selectedPic.title+'"}');
		}
	},
	setPicButtonHeight : function(){
		aimmPic.$(this.picArrLeftId).style.height = aimmPic.$(this.picArrRightId).style.height = (aimmPic.$(this.picArrLeftId).parentNode.offsetHeight) + 'px';
	},
	/*huaban : function(num,type){
		var _w = 86, _h = 24;
		var selectedPic = epidiascope.filmstrips[epidiascope.selectedIndex];
		var param = {
			media     : selectedPic.src,
			url       : location.href,
			md        : 'aimm_cc',
			title     : '',
			style     : 'button',
			size      : 24,
			minWidth  : 100,
			minHeight : 100
		}
		var args = [];
		for( var p in param ){
			if (typeof param[p] == 'object' && param[p].constructor === Array) {
				for (m in param[p]) {
					args.push(p + '=' + encodeURIComponent(param[p][m] || ''));
				}
			}
			else {
				args.push(p + '=' + encodeURIComponent( param[p] || '' ) );
			}
		}
		aimmPic.$("huaban").innerHTML = '<iframe allowTransparency="true" frameborder="0" scrolling="no" src="http://huaban.com/share/button?' + args.join('&') + '" width="'+ _w+'" height="'+_h+'"></iframe>';
	},*/
	PVCount : function(type, imgurl){

		if(type=="auto"){
			if(this.PVUrl_a == null){return;};
		}else{
			if(this.PVUrl_m == null){return;};
		};
		if(!this.firstPage){ //第一次不请求PV
			this.firstPage = true;
			return;
		};
		//移除iframe
		if(this.PVFrame){
			this.PVFrame.parentNode.removeChild(this.PVFrame);
		};
		//create new iframe
		this.PVFrame = document.createElement("iframe");
		//style="height:0px;width:1px;overflow:hidden;"
		this.PVFrame.style.height = "0px";
		this.PVFrame.style.width = "1px";
		this.PVFrame.style.overflow = "hidden";
		this.PVFrame.style.display = "none";
		this.PVFrame.frameBorder = 0;
		aimmPic.$(this.mainBoxId).appendChild(this.PVFrame);
		var a=window.location.href;
		var b=Math.random();
		this.PVFrame.src = (type=="auto"?(a.indexOf('2010.')!==-1?(b<0?this.PVUrl_AC:this.PVUrl_a):this.PVUrl_a):this.PVUrl_m) + "/slide/count/" + pid + "?p=" + imgurl + "&r=" + Math.random();
		//set page
		this.setPageInfo(this.selectedIndex);
	},
	setPageInfo : function(num){
		window.location.hash = "p="+Math.round(num+1);
	},
	next : function(type){
		var tempNum = this.selectedIndex + 1;

		if(tempNum >= this.filmstrips.length){

			if(!this.canEntryNextAlbum)
			{
				this.canEntryNextAlbum = true;
				this.canEntryPrevAlbum = false;
			}
			else
			{
				window.location.href = slide_data.next_album.url;
				return;
			}

			if(this.repetition){ //循环播放
				tempNum = 0;
			}else{
				this.endSelect.open(); //选择
				//fanrong 建议添加统计
				//try{if(window._S_uaTrack){_S_uaTrack('ent_hdphoto_lastpage', '0');}}catch(e){}
				return;
			};
		};

		this.canEntryNextAlbum = false;

		//自动播放，判断下张图片是否载入
		if(type=="auto"){
			var testImg = new Image();
			testImg.src = this.filmstrips[tempNum].src;
			if(!testImg.complete){
				return;
			};
		};
		this.select(tempNum,type);
		//this.huaban(tempNum,type);
	},
	previous : function(){
		var tempNum = this.selectedIndex - 1;
		if(tempNum < 0){ //循环播放

			/*在首页位置 连击两次进入上一图集*/
			if(!this.canEntryPrevAlbum)
			{
				this.canEntryPrevAlbum = true;
				this.canEntryNextAlbum = false;
			}
			else
			{
				window.location.href = slide_data.prev_album.url;
			}

			if(this.repetition){
				tempNum = this.filmstrips.length - 1
			}else{
				//this.endSelect.open(); //选择    lll
				return;
			};
		};

		this.canEntryPrevAlbum = false;

		this.select(tempNum);
		//this.huaban(tempNum);
	},
	play : function(){
		clearInterval(this.autoPlayTimeObj);
		this.autoPlayTimeObj = setInterval("epidiascope.next('auto')",this.timeSpeed*1000);
		aimmPic.$(this.playButtonId).onclick = function(){epidiascope.stop()};
		aimmPic.$(this.statusId).className = "stop";
		aimmPic.$(this.statusId).title = "暂停";
		this.autoPlay = true;
	},
	stop : function(){
		clearInterval(this.autoPlayTimeObj);
		aimmPic.$(this.playButtonId).onclick = function(){epidiascope.play();epidiascope.next('auto');};
		aimmPic.$(this.statusId).className = "play";
		aimmPic.$(this.statusId).title = "播放";
		this.autoPlay = false;
	},

	rePlay : function(){ //重新播放
		if(this.endSelect.status == 1){this.endSelect.close()};
		this.autoPlay = true;
		this.select(0);
		//this.huaban(0);
	},
	downloadPic : function(){ //下载图片
		var thisFilmstrip = this.filmstrips[this.selectedIndex];

	},
	setMode : function(mode){ //切换模式
		this.speedBar.close();
		if(this.endSelect.status == 1){
			this.endSelect.close();
		};
		if(mode == 'list'){
			if(!this.listInitStatus){
				this.listInit();
			};

			this.buttonSpeed.hide();
			//this.buttonFullScreen.hide();
			this.buttonPlay.hide();
			this.buttonNext.hide();
			this.buttonPre.hide();
			aimmPic.$('ecbLine').style.visibility = 'hidden';
			this.buttonMode.element.style.display = 'none';
			this.buttonModeReturn.element.style.display = 'inline-block';
			this.buttonModeReturn.rePosi();

			this.stop();
			this.mode = 'list';

			this.listSelect(this.selectedIndex);

			aimmPic.$('eFramePic').style.display = 'none';
			aimmPic.$('ePicList-Wrap').style.display = 'inline-block';

			this.listView();
		}else{
			window.scroll(0,0);
			this.buttonSpeed.show();
			//this.buttonFullScreen.show();
			this.buttonPlay.show();
			this.buttonNext.show();
			this.buttonPre.show();
			aimmPic.$('ecbLine').style.visibility = 'visible';
			//this.buttonMode.element.className = '';

			this.buttonMode.element.style.display = 'inline-block';
			this.buttonModeReturn.element.style.display = 'none';

			this.mode = 'player';

			aimmPic.$('eFramePic').style.display = 'inline-block';
			aimmPic.$('ePicList-Wrap').style.display = 'none';

			//this.select(this.listSelectedIndex);
		};
	},
	switchMode : function(){
		if(this.mode == 'list'){
			this.setMode('player');
		}else{
			this.setMode('list');
		};
	},
	listData : null,
	listFrameId : 'ePicList',
	listSelectedIndex : null,
	listSelect : function(num){
		if(num<0 || num >= this.filmstrips.length){return};
		if(this.listSelectedIndex !== null){
			if(aimmPic.$('picList_' + this.listSelectedIndex)){aimmPic.$('picList_' + this.listSelectedIndex).className = 'picBox'};
		};
		this.listSelectedIndex = num;
		if(aimmPic.$('picList_' + this.listSelectedIndex)){aimmPic.$('picList_' + this.listSelectedIndex).className = 'picBox selected'};
	},
	listInit : function(){
		var tempThis = this;
		var html = '';
		for(var i=0;i<this.filmstrips.length;i++){
			html += '<div class="picBox clearfix" id="picList_'+ i +'" onmousemove="epidiascope.listSelect('+i+')" onclick="epidiascope.select(epidiascope.listSelectedIndex);epidiascope.setMode(\'player\');"><a href="javascript:void(0)"><img src="' + this.filmstrips[i].lowsrc_b + '" alt="" /></a></div>';
			//html += '<div class="picBox" id="picList_'+ i +'" onmousemove="epidiascope.listSelect('+i+')" onclick="epidiascope.select(epidiascope.listSelectedIndex);epidiascope.setMode(\'player\');"><table cellspacing="0"><tr><td><img src="' + this.filmstrips[i].lowsrc_b + '" alt="" /></td></tr></table><h3>' + this.filmstrips[i].title + '</h3><p class="time">' + this.filmstrips[i].date + '</p></div>';
		};
		aimmPic.$(this.listFrameId).innerHTML = html;
		this.listInitStatus = true;
	},
	listRowSize : 4, //每行个数
	listView : function(){
		var element = aimmPic.$('picList_' + this.listSelectedIndex);

		var bodyHeight = document.documentElement.clientHeight==0?document.body.clientHeight:document.documentElement.clientHeight;
		var scrollTop = document.documentElement.scrollTop==0?document.body.scrollTop:document.documentElement.scrollTop;

		var posi = aimmPic.absPosition(element,document.documentElement);
		if((posi.top + (element.offsetHeight * 0.3)) < scrollTop || (posi.top + (element.offsetHeight * 0.7)) > scrollTop + bodyHeight){
			window.scroll(0,posi.top - Math.round((bodyHeight - element.offsetHeight)/2));
		};
	},
	listMoveUp : function(){
		var newNum = this.listSelectedIndex - this.listRowSize;
		if(newNum<0){
			return;
		};
		this.listSelect(newNum);
		this.listView();
	},
	listMoveDown : function(){
		var newNum = this.listSelectedIndex + this.listRowSize;
		if(newNum>=this.filmstrips.length){
			nweNum = this.filmstrips.length - 1;
		};
		this.listSelect(newNum);
		this.listView();
	},
	listMoveLeft : function(){
		var newNum = this.listSelectedIndex - 1;
		if(newNum<0){
			return;
		};
		this.listSelect(newNum);
		this.listView();
	},
	listMoveRight : function(){
		var newNum = this.listSelectedIndex + 1;
		if(newNum>=this.filmstrips.length){
			return;
		};
		this.listSelect(newNum);
		this.listView();
	}
};
epidiascope.fullScreen = {
	status : 'window',
	chk : function(){ //检查是否支持flash全屏
		var flash_i = false;
		if (navigator.plugins) {
			for (var i=0; i < navigator.plugins.length; i++) {
				if (navigator.plugins[i].name.toLowerCase().indexOf("shockwave flash") >= 0) {
					flash_i = true;
				};
			};
			if(flash_i == false){
				this.full();
			};
		};
	},
	full : function(){
		if(this.status == 'window'){
			this.status = 'fullScreen';
			document.body.className = 'statusFull';
		}else{
			this.status = 'window';
			document.body.className = '';
		};
	}
};

epidiascope.speedBar = { //速度条
	boxId : "SpeedBox", //容器id
	contId : "SpeedCont", //内容id
	slideId : "SpeedSlide", //滑区id
	slideButtonId : "SpeedNonius", //滑块id
	infoId : "ecbSpeedInfo", //信息id
	grades : 10, //等级数
	grade : 5, //等级
	_slideHeight : 112, //滑区高度
	_slideButtonHeight : 9, //滑块高度
	_baseTop : 4, //top基数
	_marginTop : 0,
	_mouseDisparity : 0,
	_showStep : 0,
	_showType : 'close',
	_showTimeObj : null,
	init : function(){
		var tempThis = this;
		this._marginTop = Math.round(this._slideHeight/this.grades * (this.grade - 1));

		aimmPic.$(this.slideButtonId).style.top = this._marginTop + this._baseTop + "px";
		aimmPic.$(this.infoId).innerHTML = this.grade + "秒";

		//动画效果
		this.step = new aimmPic.Step();
		this.step.element = aimmPic.$(this.contId);
		this.step.limit = 6;
		this.step.stepTime = 20;
		this.step.classBase = 'speedStep_';
		this.step.onfirst = function(){
			epidiascope.buttonSpeed.setStatus('ok');
			aimmPic.$(epidiascope.speedBar.boxId).style.display = 'none';
		};

		aimmPic.$(this.slideId).onselectstart = function(){return false};
		aimmPic.$(this.slideButtonId).onmousedown = function(e){tempThis.mouseDown(e);return false};
		aimmPic.$(this.slideId).onmousedown = function(e){tempThis.slideClick(e);return false};

		epidiascope.buttonSpeed.element.onmousedown = function(){tempThis.show();return false;};
		epidiascope.buttonSpeed.element.onselectstart = function(){return false};
	},
	show : function(){
		if(this._showType == 'close'){
			this.open();
		}else{
			this.close();
		};
	},
	open : function(){
		var tempThis = this;
		this._showType = 'open';
		var tempMouseDown = document.onmousedown;
		var mousedown = function(e){
			e = window.event?event:e;
			if(e.stopPropagation){ //阻止冒泡
				e.stopPropagation();
			}else{
				window.event.cancelBubble = true;
			};
			var eventObj = e.target?e.target:e.srcElement;

			while(eventObj != aimmPic.$(tempThis.boxId) && eventObj != epidiascope.buttonSpeed.element){
				if(eventObj.parentNode){
					eventObj = eventObj.parentNode;
				}else{
					break;
				};
			};
			if(eventObj == aimmPic.$(tempThis.boxId) || eventObj == epidiascope.buttonSpeed.element){
				return;
			}else{
				tempThis.close();
			};
			aimmPic.delEvent(document,'mousedown',mousedown);
		};
		aimmPic.addEvent(document,'mousedown',mousedown);

		epidiascope.buttonSpeed.setStatus('down');
		aimmPic.$(this.boxId).style.display = 'block';

		this.step.action('+');
	},
	close : function(){
		var tempThis = this;
		this._showType = 'close';
		epidiascope.buttonSpeed.setStatus('ok');
		this.step.action('-');
	},
	slideClick : function(e){
		e = window.event?event:e;
		var Y = e.layerY?e.layerY:e.offsetY;
		if(!Y){return};

		this._marginTop = Y - Math.round(this._slideButtonHeight/2);
		if(this._marginTop<0){this._marginTop=0};
		this.grade = Math.round(this._marginTop/(this._slideHeight/this.grades) + 1);
		aimmPic.$(this.slideButtonId).style.top = this._marginTop + this._baseTop + "px";
		aimmPic.$(this.infoId).innerHTML = this.grade + "秒";

		if(this.onend){this.onend()};
	},
	setGrade : function(num){
		this.grade = num;
		epidiascope.timeSpeed = this.grade;
		this._marginTop = Math.round(this._slideHeight/this.grades * (this.grade - 1));

		aimmPic.$(this.slideButtonId).style.top = this._marginTop + this._baseTop + "px";
		aimmPic.$(this.infoId).innerHTML = this.grade + "秒";
		aimmPic.writeCookie("eSp",this.grade,720);
	},
	mouseDown : function(e){
		var tempThis = this;
		e = window.event?window.event:e;
		this._mouseDisparity = (e.pageY?e.pageY:e.clientY) - this._marginTop;
		document.onmousemove = function(e){tempThis.mouseOver(e)};
		document.onmouseup = function(){tempThis.mouseEnd()};
	},
	mouseOver : function(e){
		e = window.event?window.event:e;
		this._marginTop = (e.pageY?e.pageY:e.clientY) - this._mouseDisparity;
		if(this._marginTop > (this._slideHeight - this._slideButtonHeight)){this._marginTop = this._slideHeight - this._slideButtonHeight};
		if(this._marginTop < 0){this._marginTop = 0;};
		aimmPic.$(this.slideButtonId).style.top = this._marginTop + this._baseTop + "px";

		this.grade = Math.round(this._marginTop/(this._slideHeight/this.grades) + 1);

		if(this.onmover){this.onmover()};
	},
	mouseEnd : function(){
		if(this.onend){this.onend()};

		document.onmousemove = null;
		document.onmouseup = null;
	},
	onmover : function(){
		aimmPic.$(this.infoId).innerHTML = this.grade + "秒";
	},
	onend : function(){
		aimmPic.writeCookie("eSp",this.grade,720);
		epidiascope.timeSpeed = this.grade;
		if(epidiascope.autoPlay){epidiascope.play()};
	}
};

epidiascope.picList = { //列表滚动
	leftArrId : "efpListLeftArr",
	rightArrId : "efpListRightArr",
	picListId : "efpPicListCont",
	timeoutObj : null,
	pageWidth : 115,
	totalWidth : 0,
	offsetWidth : 0,
	lock : false,
	init : function(){
		aimmPic.$(this.rightArrId).onmousedown = function(){epidiascope.picList.leftMouseDown()};
		aimmPic.$(this.rightArrId).onmouseout = function(){epidiascope.picList.leftEnd("out");this.className='';};
		aimmPic.$(this.rightArrId).onmouseup = function(){epidiascope.picList.leftEnd("up")};
		aimmPic.$(this.leftArrId).onmousedown = function(){epidiascope.picList.rightMouseDown()};
		aimmPic.$(this.leftArrId).onmouseout = function(){epidiascope.picList.rightEnd("out");this.className='';};
		aimmPic.$(this.leftArrId).onmouseup = function(){epidiascope.picList.rightEnd("up")};
		this.totalWidth = epidiascope.filmstrips.length * this.pageWidth;
		this.offsetWidth = aimmPic.$(this.picListId).offsetWidth;
	},
	leftMouseDown : function(){
		if(this.lock){return};
		this.lock = true;
		this.timeoutObj = setInterval("epidiascope.picList.moveLeft()",10);
	},
	rightMouseDown : function(){
		if(this.lock){return};
		this.lock = true;
		this.timeoutObj = setInterval("epidiascope.picList.moveRight()",10);
	},
	moveLeft : function(){
		if(aimmPic.$(this.picListId).scrollLeft + 10 > this.totalWidth - this.offsetWidth){
			aimmPic.$(this.picListId).scrollLeft = this.totalWidth - this.offsetWidth;
			this.leftEnd();
		}else{
			aimmPic.$(this.picListId).scrollLeft += 10;
		};
	},
	moveRight : function(){
		aimmPic.$(this.picListId).scrollLeft -= 10;
		if(aimmPic.$(this.picListId).scrollLeft == 0){this.rightEnd()};
	},
	leftEnd : function(type){
		if(type=="out"){if(!this.lock){return}};
		clearInterval(this.timeoutObj);
		this.lock = false;
		this.move(30);
	},
	rightEnd : function(type){
		if(type=="out"){if(!this.lock){return}};
		clearInterval(this.timeoutObj);
		this.lock = false;
		this.move(-30);
	},
	foucsTo : function(num){
		if(this.lock){return;};
		this.lock = true;

		// 在倒数第三张加载"猜你喜欢"和"看了还看"数据，并渲染 daichang 20130201
	 	setTimeout(function(){
	 		if(epidiascope.filmstrips.length !=0) {
	 			if(epidiascope.selectedIndex > (epidiascope.filmstrips.length - 3)) {
	 				if(!epidiascope.isEndMsgBoxOK) {
	 					epidiascope.endSelect.render();
	 					epidiascope.isEndMsgBoxOK = true;
	 				}
	 			}
	 		}
	 	},1000);

		var _moveWidth = Math.round(num * this.pageWidth - this.offsetWidth / 2) - 33;

		_moveWidth -= aimmPic.$(this.picListId).scrollLeft;

		if(aimmPic.$(this.picListId).scrollLeft + _moveWidth < 0){
			_moveWidth = - aimmPic.$(this.picListId).scrollLeft;
		};
		if(aimmPic.$(this.picListId).scrollLeft + _moveWidth >= this.totalWidth - this.offsetWidth){
			_moveWidth = this.totalWidth - this.offsetWidth - aimmPic.$(this.picListId).scrollLeft;
		};

		this.move(_moveWidth);
	},
	move : function(num){
		var thisMove = num/4;
		if(Math.abs(thisMove)<1 && thisMove!=0){
			thisMove = (thisMove>=0?1:-1)*1;
		}else{
			thisMove = Math.round(thisMove);
		};

		var temp = aimmPic.$(this.picListId).scrollLeft + thisMove;
		if(temp <= 0){aimmPic.$(this.picListId).scrollLeft = 0;this.lock = false;return;}
		if(temp >= this.totalWidth - this.offsetWidth){aimmPic.$(this.picListId).scrollLeft = this.totalWidth - this.offsetWidth;this.lock = false;return;}
		aimmPic.$(this.picListId).scrollLeft += thisMove;
		num -= thisMove;
		if(Math.abs(num) <= 1){this.lock = false;return;}else{
			setTimeout("epidiascope.picList.move(" + num + ")",10)
		}
	}
};
//键盘控制
epidiascope.keyboard = {
	_timeObj : null,
	status : 'up',
	init : function(){
		var tempThis = this;
		aimmPic.addEvent(document,'keydown',function(e){tempThis.keyDown(e)});
		aimmPic.addEvent(document,'keyup',function(e){tempThis.keyUp(e)});

		// 产品需求不再有提示关闭按钮
		return;
		this.step = new aimmPic.Step();
		this.step.element = aimmPic.$('efpClew');
		this.step.limit = 5;
		this.step.stepTime = 30;
		this.step.classBase = 'efpClewStep_';

		if(!this.closeObj){
			this.closeObj = document.createElement('span');
			this.closeObj.style.display = 'block';
			this.closeObj.id = 'efpClewClose';
			aimmPic.$('efpClew').appendChild(this.closeObj);

			this.closeObj.onclick = function(){tempThis.clewClose()};
		};

		//提示次数
		this.clewNum = parseInt(aimmPic.readCookie('eCn'));
		if(isNaN(this.clewNum)){this.clewNum = 0};
		if(this.clewNum<5){
			//this.clewNum ++;
			//aimmPic.writeCookie('eCn',this.clewNum,24*7);
			this.clewOpen();
		};

	},
	clewClose : function(){
		this.step.action('-');
		aimmPic.writeCookie('eCn',6,24*7);
	},
	clewOpen : function(){
		this.step.action('+');
	},
	keyDown : function(e){
		if(this.status == 'down'){return};
		this.status = 'down';
		e = window.event?event:e;
		var obj = e.target?e.target:e.srcElement;
		if(obj.tagName == 'INPUT' || obj.tagName == 'SELECT' || obj.tagName == 'TEXTAREA'){
			if(e.stopPropagation){ //阻止冒泡
				e.stopPropagation();
			}else{
				window.event.cancelBubble = true;
			};
			return;
		};

		var stopKey = false; //是否阻止按键
		if(epidiascope.mode == 'list'){ //列表模式
			if(e.keyCode == 40){
				epidiascope.listMoveDown();
				stopKey = true;
			};
			if(e.keyCode == 37){
				epidiascope.listMoveLeft();
				stopKey = true;
			};
			if(e.keyCode == 38){
				epidiascope.listMoveUp();
				stopKey = true;
			};
			if(e.keyCode == 39){
				epidiascope.listMoveRight();
				stopKey = true;
			};
			if(e.keyCode == 13){
				epidiascope.setMode('player');
				epidiascope.select(epidiascope.listSelectedIndex);
				stopKey = true;
			};

		}else{ //默认模式
			if(e.keyCode == 39){
				epidiascope.next();
				stopKey = true;
				this.clewClose();
			};
			if(e.keyCode == 37){
				epidiascope.previous();
				stopKey = true;
				this.clewClose();
			};
		};

		if(e.keyCode == 9){
			epidiascope.switchMode();
			stopKey = true;
		};

		if(stopKey === true){
			if(e.preventDefault){
				e.preventDefault();
			}else{
				e.returnValue=false;
			};
		};
	},
	keyUp : function(){
		this.status = 'up';
	}
};

//结束选择
epidiascope.endSelect = {
	endSelectId : "endSelect",
	closeId : "endSelClose",
	rePlayButId : "rePlayBut",
	status : 0, //1:open  0:close
	open : function(){
		// 小图定位与图片中央，大图(超过可视区)定位于屏幕中央 daichang 20130131

		var clearSelection = function() {
			if(document.selection && document.selection.empty) {
				document.selection.empty();
			} else if(window.getSelection) {
				var sel = window.getSelection();
				sel.removeAllRanges();
			}
		};
		clearSelection();
		var docEle = document.documentElement;
		var docBody = document.body;
		var getWinHeight = function() {
			var clientHeight = 0;
			if(docBody.clientHeight && docEle.clientHeight) {
				clientHeight = (docBody.clientHeight < docEle.clientHeight) ? docBody.clientHeight : docEle.clientHeight;
			} else {
				clientHeight = (docBody.clientHeight > docEle.clientHeight) ? docBody.clientHeight : docEle.clientHeight;
			}
			return clientHeight;
		};
		var setPos = function(){
			var byId = aimmPic.$;
			//图片容器，尺寸与图片一致
			var imgWrap = byId(epidiascope.mainBoxId);
			var imgWrapHeight = imgWrap.offsetHeight;
			//弹窗
			var pop = byId(this.endSelectId);
			var popHeight = pop.offsetHeight;
			//原scrollTop
			var popTop = pop.offsetTop;
			//可视区
			var winHeight = getWinHeight();
			//离浏览器高度
			var top = Math.round(((winHeight-220) - popHeight)/2);
			// 滚动至位置
    		docEle.scrollTop = popTop - top;
			docBody.scrollTop = popTop - top;
		};
		this.status = 1;
			aimmPic.$(this.endSelectId).style.display = "block";   // lll 2013-01-18

			//临时修正ie6卡死问题，added by zy
			// var isIE6= /msie 6/i.test(navigator.userAgent);
			// if(isIE6){
			// 	var imgs = aimmPic.$(this.endSelectId).getElementsByTagName('img');
			// 	for(var i=0,iL=imgs.length; i<iL; i++){
			// 		if(imgs[i].style.width != '') break;
			// 		var cWidth = imgs[i].clientWidth,
			// 			cHeight = imgs[i].clientHeight - 15,
			// 			scaleYX = cHeight / cWidth,
			// 			scaleBln = scaleYX < 0.75 ? true : false,
			// 			rWidth, rHeight;
			// 		rWidth = scaleBln ? cWidth > 120 ? 120 : undefined : cHeight > 90 ? Math.round(90 / scaleYX) : undefined;
			// 		rHeight = scaleBln ? cWidth > 120 ? Math.round(scaleYX * 120) : undefined : cHeight > 90 ? 90 : undefined;
			// 		if(!rWidth) continue;
			// 		imgs[i].style.width = rWidth + 'px';
			// 		imgs[i].style.height = rHeight + 'px';
			// 	}
			// }
			//滚动页面至旭窗居中
			setPos.call(this);
			//added over
			// aimmPic.$(this.endSelectId).style.left = Math.round((aimmPic.$(epidiascope.mainBoxId).offsetWidth - aimmPic.$(this.endSelectId).offsetWidth)/2) + "px";
			// aimmPic.$(this.endSelectId).style.top = Math.round((aimmPic.$(epidiascope.mainBoxId).offsetHeight - aimmPic.$(this.endSelectId).offsetHeight)/2) + "px";

		epidiascope.stop();
		aimmPic.$(epidiascope.playButtonId).onclick = function(){epidiascope.rePlay()};
		aimmPic.$(this.closeId).onclick = function(){epidiascope.endSelect.close()};
		//aimmPic.$(this.rePlayButId).onclick = function(){epidiascope.rePlay()};

		// suda统计
		epidiascope.endSelect.sudaTrackWithAD('pageview');

		// 广告提供的判断广告有无的方法不准确，在打开时再次判断，如果没有广告，则显示热门图集
		var hotList = aimmPic.$('SI_Scroll_View_Wrap');
		// 是否有广告
		var hasAD = (function(){
			var ad = false;
			if(window.epidiaAdValid&&typeof epidiaAdValid == 'function'){
				// ad = epidiaAdValid(epidiaAdResource.end.ads);
				try{
					ad = epidiaAdValid(epidiaAdResource.end);
				}catch(e){

				}

			}
			return ad?true:false;
		})();
		if(hotList&&hasAD){
			hotList.style.display = 'none';
		}
	},
	close : function(){
		this.status = 0;
		//aimmPic.$(epidiascope.playButtonId).onclick = function(){epidiascope.play()};
		aimmPic.$(this.endSelectId).style.visibility = "hidden";
		epidiascope.endSelect.sudaTrackWithAD('close');
	},
	//请求"猜你喜欢"和"看了还看"数据并渲染 daichang 20130201
	render: function(){
		// daichang edited 20130607
		// 是否有广告
		var hasAD = (function(){
			var ad = false;
			if(window.epidiaAdValid&&typeof epidiaAdValid == 'function'){
				// ad = epidiaAdValid(epidiaAdResource.end.ads);
				try{
					ad = epidiaAdValid(epidiaAdResource.end);
				}catch(e){

				}

			}
			return ad?true:false;
		})();
		var Recommender =  window.___AimmRecommender___;
		if(typeof Recommender == 'undefined'){
			return;
		}
		// 渲染猜你喜欢，看了又看和高清图集
		Recommender.slide.render.init(hasAD);
	},
	sudaTrackWithAD: function(val){
		// suda统计
		//  具体咨询 @孙晗
		// 1.有广告时右上角关闭按钮 点击 每次点击 请求 suda-uatrack="key=new_photo_stats&value=close_with_ad" epidiascope中
		// 2.无广告时右上角关闭按钮 点击 每次点击 请求 suda-uatrack="key=new_photo_stats&value=close_with_ad"  epidiascope中
		// 5.推荐悬浮框弹出，且有广告时请求  suda-uatrack="key=new_photo_stats&value=pageview_with_ad"
		// 6.推荐悬浮框弹出，且无广告时请求  suda-uatrack="key=new_photo_stats&value=pageview_without_ad"
		var hasAD = (function() {
			var ad = 0;
			if (window.epidiaAdValid && typeof epidiaAdValid == 'function') {
				try {
					ad = epidiaAdValid(epidiaAdResource.end);
				} catch (e) {}
			}
			return ad ? 1 : 0;
		})();
		var sudaValSuffix = 'widthout_ad';
		var sudaVal = val+'_';
		if(hasAD){
			sudaValSuffix = 'width_ad';
		}
		sudaVal += sudaValSuffix;
		try{if(window._S_uaTrack){_S_uaTrack('new_photo_stats', sudaVal);}}catch(e){}
	}
};
epidiascope.onstart = function(){
	try{document.execCommand('BackgroundImageCache', false, true);}catch(e){};

	//速度条
	epidiascope.speedBar.grade = parseInt(aimmPic.readCookie("eSp"));
	if(isNaN(epidiascope.speedBar.grade)){epidiascope.speedBar.grade = 5};
	epidiascope.speedBar.init();
	epidiascope.speedBar.onend();

	//图片列表滚动
	epidiascope.picList.init();

	//按键控制
	epidiascope.keyboard.init();
};
//按钮构造函数
epidiascope.Button = function(id,classNameNum){
	this.status = 'ok';
	this.id = id;
	this.classNameNum = classNameNum;
	this.init();
};
epidiascope.Button.prototype.init = function(){
	if(!aimmPic.$(this.id)){return};
	var tempThis = this;
	this.element = aimmPic.$(this.id);

	if(this.element.offsetWidth == 43){
		this.classNameNum = '1';
	};
	if(!this.classNameNum){
		this.classNameNum = '';
	};
	this.mouseStatus = 'out';

	// this.bgDiv = document.createElement('div');
	// this.bgDiv.className = 'buttonBg' + this.classNameNum;
	// this.element.parentNode.style.position = 'relative';
	// this.element.style.position = 'relative';
	// this.element.style.zIndex = '5';
	// this.element.parentNode.appendChild(this.bgDiv);
	// this.bgDiv.style.top = this.element.offsetTop - 6 + 'px';
	// this.bgDiv.style.left = this.element.offsetLeft - 6 + 'px';

	//动画效果
	// this.step = new aimmPic.Step();
	// this.step.element = this.bgDiv;
	// this.step.limit = 3;
	// this.step.stepTime = 30;
	// this.step.classBase = 'buttonBg' + this.classNameNum + ' bBg' + this.classNameNum + 'S_';

	//aimmPic.addEvent(this.element,'mouseover',function(){tempThis.mouseover()});
	//aimmPic.addEvent(this.element,'mouseout',function(){tempThis.mouseout()});
	//aimmPic.addEvent(this.element,'mousedown',function(){tempThis.mousedown()});
	//aimmPic.addEvent(this.element,'mouseup',function(){tempThis.mouseup()});
};
epidiascope.Button.prototype.rePosi = function(){
	// this.bgDiv.style.top = this.element.offsetTop - 6 + 'px';
	// this.bgDiv.style.left = this.element.offsetLeft - 6 + 'px';
};
epidiascope.Button.prototype.setStatus = function(status){
	// switch(status){
	// 	case 'ok':
	// 		this.status = 'ok';
	// 		this.element.className = "";
	// 		if(this.mouseStatus == 'in'){
	// 			this.step.action('+');
	// 		}else{
	// 			this.step.action('-');
	// 		};
	// 		break;
	// 	case 'down':
	// 		this.status = 'down';
	// 		this.step.action('-');
	// 		this.element.className = "active";
	// 		break;
	// };
};
epidiascope.Button.prototype.hide = function(){
	this.element.style.visibility = 'hidden';
	// this.bgDiv.style.visibility = 'hidden';
};
epidiascope.Button.prototype.show = function(){
	this.element.style.visibility = 'visible';
	// this.bgDiv.style.visibility = 'visible';
};
epidiascope.iPad = {
	x : 0,
	y : 0,
	lastX : 0,
	lastY : 0,
	status : 'ok',
	init : function(){
		if(!(/\((iPhone|iPad|iPod)/i).test(navigator.userAgent)){ //不支持触屏
			return;
		};
		aimmPic.addEvent(window,'load',function(){setTimeout('window.scrollTo(0,78)'),500});

		// aimmPic.$('efpClew').style.backgroundImage = 'url(http://a.aimm-img.com/images/e_ipad_m_02.png)';
		var tempThis = this;
		aimmPic.addEvent(aimmPic.$('efpBigPic'),'touchstart',function(e){tempThis._touchstart(e)});
		aimmPic.addEvent(aimmPic.$('efpBigPic'),'touchmove',function(e){tempThis._touchmove(e)});
		aimmPic.addEvent(aimmPic.$('efpBigPic'),'touchend',function(e){tempThis._touchend(e)});
	},
	_touchstart : function(e){

		this.x = e.touches[0].pageX;
		this.scrollX = window.pageXOffset;
		this.scrollY = window.pageYOffset; //用于判断页面是否滚动
	},
	_touchmove : function(e){
		if(e.touches.length > 1){ //多点触摸
			this.status = 'ok';
			return;
		};
		this.lastX = e.touches[0].pageX;
		var cX = this.x - this.lastX;

		if(cX<0){//第一页禁止向左
			if(epidiascope.selectedIndex == 0){
				return;
			};
		};

		if(this.status == 'ok'){
			if(this.scrollY == window.pageYOffset && this.scrollX == window.pageXOffset && Math.abs(cX)>50){ //横向触摸
				if(cX>0){//最后一页禁止向右
					if(epidiascope.selectedIndex == epidiascope.filmstrips.length - 1){
						if(epidiascope.endSelect.status == 0){
							epidiascope.endSelect.open();
						};
						return;
					};
				};

				this.status = 'touch';
				aimmPic.$('efpBigPic').style.textAlign = 'left';
			}else{
				return;
			};
		};

		epidiascope.ImgObj1.style.marginLeft = - cX + Math.round((950 - epidiascope.ImgObj1.offsetWidth)/2) + 'px';
		e.preventDefault();
	},
	_touchend : function(e){
		if(this.status != 'touch'){return};
		this.status = 'ok';
		var cX = this.x - this.lastX;

		aimmPic.extend.actPX(epidiascope.ImgObj1.style,'marginLeft',epidiascope.ImgObj1.offsetLeft,cX>0?-951:951,200,function(){
			epidiascope.ImgObj1.style.marginLeft = 0;
			aimmPic.$('efpBigPic').style.textAlign = 'center';
			epidiascope.ImgObj1.style.paddingLeft = 0;
			if(cX<0){
				epidiascope.previous();
			}else{
				epidiascope.next();
			};
			//epidiascope.keyboard.clewClose();
		});
	}

}
// -------------------------------------------------------------------------------------

function DrawImage(ImgD,iwidth,iheight){
	var image=new Image();
	if(!iwidth)iwidth = 90;
	if(!iheight)iheight = 90; //定义允许高度，当宽度大于这个值时等比例缩小
	image.src=ImgD.src;
	if(image.width>0 && image.height>0){
		var flag=true;
		if(image.width/image.height>= iwidth/iheight){
			if(image.width>iwidth){
				ImgD.width=iwidth;
				ImgD.height=(image.height*iwidth)/image.width;
			}else{
				ImgD.width=image.width;
				ImgD.height=image.height;
			}
		}else{
			if(image.height>iheight){
				ImgD.height=iheight;
				ImgD.width=(image.width*iheight)/image.height;
			}else{
				ImgD.width=image.width;
				ImgD.height=image.height;
			}
		}
	}
};

//模拟Select mengjia 2008.12.30
function DivSelect(O,l,I){var C=this;C.id=O;C.divId=l;C.divClassName=I;C.selectObj=aimmPic.$(C.id);if(!C.selectObj){return};var o=C;C.status="close";C.parentObj=C.selectObj.parentNode;while(aimmPic.readStyle(C.parentObj,"display")!="block"){if(C.parentObj.parentNode){C.parentObj=C.parentObj.parentNode}else{break}};C.parentObj.style.position="relative";C.selectObjWidth=C.selectObj.offsetWidth;C.selectObjHeight=C.selectObj.offsetHeight;C.selectPosition=aimmPic.absPosition(C.selectObj,C.parentObj);C.selectObj.style.visibility="hidden";C.divObj=document.createElement("div");C.divObj.id=C.divId;if(C.divClassName){C.divObj.className=C.divClassName};C.parentObj.appendChild(C.divObj);C.divObj.style.width=C.selectObjWidth+"px";C.divObj.style.position="absolute";C.divObj.style.left=C.selectPosition.left+"px";C.divObj.style.top=C.selectPosition.top+"px";C.divObj.onclick=function(){o.click()};C.divObj_count=document.createElement("div");C.divObj.appendChild(C.divObj_count);C.divObj_count.className="ds_cont";C.divObj_title=document.createElement("div");C.divObj_count.appendChild(C.divObj_title);C.divObj_title.className="ds_title";C.divObj_button=document.createElement("div");C.divObj_count.appendChild(C.divObj_button);C.divObj_button.className="ds_button";C.divObj_list=document.createElement("div");C.divObj.appendChild(C.divObj_list);C.divObj_list.className="ds_list";C.divObj_list.style.display="none";C.divObj_listCont=document.createElement("div");C.divObj_list.appendChild(C.divObj_listCont);C.divObj_listCont.className="dsl_cont";C.list=[];var i;for(var c=0;c<C.selectObj.options.length;c++){i=document.createElement("p");C.list.push(i);C.divObj_listCont.appendChild(i);i.innerHTML=C.selectObj.options[c].innerHTML;if(C.selectObj.selectedIndex==c){C.divObj_title.innerHTML=i.innerHTML};i.onmouseover=function(){this.className="selected"};i.onmouseout=function(){this.className=""};i.onclick=function(){o.select(this.innerHTML)}};C.select=function(i){var l=this;for(var I=0;I<l.selectObj.options.length;I++){if(l.selectObj.options[I].innerHTML==i){l.selectObj.selectedIndex=I;if(l.selectObj.onchange){l.selectObj.onchange()};l.divObj_title.innerHTML=i;break}}};C.clickClose=function(I){var i=I.target?I.target:event.srcElement;do{if(i==o.divObj){return};if(i.tagName=="BODY"){break};i=i.parentNode}while(i.parentNode);o.close()};C.open=function(){var i=this;i.divObj_list.style.display="block";i.status="open";aimmPic.addEvent(document,"click",i.clickClose)};C.close=function(){var i=this;i.divObj_list.style.display="none";i.status="close";aimmPic.delEvent(document,"click",i.clickClose)};C.click=function(){var i=this;if(i.status=="open"){i.close()}else{i.open()}}};