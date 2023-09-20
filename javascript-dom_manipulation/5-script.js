const NewHeader = document.getElementById('update_header')

NewHeader.addEventListener('click', function ChangingHeader() {
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!'


})
