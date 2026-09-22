// Wait until the page has loaded
document.addEventListener("DOMContentLoaded", function () {

    // Get all order buttons
    const orderButtons = document.querySelectorAll(".order-btn");

    // Add an event to every order button
    orderButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const foodName = button.getAttribute("data-food");

            alert("You selected: " + foodName);
        });

    });


    // Contact form
    const contactForm = document.getElementById("contactForm");

    contactForm.addEventListener("submit", function (event) {

        // Prevent the page from refreshing
        event.preventDefault();

        const name = document.getElementById("name").value;

        const formMessage = document.getElementById("formMessage");

        formMessage.innerHTML =
            "Thank you, " + name + "! Your message has been sent.";

        formMessage.classList.add("text-success");

        // Clear the form
        contactForm.reset();

    });

});