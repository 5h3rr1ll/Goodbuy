//CSRF-Token gets created for Post request validation
//Through an API the logoname of the object on an uploaded picture is recognized
//Through a database request all associated information is displayed
//Alternativly there is a videostream where you can take snapshots of the product
//Through a post request to the server where the picture is transformed into a png 
//and then send to the API to do the same as in the first method


//CSRF-Token
function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}

//Logograb upload image -> get logoname
$('#logoGrabWebScannerButton').logoGrabWebScanner({
developerKey: 'nb9n3ra9fpmrk0u0binh2b03jr3acq510tqhldmr',
    onInputImage: function(imageData) {
        // Callback invoked after the image has been uploaded to the device
    }, 
    onStart: function() {
        // Callback invoked before the image is uploaded to the server
    },
    onEnd: function(response) {
        // Callback invoked when the response JSON is returned
        if (!response.logoName)
        $('#stage_result').html("No result");
        else
        $('#stage_result').html(response.logoName);
        requestLogonameData(response.logoName);
    }
    }
);

//Post request -> give me all data associated with the logoname 
function requestLogonameData(logoName){
    var csrftoken = getCookie('csrftoken');
    const url = "http://127.0.0.1:8000/mvpLogoGrab/data/?name="+ logoName;
    fetch(url,{
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        credentials: "include",
        body: JSON.stringify(logoName), // body data type must match "Content-Type" header
    })
    .then(response => response.json() // parses JSON response into native Javascript objects 
    ).then(
    html => console.log(html)
    );
    window.location.replace(url);
}

//Creates a video stream
var video = document.querySelector("#videoElement");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
    video.srcObject = stream;
    })
    .catch(function (err0r) {
    console.log("Something went wrong!");
    });
}

var canvas = document.querySelector('canvas');
// Get a handle on the 2d context of the canvas element
var context = canvas.getContext('2d');
// Define some vars required later
var w, h, ratio;

// Add a listener to wait for the 'loadedmetadata' state so the video's dimensions can be read
video.addEventListener('loadedmetadata', function() {
    // Calculate the ratio of the video's width to height
    ratio = video.videoWidth / video.videoHeight;
    // Define the required width as 100 pixels smaller than the actual video's width
    w = video.videoWidth - 100;
    // Calculate the height based on the video's width and the ratio
    h = parseInt(w / ratio, 10);
    // Set the canvas width and height to the values just calculated
    canvas.width = w;
    canvas.height = h;			
}, false);

// Takes a snapshot of the video
function snap() {
    // Define the size of the rectangle that will be filled (basically the entire element)
    context.fillRect(0, 0, w, h);
    // Grab the image from the video
    var snap = context.drawImage(video, 0, 0, w, h);
    sendSnapToServer(snap);
};
//Post request -> Sends the picture to the server/api no defined yet
function sendSnapToServer(snap){
        alert("POST clicked");
        var csrftoken = getCookie('csrftoken');
        const url = "http://127.0.0.1:8000/mvpLogoGrab/post/"
        fetch(url,{
                    method: 'POST', 
                    body: JSON.stringify({snap}), 
                    headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken,
                    },
                    credentials: "include",
        })
        .then(res => res.json())
        .then(console.log);
 };       
 