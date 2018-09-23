var config = {
    apiKey: "AIzaSyDWzM3FMAcZvL6lMvqj0o-jTvnWWa-mwb4",
    authDomain: "markup-8f904.firebaseapp.com",
    databaseURL: "https://markup-8f904.firebaseio.com",
    projectId: "markup-8f904",
    storageBucket: "markup-8f904.appspot.com",
    messagingSenderId: "794740502574"
};
firebase.initializeApp(config);

var doc = new jsPDF()
var listexists = false;
var questionArray = [];
var input_title = document.getElementById("input_title");
var input_question = document.getElementById("input_question");
var input_choices = document.getElementById("input_choices");
var input_answer = document.getElementById("input_answer");


function Question(question, choices, answer) {
    this.question = question;
    this.choices = choices;
    this.answer = answer;
    this.delete = function () {
        this.question = "";
        this.choices = "";
        this.answer = "";
        resetDiv();
        printQuestions();
    }
}

$("#btnAddQuestion").click(function () {
    addQuestion();
});

$("#submitbtn").click(function () {
    createPDF();
});

function addQuestion() {
    var newQuestion = new Question(input_question.value, input_choices.value, input_answer.value);
    questionArray.push(newQuestion);
    if (listexists) resetDiv();
    printQuestions();
    listexists = true;
}

function resetDiv() {
    $("#curTest").html("");
}

function printQuestions() {
    for (var i = 0; i < questionArray.length; i++) {
        if (questionArray[i].question == "") questionArray.splice(i, 1);
    }


    for (var i = 0; i < questionArray.length; i++) {
        if (questionArray[i].question != "") {
            $("#curTest").append("<h1><strong>Question " + (i + 1) + ": </strong>" + questionArray[i].question + "</h1>");
            if (questionArray[i].choices != "") $("#curTest").append("<h1><strong>Choices: </strong>" + questionArray[i].choices + "</h1>");
            $("#curTest").append("<h1><strong>Answer: </strong>" + questionArray[i].answer + "</h1>");
            $('#curTest').append("<button onclick = 'questionArray[" + i + "].delete()'>Delete Question " + (i + 1) + "</button><br>");
        }
    }
}

function createPDF() {
    /*  4 questions per page
        first page heights are 50, 110, 170, 230
        other page heights are 30, 90, 150, 210
        +5 height for new line for text
        roughly 80 characters available per line
        lines start +5 rectange height*/

    //initial title
    doc.setFontSize(30)
    doc.rect(10, 32, 190, 12);
    doc.text(11, 40, input_title.value);

    //drawing of rectangle
    var qcount = 0;
    firstPage = true;
    for (var i = 0; i < questionArray.length; i++) {
        if (qcount == 0) {
            if (!firstPage) {
                doc.addPage();
            }
            doc.setFontSize(18);
            doc.rect(140, 10, 60, 10);
            doc.text(141, 15, 'Name:');
        }
        var base_height = 0;
        if (firstPage) {
            if (qcount == 0) {
                base_height = 50;
            } else if (qcount == 1) {
                base_height = 110;
            } else if (qcount == 2) {
                base_height = 170;
            } else if (qcount == 3) {
                base_height = 230;
            }
        } else {
            if (qcount == 0) {
                base_height = 30;
            } else if (qcount == 1) {
                base_height = 90;
            } else if (qcount == 2) {
                base_height = 150;
            } else if (qcount == 3) {
                base_height = 210;
            }
        }

        doc.rect(10, base_height, 190, 50);

        //separating string
        var stringArray = [];
        var curStr = questionArray[i].question
        var index = 0;
        var start = 0;
        var count = 0;
        for (var j = 0; j < curStr.length; j++) {
            if (count > 110 && curStr[j] == " ") {
                console.log(count);
                console.log(start);
                console.log(j);
                stringArray[index] = curStr.substring(start, j);
                index++;
                start = j + 1;
                count = 0;
            }
            if (j == (curStr.length - 1)) {
                stringArray[index] = curStr.substring(start);
            }
            count++;
        }

        var newHeight = base_height + 5;
        //printing of question
        for (var j = 0; j < stringArray.length; j++) {
            doc.setFontSize(10);
            if(j==0){
                var tempStr = "Q" + i +": " + stringArray[j];
                console.log(tempStr);
                doc.text(12, newHeight, tempStr);
                newHeight += 5;
            }else{
                doc.text(12, newHeight, stringArray[j]);
                newHeight += 5;
            }
        }

        //printing of choices if applicable
        var choiceStr = questionArray[i].choices;
        var choiceArray = [];
        choiceStr = choiceStr.replace(/ /g, "");
        var cStart = 0;
        var cIndex = 0;
        for (var j = 0; j < choiceStr.length; j++) {
            if (choiceStr[j] == ",") {
                choiceArray[cIndex] = choiceStr.substring(cStart, j);
                cStart = j + 1;
                cIndex++;
            }
            if (j == choiceStr.length - 1) {
                choiceArray[cIndex] = choiceStr.substr(cStart);
            }
        }
        for (var j = 0; j < choiceArray.length; j++) {
            var tempStr = String.fromCharCode(65 + j) + ") "+ choiceArray[j]
            doc.text(12, newHeight, tempStr);
            newHeight += 5;
        }

        //increment and check for new page reset
        qcount++;
        if (qcount == 4) {
            qcount = 0;
            firstPage = false;
        }
    }
    doc.save('test.pdf')
    postContent();
}

function postContent() {

    var jsonQArray = [];
    
    for (var i = 0; i < questionArray.length; i++) {
        var jsonQuestion = {
            question: questionArray[i].question,
            choices: questionArray[i].choices,
            answer: questionArray[i].answer
        };
        jsonQArray[i] = jsonQuestion;
    }

    var testName = input_title.value;

    var email = firebase.auth().currentUser.email;
    $.ajax({
        method: "POST",
        crossDomain: true,
        dataType: 'json',
        url: "http://10.24.181.158:2567/ParseAnswer/",
        data: JSON.stringify({
            email: [email],
            [testName]: jsonQArray
        })
    }).fail(function (XHR, error, code) {
        console.log("fail: " + error + code);
    }).done(function (data) {
        jsonObj = JSON.parse(data);
        console.log(jsonObj);
    });

};
