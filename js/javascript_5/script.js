document.addEventListener("DOMContentLoaded", () => {
    const road = document.querySelector(".road");
    road.style.border = "2px solid black";
    
    const roadElements = document.querySelectorAll('.road > div');
    const buttons = document.querySelectorAll('.buttons button'); 
    const white = document.querySelectorAll('.white_color');

    roadElements.forEach((element) => {
        if (element.classList.contains('black_color')) {
            element.style.backgroundColor = 'black';
        }
    });

    buttons[0].addEventListener('click', function() {
        white.forEach((element) => {
            element.innerHTML = '';

            let image = document.createElement('IMG');
            image.src = 'up.svg';

            element.append(image);
        });
    });

    buttons[1].addEventListener('click', function() {
        white.forEach((element) => {
            element.innerHTML = ''; 

            let image = document.createElement('IMG');

            image.src = 'up.svg';
            image.style.transform = 'rotate(180deg)';

            element.append(image);
        });
    });
});