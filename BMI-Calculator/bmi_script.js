function calculateBmi(){
    let weight = document.getElementById('weight').value
    let height = document.getElementById('height').value
    let height1 = height / 39.3701

    let bmi = (weight / (height1*height1))
    document.getElementById('heading').innerHTML = 'Your BMI is :'
    document.getElementById('bmi-output').innerHTML = bmi.toFixed(2)
    

    if (bmi<= 18.5) {
        document.getElementById('message').innerHTML = 'You are Underweight'
    
    } else if ( bmi>= 18.5 && bmi <= 24.9){
        document.getElementById('message'). innerHTML='You have a healthy weight'

    } else {
        document.getElementById('message').innerHTML= 'You are overweight' 
    
    }

    
    
}


function reload(){
    window.location.reload()
}