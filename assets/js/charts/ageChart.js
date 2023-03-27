(async () => {


    const allRepartition = await getPythonResults('/repartition/all'),
        repartitionByAge = await getPythonResults('/repartition/age/all');

    const ctx = document.getElementById('ageChart');
    const select = document.getElementById("filterAge");

    const addAgeList = (selectElement, repartitionAge) => {
            for (let {age} of repartitionAge) {
                const ageOption = document.createElement("option");
                ageOption.value = age;
                ageOption.innerText = `${age} ans`;

                selectElement.appendChild(ageOption);
            }
        },
        generateChartData = array => {
            return array.map(e => e.count)
        },
        generateChartLabel = array => {
            return array.map(e => e.type_aliment)
        },
        generateChartColors = array => {
            return generateColors(array.length)
        },
        generateData = (data) => {
            return {
                labels: generateChartLabel(data),
                datasets: [{
                    data: generateChartData(data),
                    backgroundColor: generateChartColors(data),
                }]
            }
        }


    addAgeList(select, repartitionByAge);

    const data = generateData(allRepartition)

    data.datasets[0] = {
        ...data.datasets[0],
        label: "Répartition des aliments par rapport à l'âge",
        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--base-navbar-background-color'),
        hoverOffset: 4
    }

    const chart = new Chart(ctx, {
        type: 'doughnut',
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Répartition des aliments par âge, actuellement : (Tout âge compris)'
                },
            },
        },
        data
    });

    select.onchange = () => {
        const value = select.options[select.selectedIndex].value;
        let data = (value === "all") ? allRepartition : repartitionByAge.filter(e => e.age === +value)[0].data

        chart.options.plugins.title.text = `Répartition des aliments par âge, actuellement : (${(value === "all") ? "Tout âge compris" : value + " ans"})`

        chart.data.labels = generateChartLabel(data)
        chart.data.datasets = [{
            data: generateChartData(data),
            backgroundColor: generateChartColors(data)
        }]

        chart.update();

    }

})();