var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");

        var content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}

function sendButton(){
    event.preventDefault()
        container=document.querySelector('.chatwrap')
        dbox=document.createElement('div')
        dbox.setAttribute('class','chatbox')
        dp=document.createElement('p')
        dp.setAttribute('class','botText')
        dp.setAttribute('id','botStarterMessage')

        ds=document.createElement('span')

        us=document.createElement('span')



        var message=document.chats.message.value
        document.chats.message.value=""
        const data = { message: String(message) };
        var ubox=document.createElement('div')
        ubox.setAttribute('class','chatbox')
        up=document.createElement('p')
        up.setAttribute('class','ubotText')
        up.setAttribute('id','botStarterMessage')
        us.appendChild(document.createTextNode(message))

        up.appendChild(us)
        
        //k.appendChild(document.createTextNode(message))
        ubox.appendChild(up)
        container.appendChild(ubox)

        fetch('http://localhost:8000/simple_chatbot/', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        })
        .then(response =>response.json())
        .then((result)=>{
            ds.appendChild(document.createTextNode(result.message))
        dp.appendChild(ds)
        dbox.appendChild(dp)
        container.appendChild(dbox)
        message=''
        })
        .catch((error) => {
            ds.appendChild(document.createTextNode('Sorry Try again '))
            dp.appendChild(ds)
            dbox.appendChild(dp)
            container.appendChild(dbox)
        message=''
        });
}