document.addEventListener("DOMContentLoaded", function () {

    const checkIn = document.querySelector('input[name="check_in"]');
    const checkOut = document.querySelector('input[name="check_out"]');

    if (!checkIn || !checkOut) return;

    const today = new Date().toISOString().split("T")[0];

    checkIn.addEventListener("change", function () {

        if (checkIn.value < today) {
            alert("Check-in date cannot be in the past.");
            checkIn.value = "";
        }

        // Checkout cannot be before check-in
        checkOut.min = checkIn.value || today;
    });

    checkOut.addEventListener("change", function () {

        if (checkOut.value < checkIn.value) {
            alert("Check-out date must be after check-in date.");
            checkOut.value = "";
        }

    });

});
