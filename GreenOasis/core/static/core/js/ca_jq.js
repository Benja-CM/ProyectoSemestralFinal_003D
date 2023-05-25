$(document).ready(function() {
    /* Validación de formulario */
    $("#pp-form").submit(function(e) {
        
    
        var alias       = $("#ca-nombre").val();
        var email       = $("#ca-email").val();
        var clave       = $("#ca-clave").val();
        var confClave   = $("#ca-confClave").val();

        var msj = "";
        let enviar = false;

        if (!ValidarAlias(alias)) {
            msj += "Existen caracteres no válidos en el Alias<br>";
            enviar = true;
        }
        if (alias.trim().length < 4 || alias.trim().length > 20) {
            msj += "El Alias debe tener entre 4 y 20 caracteres<br>";
            enviar = true;
        }
        //validacion de email
        if (!ValidarEmail(email)) {
            msj += "Ingrese un correo electrónico válido<br>";
            enviar = true;
        }

        //validacion de clave
        if (!ValidarClave(clave)) {
            msj += "Existen caracteres no válidos en la Contraseña<br>";
            enviar = true;
        }

        if (clave.trim().length < 8 || clave.trim().length > 20) {
            msj += "La contraseña debe tener entre 8 y 20 caracteres<br>";
            enviar = true;
        }

        // Validación de Minusculas clave
        var lowerCaseRegex = /[a-z]/;
        if (!lowerCaseRegex.test(clave)) {
            msj += "La contraseña debe contener por lo menos una letra Minuscula<br>";
            enviar = true;
        }
        // Validación de mayúsculas clave

        var upperCaseRegex = /[A-Z]/;
        if (!upperCaseRegex.test(clave)) {
            msj += "La contraseña debe contener por lo menos una letra Mayuscula<br>";
            enviar = true;
        }
        // Validación de caracteres especiales
        var specialRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;//Consulta que la contraseña tenga caracteres especiales
        if (!specialRegex.test(clave)) {
            msj += "La contraseña debe contener por lo menos un caracter especial<br>";
            enviar = true;
        }

        // Validar coincidencia entre ambas claves
        if (clave != confClave){
            msj += "Las contraseñas no coinciden<br>";
            enviar = true;
        }

        // Enviar \\
        if (enviar) {
            $("#ca-w").html(msj);
            e.preventDefault();
        }
        else {
            $("#ca-w").html("Guardado");
            
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
    function ValidarClave(password) {
        var regex = /^[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+$/;
        if (!regex.test(password)) {
            return false;
        }
        return true;
    }
});