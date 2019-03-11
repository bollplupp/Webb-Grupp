

var SL = require('https://api.sl.se/api2/TravelplannerV3_1/trip.<FORMAT>?key=<DIN API NYCKEL>&parametrar');
 
var sl = new SL({
    tripPlanner: "e8573d1eecc642ee8da3fbc6c5936fd8",
  }, 'json');

  sl.tripPlanner.trip({originId: 9118, destId: 9507}, callback);

  