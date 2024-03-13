$(document).ready(function(){
    let inputCounter = 3; // Initialize a counter for input IDs
    
    $('#rowAdder').click(function (e) {
        e.preventDefault();
        const newRowAdd = 
        '<div class="inputfield" id="row">'+
        `<input type="text" id="ingre-${inputCounter}" name="ingre-${inputCounter}" class="form-control rounded-0 border border-dark input_field" placeholder="Add Ingredients" />`+
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

$(document).ready(function (){
    $('#textareaAdder').click(function (e) {
        e.preventDefault();
        newRowAdd = 
        '<div class="inputfield" id="row">'+
        '<textarea type="text" name="step" class="form-control rounded-0 border border-dark input_field" placeholder="Add Step"></textarea>'+
        '<a href=""  id="DeleteRow"><i class="fa-solid fa-xmark text-dark "></i></a> </div>';

        $('#newinputstep').append(newRowAdd);
    });
})
