<?php
	$db = mysqli_connect ('localhost','root','1234','mysitedb') or die ('Fail');
?>
<html>
<head>

<style>
.game-item {
            opacity: 1;
            transition: opacity 0.5s ease-in-out;
        }

        .game-item:hover {
            opacity: 0.5; 
        }




h1{
font-size :34px;
font-family: Arial Black, Gadget, sans-serif;
text-align: center;

}


table{

font-family: Arial, sans-serif;
border-collapse: collapse;
width: 100%;
borde: 1px solid #dddddd;

}
th, td{
border: 1px solid #dddddd;
text-align: left;
padding: 8px;

}

th{
background-color:#f2f2f2;

}

.game-image{
max-width: 175px;
}

</style>

</head>

<body>

<h1>Juegos que he jugado ultimamente</h1>
<table>
<tr>
<th>Id</th>
<th>Nombre</th>
<th>Imagen</th>
<th>Empresa</th>
<th>Precio</th>

</tr>
<?php
 //Lanzar una query
$query = 'SELECT * FROM tJuegos';
$result=mysqli_query($db, $query) or die ('Query error');
//Recorrer el resultado
while ($row = mysqli_fetch_array($result)){
echo '<tr class="game-item">';
echo '<td class="game-item">' . $row['id'] . '</td>';
echo '<td><a href="detail.php?id=' . $row['id'] . '">'. $row['nombre'] . '</a></td>';
echo '<td><img src="' .$row['url_imagen'] . '" class="game-image"></td>';
echo '<td>' . $row['empresa'] . '</td>';
echo '<td>' . $row['precio'] . '€ ' .  '</td>';
}
mysqli_close($db);
?>
</table>


<a href="logout.php">Cerrar sesión</a>
</body>

</html>
