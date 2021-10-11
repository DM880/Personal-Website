$(document).on('click', '#links', function(e){
    e.preventDefault();
    var url = $(this).attr('href');
    window.open(url, '_blank');
});