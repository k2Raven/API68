function onButtonClick(url) {
    let inputA = $('#A').val();
    let inputB = $('#B').val();
    $.ajax({
        url:`http://localhost:8000/api/v1/${url}`,
        method:'POST',
        dataType:'json',
        contentType: 'application/json',
        data: JSON.stringify({"A": inputA, "B": inputB}),
        success: function (response, status) {
            console.log(response);
            console.log(status);
            answer('success',response)
        },
        error: function (response) {
            console.log(response);
            answer('error',response)
        }
    });
}

let answerAB = document.getElementById('answer');

function answer(ans, rasponse){
    if (ans!== 'error'){
        answerAB.innerHTML= `Answer <span style="color: green">${rasponse.answer}</span>`
    }
    else {
        answerAB.innerHTML= `Answer <span style="color: red">${rasponse.responseJSON.error}</span>`
    }
}
let buttonAdd =document.getElementsByName('add')[0];
let buttonSubtract =document.getElementsByName('subtract')[0];
let buttonMultiply =document.getElementsByName('multiply')[0];
let buttonDivide =document.getElementsByName('divide')[0];


buttonAdd.addEventListener('click', function () {
        onButtonClick('add/')
});
buttonSubtract.addEventListener('click', function () {
        onButtonClick('subtract/')
});
buttonMultiply.addEventListener('click', function () {
        onButtonClick('multiply/')
});
buttonDivide.addEventListener('click', function () {
        onButtonClick('divide/')
});

// buttonAdd.onclick = onButtonClick;
// buttonSubtract.onclick = onButtonClick('subtract/');
// buttonMultiply.onclick = onButtonClick('multiply/');
// buttonDivide.onclick = onButtonClick('divide/');