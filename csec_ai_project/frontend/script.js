async function send(){

 let msg=document.getElementById("message").value;

 let res = await fetch("http://127.0.0.1:8005/chat",{
   method:"POST",
   headers:{"Content-Type":"application/json"},
   body:JSON.stringify({message:msg})
 });

 let data=await res.json();

 document.getElementById("chat").innerHTML+=
 "<p><b>Bot:</b> "+data.response+"</p>";
}

async function upload(){

 let file=document.getElementById("file").files[0];

 let form=new FormData();
 form.append("file",file);

 await fetch("http://127.0.0.1:8005/upload",{
   method:"POST",
   body:form
 });

 alert("Uploaded!");
}
