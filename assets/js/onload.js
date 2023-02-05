window.onload = function() {
    BoutonsEns = document.getElementsByClassName('Ens');
    BoutonsMoment = document.getElementsByClassName('moment');
    for(i=0; i<BoutonsEns.length;i++){
        BoutonsEns[i].onclick = function() {
            clickButtEns(this);
        }
    }
    for(i=0; i<BoutonsMoment.length;i++){
        BoutonsMoment[i].onclick = function() {
            clickButtMoment(this);
        }
    }
}

function clickButtEns(butt) {
    butt.classList.toggle('selectionne');
    for(i=0; i<BoutonsEns.length;i++){
        if(BoutonsEns[i] != butt){
            BoutonsEns[i].classList.remove('selectionne');
        }
    }
}

function clickButtMoment(butt) {
    butt.classList.toggle('selectionne');
    for(i=0; i<BoutonsMoment.length;i++){
        if(BoutonsMoment[i] != butt){
            BoutonsMoment[i].classList.remove('selectionne');
        }
    }
}