<?php
$dbHostname = "localhost";
$dbName = "sondage";
$dbLogin = "root";
$dbPwd = "";
$dbURL = "mysql:server=$dbHostname;dbname=$dbName";
function connectToDB () {
    try {
        global $dbLogin, $dbPwd, $dbURL;
        return new PDO ($dbURL, $dbLogin, $dbPwd, array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8'));
    } catch (PDOException $e) {
        $error = $e->getMessage();
        echo mb_convert_encoding("Error accessing database : $error \n", 'UTF-8');
        return null;
    }
}
