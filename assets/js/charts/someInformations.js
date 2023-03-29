(async () => {
    const mean_aliments_type = document.getElementById("mean-aliments-type");

    const {mean} = await getPythonResults('/mean/kcal');
    const divMeanKcal = document.getElementById("mean-kcal");

    const age = await getPythonResults('/mean/age');

    const mostAliment = await getPythonResults('/most/aliment');
    const divMostAliment = document.getElementById("most-aliment");

    age.forEach(({type_aliment, mean}) => {
        const li = document.createElement("li");
        li.innerHTML = `"${type_aliment.charAt(0).toUpperCase() + type_aliment.slice(1, type_aliment.length)}" est consommé en moyenne par des individus de ${Math.round(+mean)} ans.`
        mean_aliments_type.appendChild(li)
    })

    divMeanKcal.innerHTML = `Le nombre moyen de calories pour un repas est de ${mean.toFixed(2)} kcal/100g.`;

    divMostAliment.innerHTML = `L'aliment le plus consommé est "${mostAliment.type_aliment}". Il a été consommé ${mostAliment.count} fois. `
})();//42