// Script that fetches and prints how to say “Hello” depending of the language.
const base = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    const url = base + lang;
    if (lang !== '') {
      $.get(url, function (data) {
        if (data.code !== 'none') {
          $('DIV#hello').text(data.hello);
        } else {
          $('DIV#hello').text('');
        }
      });
    }
  });
});
