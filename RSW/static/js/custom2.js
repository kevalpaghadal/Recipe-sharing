

// profile photo logic

document.addEventListener("DOMContentLoaded", function() {
    let profile_pic = document.getElementById("profile-pic");
    let input_file = document.getElementById("input-file");

    input_file.onchange = function(){
        profile_pic.src = URL.createObjectURL(input_file.files[0]);
    }
});


// add recipe photo logic

document.addEventListener("DOMContentLoaded", function() {
    let Recipe_pic = document.getElementById("input-img");
    let Recipe_input_file = document.getElementById("upload-img");

    Recipe_input_file.onchange = function(){
        Recipe_pic.src = URL.createObjectURL(Recipe_input_file.files[0]);
    }
});



// social sharing logic
function shareOnFacebook(url) {
    window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url), '_blank');
}

function shareOnTwitter(url, title) {
    window.open('https://twitter.com/intent/tweet?url=' + encodeURIComponent(url) + '&text=' + encodeURIComponent(title), '_blank');
}

function shareOnWhatsApp(url, title) {
    window.open('whatsapp://send?text=' + encodeURIComponent(title + ': ' + url), '_blank');
}
