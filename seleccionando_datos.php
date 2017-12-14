<pre><?php
require_once('connection.php');
$sql = 'SELECT * FROM grados';

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
 
 
<div class="row column text-center">
<h2>Universidad VillaMayor</h2>
<hr>
</div>
<div class="contenido">

<blockquote>
  <h3>Lista de Grados:</h3>
</blockquote>

<table width="100%">
  <thead>
    <tr class="borde" style="border:1px;">
      <th width="25%"><u>Nombre de la Carrera</u></th>
      <th width="10%"><u>Identificador</u></th>
      <th width="65%"><u>Descripción</u></th>
    </tr>
  </thead>
  <tbody>
  <?php
  	foreach($results as $rs)
	{
  ?>
    <tr>
      <td><?php echo $rs['Nombre'] ?></td>
      <td><?php echo $rs['Identificador'] ?></td>
      <td><?php echo $rs['Descripcion'] ?></td>
    </tr>
    
    <?php
      }
      ?>
  </tbody>
</table>
</div>



</body>
</html>
