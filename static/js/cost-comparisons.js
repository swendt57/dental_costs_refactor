let windowWidth = $(window).width();

queue()
    .defer(d3.json, "/static/data/combined_flat.json")
    .await(function makeGraphs(error, allData) {

    if(windowWidth <= 400) {
        $(".smartphone-message").html(`<strong>NOTE:</strong> Please use landscape mode for best viewing on your smartphone`);
    }

    //OVERLAY CHART****************************************************************

    let overlayData = assembleOverlayDataSet(allData);

    let width = 400;
    let height = 500;
    let barLabelOffset = 20;

    if(windowWidth >= 768) {
        width = 600;
        barLabelOffset = 40;
    }

    let margin = {top: 20, right: 20, bottom: 30, left: 40};

    let x = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1);
    let y = d3.scale.linear()
        .range([height, 0]);

    let xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");
    let yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    let svg = d3.select("#overlay-bar-chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    setDomains(x, y);

    appendAttributes(svg);

    createTheBars(svg);

    addBarLabels(svg);

    addLegend(svg);


    function setDomains(x, y) {
        x.domain(overlayData.map(function (d) {
            return d.procedure;
        }));
        y.domain([0, Math.ceil(overlayData[4].sd_average/100)*100 ]); //SD crown is the most expensive procedure
    }

    function appendAttributes(svg) {
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Values");
    }

    function createTheBars(svg) {
        let g = svg.selectAll(".bars")
            .data(overlayData)
            .enter().append("g");

        g.append("rect")
            .attr("class", "sdBar")
            .attr("x", function (d) {
                return x(d.procedure) + 10; // center it
            })
            .attr("width", x.rangeBand() - 20) // make it slimmer
            .attr("y", function (d) {
                return y(d.sd_average);
            })
            .attr("height", function (d) {
                return height - y(d.sd_average)
            })
            .on("mouseover", sdHighlightOn)
            .on("mouseleave", sdHighlightOff);

        g.append("rect")
            .attr("class", "tjBar")
            .attr("x", function (d) {
                return x(d.procedure);
            })
            .attr("width", x.rangeBand())
            .attr("y", function (d) {
                return y(d.tj_average);
            })
            .attr("height", function (d) {
                return height - y(d.tj_average)
            })
            .on("mouseover", tjHighlightOn)
            .on("mouseleave", tjHighlightOff);
    }

    function addBarLabels(svg) {
        svg.selectAll(".text")
            .data(overlayData)
            .enter()
            .append("text")
            .attr("class", "label sdBar")
            .attr("x", (function(d) { return x(d.procedure) + barLabelOffset; }  ))
            .attr("y", function(d) { return y(d.sd_average) + 3; })
            .attr("dy", ".75em")
            .text(function(d) { return `$${d.sd_average}`; });

        svg.selectAll(".text")
            .data(overlayData)
            .enter()
            .append("text")
            .attr("class", "label tjBar")
            .attr("x", (function(d) { return x(d.procedure) + barLabelOffset; }  ))
            .attr("y", function(d) { return y(d.tj_average) + 5; })
            .attr("dy", ".75em")
            .text(function(d) { return `$${d.tj_average}`; });
    }

    function addLegend(svg) {
        const legendSpacing = 25;
        let rectClasses = ["sdBar", "tjBar"];
        let labels = ["San Diego", "Tijuana"];
        let colors = d3.scale.ordinal()
            .range(["#4e92c3", "#57b358"]);

        let legend = svg.selectAll(".legend")
            .data(["San Diego","Tijuana"])
            .enter()
            .append("g")

        legend.append("rect")
            .attr("class", function(d, i) {
                return rectClasses[i];
            })
            .attr("fill", colors)
            .attr("width", 20)
            .attr("height", 20)
            .attr("y", function (d, i) {
                return i * legendSpacing + 20;
            })
            .attr("x", 50);

        legend.append("text")
            .attr("class", function(d, i) {
                return "legend " + labels[i]
            })
            .attr("y", function (d, i) {
                return i * legendSpacing + 32;
            })
            .attr("x", 75)
            .attr("text-anchor", "start")
            .text(function (d, i) {
                return labels[i];
            });
        legend.select("text.legend.San.Diego")
            .on("mouseover", sdHighlightOn)
            .on("mouseleave", sdHighlightOff);
        legend.select("text.legend.Tijuana")
            .on("mouseover", tjHighlightOn)
            .on("mouseleave", tjHighlightOff);
        legend.select("rect.sdBar")
            .on("mouseover", sdHighlightOn)
            .on("mouseleave", sdHighlightOff)
        legend.select("rect.tjBar")
            .on("mouseover", tjHighlightOn)
            .on("mouseleave", tjHighlightOff);;

    }

    function sdHighlightOn(d, i) {
        d3.selectAll("rect.sdBar").style("opacity", 1);
        d3.selectAll("rect.tjBar").style("opacity", .2);
    }
    function sdHighlightOff(d, i) {
        d3.selectAll("rect.sdBar").style("opacity", .7);
        d3.selectAll("rect.tjBar").style("opacity", .7);
    }

    function tjHighlightOn(d, i) {
        d3.selectAll("rect.tjBar").style("opacity", 1);
        d3.selectAll("rect.sdBar").style("opacity", .2);
    }
    function tjHighlightOff(d, i) {
        d3.selectAll("rect.tjBar").style("opacity", .7);
        d3.selectAll("rect.sdBar").style("opacity", .7);
    }

    //SCATTER CHART********************************************************************************

    width = 575;
    height = 600;
    //doubble check this!!!!!!!
    if(windowWidth >= 768) {
        width = 650;
        height = 650;
    }

    let ndx = crossfilter(allData);
    let proc_dim = ndx.dimension(dc.pluck('procedure'));
    let cost_dim = ndx.dimension(function(d) {
        return [d.procedure, d.cost, d.name];
    });
    let cost_group = cost_dim.group().reduceSum(function(d) {
        return [d.cost];
    });

    let scatter_chart = dc.scatterPlot('#scatter-chart');

    scatter_chart
        .width(width)
        .height(height)
        .dimension(proc_dim)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .y(d3.scale.linear().domain([0, 1200]))
        .brushOn(false)
        .symbolSize(8)
        .clipPadding(10)
        .yAxisLabel("Cost")
        .renderHorizontalGridLines(true)
        .group(cost_group)
        .renderlet(function (chart) {
            chart.selectAll("g.x text")
                .attr('dx', '-30')
                .attr('transform', "translate(-20,0)")
        });


    //PIE CHARTS ***************************************************

    let dataByCity = assemblePieData();

    width = 275;
    height = 300;

    if(windowWidth >= 768) {
        width = 320;
        height = 350;
    }

    let colorScale = d3.scale.linear().domain([0,2]).range(["green", "blue"]);
    labels = ["Actual Data", "Mock Data"];

    let arc = setPieChartRadii()[0];
    let arcOver = setPieChartRadii()[1];

    //San Diego start
    svg = createPieChart('#sd-pie-chart');

    let pie = d3.layout.pie()
        .value(function(d){ return d.value; });

    let data = pie(dataByCity[0]); //SD data

    let arcs = renderPieArcs(svg);
    setArcFunctionality(arcs);

    //add labels and position them
    arcs.append('text')
        .attr("transform", function(d) {
            var c = arc.centroid(d);
            return "translate(" + c[0]*4.5 +"," + c[1]*2.5 + ")";
        })
        .attr("text-anchor", "top")
        .text(function(d, i){ return labels[i]; })
        .attr("class", "pie-label")
        .style("stroke-width", "0");

    //San Diego end

    //Tijuana start
    svg = createPieChart('#tj-pie-chart')

    pie = d3.layout.pie()
        .value(function(d){ return d.value; });
    data = pie(dataByCity[1]); //TJ data

    arcs = renderPieArcs(svg);
    setArcFunctionality(arcs);

    //add labels and position them
    arcs.append('text')
        .attr("transform", function(d) {
            var c = arc.centroid(d);
            return "translate(" + c[0]*2.0 +"," + c[1]*4.0 + ")";
        })
        .attr("text-anchor", "top")
        .text(function(d, i){ return labels[i]; })
        .attr("class", "pie-label")
        .style("stroke-width", "0");

    //Tijuana end

    function assemblePieData() {
        let dataByCity = sortDataByCity(allData);
        return determineMockDataTotals(dataByCity);
    }

    function createPieChart(anchorId) {
        return d3.select(anchorId)
            .append('svg')
            .attr("width", width)
            .attr("height", height)
            .attr('viewBox','260 35 350 350');
    }

    function setPieChartRadii() {
        return [
            d3.svg.arc()
                .innerRadius(0)
                .outerRadius(100),
            d3.svg.arc()
                .innerRadius(0)
                .outerRadius(150)
        ];
    }

    function renderPieArcs() {
        return svg.append('g')
            .attr('transform','translate(440,200)')
            .selectAll('.arc')
            .data(data)
            .enter()
            .append('g')
            .attr('class',"arc")
            .attr("stroke", "black")
            .style("stroke-width", "1px");
    }

    function setArcFunctionality(arcs) {
        arcs.append('path')
            .attr('d',arc)
            .attr('fill',function(d,i){ return colorScale(i); })
            .on("mouseover", function(d) {
                d3.select(this).transition()
                    .duration(1000)
                    .attr("d", arcOver)
                    .style('opacity', .7);
            })
            .on("mouseout", function(d) {
                d3.select(this).transition()
                    .duration(1000)
                    .attr("d", arc)
                    .style('opacity', 1);
            });
    }




    dc.renderAll(); //currently this only renders the scatter chart


    });


