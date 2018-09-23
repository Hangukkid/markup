var config = {
    apiKey: "AIzaSyDWzM3FMAcZvL6lMvqj0o-jTvnWWa-mwb4",
    authDomain: "markup-8f904.firebaseapp.com",
    databaseURL: "https://markup-8f904.firebaseio.com",
    projectId: "markup-8f904",
    storageBucket: "markup-8f904.appspot.com",
    messagingSenderId: "794740502574"
};
firebase.initializeApp(config);

const toptext = document.getElementById('toptext');

btnCreate.addEventListener('click', e => {
    document.location.href = "create.html"
})


firebase.auth().onAuthStateChanged(firebaseUser => {
    if (firebaseUser) {
        //user is signed in/signs in
        changename();
    } else {
        //user signs out
        document.location.href = "login.html";
    }
});

function changename() {
    var user = firebase.auth().currentUser;
    toptext.innerHTML = "Welcome to MarkUp,</br>" + user.email;
    //getContent(user.email);
}

navbarLogout.addEventListener('click', e => {
    firebase.auth().signOut();
})

btnMark.addEventListener('click', e=>{
    document.location.href = "mark.html"
})
//=====================update table=========================//

var receivedData;
var jsonObj;
var iconObj;
var myTable = document.getElementById('iconTable');

function getContent(email){

    var jsonQuestion = {
        question: "",
        choices: "",
        answer: ""
    };

    var jsonQArray = [];
    
    

    var email = firebase.auth().currentUser.email;
    $.ajax({
        method: "POST",
        crossDomain: true,
        dataType: 'json',
        url: "10.24.181.158:2567/ParseAnswers/",
        data: JSON.stringify({
            [email]: markers
        })
    });

    alert("done");
    
    /*$.ajax({
        method: "POST",
        crossDomain: true,
        url: "http://www.arnocular.org/AddIcons/",
        data: email,
    }).fail(function (XHR, error, code) {
        console.log("fail: " + error + code);
    }).done(function (data) {
        jsonObj = JSON.parse(data);
        console.log(jsonObj);
    });*/
};

