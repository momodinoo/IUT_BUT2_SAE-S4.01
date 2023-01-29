<?php
require_once 'connectToDB.php';

function getAlimentsByType($type){
    $pdo = connectToDB();
    $sql = "SELECT alim_nom_fr FROM aliments WHERE alim_grp_nom_fr = :valType";

    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(":valType", $type);
    $bool = $stmt->execute();
    $results = [];
    if ($bool) {
        $results = $stmt->fetchAll(PDO::FETCH_ASSOC);-
        $stmt->closeCursor();
    }
    return $results;
}

function getAlimentListName($aliment) {

    return $aliment["alim_nom_fr"];

}

if(isset($_POST) && !empty($_POST)) {

    if(isset($_POST["type"])) {

        $type = $_POST["type"];
        $alimentList = getAlimentsByType($type);

        echo json_encode(array_map("getAlimentListName", $alimentList));
    }
}