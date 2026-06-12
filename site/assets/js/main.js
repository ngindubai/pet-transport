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

    // ===== CRM INTAKE — native-POST quote forms =====
    // Quote forms without a .quote-success sibling submit natively to PHP.
    // Fire-and-forget to CRM with keepalive so the request survives page navigation.
    (function () {
        var CRM_URL = 'https://logistics-crm.onrender.com/api/public/leads';
        var CRM_KEY = 'uRc1IHymlMUnYfAB9i79iA3NUARQKFJdRCdo+4VDY/A=';
        var qs = new URLSearchParams(window.location.search);

        document.querySelectorAll('.quote-form').forEach(function (form) {
            // Skip forms handled by the AJAX block (those have a .quote-success sibling)
            if (form.parentElement && form.parentElement.querySelector('.quote-success')) return;

            form.addEventListener('submit', function () {
                var fd = new FormData(form);
                var name = (fd.get('name') || '').toString().trim() ||
                           (fd.get('email') || '').toString().split('@')[0] ||
                           'Website enquiry';
                try {
                    fetch(CRM_URL, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'x-api-key': CRM_KEY },
                        keepalive: true,
                        body: JSON.stringify({
                            company: 'pet-transport',
                            name: name,
                            email: fd.get('email') || undefined,
                            phone: fd.get('phone') || undefined,
                            source: 'PetTransport website',
                            landing_page: window.location.href,
                            utm_source: qs.get('utm_source') || undefined,
                            utm_medium: qs.get('utm_medium') || undefined,
                            utm_campaign: qs.get('utm_campaign') || undefined,
                            utm_keyword: qs.get('utm_keyword') || undefined,
                            message: fd.get('message') || undefined,
                            fields: {
                                originCountry: fd.get('origin_country') || undefined,
                                destCountry: fd.get('destination_country') || undefined,
                                petType: fd.get('pet_type') || undefined,
                                breed: fd.get('breed') || undefined,
                                weight: fd.get('pet_weight_kg') || undefined,
                                travelDate: fd.get('travel_date') || undefined
                            }
                        })
                    });
                } catch (e) { /* swallow — never block native submit */ }
            });
        });
    }());


})();
