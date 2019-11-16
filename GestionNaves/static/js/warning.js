document.contactform.onsubmit=function()
{
    if(document.contactform.name.value=='')
    {
        alert("Ingrese su nombre");
        document.contactform.name.focus();
        return false;
    }
    else if (document.contactform.email.value=='')
    {
        alert("Ingrese su correo electronico");
        document.contactform.email.focus();
        return false;
    }
    return true;
}