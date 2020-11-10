function saveIncidencias() {
    var selectDoenca = document.getElementById('doencas');
    var dataIncidencia = document.getElementById('data-incidencia');

    if (!selectDoenca.value || !dataIncidencia.value) {
        !selectDoenca.value ? selectDoenca.style.border = '2px solid red' : null;
        !dataIncidencia.value ? dataIncidencia.style.border = '2px solid red' : null;
        return null;
    }  

    let obj = { 
        selectDoenca: selectDoenca.value,
        dataIncidencia: dataIncidencia.value,
    }

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/incidencia/save", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = (e) => {
        var data = JSON.parse(ajax.responseText);
        if (ajax.readyState == 4 && ajax.status == 200) {
            window.location.href = '/';
        } else {
            alert(`Tente novamente: ${data.Erro}`)
        }
    }

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
    }

    ajax.send(JSON.stringify(obj));   
}