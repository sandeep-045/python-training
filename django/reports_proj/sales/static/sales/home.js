console.log('Hello World')

const reportBtn     = document.getElementById('report-btn')
const img           = document.getElementById('img')
const reportName    = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf          = document.getElementsByName('csrfmiddlewaretoken')[0].value
const reportForm    = document.getElementById('report-form')
console.log(reportForm)
if(img)
{     
   
    reportBtn.classList.remove('not-visible')
}
reportBtn.addEventListener('click',()=>{
    img.setAttribute('class','w-100')
    document.getElementById('modal-id').prepend(img)

    reportForm.addEventListener('submit',e=>{
        e.preventDefault()
        const formData = new FormData()
        formData.append('csrfmiddlewaretoken',csrf)
        formData.append('name',reportName.value)
        formData.append('remarks',reportName.value)
        formData.append('image',img.src)

        $.ajax({
            type:'POST',
            url:'reports/save',
            data:formData,
            success:function(response){console.log(response)},
            error: function(error){console.log(error)},
            contentType:false,
            processData:false,
        })
    })
});