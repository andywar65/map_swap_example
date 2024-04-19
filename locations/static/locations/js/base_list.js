function map_init(map, options) {

    function onEachFeature(feature, layer) {
      if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent.content, {minWidth: 256});
      }
    }

    const base_map = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 10,
      });

    const layer_control = L.control.layers(null).addTo(map);

    function getCollections() {
      // add eventually inactive base layers so they can be removed
      base_map.addTo(map);
      // remove all layers from layer control and from map
      map.eachLayer(function (layer) {
        layer_control.removeLayer(layer);
        map.removeLayer(layer);
      });
      // add base layers back to map and layer control
      base_map.addTo(map);
      // add objects to layers
      collection = JSON.parse(document.getElementById("marker_data").textContent);
      for (marker of collection.features) {
        L.geoJson(marker, {onEachFeature: onEachFeature}).addTo(map);
      }
      map.fitBounds(L.geoJson(collection).getBounds(), {padding: [30,30]});
    }

    getCollections()

    addEventListener("refreshCollections", function(evt){
      getCollections();
    })
  }

  function openDrawing(path) {
    htmx.ajax('GET', path, '#nav-card')
  }
