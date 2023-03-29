(async () => {


    const allRepartition = await getPythonResults('/repartition/all'),
        repartitionByAge = await getPythonResults('/repartition/age/all');

    const ctx = document.getElementById('ageChart');
    const select = document.getElementById("filterAge");

    const addAgeList = (selectElement, repartitionAge) => {
            for (let {age} of repartitionAge) {
                const ageOption = document.createElement("li");
                ageOption.setAttribute("value", age)
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
        getAlimentCount = array => {
            let sum = 0;
            array.forEach(e => sum += e.count)
            return sum
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



    const data = generateData(allRepartition),
        count = getAlimentCount(allRepartition)

    data.datasets[0] = {
        ...data.datasets[0],
        label: " Nombre d'utilisateurs ",
        borderColor: getComputedStyle(document.body).getPropertyValue('--base-color'),
        hoverOffset: 4
    }

    const chart = new Chart(ctx, {
        type: 'doughnut',
        options: {
            responsive: true,
            plugins: {
                legend:{
                    position: 'right',
                    labels:{
                        color:getComputedStyle(document.body).getPropertyValue('--base-color'),
                        boxWidth : 80,
                        boxHeight : 25,
                        padding : 30,
                        font:{
                            size:16
                        }
                    },
                },
                tooltip: {
                    callbacks: {
                        label: ({label, parsed}) => {
                            const percentage = (parsed / count) * 100
                            return ` Pourcentage : ${percentage.toFixed(2)}%`
                        },
                    }
                }
            },
        },
        data
    });

    const ageContext = document.getElementById("ageContext")
    const ageSelector = document.getElementById("ageChoices")
    addAgeList(ageSelector, repartitionByAge);

    [...ageSelector.children].forEach(e => {
        e.addEventListener("click", a => {

            ageSelected.innerHTML = e.innerHTML
            ageSelected.setAttribute("value", e.getAttribute("value"))

            ageContext.classList.toggle("show");
            ageSelected.classList.toggle("hide");

            const event = new CustomEvent("ageChange")
            document.dispatchEvent(event);
        })
    })

    const ageSelected = document.getElementById("ageSelected");
    ageSelected.onclick = () => {
        ageContext.classList.toggle("show");
        ageSelected.classList.toggle("hide");
    }

    document.addEventListener("ageChange", () => {

        const value = ageSelected.getAttribute("value");
        const data = (value === "all") ? allRepartition : repartitionByAge.filter(e => e.age === +value)[0].data

        chart.data.labels = generateChartLabel(data)
        chart.data.datasets = [{
            data: generateChartData(data),
            backgroundColor: generateChartColors(data)
        }]
        chart.options.plugins.tooltip.callbacks.label = ({parsed}) => {
            const count = getAlimentCount(data)
            const percentage = (parsed / count) * 100
            return ` Pourcentage : ${percentage.toFixed(2)}%`
        }
        chart.update();
    })

    document.addEventListener("toggleBlackMode", () => {
        chart.data.datasets[0].borderColor= getComputedStyle(document.body).getPropertyValue('--base-color');
        chart.options.plugins.legend.labels.color = getComputedStyle(document.body).getPropertyValue('--base-color');
        chart.update();
    })

})();