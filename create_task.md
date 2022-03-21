{% include navigation.html %}
## [Video](https://www.loom.com/share/944719199555433e860f734f174e48fd)

## Prompts
3a)
* i. The overall purpose of my program is to simulate a trivia/jeopardy style game where users can choose their difficulty level and answer a random question.
* ii. In the video, I demonstrate the entire program, as I go through each difficulty and how the score updates.
* iii. The input of the program is when the user chooses a genre and a specific difficulty question that they desire. When the choose it, the output is the question being displayed. Another input is when the user chooses true or false and the output for that would be when the question is scored and the necessary points are added to the total.

3b)
* i. `const genres = [
             {
                 name: 'Books',
                id: 10
             },
             {
                 name: 'Film',
                 id: 11
             },
             {
                 name: 'Music',
                 id: 12
             },
             {
                 name: 'Video Games',
                 id: 15
             }
         ]`
 `        const levels = ['easy', 'medium', 'hard']`
* ii. `function addGenre(genre) {
             const column = document.createElement('div')
             column.classList.add('genre-column')
             column.innerHTML = genre.name
             game.append(column)`

             `levels.forEach(level => {
                 const card = document.createElement('div')
                 card.classList.add('card')
                 column.append(card)

                 if (level === 'easy') {
                     card.innerHTML = 100
                 }
                 if (level === 'medium') {
                     card.innerHTML = 200
                 }
                 if (level === 'hard') {
                     card.innerHTML = 300
                 }`
* iii. The list this response is about is the levels lists.
* iv. The data contained in this list represents the different difficulty levels in the questions. There is an easy, medium, and hard item which corresponds to the point values of the questions which increase with difficulty.
* v. If I didn't use this list, then the program would function very differently as there wouldn't be different point value awarded for different questions. This list allows for the classification of different questions so that the program knows what point values to give for a question and without it, all the questions would be worth the same.

3c)
* i. `function getResult() {
            const allCards = Array.from(document.querySelectorAll('.card'))
            allCards.forEach(card => card.addEventListener('click', flipCard))`

            `const cardOfButton = this.parentElement
            if (cardOfButton.getAttribute('data-answer') === this.innerHTML) {
                score = score + parseInt(cardOfButton.getAttribute('data-value'))
                scoreDisplay.innerHTML = score
                cardOfButton.classList.add('correct-answer')
                setTimeout(() => {
                    while (cardOfButton.firstChild) {
                        cardOfButton.removeChild(cardOfButton.lastChild)
                    }
                    cardOfButton.innerHTML = cardOfButton.getAttribute('data-value')
                }, 100)
            } else {
                cardOfButton.classList.add('wrong-answer')
                setTimeout(() => {
                    while (cardOfButton.firstChild) {
                        cardOfButton.removeChild(cardOfButton.lastChild)
                    }
                    cardOfButton.innerHTML = 0
                }, 100)
            }
            cardOfButton.removeEventListener('click',flipCard)
        }`
* ii. `trueButton.addEventListener('click', getResult)
            falseButton.addEventListener('click', getResult)`
* iii. Overall, what the procedure does is that is updates the score value based on the correct and incorrect answers. When a question is correct, you are awarded those points, when it is incorrect, you are given no points.
* iv. First, I set the constant allCards so that is assigned to the array from cards. Then it goes through each item in that array and then it runs the flip card function when it is clicked. Then I created the constant cardOfButton and set it to a parent Element. Next, I created an if-else function where it first goes through and checks if a question is right, and if it is, it adds points to the score value. The else portion goes through and makes sure that no points are added for incorrect answers.

3d)
* i. The first call is when the true button is clicked. When the true button is clicked and the answer is correct, points are added. Same with when the false button is clicked and the answer is correct. THe second call is when those buttons are pressed and the answer is incorrect, in which case no points are added.
* ii. The conditions tested by the first call is if the answer chosen matched what is already in the database. The condition tested by the second call is if the answer chosen doesn't match the answer in the database.
* iii. The result of the first call is that points are added. The result of the second call is that no points are added.
