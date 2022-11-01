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


function new_acc(){
    alert('Conta nova criada');
}