$(document).ready(function() {

    $('#id_toppings_options').on('change', function() {

        var select_val = $("select[name=toppings_options").val();

        if (select_val === '1') {
            // If "1" is hidden
            if ($("#1top").is(":hidden") === true) {
                $("#1top").toggle();
            }
            // If "2" and "3" are displayed
            if ($("#2top").is(":visible") === true) {
                $("#2top").toggle();
                
            }
            if ($("#3top").is(":visible") === true) {
                $("#3top").toggle();
            }
            // Reset toppings form 2 and 3
            $('.topping2').val("");
            $('.topping3').val("");
        }

        else if (select_val === '2') {
            // If "2" is hidden, show it
            if ($("#2top").is(":hidden") === true) {
                $("#2top").toggle();
            }
            // If "1" is hidden
            if ($("#1top").is(":hidden") === true) {
                $("#1top").toggle();
            }
            // If "3" displays, hide it
            if ($("#3top").is(":visible") === true) {
                $("#3top").toggle();
            }
            // Reset toppings form 3
            $('.topping3').val("");
        }

        else if (select_val === '3') {
            // If "3" is hidden
            if ($("#3top").is(":hidden") === true) {
                $("#3top").toggle();
            }
            // If other are hidden too
            if ($("#1top").is(":hidden") === true) {
                $("#1top").toggle();
            }
            if ($("#2top").is(":hidden") === true) {
                $("#2top").toggle();
            }
        }

        // For "Cheese" and "Special"
        else {
            if ($("#1top").is(":visible") === true) {
                $("#1top").toggle();
            }
            if ($("#2top").is(":visible") === true) {
                $("#2top").toggle();
            }
            if ($("#3top").is(":visible") === true) {
                $("#3top").toggle();
            }
            // Reset all
            $('.topping1').val("");
            $('.topping2').val("");
            $('.topping3').val("");
        }
    })
})