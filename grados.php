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
<h3> Lista de Grados:</h3>
<div class="contenido">

  <table class="GeneratedTable" width="100%">
    <thead>
      <tr class="borde" style="border:1px;">
        <th>Nombre de la Carrera</th>
        <th>Identificador</th>
        <th>Creditos Grado</th>
        <th>Creditos Optativos</th>
        <th>Creditos Transversales</th>
        <th>Identificador Escuela</th>
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
<p>&nbsp;</p>
<div id="cred" >
  2018 © Universidad de VillaMayor
  - Todos los derechos reservados
  <p> Contacto: infoedu@uvm.es</p>
</div>


</body>
</html>
