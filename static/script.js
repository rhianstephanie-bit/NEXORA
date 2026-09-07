function showRoleChoice() {

    document.querySelector(".landing").classList.add("hidden");

    document
        .getElementById("roleChoice")
        .classList.remove("hidden");

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


function chooseStudent() {

    window.location.href = "/student";

}


function chooseTeacher() {

    window.location.href = "/teacher";

}


if ("serviceWorker" in navigator) {

    window.addEventListener("load", () => {

        navigator.serviceWorker
            .register("/static/service-worker.js")
            .then(() => {

                console.log("NEXORA service worker registered!");

            })
            .catch(error => {

                console.log(
                    "Service worker registration failed:",
                    error
                );

            });

    });

}

 function getLocation() {

    const result = document.getElementById("location-result");

    if (!navigator.geolocation) {
        result.textContent = "Location is not supported by this browser.";
        return;
    }

    result.textContent = "Getting your location...";

    navigator.geolocation.getCurrentPosition(
        function(position) {

            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            result.innerHTML =
                "Latitude: " + latitude.toFixed(5) +
                "<br>Longitude: " + longitude.toFixed(5);
        },

        function() {
            result.textContent =
                "Location permission was denied or unavailable.";
        }
    );
}function getLocation() {

    const result = document.getElementById("location-result");

    if (!navigator.geolocation) {
        result.textContent = "Location is not supported by this browser.";
        return;
    }

    result.textContent = "Getting your location...";

    navigator.geolocation.getCurrentPosition(
        function(position) {

            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            result.innerHTML =
                "Latitude: " + latitude.toFixed(5) +
                "<br>Longitude: " + longitude.toFixed(5);
        },

        function() {
            result.textContent =
                "Location permission was denied or unavailable.";
        }
    );
}function getLocation() {

    const result = document.getElementById("location-result");

    if (!navigator.geolocation) {
        result.textContent = "Location is not supported by this browser.";
        return;
    }

    result.textContent = "Getting your location...";

    navigator.geolocation.getCurrentPosition(
        function(position) {

            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            result.innerHTML =
                "Latitude: " + latitude.toFixed(5) +
                "<br>Longitude: " + longitude.toFixed(5);
        },

        function() {
            result.textContent =
                "Location permission was denied or unavailable.";
        }
    );
}