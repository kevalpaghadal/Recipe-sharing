$(document).ready(function () {
    let inputCounter = 2; // Initialize a counter for input IDs

    $('#rowAdder').click(function (e) {
        e.preventDefault();
        const newRowAdd =
            '<div class="inputfield" id="row">' +
            `<input type="text" id="ingre-${inputCounter}" name="ingre-${inputCounter}" class="form-control rounded-0 border border-dark input_field1" placeholder="Add Ingredients" />` +
            '<a href=""  id="DeleteRow"><i class="fa-solid fa-xmark text-dark "></i></a> </div>';

        $('#newinput').append(newRowAdd);
        inputCounter++; // Increment the counter for the next input field
        $('#js_inputCounter').val(inputCounter);
    });

    $("body").on("click", "#DeleteRow", function (e) {
        e.preventDefault();
        $(this).parents("#row").remove();
    })
});

$(document).ready(function () {
    let inputCounterX = 2;
    $('#textareaAdder').click(function (e) {
        e.preventDefault();
        let newRowAdd =
            '<div class="inputfield">'+
            `<textarea type="text" id="step-${inputCounterX}" name="step-${inputCounterX}" class="form-control rounded-0 border border-dark input_field1" placeholder="Add Step"></textarea>`+
            '<a href="" class="DeleteRow"><i class="fa-solid fa-xmark text-dark "></i></a> </div>';

        $('#newinputstep').append(newRowAdd);
        inputCounterX++; // Increment the counter for the next input field
        $('#js_inputCounter_step').val(inputCounterX);
    });

    // Event delegation for dynamically added elements
    $('#newinputstep').on('click', '.DeleteRow', function (e) {
        e.preventDefault();
        $(this).closest('.inputfield').remove();
    });
});

