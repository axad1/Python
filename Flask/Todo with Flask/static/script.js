document.querySelector('ul').onclick = e=> e.target.classList.toggle("completed")
document.querySelector('ul').oncontextmenu = e=> location.href = '/'+e.target.id