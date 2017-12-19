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
      <th><u>Nombre de la Carrera</u></th>
      <th><u>Identificador</u></th>
      <th><u>Creditos Grado</u></th>
      <th><u>Creditos Optativos</u></th>
      <th><u>Creditos Transversales</u></th>
      <th><u>Identificador Escuela</u></th>
    </tr>
  </thead>
  <tbody>
  <?php
  	foreach($results as $rs)
	{
  ?>
    <tr>
      <td><?php echo $rs['NombreGrado'] ?></td>
      <td><?php echo $rs['GradoID'] ?></td>
      <td><?php echo $rs['CreditosGrado'] ?></td>
      <td><?php echo $rs['CreditosOptativos'] ?></td>
      <td><?php echo $rs['CreditosTransversales'] ?></td>
      <td><?php echo $rs['id'] ?></td> 
    </tr>
    
    <?php
      }
      ?>
  </tbody>
</table>
</div>



</body>
</html>
