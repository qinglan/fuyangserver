$(function () {
    //用户中心标记当前菜单项
    var curl = location.pathname;
    $('#usermenus li').each(function (idx, ele) {
        var linkurl = $(ele).find('a').attr('href');
        if (linkurl == curl) {
            $(ele).siblings().removeClass('active');
            $(ele).addClass('active');
        }
    });
})