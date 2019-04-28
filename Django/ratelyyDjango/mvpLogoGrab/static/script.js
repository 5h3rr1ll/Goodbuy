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
    canvas.width = w / 20;
    canvas.height = h / 20;			
}, false);

// Takes a snapshot of the video
function snap() {
    context.fillRect(0, 0, w, h);
    // Grab the image from the video
    context.drawImage(video, 0, 0, w / 20, h / 20);
    var canvas = document.getElementById("canvas");
    var dataUrl = canvas.toDataURL();
    console.log(dataUrl);
    alert("test");
    //uploadAndGetImgurLink(dataUrl);
    sendSnapToServerTwo(dataUrl);
};
/*
function sendToBackEnd(dataUrl){
    alert("POST clicked");
    var csrftoken = getCookie('csrftoken');
    const url = "http://127.0.0.1:8000/mvpLogoGrab/post/"
    fetch(url,{
                method: 'POST', 
                body: JSON.stringify(dataUrl), 
                headers: {
                        'Content-Type': "application/json",
                        'X-CSRFToken': csrftoken,
                },
                credentials: "include",
    })
    .then(response => response.json())
    .then(console.log);
   // window.location.replace(url);
};
*/

function sendSnapToServerTwo(dataUrl){
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://api.logograb.com/detect?mediaUrl="+ dataUrl +"&developerKey=nb9n3ra9fpmrk0u0binh2b03jr3acq510tqhldmr",
        "method": "POST",
        "headers": {}
      }
    
    
    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

//Post request -> Sends the picture to the server/api not defined yet
function sendSnapToServer(canvas){
        alert("POST clicked");
        var csrftoken = getCookie('csrftoken');
        const url = "http://127.0.0.1:8000/mvpLogoGrab/post/"
        fetch(url,{
                    method: 'POST', 
                    body: JSON.stringify(canvas), 
                    headers: {
                            'Content-Type': "application/json",
                            'X-CSRFToken': csrftoken,
                    },
                    credentials: "include",
        })
        .then(response => response.json())
        .then(console.log);
       // window.location.replace(url);
 };