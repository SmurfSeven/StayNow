/*MAS DE UN MAPA POR PAGINA: con bucle for*/
var marker, map;

function initialize(condition) {
    // ARRAYS COORDENADAS
    let coord = [
        [-33.016035, -71.557050], //viña
        [-29.939295, -71.285818], //serena
        [-39.279593, -71.966430], //pucon
        [-20.236548, -70.150183],//iquique
        [-39.280288, -72.230853],//Villarica
        [-39.817807, -73.238000],//valdivia
        [-41.123783, -73.054289],//frutillar
    ]

    //ARRAY guarda id de mapas del html
    let idMaps = [
        'map_vina',
        'map_serena',
        'map_pucon',
        'map_iquique',
        'map_villarica',
        'map_valdivia',
        'map_frutillar',
    ]

    //mapas con for
    for (var i = 0; i<=9; i++){
        
        mapa = new google.maps.Map(document.getElementById(idMaps[i]),{
            zoom: 15,
            center: {lat: coord[i][0],lng:coord[i][1]}
            //center: coordenadas[i][0]
        })

        marker = new google.maps.Marker({
            position: {lat: coord[i][0],lng:coord[i][1]},
            map: mapa,
            title: "Turismo Real",
          });
        
    }
  
}