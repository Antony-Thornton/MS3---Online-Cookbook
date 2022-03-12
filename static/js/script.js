

/** jSON for nav bar */
  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });



/* Javascript for collapsible section in profile html page - https://materializecss.com/collapsible.html*/
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(elems, options);
});

// Or with jQuery

$(document).ready(function(){
  $('.collapsible').collapsible();
});




$('.button_delete').click(function(){
  $('.wrapper_delete').toggle();
});  



$('.button_edit').click(function(){
  $('.wrapper_edit').toggle();
});  