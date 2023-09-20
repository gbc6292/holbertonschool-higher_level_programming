const togglesheader = document.getElementById('toggle_header')

togglesheader.addEventListener('click', function addRedClassToHeader() {
    const header = document.querySelector('header')
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    }
    else {
        header.classList.remove('green');
        header.classList.add('red');
    }
})
