(async () => {

    const ctx = document.getElementById("schoolMomentChart");

    const [lycee, college] = await getPythonResults('/repartition/school_moment/all');

    const morningAlimentSet = new Set()
    const eveningAlimentSet = new Set()

    const capitalizeAliment = aliment => {
            return aliment.charAt(0).toUpperCase() + aliment.slice(1)
        },
        addAlimentToSet = (setElement, array) => {
            array.forEach(e => {
                setElement.add(capitalizeAliment(e.type_aliment))
            })
        },
        getAlimentCount = (array, alimentName) => {
            return array.filter(e => capitalizeAliment(e.type_aliment) === alimentName)[0]?.count ?? 0;
        },
        getColor = (array, alimentName) => {
            return array.filter(e => e.aliment === alimentName)[0].color
        },
        generateSet = () => {
            addAlimentToSet(morningAlimentSet, college.morning)
            addAlimentToSet(morningAlimentSet, lycee.morning)
            addAlimentToSet(eveningAlimentSet, college.evening)
            addAlimentToSet(eveningAlimentSet, lycee.evening)
        },
        generateDataset = (arrayType, alimentName) => {
            return {
                label: alimentName,
                data: [
                    getAlimentCount(college[arrayType], alimentName),
                    getAlimentCount(lycee[arrayType], alimentName)
                ],
                backgroundColor: getColor(alimentColor, alimentName),
            }
        }

    generateSet();

    const alimentList = [...morningAlimentSet, ...eveningAlimentSet]
    const colorList = generateColors(alimentList.length)
    const alimentColor = [];

    for (const aliment of alimentList) {
        alimentColor.push({
            aliment,
            color: colorList.pop()
        })
    }

    const morningDataset = [],
        eveningDataset = []

    for (let alimentName of [...morningAlimentSet]) {
        morningDataset.push({
            ...generateDataset("morning", alimentName),
            stack: "Matin"
        })
    }

    for (let alimentName of [...eveningAlimentSet]) {
        eveningDataset.push({
            ...generateDataset("evening", alimentName),
            stack: "Soir"
        })
    }

    const data = {
        labels: ["Collège", "Lycée"],
        datasets: [...morningDataset, ...eveningDataset]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        title: (tooltipItems) => {
                            return `${tooltipItems[0].dataset.stack}`;
                        },
                        label: (tooltipItem) => {
                            const getSchoolLevel = tooltipItem.label === "Collège" ? college : lycee
                            const getMoment = tooltipItem.dataset.stack === "Matin" ? getSchoolLevel.morning : getSchoolLevel.evening;
                            let countElements = 0;
                            getMoment.forEach(e => countElements += e.count);

                            const elementCount = tooltipItem.parsed.y;
                            const percentage = ((elementCount / countElements) * 100).toFixed(2);
                            return `${tooltipItem.dataset.label} : ${percentage}%`
                        }
                    }
                }
            },
            responsive: true,
            interaction: {
                intersect: true,
            },
            scales: {
                x: {
                    stacked: true,
                    grid: {
                        //color: getComputedStyle(document.body).getPropertyValue('--base-color'),
                        color:"#D93D3D",
                        lineWidth:2
                    },
                },
                y: {
                    stacked: true,
                    grid: {
                        color:"#D93D3D",
                        lineWidth:2
                    }
                },
            },
        },
    };

    Chart.defaults.color = "#D93D3D"
    Chart.defaults.font.size = 16
    let chart = new Chart(ctx, config)
    chart.reset()
    chart.update()

    document.addEventListener("toggleBlackMode", () => {
        //chart.options.scales.x.grid.color = getComputedStyle(document.body).getPropertyValue('--base-color');
        //chart.options.scales.y.grid.color = getComputedStyle(document.body).getPropertyValue('--base-color');
        chart.update()
    })

})();