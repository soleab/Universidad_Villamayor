<?php


$dsn = 'mysql:dbname=php_sql_course;host=127.0.0.1';
$user = 'root';
$password = '';

try{

	$pdo = new PDO(	$dsn, 
					$user, 
					$password, array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES  \'UTF8\''));
	

}catch( PDOException $e ){
	echo 'Error al conectarnos: ' . $e->getMessage();
}




