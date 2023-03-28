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
            return array.map(e => e.type_aliment.charAt(0).toUpperCase() + e.type_aliment.slice(1))
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
        label: " Nombre d'utilisateurs ",
        borderColor: getComputedStyle(document.documentElement).getPropertyValue('--base-color-dark'),
        hoverOffset: 4
    }

    const chart = new Chart(ctx, {
        type: 'doughnut',
        options: {
            responsive: true,
            plugins: {
                /*title: {
                    display: false,
                    text: "Répartition des types d'aliments par âge, actuellement : Tous les âges",
                    padding : {
                        top : 15
                    },
                    color: getComputedStyle(document.documentElement).getPropertyValue('--base-color-dark'),
                    font : {
                        weight : "normal",
                        size : 25
                    },
                },*/
                legend:{
                    position: 'right',

                    labels:{
                        color:getComputedStyle(document.documentElement).getPropertyValue('--base-color-dark'),
                        boxWidth : 75,
                        padding : 20,
                        font:{
                            size:16
                        }
                    },
                },
            },
        },
        data
    });

    select.onchange = () => {
        const value = select.options[select.selectedIndex].value;
        let data = (value === "all") ? allRepartition : repartitionByAge.filter(e => e.age === +value)[0].data

        document.getElementById("titleChartAge").innerHTML = `Répartition des aliments par âge, actuellement : ${(value === "all") ? "Tous les âges" : value + " ans"}`

        chart.data.labels = generateChartLabel(data)
        chart.data.datasets = [{
            data: generateChartData(data),
            backgroundColor: generateChartColors(data)
        }]

        chart.update();

    }

})();