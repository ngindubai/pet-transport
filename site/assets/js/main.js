/* Pet Transport Global - Main JS
   List filter, quote form submission, smooth scroll.
   Template provides: Bootstrap 5 collapse/accordion, navbar toggle, carousel.
*/

(function () {
    'use strict';

    // ===== QUOTE FORM SUBMISSION =====
    var forms = document.querySelectorAll('.quote-form');
    forms.forEach(function (form) {
        var successMsg = form.parentElement.querySelector('.quote-success');
        if (!successMsg) return;

        form.addEventListener('submit', function (e) {
            e.preventDefault();

            var required = form.querySelectorAll('[required]');
            var valid = true;
            required.forEach(function (field) {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    valid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });

            var emailField = form.querySelector('[type="email"]');
            if (emailField && emailField.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value)) {
                emailField.classList.add('is-invalid');
                valid = false;
            }

            var honeypot = form.querySelector('[name="website"]');
            if (honeypot && honeypot.value) return;

            if (!valid) return;

            var endpoint = form.getAttribute('action');
            if (!endpoint) {
                form.hidden = true;
                successMsg.hidden = false;
                return;
            }

            var data = new FormData(form);
            data.delete('website');

            fetch(endpoint, { method: 'POST', body: data })
                .then(function (res) {
                    if (res.ok) {
                        form.hidden = true;
                        successMsg.hidden = false;
                    }
                })
                .catch(function () { /* silent */ });
        });
    });

    // ===== LIST PAGE SEARCH / FILTER =====
    var filterInput = document.getElementById('listFilter');
    if (filterInput) {
        var targetGrid = document.getElementById('allItemsGrid');
        var filterCount = document.getElementById('filterCount');
        var noResults = document.getElementById('noResults');

        if (targetGrid) {
            var cards = targetGrid.querySelectorAll('[data-filter-title]');
            var totalCards = cards.length;

            filterInput.addEventListener('input', function () {
                var query = filterInput.value.toLowerCase().trim();
                var visible = 0;

                cards.forEach(function (card) {
                    var title = card.getAttribute('data-filter-title') || '';
                    if (!query || title.indexOf(query) !== -1) {
                        card.classList.remove('filter-hidden');
                        visible++;
                    } else {
                        card.classList.add('filter-hidden');
                    }
                });

                if (filterCount) {
                    filterCount.textContent = query ? visible + ' of ' + totalCards + ' shown' : '';
                }
                if (noResults) {
                    noResults.style.display = visible === 0 ? 'block' : 'none';
                }
            });
        }
    }
})();
