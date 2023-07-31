// Global Variables
// Creating Error Element
let error = $('<p class="error"></p>');
// Creating Verify field
let html = 
        `<div class="placeholder hint code">
            <input type="text" id="code" name="code" class="input" autocomplete="off" required pattern=".*">
        </div>`; 
// https://www.ocpsoft.org/tutorials/regular-expressions/password-regular-expression/
// https://stackoverflow.com/questions/19605150/regex-for-password-must-contain-at-least-eight-characters-at-least-one-number-a
let passPattern = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/
let userPattern = /^(?!.*?[0-9])(?!.*?[#?!@$%^&*-]).{2,}$/
let emailPattern = /[a-z]*_[0-9]*@fci.helwan.edu.eg/


// Functions to be used
function patternCheck(word, pattern){
    return pattern.test(word);
}

function fieldCheck(ele, name, func, pattern, msg){
    let text = ele.value;
    let error = $('<p class="error"></p>');
    $(`.${name} .error`).remove();
    // Remove func and variable and put the pattern check
    if (func(text, pattern)){
        $(`.${name} .error`).remove();
        return true;
    }
    else{
        $(`.${name}`).prepend(error.text(msg));
    }
    return false;
}

function databaseCheck(ele, name){
    let text = ele.value;
    let error = $('<p class="error"></p>');
    let msg = `${name} is already taken!`;
    return true
    // $.getJSON(
    //     '{% url "login:check" %}',
    //     {name : text},
    //     (result) => {
    //         // Should return Boolean [if it does not work, edit it to return value as dict]
    //         if (result){
    //             $(`.${name}`).prepend(error.text(msg));
    //         }
    //         else{
    //             $(`.${name} .error`).remove();
    //         }
    //     }
    
    // )

}

function passwordConfirm(pass_confirm, pass){
    let error = $('<p class="error"></p>');
    let msg = 'Password does not match!'
    $('.confirm .error').remove()
    if (pass_confirm.value == pass.value){
        $('.confirm .error').remove()
    }
    else{
        $('.confirm').prepend(error.text(msg))
    }
}

//-------------------------------------------------
$('document').ready( function(){
    // Get Input Fields First
    let user = document.getElementById('username');
    let email = document.getElementById('email');
    let pass = document.getElementById('password');
    let CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
    let pass_confirm = document.getElementById('password-confirm');
    let code_number;


    // Validation
    // Username Check
    $('#username').blur(()=>{
        let val = fieldCheck(user, 'username', patternCheck, userPattern, 'Username must be alphabetic charaters only & more than 2 characters');
        if (val){
            databaseCheck(user, 'username')
        }
    })

    // Password Check
    $('#password').blur( ()=>{
        fieldCheck(pass, 'password:nth-of-type(3)', patternCheck, passPattern, 'Enter 8 characters or more, including special characters');
    })

    // Email Checking
    $('#email').blur( ()=>{
        let val = fieldCheck(email, 'email:nth-of-type(2)', patternCheck, emailPattern, 'Enter Your edu mail of computer science faculty');
        if (val){
            databaseCheck(user, 'username')
        }
    })

    // Confriming Password
    $('#password-confirm').blur(()=>{
        passwordConfirm(pass_confirm, pass);
    })
    $('#password').change(()=>{
        if ($('#password-confirm').val().length)
        {
            passwordConfirm(pass_confirm, pass);
        }
    })

    // Submission
    $('.blue-btn').click( (e)=>{
        let msg = 'Choose one of below options!'
        $('.gender .error').remove();
        $('form > .error').remove();
        // Check Gender Value (Do not trust client)
        if (!['male', 'female'].includes($('#gender').val())){
            $('.gender').prepend(error.text(msg));
            // e.preventDefault();
            // return false;   
        }
        msg = 'Please Enter all fields correctly before submit!'
        // Check all fields again (Do not trust client)
        if ($('.error').length){
            $('.username').before(error.text(msg));
            // e.preventDefault();
            // return false;
        }
        // Sent a JSON request to Django to sent a verification code by email 
        // Get the code in the browser as a response for checking

        // code_number = 30112003; // Response simulation
        // Remove Form of register and add below so user can enter that code
        // $('.placeholder').remove();
        // $('.blue-btn').remove();
        // $('form').append(html);
        // //Verify Code
        // $('#code').on('change paste keyup', ()=>{
        //     if ($('#code').val().length === 8){
        //         console.log("8 Length");
        //         if (+$('#code').val() === code_number){
        //             // Redirect POST With Data
        //             $.post(
        //                 '{% url "login:signup" %}',
        //                 {
        //                     'username' : user.value,
        //                     'email' : email.value,
        //                     'password' : pass.value,
        //                     'csrfmiddlewaretoken': CSRFtoken
        //                 }
        //             )
        //             console.log("True")
        //         }
        //     }
        // })
    })

   
})
