/////////////////////////
//JavaScript for Posts page
////////////////////////
$(function(){
    // EXecuted when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        $(this).next().toggle();
    })
})