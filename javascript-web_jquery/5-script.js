$(document).ready(function () {
    const addNewList = $('#add_item');

    addNewList.click(function () {
        const newItem = $('<li>').text('Item');

        const myList = $('ul.my_list');

        myList.append(newItem);
    });
});
