//CSRF-Token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//Logograb upload image -> get logoname
$("#logoGrabWebScannerButton").logoGrabWebScanner({
developerKey: "nb9n3ra9fpmrk0u0binh2b03jr3acq510tqhldmr",
    onInputImage: function(imageData) {
        // Callback invoked after the image has been uploaded to the device
    }, 
    onStart: function() {
        // Callback invoked before the image is uploaded to the server
    },
    onEnd: function(response) {
        // Callback invoked when the response JSON is returned
        if (!response.logoName) {
            $("#stage_result").html("No result");
        }
        else {
        $("#stage_result").html(response.logoName);
        }
        requestLogonameData(response.logoName);
    }
    }
);

//Post request -> give me all data associated with the logoname 
function requestLogonameData(logoName){
    var csrftoken = getCookie("csrftoken");
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
    .then((response) => response.json() // parses JSON response into native Javascript objects 
    ).then(
    (html) => console.log(html)
    );
    window.location.replace(url);
}