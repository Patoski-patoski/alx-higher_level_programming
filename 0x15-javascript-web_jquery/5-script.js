$(document).ready(() => {
    $("#add_item").click(() => {
        let new_list = $("<li>Item</li>");
        $("ul.my_list").append(new_list);
    });
});
