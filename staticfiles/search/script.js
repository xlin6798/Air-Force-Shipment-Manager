$(document).ready(function () {
    $("#filterInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#pnTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

function openNav(eid) {
    document.getElementById(eid).style.width = "400px";
}

function closeNav(eid) {
    document.getElementById(eid).style.width = "0";
}