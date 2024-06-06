const map = L.map('swap_map');

function onEachFeature(feature, layer) {
  if (feature.properties && feature.properties.popupContent) {
    layer.bindPopup(feature.properties.popupContent.content, {minWidth: 256});
  }
}

const base_map = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19,
  });
base_map.addTo(map);
const layerGroup = L.layerGroup().addTo(map);

function getCollections() {
  // remove all objects
  layerGroup.clearLayers();
  // add objects to layers
  collection = JSON.parse(document.getElementById("marker_data").textContent);
  for (marker of collection.features) {
    L.geoJson(marker, {onEachFeature: onEachFeature}).addTo(layerGroup);
  }
  // fit bounds
  if (collection.features.length !== 0) {
    map.fitBounds(L.geoJson(collection).getBounds(), {padding: [30,30]});
  } else {
    map.setView([0,0], 2)
  }
}

getCollections()

addEventListener("refreshData", function(evt){
  getCollections();
})

function openLocation(path) {
  htmx.ajax('GET', path, '#dialog-box')
}
