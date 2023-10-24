var updateBtns = document.getElementsByClassName('update_cart')

for(var i = 0, i < updateBtns.length, i++){updateBtns[i].addEventListener
('click', function(){
var shirtId= this.dataset.shirt
var action = this.dataset.action
console.Log('shirtId:', shirtId, 'action:', action)})
}
