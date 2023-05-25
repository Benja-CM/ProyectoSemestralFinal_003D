$(document).ready(function () {
    /* Validación de formulario */
    $("#pp-form").submit(function (e) {

        var nro_tarjeta = $("#pp-nroTarjeta").val();
        var fch_vencMes = $("#pp-fecVencMes").val();
        var fch_vencAnio = $("#pp-fecVencAnio").val();
        var cod_seguridad = $("#pp-codigo").val();

        var msj = "";
        let enviar = false;

        // Validar cantidad de digitos en el número de tarjeta
        nro_tarjeta = nro_tarjeta.replaceAll(" ", ""); // eliminar espacios en blanco
        if (nro_tarjeta.length != 16) {
            msj += "La tarjeta debe tener 16 digitos<br>";
            $("#pp-nroTarjeta").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pp-nroTarjeta").removeClass('is-invalid').addClass('is-valid');
        }

        // Validar que solo hayan números y espacios en la tarjeta (Espacios dobles no cuentan)
        if (!/^(\d+\s?)+$/.test(nro_tarjeta)) {
            msj += "La tarjeta debe contener solo números y espacios<br>";
            $("#pp-nroTarjeta").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }
        else {
            $("#pp-nroTarjeta").removeClass('is-invalid').addClass('is-valid');
        }

        // Validar que codigo de seguridad tenga 3 o más digitos
        if (cod_seguridad.trim().length > 2 && cod_seguridad.trim().length < 5) {
            $("#pp-codigo").removeClass('is-invalid').addClass('is-valid');
        }
        else {
            if (cod_seguridad.trim().length < 5) {
                msj += "El codigo de seguridad debe tener 3 o más digitos<br>";
            }
            else {
                msj += "El codigo de seguridad debe tener 4 o menos digitos<br>";
            }
            $("#pp-codigo").removeClass('is-valid').addClass('is-invalid');
            enviar = true;
        }

        // Enviar \\
        if (enviar) {
            $("#pp-w").html(msj);
            e.preventDefault();

        }
        else {
            $("#pp-w").html("Guardado");
            e.preventDefault();
        }

    });

    $("#pp-nroTarjeta").on("focusout", function () {
        var nro_tarjeta = $(this).val();
        nro_tarjeta = nro_tarjeta.replaceAll(" ", ""); // eliminar espacios en blanco

        // formatear la tarjeta con espacios cada cuatro digitos
        nro_tarjeta = nro_tarjeta.replace(/(\d{4})/g, '$1 ').trim();

        // establecer el valor del campo con la tarjeta formateada
        $(this).val(nro_tarjeta);
    });

    $("#pp-fecVencMes").on("focusout", function () {
        var fch_vencMes = $(this).val();
        fch_vencMes = parseInt(fch_vencMes);

        if (fch_vencMes < 10) {
            fch_vencMes = "0" + fch_vencMes;
        } else {
            fch_vencMes = fch_vencMes.toString();
        }

        // establecer el valor del campo con el mes formateado
        $(this).val(fch_vencMes);
    });

    // establecer el valor del campo con el mes formateado
    let fechaActual = new Date();
    let yActual = fechaActual.getFullYear() - 2000;
    let maxY = yActual + 10;
    let minY = yActual;

    document.getElementById("pp-fecVencAnio").setAttribute("max", maxY);
    document.getElementById("pp-fecVencAnio").setAttribute("min", minY);

    document.querySelector(".intNumber").addEventListener("keypress", function (evt) {
        if (evt.which != 8 && evt.which != 0 && evt.which < 48 || evt.which > 57) {
            evt.preventDefault();
        }
    });
});