<pre><?php
require_once('connection.php');
$sql = 'SELECT * FROM gradoss';

$statement = $pdo->prepare($sql);
$statement->execute();
$results = $statement->fetchAll();
//var_dump($results);


?>
</pre>
<!doctype html>
<html class="no-js" lang="es">
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Universidad VillaMayor</title>
<link rel="stylesheet" href="estilos.css">
</head>
<body>
 
 
<div class="banner">
<h2>Universidad VillaMayor</h2>
</div>

<div class="contenido">
<table width="100%" border="0">
  <tbody>
    <tr>
      <td width="600px"><center><img src="logo.png" width="500" height="500" alt="logo"/></center></td>
      <td><p><h3>Índice:</h3></p>
        <div class="listado">
          <ul>
            <li><a href="grados.php">Lista de Grados</a></li>
            <li>Ejemplo </li>
            <li>Ejemplo</li>
            <li>Ejemplo</li>
          </ul>
        </div></td>
    </tr>
  </tbody>
</table>
	
  
</div>
<div id="cred" >
  2018 © Universidad de VillaMayor
  - Todos los derechos reservados
  <p> Contacto: infoedu@uvm.es</p>
</div>


</body>
</html>
