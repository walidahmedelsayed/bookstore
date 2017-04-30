$('.rating').rating({
    initialRating: 0,
    maxRating: 5,
    onRate:function (value) {
        $.ajax({
        url: "bookdetails/rate",
         data: {
            rating: value,
            book: $(this).data('id')
         },
        type: 'get',
        success: function (data) {
          if (data) {
          }
        }
      });
    }
});


$('button.book-status').on('click', function() {
    elm = $(this);
    $(this).addClass("loading");
    $.ajax({
        url: "bookdetails/read",
        data: {
            status: 2,
            book: $(this).data('id')
        },
        method: 'GET'
    })
        .done(function (msg) {
            if (msg) {
                if(msg.read)
                {
                    setTimeout(function(){
                        elm.removeClass("loading");
                        elm.append('<i class="Checkmark icon"></i>');
                        setTimeout(function(){
                            //window.location.href = "/bookdetails/"+elm.data('id');
                        }, 1000);
                    }, 1000);
                }
                else {
                    setTimeout(function(){
                        elm.removeClass("loading");
                        elm.find('i.Checkmark').remove();
                    }, 1000);
                }
            }
        })
        .fail(function (error) {
            if (error){
                console.log(error);
            }

        })
});

$(function () {
    $("#follow_btn").click(function () {
        $.ajax({
            type: "get",
            url: "authordetails/follow",
            data: { 'author_id': $(this).data('id'),
                    'followstatus' :$(this).data('followstatus') },
            success: function (e) {
                alert('Success!');
            }
        });
    });
});
// $('.rating').rating('disable');

