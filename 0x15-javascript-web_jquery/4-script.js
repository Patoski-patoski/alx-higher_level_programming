$(document).ready(function () {
    $("#toggle_header").click(() => {
        if ($("header").hasClass("green"))
            $("header").removeClass("green").addClass("red")

        else
            $("header").addClass("green");
    })
});
