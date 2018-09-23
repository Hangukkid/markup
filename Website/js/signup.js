//================================== INITIALIZE DATABASE =======================================//
var config = {
    apiKey: "AIzaSyDWzM3FMAcZvL6lMvqj0o-jTvnWWa-mwb4",
    authDomain: "markup-8f904.firebaseapp.com",
    databaseURL: "https://markup-8f904.firebaseio.com",
    projectId: "markup-8f904",
    storageBucket: "markup-8f904.appspot.com",
    messagingSenderId: "794740502574"
  };
firebase.initializeApp(config);

const txtEmail = document.getElementById('txtEmail');
const txtPassword = document.getElementById('txtPassword');
const txtPassword2 = document.getElementById('txtPassword2');
const errorText = document.getElementById('errorText');
const btnSignUp = document.getElementById('btnSignUp');


//============================ SIGN IN FUNCTIONS =============================================//
btnSignUp.addEventListener('click', e => {
    errorReset();
    if (!allFieldsFilledOut()) {
        return;
    }
    if (!checkPasswordMatch()) {
        return;
    }
    const email = txtEmail.value;
    const pass = txtPassword.value;
    const auth = firebase.auth();
    //creation of user and automatic subsequent sign in
    auth.createUserWithEmailAndPassword(email, pass).catch(function (error) {
        // Handle account creation error here
        var errorCode = error.code;
        var errorMessage = error.message;
        inputErrorClassChange();
        errorText.classList.remove('hide');
        errorText.innerHTML = "Error Code: " + errorCode + "</br>Error Message: " + errorMessage;
        return;
    });
});

//add a realtime listener for whenever user logs in or out
firebase.auth().onAuthStateChanged(firebaseUser => {
    if (firebaseUser) {
        var user = firebase.auth().currentUser;
         //go to verification page
         document.location.href = "profile.html";

    }
});

function allFieldsFilledOut() {
    //check if all the fields are filled out
    var allFilledOut = true;
    if (txtEmail.value == "") {
        allFilledOut = false;
        $("#txtEmail").attr('id', 'txtEmailError');
        txtEmail.classList.add('errorBorder');
    }
    if (txtPassword.value == "") {
        allFilledOut = false;
        $("#txtPassword").attr('id', 'txtPasswordError');
        txtPassword.classList.add('errorBorder');
    }
    if (txtPassword2.value == "") {
        allFilledOut = false;
        $("#txtPassword2").attr('id', 'txtPassword2Error');
        txtPassword2.classList.add('errorBorder');
    }

    if (!allFilledOut) {
        errorText.classList.remove('hide');
        errorText.innerHTML = "Error: Please fill in all fields";
    }
    return allFilledOut;
}

function checkPasswordMatch() {
    pass1 = txtPassword.value;
    pass2 = txtPassword2.value;
    if (pass1 == pass2) {
        return true;
    } else {
        passwordErrorClassChange();
        errorText.innerHTML = "Error: Passwords Must Match";
        return false;
    }
}

//============================ HELPER VISUAL FUNCTIONS ====================================//
function errorReset() {
    $("#txtEmailError").attr('id', 'txtEmail');
    $("#txtPasswordError").attr('id', 'txtPassword');
    $("#txtPassword2Error").attr('id', 'txtPassword2');
    txtEmail.classList.remove('errorBorder');
    txtPassword.classList.remove('errorBorder');
    txtPassword2.classList.remove('errorBorder');
}

function inputErrorClassChange() {
    $("#txtEmail").attr('id', 'txtEmailError');
    $("#txtPassword").attr('id', 'txtPasswordError');
    $("#txtPassword2").attr('id', 'txtPassword2Error');

    txtEmail.classList.add('errorBorder');
    txtPassword.classList.add('errorBorder');
    txtPassword2.classList.add('errorBorder');
    errorText.classList.remove('hide');
}

function passwordErrorClassChange() {
    $("#txtPassword").attr('id', 'txtPasswordError');
    $("#txtPassword2").attr('id', 'txtPassword2Error');    
    txtPassword.classList.add('errorBorder');
    txtPassword2.classList.add('errorBorder');
    errorText.classList.remove('hide');
}
