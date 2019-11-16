document.getElementById('player').addEventListener("mouseover",sumarPuntos);
var puntos = 0;
var tiempo = 60;
var necesarios = Math.round(Math.random()*100);
function sumarPuntos(){
    puntos++;// suma los puntos
    document.getElementById("puntos").innerHTML = "Puntos : <b>"+ puntos +"/"+necesarios+"<b>";//escribe los puntos en la pantalla
    randNum = Math.round(Math.random()*450);// da un numero ranmdom
    randNum2 = Math.round(Math.random()*450);
    document.getElementById("player").style.marginTop = randNum+ "px";//utilisa el numero ramdom para mover el circulo
    document.getElementById("player").style.marginLeft = randNum2+ "px";
    if(puntos == necesarios){
        alert("Ganaste");
    }
}
function restarTiempo(){
    tiempo--;//resta el tiempo en la pantalla
    document.getElementById("tiempo").innerHTML = "Tiempo: "+tiempo ;//escribe el tiempo en la pantalla
    if(tiempo == 0)
    alert("Perdiste");
    
}
setInterval(restarTiempo,1000);