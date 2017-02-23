(function ($, window, document, undefined) {

  'use strict';

  $(function () {
    var isTouchDevice = navigator.userAgent.match(/(iPhone|iPod|iPad|Android|playbook|silk|BlackBerry|BB10|Windows Phone|Tizen|Bada|webOS|IEMobile|Opera Mini)/);

    $('html').addClass(isTouchDevice ? 'touchable' : 'non-touchable');

    var $input = $('.input'),
      inputFieldEmptyClass = '',
      inputFieldDirtyClass = '',
      inputFieldErrorClass = '',
      errors = {},
      errorCallbacks = {};


    inputFieldEmptyClass = 'input--empty';
    inputFieldDirtyClass = 'input--dirty';
    inputFieldErrorClass = 'input-field--error';


    errors = {
      usernameEmpty: 'Please enter a username',
      passwordEmpty: 'Please enter a password',
      nameEmpty: 'Please enter a name',
      authorEmpty: 'Please enter an author'
    };


    $input.removeAttr('disabled');


    function checkInputEmptyField($field) {
      if (!$field.val().length) {
        $field.addClass(inputFieldEmptyClass);
        $field.removeClass(inputFieldDirtyClass);
      } else {
        $field.removeClass(inputFieldEmptyClass);
        $field.addClass(inputFieldDirtyClass);
      }
    }


    function updateInputLabel(currentInput, inputDataValid, errorLabel) {
      if (inputDataValid === 'valid') {
        currentInput.removeClass(inputFieldErrorClass);
        currentInput.addClass(inputFieldDirtyClass);

        errorLabel.css('display', 'none');
      } else {
        if (!currentInput.hasClass(inputFieldErrorClass)) {
          currentInput.addClass(inputFieldErrorClass);
        }

        currentInput.removeClass(inputFieldDirtyClass);

        errorLabel.css('display', 'block');
      }
    }


    function handleInputsErrors($input) {
      var $errorLabel = $input.parent().find('.input--error'),
        value = $.trim($input.val()),
        name = $input.attr('data-validation-name');

      if (value) {
        $input.attr('data-valid', 'valid');
      } else {
        $input.attr('data-valid', 'invalid');
        $errorLabel.text(errors[name + 'Empty']);
      }

      updateInputLabel($input, $input.attr('data-valid'), $errorLabel);
    }


    function setInputAnimationEvents() {
      $input
        .on('focus', function () {
          // $(this).addClass(inputFieldDirtyClass);
        })
        .on('paste', function () {
          var $this = $(this);

          setTimeout(function () {
            checkInputEmptyField($this);
            handleInputsErrors($this);
          }, 1);
        })
        .on('change blur', function () {
          checkInputEmptyField($(this));
          handleInputsErrors($(this));
        })
        .each(function () {
          var $this = $(this);

          setTimeout(function () {
            checkInputEmptyField($this);
          }, 0);
        });

      $(window).on('beforeunload', function () {
        $input.blur();
        $input.attr('disabled', 'disabled');
      });
    }

    setInputAnimationEvents();
  });

})(jQuery, window, document);
