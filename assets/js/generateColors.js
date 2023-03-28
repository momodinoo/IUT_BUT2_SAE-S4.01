const _shuffleArray = array => {
    for (let i = array.length - 1; i > 0; i--) {
        const j = ~~(Math.random() * (i + 1));
        const temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array
}

const generateColors = (count) => {

    let arrayToReturn = [
        "rgb(242,164,183)",
        "rgb(110,198,236)",
        "rgb(239,215,85)",
        "rgb(143,197,117)",
        "rgb(157,130,227)",
        "rgb(244,67,67)",
        "rgb(243,140,67)",
        "rgb(80,122,227)",
        "rgb(177,248,228)",
        "rgb(9,109,10)",
        "rgb(189,57,193)",
        "rgb(58,49,116)",
    ]

    arrayToReturn = _shuffleArray(arrayToReturn)

    arrayToReturn.length = count
    return arrayToReturn
}