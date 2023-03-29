<?php

try {
    $sum = 0;
    for ($i = 0; $i < 20; $i++) {
        $age = random_int(10, 18);
        $schoolLevel = random_int(0, 1) === 0 ? "Collège" : "Lycée";
        $moment = random_int(0, 1) === 0 ? "Matin" : "Soir";

        include_once('./php/getAlimentsTypes.php');
        include_once('./php/getAlimentsByType.php');
        include_once('./php/addPollResults.php');
        $types = getAlimentsTypes();

        $selectedType = $types[array_rand($types)]["alim_grp_nom_fr"];

        $alimentList = getAlimentsByType($selectedType);

        $aliment = $alimentList[array_rand($alimentList)]["alim_nom_fr"];

        $quantity = random_int(1, 5);
        $sum += $quantity;

        addPollResults($age, $schoolLevel, $moment, $selectedType, $aliment, $quantity);

        echo "Sondage ajouté : $age ans | Établissement : $schoolLevel | Moment : $moment | Type : $selectedType | Aliment : $aliment | Quantité : $quantity <br>";
    }

    echo "$sum lignes ajoutés. <br>";

} catch (Exception $e) {
}

