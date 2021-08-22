// Funcionar o menu, selecionar um por vez
let menu = document.querySelectorAll('.selec-navigation')
for (let i=0; i < menu.length; i++) {
    menu[i].onclick = function () { //primeriro identificar os clicks
        let contador = 0;
        while(contador < menu.length) {
            menu[contador++].classList.remove('active');
        }
        menu[i].classList.add('active')
    }
}
