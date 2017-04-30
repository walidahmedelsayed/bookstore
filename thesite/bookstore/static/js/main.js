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


// $('.rating').rating('disable');

