console.log("ARCHIVO CONECTADO");


$(".login").on("submit", function(e){
    e.preventDefault();
    console.log(e.target.email_1.value, " QUIERO SABER QUE CONTIENE E")
    let is_valid = true;
    let mensaje = '';
    let regex_email = /^[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$/
    
    if (!regex_email.test(e.target.email_1.value)){
        mensaje = " <p class=text-danger> Correo no valido </p>"
        is_valid =  false;
    }

    if(is_valid == true){
        login(e.target)
    }
    else{
        $(e.target).children(".message").html(mensaje)
    }

})

login = async function(data){
    let informacion_formulario = new FormData(data);
    let url = '/login';
    let settings = {
        method:"POST",
        body: informacion_formulario
    };

    let enviar = await fetch(url, settings);
    let respuesta = await enviar.json();
    if (respuesta.ok){
        window.location.href = '/welcome'
    }
    else {
        $(data).children(".message").text(response.content);
    }
}