// Selecciona el formulario por su ID
const form = document.querySelector('form');

// Agrega un evento de escucha para el envío del formulario
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Evita el envío del formulario por defecto

  // Realiza aquí tu lógica de validación de campos, por ejemplo:
  const emailInput = document.getElementById('form3Example3cg').value;
  const passwordInput = document.getElementById('form3Example4cg').value;

  if (emailInput && passwordInput) {
    // Si la validación es exitosa, redirige al usuario a la página deseada
    window.location.href = 'dash-ventas.html';
  } else {
    // Si la validación falla, muestra un mensaje de error o toma alguna otra acción
    alert('Por favor, complete todos los campos.');
  }
});
