<?php
session_start(); // Iniciar la sesión para acceder a $_SESSION

$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$juego_id = $_POST['id'];
$comentario = $_POST['new_comment'];

// Verificar si el usuario está logueado
if (isset($_SESSION['user_id'])) {
    $usuario_id = $_SESSION['user_id'];

    // Insertar el comentario con el usuario_id
    $query = "INSERT INTO tComentarios (comentario, usuario_id, juego_id, fecha_comentario) VALUES ('$comentario', $usuario_id, $juego_id, CURDATE())";
    mysqli_query($db, $query) or die('Error al agregar comentario.');
    
    echo "<p>Nuevo comentario añadido</p>";
} else {
    // Si el usuario no está logueado, puede manejar este caso de otra manera
    echo "<p>Debes iniciar sesión para añadir un comentario.</p>";
}

echo "<a href='/detail.php?id=$juego_id'>Volver</a>";
mysqli_close($db);
?>
