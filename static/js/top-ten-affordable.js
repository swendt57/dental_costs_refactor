$(document).ready(function() {

    <!--TODO combine duplicated code, if possible-->

    let windowWidth = $(window).width();

    let sdList = document.getElementById("sdList");
    let tjList = document.getElementById("tjList");

    function truncateText(text) {
        if(text.length >= 30) {
            return $.trim(text).substring(0, 30)
                .split(" ").slice(0, -1).join(" ") + "...";
        } else {
            return text;
        }
    }

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

    readTextFile('/static/data/combined_flat.json', function(text) {
        let allData = JSON.parse(text);

        let cityData = sortDataByCity(allData);

        $(cityData[0]).each(function(i, item){ //San Diego
            createHtmlList(sdList, item);
        });


        $(cityData[1]).each(function(i, item){ //Tijuana
            createHtmlList(tjList, item);
        });

        function createHtmlList(list, item) {
            if(windowWidth >= 768) {
                list.innerHTML += `<li><a href="https://www.google.com/maps/dir/?api=1&destination=${item.latitude},${item.longitude}" target="_blank">${item.name}</a> &mdash; ${truncateText(item.address)}</li>`;
            } else {
                list.innerHTML += `<li><a href="https://www.google.com/maps/dir/?api=1&destination=${item.latitude},${item.longitude}" target="_blank">${item.name}</a></li>`;
            }
        }

        function sortDataByCity(allData) {
            let sdData = [];
            let tjData = [];

            for(let i=0; i<allData.length; i+=5) { //dentists repeat for each of five procedures - we only want one each
                if(allData[i].city === "San Diego") {
                    sdData.push(allData[i]);
                } else {
                    tjData.push(allData[i]);
                }
            }

            return [sdData, tjData];
        }
    });



});