$('.rating').rating({
    initialRating: 0,
    maxRating: 5,
    onRate: function (value) {
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


$('button.read-status').on('click', function () {
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
                if (msg.read) {
                    setTimeout(function () {
                        elm.removeClass("loading");
                        elm.prepend('<i class="Checkmark icon"></i>');
                        elm.siblings('button.wish-status').find('i.Checkmark').remove();
                        setTimeout(function () {
                            //window.location.href = "/bookdetails/"+elm.data('id');
                        }, 1000);
                    }, 1000);
                }
                else {
                    setTimeout(function () {
                        elm.removeClass("loading");
                        elm.find('i.Checkmark').remove();
                    }, 1000);
                }
            }
        })
        .fail(function (error) {
            if (error) {
                console.log(error);
            }

        })
});


$('button.wish-status').on('click', function () {
    elm = $(this);
    $(this).addClass("loading");
    $.ajax({
        url: "bookdetails/wish",
        data: {
            status: 3,
            book: $(this).data('id')
        },
        method: 'GET'
    })
        .done(function (msg) {
            if (msg) {
                if (msg.read) {
                    setTimeout(function () {
                        elm.removeClass("loading");
                        elm.prepend('<i class="Checkmark icon"></i>');
                        elm.siblings('button.read-status').find('i.Checkmark').remove();
                        setTimeout(function () {
                            //window.location.href = "/bookdetails/"+elm.data('id');
                        }, 1000);
                    }, 1000);
                }
                else {
                    setTimeout(function () {
                        elm.removeClass("loading");
                        elm.find('i.Checkmark').remove();
                    }, 1000);
                }
            }
        })
        .fail(function (error) {
            if (error) {
                console.log(error);
            }

        })
});


$('div.button.author-follow').click(function () {
    elm = $(this);
    $(this).addClass("loading");
    $.ajax({
        url: "authordetails/follow",
        data: {
            status: 1,
            author: $(this).data('id')
        },
        method: 'GET'
    })
        .done(function (msg) {
            if (msg) {
                if (msg.follow) {
                    setTimeout(function () {
                        elm.removeClass("loading");
                        elm.children('i.add').removeClass("add").addClass("remove");
                        elm.children('span').text("Un Follow")

                    }, 1000);
                }
                else {
                    setTimeout(function () {
                        elm.removeClass("loading");
                        elm.children('i.remove').removeClass("remove").addClass("add");
                        elm.children('span').text("Follow")
                    }, 1000);
                }
            }
        })
        .fail(function (error) {
            if (error) {
                console.log(error);
            }

        })
});
// $('.rating').rating('disable');

