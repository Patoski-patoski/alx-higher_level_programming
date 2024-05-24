/**
* Write a JavaScript script that fetches and prints how to say "Hello"
* depending on the language

* You should use this API service:
* https://www.fourtonfish.com/hellosalut/hello/
* The language code will be the value entered in the tag INPUT#language_code
* (ex: es, fr, en etc.)
* The translation must be fetched when the user clicks on INPUT#btn_translate
* The translation of "Hello" must be displayed in the HTML tag DIV#hello
* You can't use document.querySelector to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the <head> tag
**/

$(function () {
    $("INPUT#btn_translate").click(() => {
        const $codeValue = $("INPUT#language_code").val();
        const url = `https://hellosalut.stefanbohacek.dev/?lang=${$codeValue}`;

        $.ajax({
            url: url,
            type: "GET",
            success: data => {
                if (data.code)
                    $("DIV#hello").text(data.hello);
            },
            error: (xhr, textStatus, error) => {
                if (error)
                    console.error(error);
            },
        })
    })
});
