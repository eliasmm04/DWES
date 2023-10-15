<html>
<body>
<h1>Jubilacion</h1>
<?php
$edad=$_GET["edad"];

function edad_en_10_anyo($edad) {

return  $edad + 10;
}
if (edad_en_10_anyo($edad) >65 ){

echo "En 10 años tendras edad de jubilacion";
}else{
echo"Disfruta de tu tiempo!";

}

?>

</body>
</html>
