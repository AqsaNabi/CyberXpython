const form = document.getElementById("myForm");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const formData = new FormData(form);

    const response = await fetch("http://127.0.0.1:8000/submit", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    console.log(result);

    alert(result.message);

    form.reset();
});