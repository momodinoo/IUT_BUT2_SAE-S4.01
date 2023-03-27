const alimentsType = document.getElementById("typeAliment");

alimentsType.onchange = async () => {
    let value = alimentsType.options[alimentsType.selectedIndex].value;

    if (value === "NON_SELECTED_VALUE") return;

    const formData = new FormData();
    formData.append('type', value);

    const res = await fetch("./php/getAlimentsByType.php", {
        method: "POST",
        body: formData,
    })

    const content = JSON.parse(await res.text())
    const alimentList = document.getElementById("aliment");

    while (alimentList.childElementCount !== 1) {
        alimentList.removeChild(alimentList.lastChild);
    }

    for (let aliment of content) {
        const alimentOption = document.createElement("option");
        alimentOption.value = aliment;
        alimentOption.innerText = aliment;

        alimentList.appendChild(alimentOption);
    }
}