const reportBtn     = document.getElementById('report-btn')
const img           = document.getElementById('img')
const reportName    = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf          = document.getElementsByName('csrfmiddlewaretoken')[0].value
const reportForm    = document.getElementById('report-form')
const alertBox      = document.getElementById('alert-box')

const handleAlerts  = (type,msg)=>{
    
    alertBox.innerHTML=`
    <div class="alert alert-${type}" role="alert">
    ${msg}
    </div>`
}
if(img)
{     
   
    reportBtn.classList.remove('not-visible')
}
reportBtn.addEventListener('click',()=>{
    
    img.setAttribute('class','w-100')
    document.getElementById('modal-id').prepend(img)
    // console.log(img.src)


    reportForm.addEventListener('submit',e=>{
        e.preventDefault()
        // console.log(reportForm)
        // console.log(reportName.value)
        const formData = new FormData()
        formData.append('csrfmiddlewaretoken',csrf)
        formData.append('name',reportName.value)
        formData.append('remarks',reportName.value)
        formData.append('image',img.src)
        
        // for (var key of formData.entries()) {
        //     console.log(key[0] + ', ' + key[1]);
        // }

        console.log(img.src)
        $.ajax({
            url:'reports/save/',
            cache:false,    
            data: formData,
            contentType:false,
            processData:false,
            type:'POST',
            success: function(response){
                console.log(response);
                handleAlerts('success','Report Created');
                reportForm.reset()
            },
            error: 
            function(error)
            {
                console.log(error)
                handleAlerts('danger','Something Went Wrong');
            },
           
            
        })
    })
 });