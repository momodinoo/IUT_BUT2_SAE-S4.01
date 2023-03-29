(async () => {
    const mean_aliments_type = document.getElementById("mean-aliments-type");

    const {mean} = await getPythonResults('/mean/kcal');
    const divMeanKcal = document.getElementById("mean-kcal");

    const age = await getPythonResults('/mean/age');

    const mostAliment = await getPythonResults('/most/aliment');
    const divMostAliment = document.getElementById("most-aliment");

    const mostAge = await getPythonResults('/most/age');
    const divMostAge = document.getElementById("most-age");

    const mostSchool = await getPythonResults('/most/school');
    const divMostSchool = document.getElementById("most-school");

    age.forEach(({type_aliment, mean}) => {
        const li = document.createElement("li");
        li.innerHTML = `"${type_aliment.charAt(0).toUpperCase() + type_aliment.slice(1, type_aliment.length)}" est consommé en moyenne par des individus de ${Math.round(mean)} ans.`
        mean_aliments_type.appendChild(li)
    })

    divMeanKcal.innerHTML = `Le nombre moyen de calories pour un repas est de ${mean.toFixed(2)} kcal/100g.`;

    divMostAliment.innerHTML = `L'aliment le plus consommé est "${mostAliment.type_aliment}". Il a été consommé ${mostAliment.count} fois.`;

    divMostAge.innerHTML = `Les personnes âgées de ${mostAge.age} ans sont les plus présentes parmi les réponses du sondages (${mostAge.count} participations).`;

    divMostSchool.innerHTML = `Les personnes scolarisées au ${mostSchool.niveau_enseignement.toLowerCase()} sont les plus présentes parmi les réponses du sondages (${mostSchool.count} participations).`;
})();