$(function() {
    var $textarea = $('#textarea');
    var lineHeight = parseInt($textarea.css('lineHeight'));
    $textarea.on('input', function(e) {
      var lines = ($(this).val() + '\n').match(/\n/g).length;
      $(this).height(lineHeight * lines);
    });
  });