function validate(){
    var useranme = document.getElementById ("username").Value;
    var password = document.getElementById ("password").Value;
    if (Username == "admin" && password == "user")
    {
        alert ("Login Succesfully");
        return false ;

    }
    else {
        alert ("login failed");
    }

}