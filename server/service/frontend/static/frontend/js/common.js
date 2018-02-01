var aimm = {
	init : function(){
		aimm.sorts.init();
		aimm.modslider.init();
		aimm.slider.init();
		aimm.tabs.init();
		aimm.items.init();
		aimm.plot.init();
		aimm.fav.init();
		aimm.menufixed.init();
		aimm.lazyload.init();
	},sorts : {
		init : function(){
			$(".open").hover(
				function () {
					$(".sub-menu").show();
				},function () {
					$(".sub-menu").hide();
				}
			);
		}
	},modslider : {
		init : function(){
			$(".mod-slider").bind("mouseover",function(){
				$(this).addClass("hover");
			});
			$(".mod-slider").bind("mouseout",function(){
				$(this).removeClass("hover");
			});
		}
	},slider : {
		init : function(){
			var $cur = 1;
			var $i = 1;
			var $len = $('.slide-show-ctn').length;
			var $pages = Math.ceil($len / $i);
			var $w = $('.mod-slider').width();
			var $showbox = $('#slider-show');
			var $pre = $('.slide-left-btn');
			var $next = $('.slide-right-btn');
			var $autoFun;
			$(".mod-rep-img").height();
			//@Mr.Think***调用自动滚动
			autoSlide();
			//@Mr.Think***向前滚动
			$pre.click(function(){
				if (!$showbox.is(':animated')) {
					if ($cur == 1) {
						$showbox.animate({
							left: '-=' + $w * ($pages - 1)
						}, 800);
						$cur = $pages;
					}
					else {
						$showbox.animate({
							left: '+=' + $w
						}, 800);
						$cur--;
					}
				}
			});
			$next.click(function(){
				if (!$showbox.is(':animated')) { //判断展示区是否动画
					if ($cur == $pages) {  //在最后一个版面时,再向后滚动到第一个版面
						$showbox.animate({
							left: 0
						}, 800); //改变left值,切换显示版面,500(ms)为滚动时间,下同
						$cur = 1; //初始化版面为第一个版面
					}
					else {
						$showbox.animate({
							left: '-=' + $w
						}, 800);//改变left值,切换显示版面
						$cur++; //版面数累加
					}
				}
			});
			function autoSlide(){
				$next.trigger('click');
				$autoFun = setTimeout(autoSlide, 6000);
			}
			function clearAuto(){
				clearTimeout($autoFun);
			}
		}
	},tabs : {
		init : function(){
			$(".in-grid li:first-child").addClass("cur");
			$(".channel-ctn").find(".channel-show:first-child").show();
			$(".channel-ctn .channel-show").attr("id", function(){return idNumber("channel-")+ $(".channel-ctn .channel-show").index(this)});
			$(".in-grid li").click(function(){
				var c = $(".in-grid li");
				var index = c.index(this);
				var p = idNumber("channel-");
				show(c,index,p);
			});

			function show(channelMenu,num,prefix){
				var content= prefix + num;
				$('#'+content).siblings().hide();
				$('#'+content).show();
				channelMenu.eq(num).addClass("cur").siblings().removeClass("cur");
			};

			function idNumber(prefix){
				var idNum = prefix;
				return idNum;
			};
		}
	},items : {
		init : function(){
			$(".preview").hover(
				function () {
					$(this).attr("class","preview hover");
				},function () {
					$(this).attr("class","preview");
				}
			);
		}
	},plot : {
		init : function(){
			$(".plot").hide();
			$(function () {
				$(window).scroll(function(){
					if ($(window).scrollTop()>600){
						$(".plot").fadeIn(1500);
					}
					else
					{
						$(".plot").fadeOut(1500);
					}
				});
				$(".plot a").hover(function(){
					$(this).animate({width:"70px"});
				},function(){
					$(this).animate({width:"50px"});
				})
				$(".plot a").click(function(){
					var rel=$(this).attr("rel");
					var pos=$(rel).offset().top;
					$("html, body").animate({scrollTop:pos},1000);
				})
			});
		}
	},fav : {
		init : function(){
			$("#favorites,#favorites").click(
				function () {
					var ctrl = (navigator.userAgent.toLowerCase()).indexOf('mac') != -1 ? 'Command/Cmd' : 'CTRL';
					if (document.all) {
						window.external.addFavorite('http://www.95mm.com','\u7231\u7F8E\u7709')
					} else if (window.sidebar) {
						window.sidebar.addPanel('\u7231\u7F8E\u7709','http://www.95mm.com',"")
					} else {
						alert('\u6DFB\u52A0\u5931\u8D25\n\u60A8\u53EF\u4EE5\u5C1D\u8BD5\u901A\u8FC7\u5FEB\u6377\u952E'+ctrl+'+D\u52A0\u5165\u5230\u6536\u85CF\u5939~')
				}
			})
		}
	},menufixed : {
		init : function(){
			/*$(window).scroll(function(){
				if ($(window).scrollTop()>100){
					$(".main-nav").attr("class","main-nav fixed");
					$(".main-menu-bg").attr("class","main-menu-bg js");
				}
				else
				{
					$(".main-nav").attr("class","main-nav");
					$(".main-menu-bg").attr("class","main-menu-bg");
				}
			});*/
		}
	},lazyload : {
		init : function(){
			$("img").lazyload();
		}
	}
}