$(document).ready(function () {
    $("#pf-form").submit(function (e) {
        var c_nueva = $("#clave_nueva").val();
        var c_nueva_conf = $("#clave_nueva_conf").val();
        
        var msj = "";
        let enviar = false;
        let pws = false;

        //validacion de password
        if (!ValidarPassword(c_nueva)) {
            msj += "Existen caracteres no válidos en la nueva contraseña<br>";
            enviar = true;
            pws = true;

        } 
        if (c_nueva.trim().length < 8 || c_nueva.trim().length > 20) {
            msj += "La nueva contraseña debe tener entre 8 y 20 caracteres<br>";
            enviar = true;
            pws = true;

        }
        // Validación de Minusculas poassword
        var lowerCaseRegex = /[a-z]/;
        if (!lowerCaseRegex.test(c_nueva)) {
            msj += "La nueva contraseña debe contener por lo menos una letra Minuscula<br>";
            enviar = true;
            pws = true;

        }
        // Validación de mayúsculas poassword

        var upperCaseRegex = /[A-Z]/;
        if (!upperCaseRegex.test(c_nueva)) {
            msj += "La nueva contraseña debe contener por lo menos una letra Mayuscula<br>";
            enviar = true;
            pws = true;

        }
        // Validacion de numeros 
        var regex = /[0-9]/;
        if (!regex.test(c_nueva)) {
            msj += "La nueva contraseña debe tener Por lo menos un numero <br>";
            enviar = true;
            pws = true;

        }

        if (c_nueva != c_nueva_conf){
            $("#clave_nueva_conf").removeClass('is-valid').addClass('is-invalid');
            msj += "La nueva contraseña no coincide con la confirmación de contraseña <br>";
            enviar = true;
        } else {
            $("#clave_nueva_conf").removeClass('is-invalid').addClass('is-valid');
            enviar = false;
        }

        // Validación de caracteres especiales
        var specialRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;//Consulta que la contraseña tenga caracteres especiales
        if (!specialRegex.test(c_nueva)) {
            msj += "La nueva contraseña debe contener por lo menos un caracter especial<br>";
            enviar = true;
            pws = true;
        }

        // Muestra que la calve nueva no es valida
        if (pws){
            $("#clave_nueva").removeClass('is-valid').addClass('is-invalid');  
            $("#clave_nueva_conf").removeClass('is-valid').addClass('is-invalid');
        } else {
            $("#clave_nueva").removeClass('is-invalid').addClass('is-valid');
        }
        

        if (enviar) {
            $("#pf-w").html(msj);
            e.preventDefault();
        }
    });

    //validacion de password
    function ValidarPassword(c_nueva) {
        var regex = /^[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+$/;
        if (!regex.test(c_nueva)) {
            return false;
        }
        return true;
    }

});