<?php
session_start();

$db = mysqli_connect('localhost', 'root', '1234', 'mmysitedb') or die('Error de conexión');

$current_password = $_POST['current_password'];
$new_password = $_POST['new_password'];
$confirm_password = $_POST['confirm_password'];

$user_id = $_SESSION['user_id'];

$query = "SELECT contraseña FROM tUsuarios WHERE id = '$user_id'";
$result = mysqli_query($db, $query);

if (!$result) {
    die("Error en la consulta: " . mysqli_error($db));
}

$row = mysqli_fetch_assoc($result);
$stored_password = $row['contraseña'];

if (!password_verify($current_password, $stored_password)) {
    echo "Contraseña actual incorrecta.";
} elseif ($new_password === $current_password) {
    echo "La nueva contraseña debe ser diferente de la actual.";
} elseif ($new_password !== $confirm_password) {
    echo "Las contraseñas nuevas no coinciden. Inténtalo de nuevo.";
} else {
    $hashed_password = password_hash($new_password, PASSWORD_DEFAULT);
    $update_query = "UPDATE tUsuarios SET contraseña = '$hashed_password' WHERE id = '$user_id'";
    $update_result = mysqli_query($db, $update_query);

    if (!$update_result) {
        die("Error al actualizar la contraseña: " . mysqli_error($db));
    }

    echo "Contraseña cambiada exitosamente.";
}

mysqli_close($db);
?>

