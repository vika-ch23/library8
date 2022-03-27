$(document).on("click", ".submit_edited_image", function(){

    var formdata = new FormData();  

    var image = $('#id_image')[0].files[0]

    formdata.append( 'image', image ); 

    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    formdata.append('csrfmiddlewaretoken', csrf);

    var name = $('input[name="name"]').val();

    formdata.append('name', name)

    var image_id = $(this).attr("data-id"); 


    fetch('/edit_picture/' + image_id + "/", {
     method: 'POST',
     mode: 'same-origin',  
     headers:{
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', 
        'X-CSRFToken': csrf,
     },
     body: formdata 
     })
     .then(response => {
         return response.json() 
     })
     .then(data => {

         if (!data.form_is_valid){
           $("#staticBackdrop .modal-content").html("");
           $("#staticBackdrop .modal-content").html(data.edit_picture);
         }

         if (data.form_is_valid) {
           $("#staticBackdrop").modal("hide");
           location.reload(); 
         }

      })

  return false;

  });
