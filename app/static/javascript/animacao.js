var x=0;

function animacao(){
    var fundo_img=document.getElementById('fundo_img');   
    if(x>360){
        x=0;
    }else{
        fundo_img.style.backgroundImage='linear-gradient('+x+
                                    'deg, var(--cor-1), var(--cor-2))';
        x++;
    }   
}

setInterval(animacao, 10)


function new_acc(n){
    var vrf = document.querySelectorAll('p')[0].innerHTML
    if(vrf=='A82g2frTy2a4G@G!#'){
        alert('Conta nova criada');
    }else if(vrf=='8j87fjsS!$ASQffsq!*s#'){
        alert('Senha muito fraca !');
    }
}

window.addEventListener('load', new_acc)