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
    const $translateButton = $("INPUT#btn_translate");
    const $languageCodeInput = $("INPUT#language_code");
    const $helloDiv = $("DIV#hello");

    const fetchTranslation = () => {
        const languageCode = $languageCodeInput.val();
        const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

        $.ajax({
            url: url,
            type: "GET",
            success: (data) => {
                if (data.code) {
                    $helloDiv.text(data.hello);
                }
            },
            error: (xhr, textStatus, error) => {
                console.error(error);
            }
        });
    };

    $translateButton.on('click', fetchTranslation);
    $languageCodeInput.on('keydown', fetchTranslation);
});
