$(document).ready(function () {

    $('#po-email').focusout(function(event) {
        var email = $(this).val();
        var regex = /\S+@\S+\.\S+/;
        if (!regex.test(email)) {
            alert('Por favor, ingrese un correo electrónico válido.');
            event.preventDefault();
        }
    });
    function verificarValidaciones() {
        var emailValido = false;
       
        var email = $('#po-email').val();
        var regexEmail = /\S+@\S+\.\S+/;
        if (regexEmail.test(email)) {
            emailValido = true;
        }
        if (emailValido) {
            $('#po-btn').prop('disabled', false);
        } else {
            $('#po-bt').prop('disabled', true);
        }
    }

    $('#po-email').focusout(function () {
        verificarValidaciones();
    });

})

    