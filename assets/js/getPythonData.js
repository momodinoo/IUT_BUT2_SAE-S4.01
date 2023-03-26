const getPythonResults = async (url) => {
    const host = "http://127.0.0.1:5000"
    const endpoint = `${host}${url}`

    let result = await fetch(endpoint)
    return result.json()
}

(async () => {
   console.log(await getPythonResults('/aliment_types_repartition'));
   console.log(await getPythonResults('/most_ate_aliment'));
   console.log(await getPythonResults('/mean_age_by_aliment_types'));
   console.log(await getPythonResults('/mean_kcal'));
})();

