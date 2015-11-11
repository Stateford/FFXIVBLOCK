//Window close

$(document).ready(function() {
    $('#lmaook').click(function() {
        $('.output').addClass('hidden');
        $('#output').text('');
    });
});




//Clear

$(document).ready(function() {
    $('#reset').click(function(){
        $('.output').addClass('hidden');
        $('#output').text('');
    });
});



// BLOCK DICTIONARY

var ffxiv = {
    a: '',
    b: '',
    c: '',
    d: '',
    e: "",
    f: '',
    g: '',
    h: '',
    i: "",
    j: '',
    k: '',
    l: '',
    m: '',
    n: '',
    o: '',
    p: '',
    q: '',
    r: '',
    s: '',
    t: '',
    u: '',
    v: '',
    w: '',
    x: '',
    y: '',
    z: ''
};

// TRANSLATOR STUFF


var final = '';
var getinput2 = $('#translator').val();




// TRANSLATOR ACTION
$(document).ready(function() {
    $('#submit').click(function() {
            var getinput = $('#translator').val();
            $('#output').text('');
            final = '';
            for (var i = 0; i < getinput.length; i++) {
                var midway = ffxiv[getinput.charAt(i)]
                final = final + midway;
            }
            $('.output').removeClass('hidden');
            $('#output').text(final);
        });
});
