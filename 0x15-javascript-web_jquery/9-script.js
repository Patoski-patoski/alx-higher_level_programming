/**
* Write a JavaScript script that fetches from
* https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello
* from that fetch in the HTML tag DIV#hello.

* The translation of "hello" must be displayed in the HTML
* tag DIV#hello
* You can’t use document.querySelector to select the HTML tag
* You must use the JQuery API
* Your script must work when it is imported from the <head> tag
*
**/

$(function () {
    const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    let $hello = $("#hello");

    $.ajax({
        url: url,
        type: "GET",
        success: (data) => {
            $hello.text(data.hello);
        },
        error: (xhr, textStatus, error) => {
            if (error) {
                console.error(error);
                console.error(textStatus);
                process.exit;
            }
        },
    })
});
