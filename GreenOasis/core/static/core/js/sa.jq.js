$(document).ready(function () {
  $("#sa-form").submit(function (e) {
    var nombre = $("#sa-nombre").val();
    var desc = $("#sa-desc").val();
    var precio = $("#sa-precio").val();
    var stock = $("#sa-stock").val();
    var cat = $("#sa-cat").val();
    var img = $("#sa-img").val();

    var allowedExtensions = ["jpg", "jpeg", "png", "gif"];

    var msj = "";
    let enviar = false;

    /* Validacion nombre */
    if (nombre.trim().length < 4 || nombre.trim().length > 120) {
      msj += "El nombre debe ser entre 4 y 120 carácteres<br>";
      $("#sa-nombre").removeClass("is-valid").addClass("is-invalid");
      enviar = true;
    } else {
      $("#sa-nombre").removeClass("is-invalid").addClass("is-valid");
    }

    var letra = nombre.charAt(0);
    if (!esMayuscula(letra)) {
      msj += "La primera letra del nombre debe ser mayúscula<br>";
      $("#sa-nombre").removeClass("is-valid").addClass("is-invalid");
      enviar = true;
    }

    /* Validacion descripcion */
    if (desc.trim().length < 4 || desc.trim().length > 1250) {
      msj += "La descripción debe ser entre 4 y 1250 carácteres<br>";
      $("#sa-desc").removeClass("is-valid").addClass("is-invalid");
      enviar = true;
    } else {
      $("#sa-desc").removeClass("is-invalid").addClass("is-valid");
    }

    var letra = desc.charAt(0);
    if (!esMayuscula(letra)) {
      msj += "La primera letra de la descripción debe ser mayúscula<br>";
      $("#sa-desc").removeClass("is-valid").addClass("is-invalid");
      enviar = true;
    }
    /* Validacion de precio */
    if (/^[0-9]+$/.test(precio) == false) {
      msj +=
        "El precio no puede contener ni letras ni ningún otro carácter que no sea un número natural<br>";
      $("#sa-precio").removeClass("is-valid").addClass("is-invalid");
      enviar = true;
    } else {
      $("#sa-precio").removeClass("is-invalid").addClass("is-valid");
    }

    /* Validacion de stock */
    if (/^[0-9]+$/.test(stock) == false) {
      msj +=
        "El stock no puede contener ni letras ni ningún otro carácter que no sea un número natural<br>";
      $("#sa-stock").removeClass("is-valid").addClass("is-invalid");
      enviar = true;
    } else {
      $("#sa-stock").removeClass("is-invalid").addClass("is-valid");
    }

    /* Validacion de stock */
    if (cat === 'Seleccione una categoría') {
      msj += "Debe seleccionar una categoría<br>";
      $("#sa-cat").removeClass('is-valid').addClass('is-invalid');
      enviar = true;
    }
    else {
      $("#sa-cat").removeClass('is-invalid').addClass('is-valid');
    }

    // Obtener la extensión del archivo
    var extension = img.substring(img.lastIndexOf('.') + 1).toLowerCase();

    // Verificar si la extensión coincide con una imagen permitida
    if (allowedExtensions.indexOf(extension) === -1) {
      // No es una imagen válida
      msj += "Debe seleccionar un archivo tipo imagen<br>";
      enviar = true;
      $("#sa-img").removeClass('is-valid').addClass('is-invalid');
    } else {
      // Es una imagen válida
      $("#sa-img").removeClass('is-invalid').addClass('is-valid');
    }

    /* Enviar Form */
    if (enviar) {
      $("#sa-w").html(msj);
      e.preventDefault();

    } else {
      $("#sa-w").html("Guardado");
    }
  });

  /* Funcion de Validacion de Mayuscula */
  function esMayuscula(letra) {
    console.log(letra);
    console.log(letra.toUpperCase());
    if (letra == letra.toUpperCase()) {
      return true;
    } else {
      return false;
    }
  }
});
