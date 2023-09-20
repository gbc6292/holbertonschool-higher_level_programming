const redheader = document.getElementById('red_header')

redheader.addEventListener('click', function addRedClassToHeader() {
    const header = document.querySelector('header');
    header.classList.add("red");
})
