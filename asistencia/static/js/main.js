let direccion = window.location;
console.log(direccion);

if(direccion.pathname == "/asistencia/asistencia/"){
    const div3 = document.querySelector(".object-tools .btn-group").insertAdjacentHTML("afterend",`
        <a href="#" class="import_link btn btn-outline-secondary border-quitar">
            <i class="fas fa-file-import" style="
            padding: 0px 5px;
            border-right: none;
        "></i>Reporte
        </a>
    `);
}

function loadJs(file, callback) {
    // Evitar cargar más de 1 vez
    if(document.querySelector(`script[src="${file}"]`)) {
      // Ya se cargó el script, solo se ejecuta la función de retorno
      if(typeof callback == 'function') {
        callback();
      }
    } else {
      // No se ha cargado, primero creas el elemento
      let script = document.createElement('script');
      // Si hay función de retorno
      if(typeof callback == 'function') {
        // Debe ejecutarse cuanto el script se haya cargado
        script.addEventListener('load', callback);
      }
      // Asignar ubicación del script
      script.src = file;
      // Agregar a <head>
      document.head.appendChild(script);
    }
}


let jqCdn = '//cdn.jsdelivr.net/npm/sweetalert2@11';

loadJs(jqCdn, () => {
     function accion(){
        const accion1 = document.querySelector('.border-quitar');
    
        accion1.addEventListener('click', async function(){              
            // Swal.fire(JSON.stringify(formValues))
            // window.location.href = direccion.origin+'/index';
            // console.log(direccion.origin+'/index');

            Swal.fire({
              width: 1020,
              html: `<iframe width="920" height="850" src="${direccion.origin+'/index'}" frameborder="0" allowfullscreen></iframe>`,
              showCloseButton: true,
              showCancelButton: true,
              focusConfirm: false,
          });
              
        })
    }
    accion()
})

