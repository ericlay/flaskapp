$(function() {
    $('button').click(function() {
        var checkBox = $('.handleAdd').is(':checked');
            var handle = $('#handle').val();

            $.ajax({
                    url: '/tweet',
                    data: $('form').serialize(),
                    type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
                    }
        });
    });
});
