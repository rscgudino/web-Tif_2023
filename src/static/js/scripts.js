// Código en tu HTML o archivo JS
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = {
            nombre: document.getElementById('nombre').value,
            apellido: document.getElementById('apellido').value,
            telefono: document.getElementById('telefono').value,
            email: document.getElementById('email').value,
            tipo_registro: document.getElementById('tipo_registro').value,
            tipo_propiedad: document.getElementById('tipo_propiedad').value
        };

        fetch('/api/usuarios', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta del servidor
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
