/* Pet Transport Global - Main JS
   List filter, quote form submission, smooth scroll.
   Template provides: Bootstrap 5 collapse/accordion, navbar toggle, carousel.
*/

(function () {
    'use strict';

    // Prepare native submissions. Sensitive integrations are handled by
    // submit.php; credentials and customer payloads never belong in browser JS.
    var queryParams = new URLSearchParams(window.location.search);
    document.querySelectorAll('.quote-form').forEach(function (form) {
        var startedAt = document.createElement('input');
        startedAt.type = 'hidden';
        startedAt.name = 'form_started_at';
        startedAt.value = Math.floor(Date.now() / 1000).toString();
        form.appendChild(startedAt);

        ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(function (name) {
            var value = queryParams.get(name);
            if (!value) return;
            var input = document.createElement('input');
            input.type = 'hidden';
            input.name = name;
            input.value = value.slice(0, 200);
            form.appendChild(input);
        });

        var landingPage = document.createElement('input');
        landingPage.type = 'hidden';
        landingPage.name = 'landing_page';
        landingPage.value = window.location.href.slice(0, 1000);
        form.appendChild(landingPage);

        form.addEventListener('submit', function () {
            try {
                sessionStorage.setItem('ptgLeadSubmitted', '1');
            } catch (e) { /* conversion tracking must never block the form */ }
        });
    });

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

    // ===== MOBILE MEGAMENU TOGGLE =====
    // On small screens the hover megamenu is hidden; tap the trigger to reveal.
    var megaTriggers = document.querySelectorAll('.ptg-mega-trigger');
    megaTriggers.forEach(function (trigger) {
        trigger.addEventListener('click', function (e) {
            if (window.innerWidth >= 1200) return; // desktop uses CSS hover
            e.preventDefault();
            var parent = trigger.closest('.ptg-mega-parent');
            if (!parent) return;
            var isOpen = parent.classList.contains('ptg-open');
            // Close all open megamenus first
            document.querySelectorAll('.ptg-mega-parent.ptg-open').forEach(function (el) {
                el.classList.remove('ptg-open');
            });
            if (!isOpen) parent.classList.add('ptg-open');
        });
    });

    // ===== RESPONSIVE HERO VIDEO =====
    // Phones (< 576px):  portrait 9:16 crop — fills the screen correctly.
    // Tablets (576–991px): landscape 480p video.
    // Desktop (≥ 992px):  landscape 720p video.
    // Sources injected by JS so only the appropriate file is ever requested.
    (function () {
        var vid = document.getElementById('hero-vid');
        if (!vid) return;

        // Respect reduced-motion — skip loading so file is never requested
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

        var w = window.innerWidth;
        var webm, mp4;
        if (w < 576) {
            // Portrait crop fills phone screens properly
            webm = '/videos/hero-portrait.webm';
            mp4  = '/videos/hero-portrait.mp4';
            vid.classList.add('hero-video--portrait');
        } else if (w < 992) {
            webm = '/videos/hero-mobile.webm';
            mp4  = '/videos/hero-mobile.mp4';
        } else {
            webm = '/videos/hero.webm';
            mp4  = '/videos/hero.mp4';
        }

        var s1 = document.createElement('source');
        s1.type = 'video/webm';
        s1.src  = webm;
        vid.appendChild(s1);

        var s2 = document.createElement('source');
        s2.type = 'video/mp4';
        s2.src  = mp4;
        vid.appendChild(s2);

        vid.load();
    }());

})();
