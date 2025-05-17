/**
 * Add Event Listener to run only after HTML document has completely loaded
 * - All code within this eventlistener will be accessible to the browser once the page has loaded.
 * 
 * @listens document#DOMContentLoaded - the namespace and name of the event
 */
document.addEventListener("DOMContentLoaded", function () {

    // Add eventListeners to .rod elements
    addHelpEventListeners();

    /**
     * Function to add event listeners to .help-head elements
     * - rodClick callback function is passed for to handle 'click' events on any .rod element 
     */
    function addHelpEventListeners() {
        const helpHeads = document.querySelectorAll(".help-head");
        console.log('Lets get them')
        for (let el of helpHeads) {
            el.addEventListener('click', toggleHelpExpand);

        }
    }

    function toggleHelpExpand(e) {
        const headElement = e.currentTarget;
        headElement.nextElementSibling.classList.toggle('hidden-item');
        const arrowElement = headElement.querySelector(".arrow-icons");
        arrowElement.classList.toggle('rotate');
        console.log('Clicked')
    }
});