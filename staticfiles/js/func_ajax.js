function utilizou_licenca(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/utilizou_licenca/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result){
            console.log('sucesso')
            $("#estoque_atual").text(result.response);
        }
    });
}



// $(document).ready(function() {
//     $('#estoque_atual').dataTable( {
//         "processing": true,
//         "ajax": {
//             "processing": true,
//             "url": "{% url 'utilizou_licenca' %}",
//             "dataSrc": ""
//         },
//
//         "columns": [
//                 { "data": "quantidade_disponivel", "reservadas" },
//
//             ]
//     } );
// } );
