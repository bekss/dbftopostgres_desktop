jQuery(document).ready(function () {
    $('.first').css({'color':'red'});
});



// $('#dbf').click(function () {
//     eel.get_filepath();
// });

// $( "#ad" ).on( "click", function() {
//     eel.get_filepath();
// });
$( "#ad" ).on( "click", function() {
    eel.get_filepath();
});
//
// $.get('oked.dbf', function(data) {
//      $('#textarea').append( data.text());
//     //     $.each(lines, function(n, ) {
//     //    $('#textarea').append( data);
//     // });
//     // alert(data)
//
//     // reader = new FileReader()
//     // d = reader.readAsBinaryString(data)
//     // console.log(d)
//     //
//     // reader.onload = function(){
//     //     alert(btoa(reader.result))
//     // }
//
// });


//
// $('#file-selector').on('change', function () {
//   var file = this.files[0];
//   var reader = new FileReader;
//
//   reader.onloadend = function () {
//     $('#textarea').val(reader.result)// file content
//
//   };
//    reader.readAsText(file);
//   // Если кодировка файла отличается от UTF-8,
//   // то указываем её вторым параметром
//   // reader.readAsText(file, 'cp1251');
// });
//
// function get_python() {
//     eel.get_random_number();
// }
//     function readfile(file) {
//     // Check if the file is an image.
//         if (file.type && file.type.indexOf('txt') === -1) {
//         console.log('File is not an image.', file.type, file);
//         return;
//     }
//
//       const reader = new FileReader();
//       reader.addEventListener('load', (event) => {
//         img.src = event.target.result;
//       });
//       a = reader.readAsDataURL(file);
//       eel.print_files(a)
//     }
//     const fileSelector = document.getElementById('file-selector');
//     fileSelector.addEventListener('change', (event) => {
//         const fileList = event.target.files;
//         alert(fileList)
//         readfile(fileList)
//     // eel.print_files(fileList)
//     });
