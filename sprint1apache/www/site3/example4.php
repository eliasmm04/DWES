<html>
<body>
<h1>Jubilacion</h1>
<?php

function edad_en_11_anyo($edad) {

return  $edad + 11;
}
function mensaje($edad)  {
if (edad_en_11_anyo($edad) >65 ){

return "En 11 años tendras edad de jubilacion";
}else{
return"Disfruta de tu tiempo!";

}
}
?>
<table>
<tr>
<th>Edad </th>
<th>Info </th>

</tr>
<?php
$lista = array (53,54,55,56,57);
foreach ($lista as $valor ){
echo "<tr>";
echo "<td>" .$valor."</td>";
echo "<td>".mensaje($valor)."</td>";
echo "</tr>";

}

?>

</table>

</body>
</html>
