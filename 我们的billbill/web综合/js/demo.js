$(function () {    
    var index = 1,
        $li = $('li'),
        $span = $('span'),
        $h2 = $('h2'),
        $h3 = $('h3'),
        timer;

    $('.content').click(function () { 
        // 可以根据index来识别当前点击的索引
        // window.location.href = "http://www.baidu.com";   
        if(index == 1) {
            window.open("https://www.bilibili.com/video/BV1a64y1t766?spm_id_from=333.851.b_7265636f6d6d656e64.5");
        }else if(index == 2) {
            window.open("https://www.bilibili.com/video/BV19y4y1K7S1?spm_id_from=333.851.b_7265636f6d6d656e64.3");
        }else if(index == 3) {
            window.open("https://www.bilibili.com/video/BV1D44y1B77t?spm_id_from=333.851.b_7265636f6d6d656e64.4");
        }else if(index == 4) {
            window.open("https://www.bilibili.com/bangumi/play/ep411182?spm_id_from=333.851.b_7265706f7274466972737432.6");
        }else if(index == 5) {
            window.open("https://www.bilibili.com/video/BV1Lf4y1b7Jg?spm_id_from=333.851.b_7265636f6d6d656e64.2");
        }else if(index == 6) {
            window.open("https://www.bilibili.com/video/BV15f4y187kX?spm_id_from=333.851.b_62696c695f7265706f72745f67756f636875616e67.63");
        }else if(index == 7) {
            window.open("https://www.bilibili.com/video/BV1mg411T74T?spm_id_from=333.851.b_62696c695f7265706f72745f67756f636875616e67.66");
        }
     })

    function time() {
        index = (index + 1) % 7;
        if(index === 0) {
            index = 7;
        }

        var bacStr = "url(./images/" + index +".jpg) no-repeat 0 0";
        $('.content').css("background",bacStr).css("background-size","100%");
        
        var str = $li.eq(index - 1).find('h2').text();
        $li.eq(index - 1).parents(".content").attr("title", str);

        $li.eq(index - 1).addClass("check");
        $li.eq(index - 1).siblings().removeClass("check");

        $span.eq(index - 1).addClass("icon");
        $span.eq(index - 1).parents("li").siblings().find("span").removeClass("icon");

        $h2.eq(index - 1).addClass("font-bold");
        $h2.eq(index - 1).parents("li").siblings().find("h2").removeClass("font-bold");

        $h3.eq(index - 1).removeClass("show");
        $h3.eq(index - 1).parents("li").siblings().find("h3").addClass("show");
    }

    timer = setInterval(time,5000);

    $li.hover(function () {
        clearInterval(timer);
        index = $(this).attr("indexs") - 1;
        time();
    },function () {
        timer = setInterval(time,5000);
    });
});