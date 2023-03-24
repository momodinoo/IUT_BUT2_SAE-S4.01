const getPythonResults = async (url) => {
    const host = "http://127.0.0.1:5000"
    const endpoint = `${host}${url}`

    let result = await fetch(endpoint)
    return result.json()
}

(async () => {
   console.log(await getPythonResults('/'));
})();

