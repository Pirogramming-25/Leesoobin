function makeAnswer(){
  const nums= [];
  while (nums.length<3){
    const n= Math.floor(Math.random()*10);
    if(!nums.includes(n)){
      nums.push(n);
    }
  }
  return nums;
}

let answer = makeAnswer();
let attempts = 9; 

function check_numbers(){
  const i1= document.querySelector('#number1').value;
  const i2= document.querySelector('#number2').value;
  const i3= document.querySelector('#number3').value;

  if (i1=== '' || i2===''|| i3===''){
    document.querySelector('#number1').value='';
    document.querySelector('#number2').value='';
    document.querySelector('#number3').value='';
    return;
  }
    const guess = [Number(i1), Number(i2), Number(i3)];
    console.log('내 입력:', guess, '정답:', answer);

    let strike = 0;
    let ball = 0;

    for (let i=0; i<3; i++){
      if(guess[i]==answer[i]){
        strike++;
      }
      else if(answer.includes(guess[i])){
        ball++;
      }
    }

    let result;
    if(strike==0 && ball==0){
      result= `<span class="num-result out">O</span>`;
    } else{
      result= `${strike} <span class="num-result strike">S</span> ${ball} <span class="num-result ball">B</span>`;
      
    }

    const row =`
    <div class= "check-result">
      <div class= "left"> ${i1} ${i2} ${i3} </div>
      <div>:</div>
      <div class ="right">${result}</div>
      </div>`;

    document.querySelector('#results').innerHTML += row;



  
    attempts--;
    document.querySelector('#attempts').textContent = attempts;

    if(strike===3){
      document.querySelector('#game-result-img').src = 'success.png';
      document.querySelector('.submit-button').disabled = true;
    }

    else if(attempts ===0){
      document.querySelector('#game-result-img').src= 'fail.png';
      document.querySelector('.submit-button').disabled = true;
    }

    document.querySelector('#number1').value = '';
    document.querySelector('#number2').value = '';
    document.querySelector('#number3').value = '';
}

function initGame(){
  attempts=9;
  answer= makeAnswer();
  document.querySelector('#attempts').textContent = attempts;
  document.querySelector('#results').innerHTML= '';
  document.querySelector('#game-result-img').src = '';
  document.querySelector('.submit-button').disabled = false;
  document.querySelector('#number1').value='';
  document.querySelector('#number2').value='';
  document.querySelector('#number3').value='';
}

initGame();