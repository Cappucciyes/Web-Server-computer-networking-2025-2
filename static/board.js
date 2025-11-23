const evtSource = new EventSource("http://localhost:9999/boardEvent", {
    withCredentials: false,
})

evtSource.addEventListener("haha", (event) => {
    let data = JSON.parse(event.data)
    let id = data.id
    let status = data.status
    console.log(id)
    console.log(status)

    let toUpdate = document.querySelector(`#s${id} span.status`)
    toUpdate.innerHTML= status
});

