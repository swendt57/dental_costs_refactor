
describe("maps - assembleCoordinates", function() {

    let dentists = [
        {"name": "San Diego Smile Dentistry", "latitude": "32.82225", "longitude": "-117.157913"},
        {"name": "Great Smile Dental", "latitude": "32.81897", "longitude": "-117.183968"},
        {"name": "Dental Express", "latitude": "32.753737", "longitude": "-117.223805"}
    ];

    it("should return [{lat: '32.82225', lng: '-117.157913', name: 'San Diego Smile Dentistry'},{lat: '32.81897', lng: '-117.183968', name: 'Great Smile Dental'},{lat: '32.753737', lng: '-117.223805', name: ' Dental Express'}]", function() {
        let result = assembleCoordinates(dentists);
        expect(result).toEqual([{lat: '32.82225', lng: '-117.157913', name: 'San Diego Smile Dentistry'},{lat: '32.81897', lng: '-117.183968', name: 'Great Smile Dental'},{lat: '32.753737', lng: '-117.223805', name: 'Dental Express'}]);
    });

    it("should return an array of length 3", function() {
        let result = assembleCoordinates(dentists);
        expect(result.length).toBe(3);
    });
});

