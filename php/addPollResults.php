<?php

require_once "connectToDB.php";
function addPollResults($age, $niveau_enseignement, $moment_journee, $type_aliment, $aliment)
{
    $pdo = connectToDB();
    $sql = "INSERT INTO `sondage` VALUES (:valAge,:valNiveau,:valMoment,:valAType,:valAliment)";

    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(":valAge", $age);
    $stmt->bindParam(":valNiveau", $niveau_enseignement);
    $stmt->bindParam(":valMoment", $moment_journee);
    $stmt->bindParam(":valAType", $type_aliment);
    $stmt->bindParam(":valAliment", $aliment);
    $bool = $stmt->execute();

    return $bool;

}

if (isset($_POST) && !empty($_POST)) {

    //check all values uwu
    

}