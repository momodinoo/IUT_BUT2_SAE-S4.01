(async () => {

    const ctx = document.getElementById("schoolMomentChart");

    const [college, lycee] = await getPythonResults('/repartition/school_moment/all');

    const morningAlimentSet = new Set()
    const eveningAlimentSet = new Set()

    const addAlimentToSet = (setElement, array) => {
            array.forEach(e => {
                setElement.add(e.type_aliment)
            })
        },
        getAlimentCount = (array, alimentName) => {
            return array.filter(e => e.type_aliment === alimentName)[0]?.count ?? 0;
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
                title: {
                    display: true,
                    text: 'Répartition des aliments consommés par niveau scolaire et moment de la journée'
                },
                legend: {
                    display: false
                }
            },
            responsive: true,
            interaction: {
                intersect: true,
            },
            scales: {
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true
                }
            }
        }
    };

    const chart = new Chart(ctx, config)

})();