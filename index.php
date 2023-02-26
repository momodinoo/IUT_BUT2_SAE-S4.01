<?php
session_start();

$errors = $_SESSION["errors"] ?? array();
$success = $_SESSION["success"] ?? array();

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include_once('./php/getAlimentsTypes.php');

$types = getAlimentsTypes();

function getAlimentType($element) {
    $alimGrp = "alim_grp_nom_fr";
    return key_exists($alimGrp, $element) ? trim(ucfirst($element[$alimGrp])) : "no data";
}

include_once 'main.html';

session_unset();
