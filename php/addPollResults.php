<?php

require_once "connectToDB.php";
function addPollResults($age, $niveau_enseignement, $moment_journee, $type_aliment, $aliment, $quantite)
{
    $pdo = connectToDB();
    $sql = "INSERT INTO `sondage`(age, niveau_enseignement, moment_journee, type_aliment, aliment) VALUES (:valAge,:valNiveau,:valMoment,:valAType,:valAliment)";

    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(":valAge", $age);
    $stmt->bindParam(":valNiveau", $niveau_enseignement);
    $stmt->bindParam(":valMoment", $moment_journee);
    $stmt->bindParam(":valAType", $type_aliment);
    $stmt->bindParam(":valAliment", $aliment);


    for($i=0;$i<$quantite;$i++){
        $bool = $stmt->execute();
        if(!$bool) return false;
    }

    return true;
}