function buttonText() {
    const button = document.getElementById("generate-button")
    const phrases = ["New Idea!", "Eureka!", "Lets start!", "Start to create!", "I have an idea!"]

    button.innerHTML = phrases[Math.floor((Math.random()*phrases.length))]
    console.log(button.value)
}

buttonText()