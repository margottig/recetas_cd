$(document).ready(function(){
    $("#imagen_receta").change(function(){
        var extensiones = ["image/jpeg", "image/jpg"];
        var archivo = this.files[0];
        var tipodearchivo = archivo.type;
        if (!(tipodearchivo==extensiones[0] || tipodearchivo==extensiones[1]  )){
            alert("Por favor, ingresa archivos de tipo jpg o jpeg");
            $("#imagen_receta").val("");
            return false
        }


    })



})