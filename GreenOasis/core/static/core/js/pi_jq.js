$(document).ready(function () {
    /* Validaciones del formulario 1 */
    $("#pi-form").submit(function (e) {
        var rut = $("#pi-rut").val();
        var nombre = $("#pi-nombre").val();
        var apellido = $("#pi-apellido").val();
        var telefono = $("#pi-telefono").val();

        var msj = "";
        let enviar = false;

        // Validar el RUT utilizando la función validarRut
        if (validarRut(rut)) {
            $("#pi-rut").removeClass('is-invalid').addClass('is-valid');
        } else {
            if (!validarRut(rut)) {
                msj += "El RUT ingresado es inválido<br>";
                $("#pi-rut").removeClass('is-valid').addClass('is-invalid');
            }
            enviar = true;
        }

        /* Validar Nombre */
        if (nombre.trim().length < 3 || nombre.trim().length > 12) {
            msj += "El nombre debe ser entre 3 y 12 carácteres<br>";
            $("#pi-nombre").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-nombre").removeClass('is-invalid').addClass('is-valid');
        }

        if (!validarNombre(nombre)) {
            msj += "El nombre no debe contener números<br>";
            $("#pi-nombre").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-nombre").removeClass('is-invalid').addClass('is-valid');
        }

        var letra = nombre.charAt(0);
        if (!esMayuscula(letra)) {
            msj += "La primera letra del nombre debe ser mayúscula<br>";
            $("#pi-nombre").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }

        /* Validar Apellido */
        if (apellido.trim().length < 3 || apellido.trim().length > 12) {
            msj += "El apellido debe ser entre 3 y 12 carácteres<br>";
            $("#pi-apellido").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-apellido").removeClass('is-invalid').addClass('is-valid');
        }

        if (!validarNombre(apellido)) {
            msj += "El apellido no debe contener números<br>";
            $("#pi-apellido").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-apellido").removeClass('is-invalid').addClass('is-valid');
        }

        var letra = apellido.charAt(0);
        if (!esMayuscula(letra)) {
            msj += "La primera letra del apellido debe ser mayúscula<br>";
            $("#pi-apellido").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }

        /* Validar Telefono */
        if (telefono.replace(/\s+/g, '').length != 12) {
            msj += "El teléfono ingresado posee un largo incorrecto<br>";
            $("#pi-telefono").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-telefono").removeClass('is-invalid').addClass('is-valid');
        }

        if (/^[0-9+ ]+$/.test(telefono) == false) {
            msj += "El teléfono solo debe contener números, espacios y el signo +<br>";
            $("#pi-telefono").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }

        /* Enviar Form */
        if (enviar) {
            $("#pi-w").html(msj);
            e.preventDefault();

        }
        else {
            $("#pi-w").html("Guardado");
        }
    });

    /* Validaciones del formulario 2 */
    $("#pi-form2").submit(function (a) {
        var calle = $("#pi-calle").val();
        var nro = $("#pi-numero").val();
        var region = $("#pi-regiones").val();
        var comunas = $("#pi-comunas").val();
        var codp = $("#pi-codigo-postal").val();

        var msj = "";
        let enviar = false;

        /* Validar Calle */
        if (calle.trim().length < 5 || calle.trim().length > 25) {
            msj += "El nombre de la calle debe al menos contener 5 carácteres<br>";
            $("#pi-calle").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-calle").removeClass('is-invalid').addClass('is-valid');
        }

        var letra = calle.charAt(0);
        if (!esMayuscula(letra)) {
            msj += "La primera letra de la calle debe ser mayúscula<br>";
            $("#pi-calle").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-calle").removeClass('is-invalid').addClass('is-valid');
        }

        /* Validar Nro */
        if (nro.trim().length < 1 || nro.trim().length > 4) {
            msj += "El número de domicilio debe estar entre 1 y 4 números<br>";
            $("#pi-numero").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-numero").removeClass('is-invalid').addClass('is-valid');
        }

        if ($.isNumeric(nro) == false) {
            msj += "El número de casa solo debe contener números<br>";
            $("#pi-numero").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-numero").removeClass('is-invalid').addClass('is-valid');
        }

        /* Validar Codigo Postal */
        if (codp.trim().length != 7) {
            msj += "El código postal ingresado posee un largo incorrecto<br>";
            $("#pi-codigo-postal").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-codigo-postal").removeClass('is-invalid').addClass('is-valid');
        }

        if ($.isNumeric(codp) == false) {
            msj += "El código postal solo debe contener números<br>";
            $("#pi-codigo-postal").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-codigo-postal").removeClass('is-invalid').addClass('is-valid');
        }

        /* Validar Region y Comuna */
        if (region === 'sin-region') {
            msj += "Debe seleccionar una región<br>";
            $("#pi-regiones").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-regiones").removeClass('is-invalid').addClass('is-valid');
        }

        if (comunas === 'sin-comuna') {
            msj += "Debe seleccionar una comuna<br>";
            $("#pi-comunas").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pi-comunas").removeClass('is-invalid').addClass('is-valid');
        }

        /* Enviar Form */
        if (enviar) {
            $("#pi-w2").html(msj);
            a.preventDefault();

        }
        else {
            $("#pi-w2").html("Guardado");
        }
    });

    /* Funcion de formato del rut */
    $('#pi-rut').focusout(function () {
        var div1, div2, div3, div4;
        rut = $(this).val();

        rut = rut.replace(/[.-]/g, '');

        if (!/^[0-9.-]+$/.test(rut)) {
            $(this).removeClass('is-valid').addClass('is-invalid');
            return;
        }

        if (rut.length == 9) {
            div1 = rut.slice(0, 2);
            div2 = rut.slice(2, 5);
            div3 = rut.slice(5, 8);
            div4 = rut.slice(8, 9);
            rut = $(this).val(div1 + "." + div2 + "." + div3 + "-" + div4);
        }

        if (rut.length == 8) {
            div1 = rut.slice(0, 1);
            div2 = rut.slice(1, 4);
            div3 = rut.slice(4, 7);
            div4 = rut.slice(7, 8);
            rut = $(this).val(div1 + "." + div2 + "." + div3 + "-" + div4);
        }
        if (validarRut(rut)) { // llamar a la función validarRut solo si la variable rut tiene un valor válido
            $(this).removeClass('is-invalid').addClass('is-valid');
        } else {
            $(this).removeClass('is-valid').addClass('is-invalid');
        }
    });

    /* Funcion de formato del telefono */
    $('#pi-telefono').focusout(function () {
        var div1, div2, div3;
        telefono = $(this).val();

        if (!/^[0-9+ ]+$/.test(telefono)) {
            return;
        }

        if (telefono.length == 8) {
            div1 = telefono.slice(0, 8);
            telefono = $(this).val("+56 9 " + div1);
        }
        if (telefono.length == 9) {
            div1 = telefono.slice(0, 1);
            div2 = telefono.slice(1, 9);
            telefono = $(this).val("+56 " + div1 + " " + div2);
        }
        if (telefono.length == 12) {
            div1 = telefono.slice(0, 3);
            div2 = telefono.slice(3, 4);
            div3 = telefono.slice(4, 12);
            telefono = $(this).val(div1 + " " + div2 + " " + div3);
        }
    });

    /* Funcion de Validacion de Mayuscula */
    function esMayuscula(letra) {
        console.log(letra);
        console.log(letra.toUpperCase());
        if (letra == letra.toUpperCase()) {
            return true;
        }
        else {
            return false;
        }

    }

    /* Funcion Validar Rut */
    function validarRut(rut) {
        // Eliminar puntos y guiones del RUT
        rut = rut.replace(/[.-]/g, '');

        // Validar que el RUT tenga un formato válido
        if (!/^[0-9]+[-]{0,1}[0-9kK]{1}$/.test(rut)) {
            return false;
        }

        // Separar el RUT y el dígito verificador
        if (rut.length == 9) {
            var rutSinDV = rut.slice(0, 8);
            var dv = rut.slice(8, 9);
        }

        if (rut.length == 8) {
            var rutSinDV = rut.slice(0, 7);
            var dv = rut.slice(7, 8);
        }

        if (rut.length != 9 && rut.length != 8) {
            return false;
        }

        // Calcular el dígito verificador del RUT
        var suma = 0;
        var factor = 2;
        for (var i = rutSinDV.length - 1; i >= 0; i--) {
            suma += factor * rutSinDV.charAt(i);
            factor = factor == 7 ? 2 : factor + 1;
        }
        var dvCalculado = 11 - (suma % 11);
        if (dvCalculado == 11) {
            dvCalculado = '0';
        } else if (dvCalculado == 10) {
            dvCalculado = 'K';
        }

        // Comparar el dígito verificador calculado con el dígito verificador del RUT
        return dv == dvCalculado;
    }

    /* Funcion Validar Nombre */
    function validarNombre(nombre) {
        var regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/; // expresión regular que permite solo letras, espacios y tildes
        if (!regex.test(nombre)) {
            return false; // si el nombre contiene algún número u otro carácter no permitido, la validación falla
        }
        return true; // si el nombre es válido, la validación es exitosa
    }

    /* Web Service para obtener los datos de las regiones y comunas */
    /*$.getJSON("https://gist.githubusercontent.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd/raw/b8575eb82dce974fd2647f46819a7568278396bd/comunas-regiones.json", function (data) {*/
    $.getJSON("https://raw.githubusercontent.com/Alexandio/Practica_003D/main/comunas-regiones.php", function (data) {
        console.log(data)
        /* Script para los Select de comuna y region */
        var iRegion = 0;
        var htmlRegion = '<option value="sin-region">Seleccione región</option><option value="sin-region">--</option>';
        var htmlComunas = '<option value="sin-comuna">Seleccione comuna</option><option value="sin-comuna">--</option>';

        jQuery.each(data.regiones, function () {
            htmlRegion = htmlRegion + '<option value="' + data.regiones[iRegion].region + '">' + data.regiones[iRegion].region + '</option>';
            iRegion++;
        });

        jQuery('#pi-regiones').html(htmlRegion);
        jQuery('#pi-comunas').html(htmlComunas);

        jQuery('#pi-regiones').change(function () {
            var iRegiones = 0;
            var valorRegion = jQuery(this).val();
            var htmlComuna = '<option value="sin-comuna">Seleccione comuna</option><option value="sin-comuna">--</option>';
            jQuery.each(data.regiones, function () {
                if (data.regiones[iRegiones].region == valorRegion) {
                    var iComunas = 0;
                    jQuery.each(data.regiones[iRegiones].comunas, function () {
                        htmlComuna = htmlComuna + '<option value="' + data.regiones[iRegiones].comunas[iComunas] + '">' + data.regiones[iRegiones].comunas[iComunas] + '</option>';
                        iComunas++;
                    });
                }
                iRegiones++;
            });
            jQuery('#pi-comunas').html(htmlComuna);
        });
        jQuery('#pi-comunas').change(function () {
            if (jQuery(this).val() == 'sin-region') {
                alert('seleccione Región');
            } else if (jQuery(this).val() == 'sin-comuna') {
                alert('seleccione Comuna');
            }
        });
        jQuery('#pi-regiones').change(function () {
            if (jQuery(this).val() == 'sin-region') {
                alert('seleccione Región');
            }
        });
    });
});
