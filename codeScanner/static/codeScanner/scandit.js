var ScanditSDK = require("scandit-sdk");

ScanditSDK.configure("UnIq998YicUgzxnFxrVjuGJSHI0D4PnvbxOnah8P0jw", {
  engineLocation: "build/"
});

ScanditSDK.BarcodePicker.create(document.getElementById("scandit-barcode-picker"), {
  playSoundOnScan: true,
  vibrateOnScan: true
}).then(function(barcodePicker) {
  // barcodePicker is ready here to be used (rest of the tutorial code should go here)
});
