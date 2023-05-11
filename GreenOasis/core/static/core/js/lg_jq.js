$(document).ready(function () {

    $('#Email_imp').focusout(function(event) {
        var email = $(this).val();
        var regex = /\S+@\S+\.\S+/;
        if (!regex.test(email)) {
            alert('Por favor, ingrese un correo electrónico válido.');
            event.preventDefault();
        }
    });

    $('#Password_imp').focusout(function(event) {
        var password = $(this).val();
        var regex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$&*.\-_])(?=.*[0-9]).{8,20}$/;
        if (!regex.test(password)) {
            alert('La contraseña debe tener mínimo 8 caracteres, máximo 20 caracteres, contener al menos 1 letra mayúscula, 1 minúscula, 1 número y 1 carácter especial<br>');
            event.preventDefault();
        }
    });
    

    function verificarValidaciones() {
        var emailValido = false;
        var passwordValido = false;

        var email = $('#Email_imp').val();
        var regexEmail = /\S+@\S+\.\S+/;
        if (regexEmail.test(email)) {
            emailValido = true;
        }

        var password = $('#Password_imp').val();
        var regexPassword = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$&*.\-_])(?=.*[0-9]).{8,20}$/;
        if (regexPassword.test(password)) {
            passwordValido = true;
        }

        if (emailValido && passwordValido) {
            $('#Ingresar_imp').prop('disabled', false);
        } else {
            $('#Ingresar_imp').prop('disabled', true);
        }
    }

    $('#Email_imp').focusout(function () {
        verificarValidaciones();
    });

    $('#Password_imp').focusout(function () {
        verificarValidaciones();
    });

});