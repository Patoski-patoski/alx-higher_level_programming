/**
*  a JavaScript script that fetches the character name from this URL:
*  https://swapi-api.alx-tools.com/api/people/5/?format=json
* The name must be displayed in the HTML tag DIV#character
* You can’t use document.querySelector to select the HTML tag
* You must use the JQuery API
*/

$(document).ready(() => {
    const url = "https://swapi-api.alx-tools.com/api/people5/?format=json"
    $.ajax({
        url: url,
        type: "GET",
        success: data => {
            $("#character").text(data.name);
        },
        error: (xhr, texStatus, error) => {
            console.error(error);
        }
    })
});
