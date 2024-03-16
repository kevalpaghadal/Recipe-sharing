// myProfile page

// myProfile page

document.addEventListener("DOMContentLoaded", function() {
    let profile_pic = document.getElementById("profile-pic");
    let input_file = document.getElementById("input-file");

    input_file.onchange = function(){
        profile_pic.src = URL.createObjectURL(input_file.files[0]);
    }
});

document.addEventListener("DOMContentLoaded", function() {
    let Recipe_pic = document.getElementById("input-img");
    let Recipe_input_file = document.getElementById("upload-img");

    Recipe_input_file.onchange = function(){
        Recipe_pic.src = URL.createObjectURL(Recipe_input_file.files[0]);
    }
});
