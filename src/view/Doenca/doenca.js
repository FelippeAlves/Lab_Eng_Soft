function saveDoenca() {
    var nomeDoenca = document.getElementById('doenca-campo');
    var sintomasDoenca = document.getElementById('sintomas-campo');

    if (!nomeDoenca.value || !sintomasDoenca.value) {
        !nomeDoenca.value ? nomeDoenca.style.border = '2px solid red' : null;
        !sintomasDoenca.value ? sintomasDoenca.style.border = '2px solid red' : null;
        return null;
    }

    let obj = { 
        nome: nomeDoenca.value,
        sintomas: sintomasDoenca.value,
    }

    var ajax = new XMLHttpRequest();

    ajax.open("POST", "http://127.0.0.1:5000/doenca/save", true);
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