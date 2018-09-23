var config = {
    apiKey: "AIzaSyDWzM3FMAcZvL6lMvqj0o-jTvnWWa-mwb4",
    authDomain: "markup-8f904.firebaseapp.com",
    databaseURL: "https://markup-8f904.firebaseio.com",
    projectId: "markup-8f904",
    storageBucket: "markup-8f904.appspot.com",
    messagingSenderId: "794740502574"
};
firebase.initializeApp(config);
var googleprovider = new firebase.auth.GoogleAuthProvider();
var fbprovider = new firebase.auth.FacebookAuthProvider();

// Get elements for later usage
const txtEmail = document.getElementById('txtEmail');
const txtPassword = document.getElementById('txtPassword');
const btnLogin = document.getElementById('btnLogin');
const errorText = document.getElementById('errorText');

//Add login event 
btnLogin.addEventListener('click', e => {
    //get email and pass
    const email = txtEmail.value;
    const pass = txtPassword.value;
    const auth = firebase.auth();
    //Sign in
    auth.signInWithEmailAndPassword(email, pass).catch(function (error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        inputErrorClassChange();
        errorText.classList.remove('hide'); //error code removed on successful login
        errorText.innerHTML = "Error Code: " + errorCode + "</br>Error Message: " + errorMessage;
        resetPassword.classList.remove('hide');
    });
});

/*googleSignIn.addEventListener('click', e => {
     firebase.auth().signInWithPopup(googleprovider).then(function (result) {
         // This gives you a Google Access Token. You can use it to access the Google API.
         var token = result.credential.accessToken;
         // The signed-in user info.
         var user = result.user;
         //...
     }).catch(function (error) {
         // Handle Errors here.
         var errorCode = error.code;
         var errorMessage = error.message;
         // The email of the user's account used.
         var email = error.email;
         // The firebase.auth.AuthCredential type that was used.
         var credential = error.credential;
         // ...
         console.log(errorCode);
         console.log(errorMessage);
     });
 });

 fbSignIn.addEventListener('click', e => {
     firebase.auth().signInWithPopup(fbprovider).then(function (result) {
         // This gives you a Facebook Access Token. You can use it to access the Facebook API.
         var token = result.credential.accessToken;
         // The signed-in user info.
         var user = result.user;
         // ...
     }).catch(function (error) {
         // Handle Errors here.
         var errorCode = error.code;
         var errorMessage = error.message;
         // The email of the user's account used.
         var email = error.email;
         // The firebase.auth.AuthCredential type that was used.
         var credential = error.credential;
         // ...
     });
 });*/


btnSignUp.addEventListener('click', e => {
    document.location.href = "signup.html";
});

//add a realtime listener for whenever user logs in or out
firebase.auth().onAuthStateChanged(firebaseUser => {
    if (firebaseUser) { //user is signed in/signs in
        var user = firebase.auth().currentUser;
        if (user != null) {
            user.reload();

            //forward to logged in page if email verified
            document.location.href = "profile.html";

        }
    }
});

//------------helper visual functions -------//
function inputErrorClassChange() {
    txtEmail.classList.add('errorBorder');
    txtPassword.classList.add('errorBorder');
    errorText.classList.remove('hide');
}
