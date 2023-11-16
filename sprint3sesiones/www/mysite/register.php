<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $email = $_POST['email'];
    $password = $_POST['contraseña'];
    $confirm_password = $_POST['confirmar_contraseña'];

    // Verificar si los campos están vacíos
    if (empty($nombre) || empty($apellidos) || empty($email) || empty($password) || empty($confirm_password)) {
        echo "Todos los campos son obligatorios.";
    } else {
        // Verificar si las contraseñas coinciden
        if ($password !== $confirm_password) {
            echo "Las contraseñas no coinciden.";
        } else {
            // Verificar si el correo ya existe en la base de datos
            $query_check_email = "SELECT * FROM tUsuarios WHERE email='$email'";
            $result_check_email = mysqli_query($db, $query_check_email);
            
            if (mysqli_num_rows($result_check_email) > 0) {
                echo "El correo ya está registrado.";
            } else {
                // Cifrar la contraseña antes de almacenarla en la base de datos
                $hashed_password = password_hash($password, PASSWORD_DEFAULT);

                // Insertar el nuevo usuario en la base de datos
                $query_insert_user = "INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES ('$nombre', '$apellidos', '$email', '$hashed_password')";
                mysqli_query($db, $query_insert_user) or die('Error al registrar el usuario.');

                // Redirigir al usuario a la página principal
                header("Location: main.php");
                exit();
            }
        }
    }
}
mysqli_close($db);
?>
