$(document).ready(function () {
    $("#ai-form").submit(function (e) {
        e.preventDefault();

        var alias = $("#ai-alias").val();
        var email = $("#ai-email").val();
        var password = $("#ai-password").val();

        var msj = "";
        let enviar = false;
        let pws = false;

        //validacion de Alias
        if (!ValidarAlias(alias)) {
            msj += "Existen caracteres no válidos en el Alias<br>";
            $("#ai-alias").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        if (alias.trim().length < 4 || alias.trim().length > 20) {
            msj += "El Alias debe tener entre 4 y 20 caracteres<br>";
            $("#ai-alias").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#ai-alias").removeClass('is-invalid').addClass('is-valid');
        }
        //validacion de email
        if (!ValidarEmail(email)) {
            msj += "Ingrese un correo electrónico válido<br>";
            $("#ai-email").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#ai-email").removeClass('is-invalid').addClass('is-valid');
        }

        //validacion de password
        
        if (!ValidarPassword(password)) {
            msj += "Existen caracteres no válidos en la Contraseña<br>";
            $("#ai-password").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
            pws = true;

        } 
        if (password.trim().length < 8 || password.trim().length > 20) {
            msj += "La contraseña debe tener entre 8 y 20 caracteres<br>";
            $("#ai-password").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
            pws = true;

        }
        // Validación de Minusculas poassword
        var lowerCaseRegex = /[a-z]/;
        if (!lowerCaseRegex.test(password)) {
            msj += "La contraseña debe contener por lo menos una letra Minuscula<br>";
            $("#ai-password").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
            pws = true;

        }
        // Validación de mayúsculas poassword

        var upperCaseRegex = /[A-Z]/;
        if (!upperCaseRegex.test(password)) {
            msj += "La contraseña debe contener por lo menos una letra Mayuscula<br>";
            $("#ai-password").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
            pws = true;

        }
        // Validacion de numeros 
        var regex = /[0-9]/;
        if (!regex.test(password)) {
            msj += "La contraseña debe tener Por lo menos un numero <br>";
            $("#ai-password").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
            pws = true;

        }

        // Validación de caracteres especiales
        var specialRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;//Consulta que la contraseña tenga caracteres especiales
        if (!specialRegex.test(password)) {
            msj += "La contraseña debe contener por lo menos un caracter especial<br>";
            $("#ai-password").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
            pws = true;
        }
        if (pws == false){
            
                $("#ai-password").removeClass('is-invalid').addClass('is-valid');  
        }



        if (enviar) {
            $("#ai-w").html(msj);
        } else {
            $("#ai-w").html("Guardado");
        }
    });

    //validacion de alias
    function ValidarAlias(alias) {
        var regex = /^[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+$/; //Permite entrada de caracteres Especiales pero no Espacios
        if (!regex.test(alias)) {
            return false;
        }
        return true;
    }
    //validacion de Email
    function ValidarEmail(email) {
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    //validacion de password
    function ValidarPassword(password) {
        var regex = /^[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+$/;
        if (!regex.test(password)) {
            return false;
        }
        return true;
    }
});