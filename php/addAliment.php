<?php
session_start();

$_SESSION["errors"] = array();
$_SESSION["success"] = array();

if (isset($_POST) && count($_POST) > 0) {
    if (!isset($_POST['age']) || !isset($_POST['enseignement']) || !isset($_POST['moment']) || !isset($_POST['typeAliment']) || !isset($_POST['aliment']) || !isset($_POST['quantite'])) {
        $_SESSION["errors"]['fields'] = "Veuillez remplir tous les champs.";
    }else {

        $age = $_POST['age'];
        $enseignement = $_POST['enseignement'];
        $moment = $_POST['moment'];
        $type = $_POST['typeAliment'];
        $aliment = $_POST['aliment'];
        $quantite = $_POST['quantite'];

        include_once('./addPollResults.php');

        $save = addPollResults($age, $enseignement, $moment, $type, $aliment, $quantite);

        if(!($save)) {
            $_SESSION["errors"]['saving'] = "Erreur lors de l'enregistrement du repas.";
        } else {
            $_SESSION["success"]['ok'] = "Le repas '$aliment', a bien été ajouté $quantite fois.";
        }
    }
}

header("Location: ../index.php");