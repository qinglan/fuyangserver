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

//报名区在线支付校验
function checkpay(vid, price, paytype) {
    //如果价格为0或支付方式为免费则直接添加到订单表
    if (price == 0 || paytype == 0) {
        $.get("/buyvideocurriculum/", {'pk': vid}, function (ret) {
            if (ret == "1")
                location.reload();
            else
                alert('保存支付记录失败')
        })
    } else {
        location.href = '/picture/text/signpay/' + vid;
    }
}

//验证支付密码表单
function checkpayfrm(form) {
    var op = form.currentPayCode;
    if (op != undefined) {
        var oc = $('#origcode').val();  //原支付密码
        if (op.value !== oc) {
            //op.setCustomValidity('原支付密码输入不正确');
            alert('原支付密码输入不正确');
            return false;
        }
    }

    var p1 = form.newPayPassword;
    var p2 = form.confirmPayPassword;
    if (p1.value.length < 6 || p2.value.length < 6) {
        alert('密码长度最小6位');
        return false;
    }
    if (p1.value != p2.value) {
        //p2.setCustomValidity('两次输入的密码不匹配');
        alert('两次输入的密码不匹配');
        return false;
    }
    return true;
}