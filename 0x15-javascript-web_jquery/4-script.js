// Script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header.
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
});
