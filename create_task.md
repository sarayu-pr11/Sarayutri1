<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Task</title>
    <link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>
<h1>Play Now!</h1>
<div id="trivia"></div>
<h2>Score:<span id="points">0</span></h2>
<script>
    const trivia = document.getElementById('trivia')
    const displayScore = document.getElementById('points')
    let points = 0
    const genres = [
        {
            name: 'General Knowledge',
id: 9 },
        {
            name: 'Computers',
id: 18 },
        {
            name: 'Mythology',
id: 20 },
        {
            name: 'Books',
id: 10 }
]
    //I chose these id values since the URL where I fetch the information from has
specific values for each category which correspond to the questions
    const levels = ['easy', 'medium', 'hard']
    function genreAdd(genre) {
        const column = document.createElement('div')
        // generates the columns with the id of "div"
        column.classList.add('genre-column')
        column.innerHTML = genre.name
        trivia.append(column)
        levels.forEach(level => {
            const flash = document.createElement('div')
            flash.classList.add('flash')
            column.append(flash)
//adds the point value for each flash
            if (level === 'easy') {
                flash.innerHTML = 100
            }
            if (level === 'medium') {
                flash.innerHTML = 200

            }
            if (level === 'hard') {
                flash.innerHTML = 300
            }
            fetch(`https://opentdb.com/api.php?amount=1&category=$
{genre.id}&difficulty=${level}&type=boolean`)
                //i added the ${genre.id} and the ${level} so that the link is
dynamic and changes for each category and difficulty level
                .then(response => response.json()) //this converts the json data
into data that is usable for the program
                .then(data => {
                    // This link comes from Open Trivia Database
(https://opentdb.com/) where I was able to generate an API link with the
constraints that I require for my task. The link personalizes the information so
that I can recieve questions that fit the difficulty and genre that I choose.
                    console.log(data)
                    flash.setAttribute('data-question', data.results[0].question)
                    flash.setAttribute('data-answer',
data.results[0].correct_answer)
                    flash.setAttribute('data-value', flash.getInnerHTML())
                })
                .then(done => flash.addEventListener('click', flashFlip)) //when
the flash is clicked it runs the function flashFlip
}) }
    genres.forEach(genre => genreAdd(genre))
    function flashFlip() {
        this.innerHTML = ''
        this.style.fontSize = '15px'
        const textDisplay = document.createElement('div')
        const trueButton = document.createElement('button')  // these three
constants set the ids for the actual Questions, the true button, and the false
button
        const falseButton = document.createElement('button')
        trueButton.innerHTML = 'True' //this is the text that shows up for the true
and false buttons
        falseButton.innerHTML = 'False'
        trueButton.classList.add('true-button') //this adds the true button and the
false button to a class
        falseButton.classList.add('false-button')
        trueButton.addEventListener('click', resultGet) //when you click each
button it runs the resultGet function
        falseButton.addEventListener('click', resultGet)
        textDisplay.innerHTML = this.getAttribute('data-question')
        this.append(textDisplay, trueButton, falseButton) //this makes the
questions and the two buttons show up on every flash
        const allCards = Array.from(document.querySelectorAll('.flash'))
        allCards.forEach(flash => flash.removeEventListener('click', flashFlip))
    }
    function resultGet() {
        const flashsAll = Array.from(document.querySelectorAll('.flash'))
        flashsAll.forEach(flash => flash.addEventListener('click', flashFlip))

        const flashButton = this.parentElement
        if (flashButton.getAttribute('data-answer') === this.innerHTML) {
            points = points + parseInt(flashButton.getAttribute('data-value'))
            displayScore.innerHTML = points //the line above parses the points so
that it is converted to a string and then it is shown on the flash with innerHTML
            flashButton.classList.add('correct-answer')
            setTimeout(() => {
                while (flashButton.firstChild) {
                    flashButton.removeChild(flashButton.lastChild)
                }
                flashButton.innerHTML = flashButton.getAttribute('data-value')
            }, 100)
        } else {
            flashButton.classList.add('wrong-answer')
            setTimeout(() => {
                while (flashButton.firstChild) {
                    flashButton.removeChild(flashButton.lastChild)
                }
                flashButton.innerHTML = 0
            }, 100)
}
        flashButton.removeEventListener('click',flashFlip)
    }
</script>
</body>
<style>
    body {
        marign: 0;
        padding: 0;
        background-color: #458c8c;
        color: #fff;
        font-family: 'Fantasy', Papyrus;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
}
#trivia {
        display: flex;
    }
    .genre-column {
        display: flex;
        flex-direction: column;
        text-align: center;
    }
    .flash {
        width: 200px;
        height: 120px;
        border-radius: 20px;
        background-color: #66ab63;
        border: solid #6a3680 5px;
        text-align: center;

        padding: 5px;
        margin: 10px;
        font-size: 100px;
}
    .correct-answer {
        background-color: #07cc00;
    }
    .wrong-answer {
        background-color: #c73b1e;
    }
    .true-button {
        background-color: #63b36e;
    }
    .false-button {
        background-color: #aa231e;
    }
button {
        margin: 10px;
    }
</style>
</html>
