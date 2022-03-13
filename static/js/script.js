

/** jSON for nav bar */
  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });
/* End */


/* Javascript for collapsible section in profile html page - https://materializecss.com/collapsible.html */
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(elems, options);
});

$(document).ready(function(){
  $('.collapsible').collapsible();
});
      
/* End */

/* Toggle buttons for managing recipes */
/* https://stackoverflow.com/questions/30523370/javascript-expand-collapse-button */
/* Delete */
$('.button_delete').click(function(){
  $('.wrapper_delete').toggle();
});  
/* edit */
$('.button_edit').click(function(){
  $('.wrapper_edit').toggle();
});  
/* End toggle buttons */

const editForms = document.querySelectorAll('.edit-btn');
editForms.forEach(input => input.addEventListener('click', event => {
  const form = event.target.parentNode;
  form.submit();
}))