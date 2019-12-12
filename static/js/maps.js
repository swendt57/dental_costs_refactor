
$(document).ready
{
    const mapSrc = `https://maps.googleapis.com/maps/api/js?key=${googleApiKey}&callback=initMap`;

    $.getScript(mapSrc, function () {
        console.log("map api loaded");
    });

    function readTextFile(file, callback) {
        var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
        xobj.open('GET', file, true);
        xobj.onreadystatechange = function () {
            if (xobj.readyState == 4 && xobj.status == "200") { //Do not use triple equals here
                callback(xobj.responseText);
            }
        };
        xobj.send(null);
    }

    function initMap() {

        //putting the init code in here so I can use the main combined_flat.json file

        readTextFile('/dental_costs/static/data/combined_flat.json', function (text) {
            let allData = JSON.parse(text);

            let cityData = sortDataByCity(allData);

            let sdMap = new google.maps.Map(document.getElementById("sdMap"), {
                zoom: 11,
                center: {
                    lat: 32.808800,
                    lng: -117.152970
                }
            });

            let tjMap = new google.maps.Map(document.getElementById("tjMap"), {
                zoom: 12,
                center: {
                    lat: 32.516529,
                    lng: -117.016479
                }
            });

            let labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            let sdLocations = assembleCoordinates(cityData[0]);
            let tjLocations = assembleCoordinates(cityData[1]);

            //this is a JS function, not a Google one
            let sdMarkers = sdLocations.map(function (location, i) {
                return new google.maps.Marker({
                    position: location,
                    label: labels[i % labels.length]
                });
            });

            let tjMarkers = tjLocations.map(function (location, i) {
                return new google.maps.Marker({
                    position: location,
                    label: labels[i % labels.length]
                });
            });

            let sdMarkerCluster = new MarkerClusterer(sdMap, sdMarkers, {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
            let tjMarkerCluster = new MarkerClusterer(tjMap, tjMarkers, {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

        });

    }

    function assembleCoordinates(dentists) {
        let coordinates = [];

        $(dentists).each(function (i, item) {
            coordinates.push({lat: item.latitude, lng: item.longitude});
        });

        return coordinates;
    }

    function sortDataByCity(allData) {
        let sdData = [];
        let tjData = [];

        for (let i = 0; i < allData.length; i += 5) { //dentists repeat for each of five procedures - we only want one each
            if (allData[i].city === "San Diego") {
                sdData.push(allData[i]);
            } else {
                tjData.push(allData[i]);
            }
        }

        return [sdData, tjData];
    }



}