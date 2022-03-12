

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




$(function() {
  var b = $("#button");
  var w = $("#wrapper");
  b.click(function() {
    w.toggleClass('open'); /* <-- toggle the application of the open class on click */
    window.alert("The next step cannot be undone.");
  });

});