$(document).ready(function () {
    $(".select-left").on("change", function () {
        swapLeft();
    });

    $(".select-right").on("change", function () {
        swapRight();
    });

    $("#unit-select").on("change", function () {
        hideUnits();
        $("#unit-" + $(this).val()).show();
        convert();
    });

    $(".text-left").on("input", function () {
        convert();
    });

    $(".text-right").on("input", function () {
        $("#text-left-" + $("#unit-select").val()).val($("#text-right-" + $("#unit-select").val()).val() * $("#left-" + $("#unit-select").val()).val() / $("#right-" + $("#unit-select").val()).val());
    });

    $("#filterInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#pnTable tr").filter(function () {
            var cond = $(this).text().toLowerCase().indexOf(value) > -1;
            $(this).toggle(cond);
            if (cond) {
                $(this).addClass("filtered");
            }
            else {
                $(this).removeClass("filtered");
            }
        });
        getPagination('#table-id');
    });
});

getPagination('#table-id');
hideUnits();
$("#unit-0").show();
var left = $("#left-" + $("#unit-select").val()).val();
var right = $("#right-" + $("#unit-select").val()).val();

function hideUnits() {
    $("#unit-0, #unit-1, #unit-2, #unit-3, #unit-4").hide();
}

function swapLeft() {
    var temp = $("#left-" + $("#unit-select").val()).val();
    if (temp == right) {
        $("#left-" + $("#unit-select").val()).val(right);
        $("#right-" + $("#unit-select").val()).val(left);
        right = $("#right-" + $("#unit-select").val()).val();
    }
    left = $("#left-" + $("#unit-select").val()).val();
    convert();
}

function swapRight() {
    var temp = $("#right-" + $("#unit-select").val()).val();
    if (temp == left) {
        $("#left-" + $("#unit-select").val()).val(right);
        $("#right-" + $("#unit-select").val()).val(left);
        left = $("#left-" + $("#unit-select").val()).val();
    }
    right = $("#right-" + $("#unit-select").val()).val();
    convert();
}

function convert() {
    $("#text-right-" + $("#unit-select").val()).val($("#text-left-" + $("#unit-select").val()).val() * $("#right-" + $("#unit-select").val()).val() / $("#left-" + $("#unit-select").val()).val());
}

function getPagination(table) {
    var lastPage = 1;

    $('#maxRows').on('change', function (evt) {
        lastPage = 1;
        $('.pagination')
            .find('li')
            .slice(1, -1)
            .remove();
        var trnum = 0;
        var maxRows = parseInt($(this).val());

        if (maxRows == 5000) {
            $('.pagination').hide();
        } else {
            $('.pagination').show();
        }

        var totalRows = $(table + ' tbody tr.filtered').length;
        $(table + ' tr.filtered').each(function () {
            trnum++;
            if (trnum > maxRows) {
                $(this).hide();
            }
            if (trnum <= maxRows) {
                $(this).show();
            }
        });
        if (totalRows <= maxRows) {
            $('.pagination li').hide();
            return;
        }
        if (totalRows > maxRows) {
            var pagenum = Math.ceil(totalRows / maxRows);
            for (var i = 1; i <= pagenum;) {
                $('.pagination [data-page="next"]')
                    .before(
                        '<li class="page-item" data-page="' + i + '"><a class="page-link link-dark">' + i++ + '</a> </li>'
                    )
                    .show();
            }
        }
        $('.pagination [data-page="1"]').addClass('active');
        $('.pagination li').on('click', function (evt) {
            evt.stopImmediatePropagation();
            evt.preventDefault();
            var pageNum = $(this).attr('data-page');
            var maxRows = parseInt($('#maxRows').val());

            if (pageNum == 'prev') {
                if (lastPage == 1) {
                    return;
                }
                pageNum = --lastPage;
            }
            if (pageNum == 'next') {
                if (lastPage == $('.pagination li').length - 2) {
                    return;
                }
                pageNum = ++lastPage;
            }

            lastPage = pageNum;
            var trIndex = 0;
            $('.pagination li.active').removeClass('active');
            $('.pagination [data-page="' + lastPage + '"]').addClass('active');
            limitPagging();
            $(table + ' tr.filtered').each(function () {
                trIndex++;
                if (
                    trIndex > maxRows * pageNum ||
                    trIndex <= maxRows * pageNum - maxRows
                ) {
                    $(this).hide();
                } else {
                    $(this).show();
                }
            });


            if (lastPage == 1) {
                $('.pagination [data-page="prev"]').addClass('disabled');
                return;

            }
            else if (lastPage == $('.pagination li').length - 2) {
                $('.pagination [data-page="next"]').addClass('disabled');
                $('.pagination [data-page="prev"]').removeClass('disabled');
            }
            else {
                $('.pagination [data-page="prev"]').removeClass('disabled');
                $('.pagination [data-page="next"]').removeClass('disabled');
            }
        });
        limitPagging();
    })
        .val(10)
        .change();
}

function limitPagging() {
    if ($('.pagination li').length > 11) {
        if ($('.pagination li.active').attr('data-page') >= $('.pagination li').length - 5) {
            console.log($('.pagination li').length);
            $('.pagination li').hide();
            $('.pagination li:lt(1)').show();
            $('.pagination li').slice(-10).show();
        }
        else if ($('.pagination li.active').attr('data-page') <= 5) {
            $('.pagination li:gt(9)').hide();
            $('.pagination li:lt(9)').show();
            $('.pagination [data-page="next"]').show();
        }
        else if ($('.pagination li.active').attr('data-page') > 5) {
            $('.pagination li:gt(0)').hide();
            $('.pagination [data-page="next"]').show();
            for (let i = (parseInt($('.pagination li.active').attr('data-page')) - 4); i <= (parseInt($('.pagination li.active').attr('data-page')) + 4); i++) {
                $('.pagination [data-page="' + i + '"]').show();
            }
        }
    }
}

