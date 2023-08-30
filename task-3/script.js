const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');


function showFalse(input,message){
    const formControl = input.parentElement;
    formControl.className = 'form-control error';
    const small = formControl.querySelector('small');
    small.innerText = message;
}

function showTrue(input){
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
    
}

function checkPasswordMatch(input1, input2){
    if(input1.value !== input2.value){
        showFalse(input2,'Password doesn\'t Match ')
    }
}

function isValidEmail(email){
        if( email === "" )
        {
        showFalse(email,'Email is not valid');
    }
}



function checkRequired(inputArr){
  inputArr.forEach(input => {
       if(input.value.trim() === ''){
           showFalse(input,`${getFieldName(input)} is required`)
       }else{
           showTrue(input);
       }
  });
}


 function getFieldName(input){
  return input.id.charAt(0).toUpperCase() + input.id.slice(1);
 }

 
 function checkLength(input,min,max){
     if(input.value.length<min){
         showFalse(input,`${getFieldName(input)} must be atleast ${min} characters`)
     }else{
         showTrue(input);
     }
 }


form.addEventListener('submit',(e)=>{
    e.preventDefault();
   
    checkRequired([username,email,password,password2]);
     checkLength(username,3);
     checkLength(password,6);
     isValidEmail(email);
     checkPasswordMatch(password,password2);
    

});
