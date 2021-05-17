const calculateBMI = e => {
  e.preventDefault();
  const weight = document.getElementById('weight').value;
  const height = document.getElementById('height').value;
  const bmi = (weight/height*100)/height*100;
  if(bmi < 18.5) {
    return document.getElementById('results').innerHTML = `<h3>Results:</h3><p>Your BMI: ${bmi.toFixed(2)}<br />You are in underweight range.</p>`
  }
  else if(bmi > 18.5 && bmi < 25) {
    return document.getElementById('results').innerHTML = `<h3>Results:</h3><p>Your BMI: ${bmi.toFixed(2)}<br />You are in healthy weight range.</p>`
  }
  else if(bmi > 25 && bmi < 30) {
    return document.getElementById('results').innerHTML = `<h3>Results:</h3><p>Your BMI: ${bmi.toFixed(2)}<br />You are in overweight range.`
  }
  else {
    return document.getElementById('results').innerHTML = `<h3>Results:</h3><p>Your BMI: ${bmi.toFixed(2)}<br />You are in obese range.`
  }
}