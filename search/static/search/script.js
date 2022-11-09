$(document).ready(function () {
    $("#filterInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#pnTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});