document.addEventListener('DOMContentLoaded', () => {
    let fileInput = document.querySelector('.file input[type=file]');
    fileInput.onchange = function () {
        if (fileInput.files.length > 0) {
            let fileName = document.querySelector('.file-name');
            fileName.textContent = fileInput.files[0].name;
        }
    };

    let deleteButtons = document.querySelectorAll('.notification .delete');
    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            this.parentElement.style.display = 'none';
        });
    });
});

function toggleDropdown() {
    console.log("ping");
    let dropdown = document.querySelector('#dropdown-content');

    dropdown.classList.toggle('is-active');
}

document.addEventListener('DOMContentLoaded', () => {
    // Get all elements with the class 'dropdown-trigger'
    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger');

    dropdownTriggers.forEach(trigger => {
        // Add a click event listener to each dropdown trigger
        trigger.addEventListener('click', function (event) {
            // Stop the event from bubbling up
            event.stopPropagation();

            // Get the parent dropdown element
            const dropdown = trigger.closest('.dropdown');

            // Toggle the 'is-active' class on the parent dropdown element
            dropdown.classList.toggle('is-active');

            // Close all other dropdowns
            closeOtherDropdowns(dropdown);
        });
    });

    // Function to close other dropdowns except the current one
    function closeOtherDropdowns(currentDropdown) {
        dropdownTriggers.forEach(trigger => {
            const dropdown = trigger.closest('.dropdown');
            if (dropdown !== currentDropdown && dropdown.classList.contains('is-active')) {
                dropdown.classList.remove('is-active');
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    // Functions to open and close modals
    function openModal($el) {
        $el.classList.add('is-active');
    }

    function closeModal($el) {
        $el.classList.remove('is-active');
    }

    function closeAllModals() {
        (document.querySelectorAll('.modal') || []).forEach(($modal) => {
            closeModal($modal);
        });
    }

    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
        const modal = $trigger.dataset.target;
        const $target = document.getElementById(modal);

        $trigger.addEventListener('click', () => {
            openModal($target);
        });
    });

    // Add a click event on various child elements to close the parent modal
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
        const $target = $close.closest('.modal');

        $close.addEventListener('click', () => {
            closeModal($target);
        });
    });

    // Add a keyboard event to close all modals
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' || event.key === 'Esc') { // Escape key
            closeAllModals();
        }
    });
});
