var config = {
    apiKey: "AIzaSyDWzM3FMAcZvL6lMvqj0o-jTvnWWa-mwb4",
    authDomain: "markup-8f904.firebaseapp.com",
    databaseURL: "https://markup-8f904.firebaseio.com",
    projectId: "markup-8f904",
    storageBucket: "markup-8f904.appspot.com",
    messagingSenderId: "794740502574"
};
firebase.initializeApp(config);

const email = document.getElementById('txtEmail');

btnResetPassword.addEventListener('click', e => {
    firebase.auth().sendPasswordResetEmail(
            email.value)
        .then(function () {
            // Password reset email sent.
            alert("Please check your email!");
        })
        .catch(function (error) {
            // Error occurred. Inspect error.code.
            errorText.classList.remove('hide');
            txtEmail.classList.add('errorBorder');
            errorText.innerHTML = error;
        });
});
