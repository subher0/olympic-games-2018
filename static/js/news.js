window.addEventListener('load', () => {
    let cardDeck = document.querySelector('.card-deck');
    let cards = document.querySelectorAll('.card');
    let cardCount = cards.length;

    for (let i = 0; i < (3 - cards.length % 3) % 3; i++) {
        let emptyCard = document.createElement('div');
        emptyCard.setAttribute('class', 'card hidden');
        cardDeck.appendChild(emptyCard);
    }
});