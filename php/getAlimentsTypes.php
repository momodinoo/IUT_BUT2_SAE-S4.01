<?php
require_once "connectToDB.php";

function getAlimentsTypes(){
    $pdo = connectToDB();
    $sql = "SELECT DISTINCT alim_grp_nom_fr FROM aliments;";
    $stmt = $pdo->prepare($sql);
    $bool = $stmt->execute();
    $results = [];
    if ($bool) {
        $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $stmt->closeCursor();
    }
    return $results;
}