let submit = document.getElementsByClassName('blue-btn');
submit[0].addEventListener('click', (e)=>{
    let user = document.getElementById('username').value;
    let pass = document.getElementById('password').value;
    if (!(user && pass)){
        let div = document.createElement('div')
        div.innerText = 'Please Enter Username and Password';
        div.style.color = 'red';
        div.style.fontWeight = 'bold';
        div.style.marginBottom = '20px';

        let form = document.getElementsByTagName('form');
        form[0].insertBefore(div, form[0].children[1]);
        e.preventDefault();
    }
})