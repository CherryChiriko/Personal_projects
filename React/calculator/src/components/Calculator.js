import React from 'react';
import './Calculator.css'
import data from '../data/data'
import Button from './Button';

export default function Calculator() {
const buttons = data.map( button => (
<Button keys={button.id} value={button.value} span={button.span}
        handleClick={() => {updateCalculation(button.value)}}/>
))
const [calculation, setCalculation] = React.useState('');

function compute(){
  

// let expression = '5 / 2 + 3 . 5 x 4 - 1'
let expression = '2 . 5 + 3 x 4 - 1 / 2';
expression = expression.split(' ').join('');
console.log(expression)

let regex = /(-?\d+(?:\.\d+)?)([x/])(-?\d+(?:\.\d+)?)/g;
function multiplyDivide(match, n1, op, n2) {
    n1 = Number(n1);    n2 = Number(n2);
    return (op === 'x' ? n1 * n2 : n1 / n2).toString();
}
  
function addSubtract(match, n1, op, n2){
    n1 = Number(n1); n2 = Number(n2); 
    return (op==='+'? n1 + n2: n1 - n2).toString();
}
let result = expression.replace(regex, multiplyDivide)
console.log(result)
regex = /(-?\d+(?:\.\d+)?)([+-])(-?\d+(?:\.\d+)?)/g;
while (regex.test(result)) {
    result = result.replace(regex, addSubtract);
}
console.log(result)
return result
}

console.log(compute())
function addCharacter(calc, val){
    let calcArr = calc? calc.split(' ') : [];
    if (calcArr.length >= 15) {return 'DIGIT LIMIT MET'} 
    calcArr.push(val)
    return calcArr.join(' ')
}
function updateCalculation(val){
    val==="AC"? setCalculation('') :
    val==="="? compute() :
    setCalculation(prevCalculation => addCharacter(prevCalculation, val))
}
return (
    <div className='rounded container tot-div'>
        <div className='screen container rounded'
        id="display">{calculation}</div>
        <div className='calc-div'>
            {buttons}
        </div>
    </div>
  );
}



// const regex = /(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)/;

// while (regex.test(expression)) {
//   expression = expression.replace(regex, (match, n1, op, n2) => {
//     n1 = Number(n1);    n2 = Number(n2);
//     let result = match;
//     switch (op) {
//       case '*':
//         result = n1 * n2;
//         break;
//       case '/':
//         result = n1 / n2;
//         break;      
//       case '+':
//         result = n1 + n2;
//         break;
//       case '-':
//         result = n1 - n2;
//         break;
//       default:
//         break;
//     }
//     return result.toString();
//   });
// }