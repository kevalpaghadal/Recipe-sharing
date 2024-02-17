$(document).ready(function(){
    $('#rowAdder').click(function (e) {
        e.preventDefault();
        newRowAdd = 
        '<div class="inputfield" id="row">'+
        '<input type="email" id="form3Example3" class="form-control rounded-0 border border-dark input_field" placeholder="Add Ingrediants" />'+
        '<a href=""  id="DeleteRow"><i class="fa-solid fa-xmark text-dark "></i></a> </div>';

        $('#newinput').append(newRowAdd);
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
        '<textarea type="email" id="form3Example3" class="form-control rounded-0 border border-dark input_field" placeholder="Add Step"></textarea>'+
        '<a href=""  id="DeleteRow"><i class="fa-solid fa-xmark text-dark "></i></a> </div>';

        $('#newinputstep').append(newRowAdd);
    });
})
