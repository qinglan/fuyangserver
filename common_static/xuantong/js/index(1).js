!function(t){function e(i,o){if(n[i])return n[i].exports;var s={i:i,l:!1,exports:{}};return 0!=o&&(n[i]=s),t[i].call(s.exports,s,s.exports,e),s.l=!0,s.exports}var n={};e.m=t,e.c=n,e.d=function(t,n,i){e.o(t,n)||Object.defineProperty(t,n,{configurable:!1,enumerable:!0,get:i})},e.n=function(t){var n=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(n,"a",n),n},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="/static-dist/",e(e.s="60cb72804b65ebeebd50")}({0:function(t,e){t.exports=jQuery},"17c25dd7d9d2615bc1d9":function(t,e){function n(t){if(t)return i(t)}function i(t){for(var e in n.prototype)t[e]=n.prototype[e];return t}t.exports=n,n.prototype.on=n.prototype.addEventListener=function(t,e){return this._callbacks=this._callbacks||{},(this._callbacks["$"+t]=this._callbacks["$"+t]||[]).push(e),this},n.prototype.once=function(t,e){function n(){this.off(t,n),e.apply(this,arguments)}return n.fn=e,this.on(t,n),this},n.prototype.off=n.prototype.removeListener=n.prototype.removeAllListeners=n.prototype.removeEventListener=function(t,e){if(this._callbacks=this._callbacks||{},0==arguments.length)return this._callbacks={},this;var n=this._callbacks["$"+t];if(!n)return this;if(1==arguments.length)return delete this._callbacks["$"+t],this;for(var i,o=0;o<n.length;o++)if((i=n[o])===e||i.fn===e){n.splice(o,1);break}return this},n.prototype.emit=function(t){this._callbacks=this._callbacks||{};var e=[].slice.call(arguments,1),n=this._callbacks["$"+t];if(n){n=n.slice(0);for(var i=0,o=n.length;i<o;++i)n[i].apply(this,e)}return this},n.prototype.listeners=function(t){return this._callbacks=this._callbacks||{},this._callbacks["$"+t]||[]},n.prototype.hasListeners=function(t){return!!this.listeners(t).length}},"584608d4ce1895020bac":function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t};e.buyBtn=function(t){t.on("click",function(t){$.post($(t.currentTarget).data("url"),function(t){"object"===(void 0===t?"undefined":i(t))?window.location.href=t.url:$("#modal").modal("show").html(t)})})}},"60cb72804b65ebeebd50":function(t,e,n){"use strict";function i(t){return t&&t.__esModule?t:{default:t}}var o=n("d14d05cad9e7abf02a5d"),s=n("d5fb0e67d2d4c1ebaaed"),r=i(s),a=(n("9181c6995ae8c5c94b7a"),n("e66ca5da7109f35e9051")),l=i(a),c=(n("584608d4ce1895020bac"),n("6fb6f3ee9f12fe48c057"));new l.default,echo.init(),(0,o.chapterAnimate)(),function(){var t=$(".color-primary").css("color"),e=$(".color-warning").css("color");$("#freeprogress").easyPieChart({easing:"easeOutBounce",trackColor:"#ebebeb",barColor:t,scaleColor:!1,lineWidth:14,size:145,onStep:function(t,e,n){$("canvas").css("height","146px"),$("canvas").css("width","146px"),100==Math.round(n)&&$(this.el).addClass("done"),$(this.el).find(".percent").html(Translator.trans("course_set.learn_progress")+'<br><span class="num">'+Math.round(n)+"%</span>")}}),$("#orderprogress-plan").easyPieChart({easing:"easeOutBounce",trackColor:"#ebebeb",barColor:e,scaleColor:!1,lineWidth:14,size:145});var n=$("#orderprogress-plan").length>0?"transparent":"#ebebeb";$("#orderprogress").easyPieChart({easing:"easeOutBounce",trackColor:n,barColor:t,scaleColor:!1,lineWidth:14,size:145,onStep:function(t,e,n){100==Math.round(n)&&$(this.el).addClass("done"),$(this.el).find(".percent").html(Translator.trans("course_set.learn_progress")+'<br><span class="num">'+Math.round(n)+"%</span>")}})}(),function(){$(".member-expire").length&&$(".member-expire a").trigger("click")}(),function(){var t=parseInt($("#discount-endtime-countdown").data("remaintime"));if(t>=0){var e=new Date((new Date).valueOf()+1e3*t);$("#discount-endtime-countdown").countdown(e,function(t){$(this).html(t.strftime(Translator.trans("course_set.show.count_down_format_hint")))}).on("finish.countdown",function(){$(this).html(Translator.trans("course_set.show.time_finish_hint")),setTimeout(function(){$.post(app.crontab,function(){window.location.reload()})},2e3)})}}(),$(".js-attachment-list").length>0&&new r.default($(".js-attachment-list")),$(document).on("hidden.bs.modal",function(){"block"==$(".xt-course-buy-form").parent(".modal").css("display")?$(document.body).addClass("modal-open"):$(document.body).removeClass("modal-open")}),(0,c.xuantongBuyBtn)($(".js-buy-btn")),(0,c.xuantongBuyBtn)($(".js-task-buy-btn"))},"63fff8fb24f3bd1f61cd":function(t,e,n){"use strict";function i(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function o(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function s(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}Object.defineProperty(e,"__esModule",{value:!0});var r=function(){function t(t,e){for(var n=0;n<e.length;n++){var i=e[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(t,i.key,i)}}return function(e,n,i){return n&&t(e.prototype,n),i&&t(e,i),e}}(),a=n("17c25dd7d9d2615bc1d9"),l=function(t){return t&&t.__esModule?t:{default:t}}(a),c=function(t){function e(){return i(this,e),o(this,(e.__proto__||Object.getPrototypeOf(e)).apply(this,arguments))}return s(e,t),r(e,[{key:"delay",value:function(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:0,i=function(){var t=arguments;setTimeout(function(){e.apply(self,[].concat(Array.prototype.slice.call(t)))},n)};return this.on(t,i)}},{key:"once",value:function(t,e){var n=this,i=function i(){e.apply(n,[].concat(Array.prototype.slice.call(arguments))),n.off(t,i)};return this.on(t,i)}}]),e}(l.default);e.default=c},"6fb6f3ee9f12fe48c057":function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t};e.xuantongBuyBtn=function(t){t.on("click",function(t){var e=$(t.currentTarget).data("url"),n=$(t.currentTarget).data("playbackTime");(void 0===$(t.currentTarget).data("buyLimit")||$(t.currentTarget).data("buyLimit"))&&cd.confirm({title:"报名前请了解",content:'<div class="mbm clearfix"><span class="content-title pull-left"><strong>课程回放：</strong></span><span class="content-explain">如果您需要补课或复习，请于每节直播课程结束后观看回放，回放有效期为<strong style="color:#d9534f">'+n+"</strong>天，即当堂直播课程结束后有"+n+'天时间补课或复习。</span></div><div class="mbm clearfix"><span class="content-title pull-left"><strong>申请退课：</strong></span><span class="content-explain">如果您需要退课，请于第一节直播课开始前，在“我的订单”中提出申请，申请审核通过后将全额退款。直播课程开始后，将不再接受退课申请。</span></div><div class="mbm clearfix"><span class="content-title pull-left"><strong>开具发票：</strong></span><span class="content-explain">如果您需要发票，请在“我的订单”中提出申请，教室将于第一节直播课开始后开具电子发票。</span></div><div class="mbm clearfix text-center"><span>祝您在暄桐教室学习愉快。</sapn></div>',confirmText:Translator.trans("site.confirm"),cancelText:Translator.trans("site.close"),confirmClass:"btn cd-btn cd-btn-flat-primary cd-btn-lg",dialogClass:"modal-sm",confirm:function(){$.post(e,function(t){"object"===(void 0===t?"undefined":i(t))?window.location.href=t.url:($(".modal.fade").modal("hide"),$("#modal").modal("show").html(t))})}})})}},"8f3ec98312b1f1f6bafb":function(t,e){!function(){"use strict";function t(i){if(!i)throw new Error("No options passed to Waypoint constructor");if(!i.element)throw new Error("No element option passed to Waypoint constructor");if(!i.handler)throw new Error("No handler option passed to Waypoint constructor");this.key="waypoint-"+e,this.options=t.Adapter.extend({},t.defaults,i),this.element=this.options.element,this.adapter=new t.Adapter(this.element),this.callback=i.handler,this.axis=this.options.horizontal?"horizontal":"vertical",this.enabled=this.options.enabled,this.triggerPoint=null,this.group=t.Group.findOrCreate({name:this.options.group,axis:this.axis}),this.context=t.Context.findOrCreateByElement(this.options.context),t.offsetAliases[this.options.offset]&&(this.options.offset=t.offsetAliases[this.options.offset]),this.group.add(this),this.context.add(this),n[this.key]=this,e+=1}var e=0,n={};t.prototype.queueTrigger=function(t){this.group.queueTrigger(this,t)},t.prototype.trigger=function(t){this.enabled&&this.callback&&this.callback.apply(this,t)},t.prototype.destroy=function(){this.context.remove(this),this.group.remove(this),delete n[this.key]},t.prototype.disable=function(){return this.enabled=!1,this},t.prototype.enable=function(){return this.context.refresh(),this.enabled=!0,this},t.prototype.next=function(){return this.group.next(this)},t.prototype.previous=function(){return this.group.previous(this)},t.invokeAll=function(t){var e=[];for(var i in n)e.push(n[i]);for(var o=0,s=e.length;s>o;o++)e[o][t]()},t.destroyAll=function(){t.invokeAll("destroy")},t.disableAll=function(){t.invokeAll("disable")},t.enableAll=function(){t.Context.refreshAll();for(var e in n)n[e].enabled=!0;return this},t.refreshAll=function(){t.Context.refreshAll()},t.viewportHeight=function(){return window.innerHeight||document.documentElement.clientHeight},t.viewportWidth=function(){return document.documentElement.clientWidth},t.adapters=[],t.defaults={context:window,continuous:!0,enabled:!0,group:"default",horizontal:!1,offset:0},t.offsetAliases={"bottom-in-view":function(){return this.context.innerHeight()-this.adapter.outerHeight()},"right-in-view":function(){return this.context.innerWidth()-this.adapter.outerWidth()}},window.Waypoint=t}(),function(){"use strict";function t(t){window.setTimeout(t,1e3/60)}function e(t){this.element=t,this.Adapter=o.Adapter,this.adapter=new this.Adapter(t),this.key="waypoint-context-"+n,this.didScroll=!1,this.didResize=!1,this.oldScroll={x:this.adapter.scrollLeft(),y:this.adapter.scrollTop()},this.waypoints={vertical:{},horizontal:{}},t.waypointContextKey=this.key,i[t.waypointContextKey]=this,n+=1,o.windowContext||(o.windowContext=!0,o.windowContext=new e(window)),this.createThrottledScrollHandler(),this.createThrottledResizeHandler()}var n=0,i={},o=window.Waypoint,s=window.onload;e.prototype.add=function(t){var e=t.options.horizontal?"horizontal":"vertical";this.waypoints[e][t.key]=t,this.refresh()},e.prototype.checkEmpty=function(){var t=this.Adapter.isEmptyObject(this.waypoints.horizontal),e=this.Adapter.isEmptyObject(this.waypoints.vertical),n=this.element==this.element.window;t&&e&&!n&&(this.adapter.off(".waypoints"),delete i[this.key])},e.prototype.createThrottledResizeHandler=function(){function t(){e.handleResize(),e.didResize=!1}var e=this;this.adapter.on("resize.waypoints",function(){e.didResize||(e.didResize=!0,o.requestAnimationFrame(t))})},e.prototype.createThrottledScrollHandler=function(){function t(){e.handleScroll(),e.didScroll=!1}var e=this;this.adapter.on("scroll.waypoints",function(){(!e.didScroll||o.isTouch)&&(e.didScroll=!0,o.requestAnimationFrame(t))})},e.prototype.handleResize=function(){o.Context.refreshAll()},e.prototype.handleScroll=function(){var t={},e={horizontal:{newScroll:this.adapter.scrollLeft(),oldScroll:this.oldScroll.x,forward:"right",backward:"left"},vertical:{newScroll:this.adapter.scrollTop(),oldScroll:this.oldScroll.y,forward:"down",backward:"up"}};for(var n in e){var i=e[n],o=i.newScroll>i.oldScroll,s=o?i.forward:i.backward;for(var r in this.waypoints[n]){var a=this.waypoints[n][r];if(null!==a.triggerPoint){var l=i.oldScroll<a.triggerPoint,c=i.newScroll>=a.triggerPoint,f=l&&c,u=!l&&!c;(f||u)&&(a.queueTrigger(s),t[a.group.id]=a.group)}}}for(var d in t)t[d].flushTriggers();this.oldScroll={x:e.horizontal.newScroll,y:e.vertical.newScroll}},e.prototype.innerHeight=function(){return this.element==this.element.window?o.viewportHeight():this.adapter.innerHeight()},e.prototype.remove=function(t){delete this.waypoints[t.axis][t.key],this.checkEmpty()},e.prototype.innerWidth=function(){return this.element==this.element.window?o.viewportWidth():this.adapter.innerWidth()},e.prototype.destroy=function(){var t=[];for(var e in this.waypoints)for(var n in this.waypoints[e])t.push(this.waypoints[e][n]);for(var i=0,o=t.length;o>i;i++)t[i].destroy()},e.prototype.refresh=function(){var t,e=this.element==this.element.window,n=e?void 0:this.adapter.offset(),i={};this.handleScroll(),t={horizontal:{contextOffset:e?0:n.left,contextScroll:e?0:this.oldScroll.x,contextDimension:this.innerWidth(),oldScroll:this.oldScroll.x,forward:"right",backward:"left",offsetProp:"left"},vertical:{contextOffset:e?0:n.top,contextScroll:e?0:this.oldScroll.y,contextDimension:this.innerHeight(),oldScroll:this.oldScroll.y,forward:"down",backward:"up",offsetProp:"top"}};for(var s in t){var r=t[s];for(var a in this.waypoints[s]){var l,c,f,u,d,h=this.waypoints[s][a],p=h.options.offset,g=h.triggerPoint,y=0,m=null==g;h.element!==h.element.window&&(y=h.adapter.offset()[r.offsetProp]),"function"==typeof p?p=p.apply(h):"string"==typeof p&&(p=parseFloat(p),h.options.offset.indexOf("%")>-1&&(p=Math.ceil(r.contextDimension*p/100))),l=r.contextScroll-r.contextOffset,h.triggerPoint=Math.floor(y+l-p),c=g<r.oldScroll,f=h.triggerPoint>=r.oldScroll,u=c&&f,d=!c&&!f,!m&&u?(h.queueTrigger(r.backward),i[h.group.id]=h.group):!m&&d?(h.queueTrigger(r.forward),i[h.group.id]=h.group):m&&r.oldScroll>=h.triggerPoint&&(h.queueTrigger(r.forward),i[h.group.id]=h.group)}}return o.requestAnimationFrame(function(){for(var t in i)i[t].flushTriggers()}),this},e.findOrCreateByElement=function(t){return e.findByElement(t)||new e(t)},e.refreshAll=function(){for(var t in i)i[t].refresh()},e.findByElement=function(t){return i[t.waypointContextKey]},window.onload=function(){s&&s(),e.refreshAll()},o.requestAnimationFrame=function(e){(window.requestAnimationFrame||window.mozRequestAnimationFrame||window.webkitRequestAnimationFrame||t).call(window,e)},o.Context=e}(),function(){"use strict";function t(t,e){return t.triggerPoint-e.triggerPoint}function e(t,e){return e.triggerPoint-t.triggerPoint}function n(t){this.name=t.name,this.axis=t.axis,this.id=this.name+"-"+this.axis,this.waypoints=[],this.clearTriggerQueues(),i[this.axis][this.name]=this}var i={vertical:{},horizontal:{}},o=window.Waypoint;n.prototype.add=function(t){this.waypoints.push(t)},n.prototype.clearTriggerQueues=function(){this.triggerQueues={up:[],down:[],left:[],right:[]}},n.prototype.flushTriggers=function(){for(var n in this.triggerQueues){var i=this.triggerQueues[n],o="up"===n||"left"===n;i.sort(o?e:t);for(var s=0,r=i.length;r>s;s+=1){var a=i[s];(a.options.continuous||s===i.length-1)&&a.trigger([n])}}this.clearTriggerQueues()},n.prototype.next=function(e){this.waypoints.sort(t);var n=o.Adapter.inArray(e,this.waypoints);return n===this.waypoints.length-1?null:this.waypoints[n+1]},n.prototype.previous=function(e){this.waypoints.sort(t);var n=o.Adapter.inArray(e,this.waypoints);return n?this.waypoints[n-1]:null},n.prototype.queueTrigger=function(t,e){this.triggerQueues[e].push(t)},n.prototype.remove=function(t){var e=o.Adapter.inArray(t,this.waypoints);e>-1&&this.waypoints.splice(e,1)},n.prototype.first=function(){return this.waypoints[0]},n.prototype.last=function(){return this.waypoints[this.waypoints.length-1]},n.findOrCreate=function(t){return i[t.axis][t.name]||new n(t)},o.Group=n}(),function(){"use strict";function t(t){this.$element=e(t)}var e=window.jQuery,n=window.Waypoint;e.each(["innerHeight","innerWidth","off","offset","on","outerHeight","outerWidth","scrollLeft","scrollTop"],function(e,n){t.prototype[n]=function(){var t=Array.prototype.slice.call(arguments);return this.$element[n].apply(this.$element,t)}}),e.each(["extend","inArray","isEmptyObject"],function(n,i){t[i]=e[i]}),n.adapters.push({name:"jquery",Adapter:t}),n.Adapter=t}(),function(){"use strict";function t(t){return function(){var n=[],i=arguments[0];return t.isFunction(arguments[0])&&(i=t.extend({},arguments[1]),i.handler=arguments[0]),this.each(function(){var o=t.extend({},i,{element:this});"string"==typeof o.context&&(o.context=t(this).closest(o.context)[0]),n.push(new e(o))}),n}}var e=window.Waypoint;window.jQuery&&(window.jQuery.fn.waypoint=t(window.jQuery)),window.Zepto&&(window.Zepto.fn.waypoint=t(window.Zepto))}()},"9181c6995ae8c5c94b7a":function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i={},o=navigator.userAgent.toLowerCase(),s=void 0;(s=o.match(/msie ([\d.]+)/))?i.ie=s[1]:(s=o.match(/firefox\/([\d.]+)/))?i.firefox=s[1]:(s=o.match(/chrome\/([\d.]+)/))?i.chrome=s[1]:(s=o.match(/opera.([\d.]+)/))?i.opera=s[1]:(s=o.match(/version\/([\d.]+).*safari/))&&(i.safari=s[1]),i.ie10=/MSIE\s+10.0/i.test(navigator.userAgent),i.ie11=/Trident\/7\./.test(navigator.userAgent),i.edge=/Edge\/13./i.test(navigator.userAgent);var r=function(){return navigator.userAgent.match(/(iPhone|iPod|Android|ios|iPad)/i)},a=function(t){return t.replace(/<[^>]+>/g,"").replace(/&nbsp;/gi,"")},l=function(){$('[data-toggle="tooltip"]').tooltip({html:!0})},c=function(){$('[data-toggle="popover"]').popover({html:!0})},f=function(t){var e="",n=parseInt(t%86400/3600),i=parseInt(t%3600/60),o=t%60;return n>0&&(e+=n+":"),i.toString().length<2?e+="0"+i+":":e+=i+":",o.toString().length<2?e+="0"+o:e+=o,e},u=function(t){for(var e=t.split(":"),n=0,i=0;i<e.length;i++)e.length>2&&(0==i&&(n+=3600*e[i]),1==i&&(n+=60*e[i]),2==i&&(n+=parseInt(e[i]))),e.length<=2&&(0==i&&(n+=60*e[i]),1==i&&(n+=parseInt(e[i])));return n},d=function(){return 1==$("meta[name='is-login']").attr("content")},h=function(t){return null===t||""===t||void 0===t||0===Object.keys(t).length},p=function(t){var e={};return $.each(t,function(){e[this.name]?(e[this.name].push||(e[this.name]=[e[this.name]]),e[this.name].push(this.value||"")):e[this.name]=this.value||""}),e};e.Browser=i,e.isLogin=d,e.isMobileDevice=r,e.delHtmlTag=a,e.initTooltips=l,e.initPopover=c,e.sec2Time=f,e.time2Sec=u,e.arrayToJson=p,e.isEmpty=h},a25cd36d0cf21bc7df34:function(t,e,n){var i=!1;(function(){!function(t){"function"==typeof i&&i.amd?i(["jquery"],t):t(jQuery)}(function(t){function e(e,i,o){var i={content:{message:"object"==typeof i?i.message:i,title:i.title?i.title:"",icon:i.icon?i.icon:"",url:i.url?i.url:"#",target:i.target?i.target:"-"}};o=t.extend(!0,{},i,o),this.settings=t.extend(!0,{},n,o),this._defaults=n,"-"==this.settings.content.target&&(this.settings.content.target=this.settings.url_target),this.animations={start:"webkitAnimationStart oanimationstart MSAnimationStart animationstart",end:"webkitAnimationEnd oanimationend MSAnimationEnd animationend"},"number"==typeof this.settings.offset&&(this.settings.offset={x:this.settings.offset,y:this.settings.offset}),this.init()}var n={element:"body",position:null,type:"info",allow_dismiss:!0,newest_on_top:!1,showProgressbar:!1,placement:{from:"top",align:"right"},offset:20,spacing:10,z_index:1031,delay:5e3,timer:1e3,url_target:"_blank",mouse_over:null,animate:{enter:"animated fadeInDown",exit:"animated fadeOutUp"},onShow:null,onShown:null,onClose:null,onClosed:null,icon_type:"class",template:'<div data-notify="container" class="col-xs-11 col-sm-4 alert alert-{0}" role="alert"><button type="button" aria-hidden="true" class="close" data-notify="dismiss">&times;</button><span data-notify="icon"></span> <span data-notify="title">{1}</span> <span data-notify="message">{2}</span><div class="progress" data-notify="progressbar"><div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div></div><a href="{3}" target="{4}" data-notify="url"></a></div>'};String.format=function(){for(var t=arguments[0],e=1;e<arguments.length;e++)t=t.replace(RegExp("\\{"+(e-1)+"\\}","gm"),arguments[e]);return t},t.extend(e.prototype,{init:function(){var t=this;this.buildNotify(),this.settings.content.icon&&this.setIcon(),"#"!=this.settings.content.url&&this.styleURL(),this.styleDismiss(),this.placement(),this.bind(),this.notify={$ele:this.$ele,update:function(e,n){var i={};"string"==typeof e?i[e]=n:i=e;for(var e in i)switch(e){case"type":this.$ele.removeClass("alert-"+t.settings.type),this.$ele.find('[data-notify="progressbar"] > .progress-bar').removeClass("progress-bar-"+t.settings.type),t.settings.type=i[e],this.$ele.addClass("alert-"+i[e]).find('[data-notify="progressbar"] > .progress-bar').addClass("progress-bar-"+i[e]);break;case"icon":var o=this.$ele.find('[data-notify="icon"]');"class"==t.settings.icon_type.toLowerCase()?o.removeClass(t.settings.content.icon).addClass(i[e]):(o.is("img")||o.find("img"),o.attr("src",i[e]));break;case"progress":var s=t.settings.delay-t.settings.delay*(i[e]/100);this.$ele.data("notify-delay",s),this.$ele.find('[data-notify="progressbar"] > div').attr("aria-valuenow",i[e]).css("width",i[e]+"%");break;case"url":this.$ele.find('[data-notify="url"]').attr("href",i[e]);break;case"target":this.$ele.find('[data-notify="url"]').attr("target",i[e]);break;default:this.$ele.find('[data-notify="'+e+'"]').html(i[e])}var r=this.$ele.outerHeight()+parseInt(t.settings.spacing)+parseInt(t.settings.offset.y);t.reposition(r)},close:function(){t.close()}}},buildNotify:function(){var e=this.settings.content;this.$ele=t(String.format(this.settings.template,this.settings.type,e.title,e.message,e.url,e.target)),this.$ele.attr("data-notify-position",this.settings.placement.from+"-"+this.settings.placement.align),this.settings.allow_dismiss||this.$ele.find('[data-notify="dismiss"]').css("display","none"),(this.settings.delay<=0&&!this.settings.showProgressbar||!this.settings.showProgressbar)&&this.$ele.find('[data-notify="progressbar"]').remove()},setIcon:function(){"class"==this.settings.icon_type.toLowerCase()?this.$ele.find('[data-notify="icon"]').addClass(this.settings.content.icon):this.$ele.find('[data-notify="icon"]').is("img")?this.$ele.find('[data-notify="icon"]').attr("src",this.settings.content.icon):this.$ele.find('[data-notify="icon"]').append('<img src="'+this.settings.content.icon+'" alt="Notify Icon" />')},styleDismiss:function(){this.$ele.find('[data-notify="dismiss"]').css({position:"absolute",right:"10px",top:"5px",zIndex:this.settings.z_index+2})},styleURL:function(){this.$ele.find('[data-notify="url"]').css({backgroundImage:"url(data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)",height:"100%",left:"0px",position:"absolute",top:"0px",width:"100%",zIndex:this.settings.z_index+1})},placement:function(){var e=this,n=this.settings.offset.y,i={display:"inline-block",margin:"0px auto",position:this.settings.position?this.settings.position:"body"===this.settings.element?"fixed":"absolute",transition:"all .5s ease-in-out",zIndex:this.settings.z_index},o=!1,s=this.settings;switch(t('[data-notify-position="'+this.settings.placement.from+"-"+this.settings.placement.align+'"]:not([data-closing="true"])').each(function(){return n=Math.max(n,parseInt(t(this).css(s.placement.from))+parseInt(t(this).outerHeight())+parseInt(s.spacing))}),1==this.settings.newest_on_top&&(n=this.settings.offset.y),i[this.settings.placement.from]=n+"px",this.settings.placement.align){case"left":case"right":i[this.settings.placement.align]=this.settings.offset.x+"px";break;case"center":i.left=0,i.right=0}this.$ele.css(i).addClass(this.settings.animate.enter),t.each(Array("webkit-","moz-","o-","ms-",""),function(t,n){e.$ele[0].style[n+"AnimationIterationCount"]=1}),t(this.settings.element).append(this.$ele),1==this.settings.newest_on_top&&(n=parseInt(n)+parseInt(this.settings.spacing)+this.$ele.outerHeight(),this.reposition(n)),t.isFunction(e.settings.onShow)&&e.settings.onShow.call(this.$ele),this.$ele.one(this.animations.start,function(t){o=!0}).one(this.animations.end,function(n){t.isFunction(e.settings.onShown)&&e.settings.onShown.call(this)}),setTimeout(function(){o||t.isFunction(e.settings.onShown)&&e.settings.onShown.call(this)},600)},bind:function(){var e=this;if(this.$ele.find('[data-notify="dismiss"]').on("click",function(){e.close()}),this.$ele.mouseover(function(e){t(this).data("data-hover","true")}).mouseout(function(e){t(this).data("data-hover","false")}),this.$ele.data("data-hover","false"),this.settings.delay>0){e.$ele.data("notify-delay",e.settings.delay);var n=setInterval(function(){var t=parseInt(e.$ele.data("notify-delay"))-e.settings.timer;if("false"===e.$ele.data("data-hover")&&"pause"==e.settings.mouse_over||"pause"!=e.settings.mouse_over){var i=(e.settings.delay-t)/e.settings.delay*100;e.$ele.data("notify-delay",t),e.$ele.find('[data-notify="progressbar"] > div').attr("aria-valuenow",i).css("width",i+"%")}t<=-e.settings.timer&&(clearInterval(n),e.close())},e.settings.timer)}},close:function(){var e=this,n=parseInt(this.$ele.css(this.settings.placement.from)),i=!1;this.$ele.data("closing","true").addClass(this.settings.animate.exit),e.reposition(n),t.isFunction(e.settings.onClose)&&e.settings.onClose.call(this.$ele),this.$ele.one(this.animations.start,function(t){i=!0}).one(this.animations.end,function(n){t(this).remove(),t.isFunction(e.settings.onClosed)&&e.settings.onClosed.call(this)}),setTimeout(function(){i||(e.$ele.remove(),e.settings.onClosed&&e.settings.onClosed(e.$ele))},600)},reposition:function(e){var n=this,i='[data-notify-position="'+this.settings.placement.from+"-"+this.settings.placement.align+'"]:not([data-closing="true"])',o=this.$ele.nextAll(i);1==this.settings.newest_on_top&&(o=this.$ele.prevAll(i)),o.each(function(){t(this).css(n.settings.placement.from,e),e=parseInt(e)+parseInt(n.settings.spacing)+t(this).outerHeight()})}}),t.notify=function(t,n){return new e(this,t,n).notify},t.notifyDefaults=function(e){return n=t.extend(!0,{},n,e)},t.notifyClose=function(e){void 0===e||"all"==e?t("[data-notify]").find('[data-notify="dismiss"]').trigger("click"):t('[data-notify-position="'+e+'"]').find('[data-notify="dismiss"]').trigger("click")}})}).call(window)},b334fd7e4c5a19234db2:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),n("a25cd36d0cf21bc7df34");var i=function(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},i=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{};$('[data-notify="container"]').remove();var o="";switch(t){case"info":o="cd-icon cd-icon-info-o color-info mrm";break;case"success":o="cd-icon cd-icon-success-o color-success mrm";break;case"danger":o="cd-icon cd-icon-danger-o color-danger mrm";break;case"warning":o="cd-icon cd-icon-warning-o color-warning mrm"}var s={message:e,icon:o},r={type:t,delay:3e3,placement:{from:"top",align:"center"},animate:{enter:"animated fadeInDownSmall",exit:"animated fadeOutUp"},offset:80,z_index:1051,timer:100,template:'<div data-notify="container" class="notify-content"><div class="notify notify-{0}"><span data-notify="icon"></span><span data-notify="title">{1}</span><span data-notify="message">{2}</span><div class="progress" data-notify="progressbar"><div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div></div><a href="{3}" target="{4}" data-notify="url"></a></div></div>'};$.notify(Object.assign(s,i),Object.assign(r,n))};e.default=i},c5e642028fa5ee5a3554:function(t,e){!function(){"use strict";function t(i){this.options=e.extend({},t.defaults,i),this.container=this.options.element,"auto"!==this.options.container&&(this.container=this.options.container),this.$container=e(this.container),this.$more=e(this.options.more),this.$more.length&&(this.setupHandler(),this.waypoint=new n(this.options))}var e=window.jQuery,n=window.Waypoint;t.prototype.setupHandler=function(){this.options.handler=e.proxy(function(){this.options.onBeforePageLoad(),this.destroy(),this.$container.addClass(this.options.loadingClass),e.get(e(this.options.more).attr("href"),e.proxy(function(t){var i=e(e.parseHTML(t)),o=i.find(this.options.more),s=i.find(this.options.items);s.length||(s=i.filter(this.options.items)),this.$container.append(s),this.$container.removeClass(this.options.loadingClass),o.length||(o=i.filter(this.options.more)),o.length?(this.$more.replaceWith(o),this.$more=o,this.waypoint=new n(this.options)):this.$more.remove(),this.options.onAfterPageLoad(s)},this))},this)},t.prototype.destroy=function(){this.waypoint&&this.waypoint.destroy()},t.defaults={container:"auto",items:".infinite-item",more:".infinite-more-link",offset:"bottom-in-view",loadingClass:"infinite-loading",onBeforePageLoad:e.noop,onAfterPageLoad:e.noop},n.Infinite=t}()},d14d05cad9e7abf02a5d:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=e.toggleIcon=function(t,e,n){var i=t.find(".js-remove-icon"),o=t.find(".js-remove-text");i.hasClass(e)?(i.removeClass(e).addClass(n),o&&o.text(Translator.trans("收起"))):(i.removeClass(n).addClass(e),o&&o.text(Translator.trans("展开")))};e.chapterAnimate=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"body",e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:".js-task-chapter",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"es-icon-remove",o=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"es-icon-anonymous-iconfont";$(t).on("click",e,function(t){var s=$(t.currentTarget);s.nextUntil(e).animate({height:"toggle",opacity:"toggle"},"normal"),i(s,n,o)})}},d5fb0e67d2d4c1ebaaed:function(t,e,n){"use strict";function i(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}Object.defineProperty(e,"__esModule",{value:!0});var o=function(){function t(t,e){for(var n=0;n<e.length;n++){var i=e[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(t,i.key,i)}}return function(e,n,i){return n&&t(e.prototype,n),i&&t(e,i),e}}(),s=n("b334fd7e4c5a19234db2"),r=function(t){return t&&t.__esModule?t:{default:t}}(s),a=function(){function t(e){i(this,t),this.$ele=e,this.initEvent()}return o(t,[{key:"initEvent",value:function(){var t=this;this.$ele.on("click",'[data-role="delte-item"]',function(e){return t._deleteItem(e)})}},{key:"_deleteItem",value:function(t){var e=$(t.currentTarget).button("loading");$.post(e.data("url"),{},function(t){"ok"==t.msg&&((0,r.default)("success",Translator.trans("site.delete_success_hint")),e.closest(".js-attachment-list").siblings(".js-upload-file").show(),e.closest(".js-attachment-list").closest("div").siblings('[data-role="fileId"]').val(""),e.closest("div").remove(),$(".js-upload-file").show())}).error(function(t){(0,r.default)("danger",Translator.trans("file.not_found"))})}}]),t}();e.default=a},e66ca5da7109f35e9051:function(t,e,n){"use strict";function i(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function o(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function s(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}Object.defineProperty(e,"__esModule",{value:!0});var r=function(){function t(t,e){for(var n=0;n<e.length;n++){var i=e[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(t,i.key,i)}}return function(e,n,i){return n&&t(e.prototype,n),i&&t(e,i),e}}();n("8f3ec98312b1f1f6bafb"),n("c5e642028fa5ee5a3554");var a=n("63fff8fb24f3bd1f61cd"),l=function(t){return t&&t.__esModule?t:{default:t}}(a),c=function(t){function e(t){i(this,e);var n=o(this,(e.__proto__||Object.getPrototypeOf(e)).call(this));return n.options=t,n.initDownInfinite(),n.initUpLoading(),n}return s(e,t),r(e,[{key:"initUpLoading",value:function(){$(".js-up-more-link").on("click",function(t){var e=$(t.currentTarget);$.ajax({method:"GET",url:e.data("url"),async:!1,success:function(t){$(t).find(".infinite-item").prependTo($(".infinite-container"));var n=$(t).find(".js-up-more-link");n.length>0?e.data("url",n.data("url")):e.remove()}})})}},{key:"initDownInfinite",value:function(){var t={element:$(".infinite-container")[0]};t=Object.assign(t,this.options),this.downInfinite=new Waypoint.Infinite(t)}}]),e}(l.default);e.default=c}});