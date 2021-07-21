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
        window.open("http://www.baidu.com");
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