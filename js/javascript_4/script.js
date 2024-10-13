const prizes = document.querySelectorAll('.prize');
const button = document.getElementById('prize__button');
let selectedPrizes = [];


function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}


function prize_click() {
    prizes.forEach(prize => {
        prize.classList.remove('active');
        prize.querySelector('.prize_result').textContent = '';
    });

    const randomIndex = getRandomInt(prizes.length);
    const selectedPrize = prizes[randomIndex];

    selectedPrize.classList.add('active');
    selectedPrize.querySelector('.prize_result').textContent = "Это ваш приз!";
}


button.addEventListener('click', prize_click);