//This restructures the data into a structure that the overlay chart can use
function assembleOverlayDataSet(costData) {

    let procedures = ["Adult Cleaning", "Composite Filling", "Extraction", "Root Canal", "Porcelain Crown"];

    let totalCosts = [{"procedure": "Adult Cleaning", "sd_cost": 0, "sd_count": 0, "tj_cost": 0, "tj_count": 0},
                        {"procedure": "Composite Filling", "sd_cost": 0, "sd_count": 0, "tj_cost": 0, "tj_count": 0},
                        {"procedure": "Extraction", "sd_cost": 0, "sd_count": 0, "tj_cost": 0, "tj_count": 0},
                        {"procedure": "Root Canal", "sd_cost": 0, "sd_count": 0, "tj_cost": 0, "tj_count": 0},
                        {"procedure": "Porcelain Crown", "sd_cost": 0, "sd_count": 0, "tj_cost": 0, "tj_count": 0}];

    let averageCosts = [{"procedure":"Adult Cleaning", "sd_average":0, "tj_average":0}, {"procedure": "Composite Filling", "sd_average":0, "tj_average":0}, {"procedure": "Extraction", "sd_average":0, "tj_average":0}, {"procedure": "Root Canal", "sd_average":0, "tj_average":0}, {"procedure": "Porcelain Crown", "sd_average":0, "tj_average":0}];

    //For each procedure type, add up the total cost for San Diego and Tijuana
    for (let i = 0; i < procedures.length; i++) {
        costData.forEach(function (d) {
            if (d.procedure === procedures[i]) {
                if (d.city === "San Diego") {
                    totalCosts[i].sd_cost += d.cost;
                    if (d.cost > 0) {
                        totalCosts[i].sd_count++;
                    }
                } else {
                    totalCosts[i].tj_cost += d.cost;
                    if (d.cost > 0) {
                        totalCosts[i].tj_count++;
                    }
                }
            }
        });
        //Take the total costs and divide by the number of non-zero entries to set the average for each city
        averageCosts[i].sd_average = Math.round(totalCosts[i].sd_cost/totalCosts[i].sd_count);
        averageCosts[i].tj_average = Math.round(totalCosts[i].tj_cost/totalCosts[i].tj_count);
    }

    return averageCosts;

}

function sortDataByCity(allData) {
    let sdData = [];
    let tjData = [];

    for(let i=0; i<allData.length; i++) {
        if(allData[i].city === "San Diego") {
            sdData.push(allData[i]);
        } else {``
            tjData.push(allData[i]);
        }
    }
    console.log([sdData, tjData]);
    return [sdData, tjData];
}

function determineMockDataTotals(dataByCity) {
    let mockData = [[{"label": "Actual Data", "value": 0}, {"label": "Mock Data", "value": 0}],
                    [{"label": "Actual Data", "value": 0}, {"label": "Mock Data", "value": 0}]];

    for (let cd = 0; cd < 2; cd++) {
        for (let i = 0; i < dataByCity[cd].length; i++) {
            if (dataByCity[cd][i].fake_data === "Actual Data") {
                mockData[cd][0].value++;
            } else {
                mockData[cd][1].value++;
            }
        }
    }

    return mockData;
}


