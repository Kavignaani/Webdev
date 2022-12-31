
function createbox() {
    rows=0
    var name=document.getElementById('name').value;
    var intime=document.getElementById('intime').value;
    var outtime=document.getElementById('outtime').value;
    if (outtime.slice(-2)>"00") {
        rows=rows+1
    }
    rows = rows + parseInt(outtime)-parseInt(intime)
    // rows variable has the required number of rows 
    //for loop

    var btn = document.getElementById('submit1')
    btn.disabled = true 
    
    console.log(name)

    var h = document.createElement("h3");
    h.className='titled'
    h.textContent ='Enter 4 digit project number for each hour' ;
    document.body.appendChild(h);


    form = document.getElementById('primary');

    x=parseInt(intime)
    
    for (let i = 1 ; i<=rows ; i++) {
        let div = document.createElement('div')
        document.body.appendChild(div);    
        s1="PJ"
        s2=String(i)
        result=s1.concat(s2) 
        let alpa = `
        <label class="oct labels time">${x+i-1}:00 - ${x+i-1+1}:00</label> <input type="number" class="inp oct time" id="${result}" name="PJ${result}">
        <button 
        `
        div.insertAdjacentHTML('beforeend',alpa)
    }

    var rip = document.createElement("a");
    rip.className='inp final'
    rip.style.width = "100%";
    rip.textContent ='Submit' ;
    rip.setAttribute('type','submit')
    rip.setAttribute('href','/AML')
    rip.setAttribute('id','submit2')
    rip.setAttribute('name','submit2')

    document.body.appendChild(rip);

    var s1 = document.getElementById('PJ1').value;
    console.log(s1)



}