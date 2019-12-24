
describe("cost-comparisons - data parsers", function() {

    let sampleData = [
        {"name": "San Diego Smile Dentistry", "city": "San Diego", "procedure": "Adult Cleaning", "cost": 105, "fake_data": "Actual Data"},
        {"name": "San Diego Smile Dentistry", "city": "San Diego", "procedure": "Composite Filling", "cost": 140, "fake_data": "Actual Data"},
        {"name": "San Diego Smile Dentistry", "city": "San Diego", "procedure": "Extraction", "cost": 110, "fake_data": "Actual Data"},
        {"name": "San Diego Smile Dentistry", "city": "San Diego", "procedure": "Root Canal", "cost": 725, "fake_data": "Actual Data"},
        {"name": "San Diego Smile Dentistry", "city": "San Diego", "procedure": "Porcelain Crown", "cost": 850, "fake_data": "Actual Data"},
        {"name": "Advanced Smiles Dentistry", "city": "Tijuana", "procedure": "Adult Cleaning", "cost": 40, "fake_data": "Actual Data"},
        {"name": "Advanced Smiles Dentistry", "city": "Tijuana", "procedure": "Composite Filling", "cost": 40, "fake_data": "Actual Data"},
        {"name": "Advanced Smiles Dentistry", "city": "Tijuana", "procedure": "Extraction", "cost": 90, "fake_data": "Actual Data"},
        {"name": "Advanced Smiles Dentistry", "city": "Tijuana", "procedure": "Root Canal", "cost": 250, "fake_data": "Actual Data"},
        {"name": "Advanced Smiles Dentistry", "city": "Tijuana", "procedure": "Porcelain Crown", "cost": 450, "fake_data": "Actual Data"},
        {"name": "Great Smile Dental", "city": "San Diego", "procedure": "Adult Cleaning", "cost": 95, "fake_data": "Mock Data"},
        {"name": "Great Smile Dental", "city": "San Diego", "procedure": "Composite Filling", "cost": 120, "fake_data": "Mock Data"},
        {"name": "Great Smile Dental", "city": "San Diego", "procedure": "Extraction", "cost": 110, "fake_data": "Mock Data"},
        {"name": "Great Smile Dental", "city": "San Diego", "procedure": "Root Canal", "cost": 765, "fake_data": "Mock Data"},
        {"name": "Great Smile Dental", "city": "San Diego", "procedure": "Porcelain Crown", "cost": 1105, "fake_data": "Mock Data"},
        {"name": "Dental Express", "city": "San Diego", "procedure": "Adult Cleaning", "cost": 100, "fake_data": "Mock Data"},
        {"name": "Dental Express", "city": "San Diego", "procedure": "Composite Filling", "cost": 120, "fake_data": "Mock Data"},
        {"name": "Dental Express", "city": "San Diego", "procedure": "Extraction", "cost": 125, "fake_data": "Mock Data"},
        {"name": "Dental Express", "city": "San Diego", "procedure": "Root Canal", "cost": 785, "fake_data": "Mock Data"},
        {"name": "Dental Express", "city": "San Diego", "procedure": "Porcelain Crown", "cost": 950, "fake_data": "Mock Data"},
        {"name": "Smile Builders", "city": "Tijuana", "procedure": "Adult Cleaning", "cost": 45, "fake_data": "Mock Data"},
        {"name": "Smile Builders", "city": "Tijuana", "procedure": "Composite Filling", "cost": 75, "fake_data": "Mock Data"},
        {"name": "Smile Builders", "city": "Tijuana", "procedure": "Extraction", "cost": 80, "fake_data": "Mock Data"},
        {"name": "Smile Builders", "city": "Tijuana", "procedure": "Root Canal", "cost": 400, "fake_data": "Mock Data"},
        {"name": "Smile Builders", "city": "Tijuana", "procedure": "Porcelain Crown", "cost": 550, "fake_data": "Mock Data"},
        {"name": "Dr Ignacio de la Vega", "city": "Tijuana", "procedure": "Adult Cleaning", "cost": 40, "fake_data": "Actual Data"},
        {"name": "Dr Ignacio de la Vega", "city": "Tijuana", "procedure": "Composite Filling", "cost": 65, "fake_data": "Actual Data"},
        {"name": "Dr Ignacio de la Vega", "city": "Tijuana", "procedure": "Extraction", "cost": 85, "fake_data": "Actual Data"},
        {"name": "Dr Ignacio de la Vega", "city": "Tijuana", "procedure": "Root Canal", "cost": 260, "fake_data": "Actual Data"},
        {"name": "Dr Ignacio de la Vega", "city": "Tijuana", "procedure": "Porcelain Crown", "cost": 475, "fake_data": "Actual Data"}
    ];

    it("should return a properly formatted JSON array", function() {
        let result = assembleOverlayDataSet(sampleData);
        expect(result).toEqual([{"procedure":"Adult Cleaning", "sd_average":100, "tj_average":42},
            {"procedure":"Composite Filling", "sd_average":127, "tj_average":60},
            {"procedure":"Extraction", "sd_average":115, "tj_average":85},
            {"procedure":"Root Canal", "sd_average":758, "tj_average":303},
            {"procedure":"Porcelain Crown", "sd_average":968, "tj_average":492}]);
    });

    it("should return a JSON array length of 5", function() {
        let result = assembleOverlayDataSet(sampleData);
        expect(result.length).toBe(5);
    });

    it("should return two JSON arrays with a length of 3 each", function() {
        let result = sortDataByCity(sampleData);
        expect(result[0].length).toBe(3);
        expect(result[1].length).toBe(3);
    });

    it("should return two properly formatted JSON arrays", function() {
        let result = sortDataByCity(sampleData);
        expect(result[0]).toEqual([
            {"name": "San Diego Smile Dentistry", "city": "San Diego", "procedure": "Adult Cleaning", "cost": 105, "fake_data": "Actual Data"},
            {"name": "Great Smile Dental", "city": "San Diego", "procedure": "Adult Cleaning", "cost": 95, "fake_data": "Mock Data"},
            {"name": "Dental Express", "city": "San Diego", "procedure": "Adult Cleaning", "cost": 100, "fake_data": "Mock Data"},
        ]);
        expect(result[1]).toEqual([
            {"name": "Advanced Smiles Dentistry", "city": "Tijuana", "procedure": "Adult Cleaning", "cost": 40, "fake_data": "Actual Data"},
            {"name": "Smile Builders", "city": "Tijuana", "procedure": "Adult Cleaning", "cost": 45, "fake_data": "Mock Data"},
            {"name": "Dr Ignacio de la Vega", "city": "Tijuana", "procedure": "Adult Cleaning", "cost": 40, "fake_data": "Actual Data"},
        ])
    });

    it("should determine the number of Actual vs Mock Data for each city", function() {
        let cityData = sortDataByCity(sampleData);
        console.log('city data: ' + cityData.length);
        let result = determineMockDataTotals(cityData);
        console.log('result: ' + result[0][0].value);



        expect(result).toEqual([[{"label": "Actual Data", "value": 1}, {"label": "Mock Data", "value": 2}],[{"label": "Actual Data", "value": 2}, {"label": "Mock Data", "value": 1}]]);
    });

});