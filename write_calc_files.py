"""
Rebuild the cost calculator layout and content files.
Restores the superior ptg-calc implementation (75 countries, USD, Bootstrap, event listeners).
"""
import os

LAYOUT = r"""{{ define "schema" }}
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": {{ .Title | jsonify }},
    "description": {{ .Description | jsonify }},
    "applicationCategory": "UtilityApplication",
    "operatingSystem": "Any",
    "browserRequirements": "Requires JavaScript",
    "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
    },
    "publisher": {
        "@type": "Organization",
        "name": "PetTransportGlobal",
        "url": "https://pettransportglobal.com"
    },
    "datePublished": {{ .Date.Format "2006-01-02" | jsonify }},
    "dateModified": {{ .Lastmod.Format "2006-01-02" | jsonify }}
}
</script>
{{ with .Params.faqs }}
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {{ range $i, $faq := . }}{{ if $i }},{{ end }}
        {
            "@type": "Question",
            "name": {{ $faq.question | jsonify }},
            "acceptedAnswer": {
                "@type": "Answer",
                "text": {{ $faq.answer | jsonify }}
            }
        }
        {{ end }}
    ]
}
</script>
{{ end }}
{{ end }}

{{ define "main" }}
<section class="route-section">
    <div class="section-inner">
        <h1>{{ .Title }}</h1>
        {{ .Content }}

        <div id="ptg-calc" class="ptg-calc" aria-live="polite">
            <form id="ptg-calc-form" class="ptg-calc-form" novalidate>
                <div class="ptg-calc-row">
                    <label for="calc-origin">Origin country</label>
                    <select id="calc-origin" name="origin" required>
                        <option value="">Select origin...</option>
                        <option value="argentina">Argentina</option>
                        <option value="australia">Australia</option>
                        <option value="austria">Austria</option>
                        <option value="bahrain">Bahrain</option>
                        <option value="bangladesh">Bangladesh</option>
                        <option value="belgium">Belgium</option>
                        <option value="brazil">Brazil</option>
                        <option value="bulgaria">Bulgaria</option>
                        <option value="cambodia">Cambodia</option>
                        <option value="canada">Canada</option>
                        <option value="chile">Chile</option>
                        <option value="china">China</option>
                        <option value="colombia">Colombia</option>
                        <option value="costa-rica">Costa Rica</option>
                        <option value="croatia">Croatia</option>
                        <option value="cyprus">Cyprus</option>
                        <option value="czech-republic">Czech Republic</option>
                        <option value="denmark">Denmark</option>
                        <option value="ecuador">Ecuador</option>
                        <option value="egypt">Egypt</option>
                        <option value="ethiopia">Ethiopia</option>
                        <option value="finland">Finland</option>
                        <option value="france">France</option>
                        <option value="germany">Germany</option>
                        <option value="ghana">Ghana</option>
                        <option value="greece">Greece</option>
                        <option value="hong-kong">Hong Kong</option>
                        <option value="hungary">Hungary</option>
                        <option value="india">India</option>
                        <option value="indonesia">Indonesia</option>
                        <option value="ireland">Ireland</option>
                        <option value="israel">Israel</option>
                        <option value="italy">Italy</option>
                        <option value="japan">Japan</option>
                        <option value="jordan">Jordan</option>
                        <option value="kenya">Kenya</option>
                        <option value="kuwait">Kuwait</option>
                        <option value="luxembourg">Luxembourg</option>
                        <option value="malaysia">Malaysia</option>
                        <option value="malta">Malta</option>
                        <option value="mauritius">Mauritius</option>
                        <option value="mexico">Mexico</option>
                        <option value="morocco">Morocco</option>
                        <option value="myanmar">Myanmar</option>
                        <option value="nepal">Nepal</option>
                        <option value="netherlands">Netherlands</option>
                        <option value="new-zealand">New Zealand</option>
                        <option value="nigeria">Nigeria</option>
                        <option value="norway">Norway</option>
                        <option value="oman">Oman</option>
                        <option value="pakistan">Pakistan</option>
                        <option value="peru">Peru</option>
                        <option value="philippines">Philippines</option>
                        <option value="poland">Poland</option>
                        <option value="portugal">Portugal</option>
                        <option value="qatar">Qatar</option>
                        <option value="romania">Romania</option>
                        <option value="saudi-arabia">Saudi Arabia</option>
                        <option value="singapore">Singapore</option>
                        <option value="slovakia">Slovakia</option>
                        <option value="south-africa">South Africa</option>
                        <option value="south-korea">South Korea</option>
                        <option value="spain">Spain</option>
                        <option value="sri-lanka">Sri Lanka</option>
                        <option value="sweden">Sweden</option>
                        <option value="switzerland">Switzerland</option>
                        <option value="taiwan">Taiwan</option>
                        <option value="tanzania">Tanzania</option>
                        <option value="thailand">Thailand</option>
                        <option value="turkey">Turkey</option>
                        <option value="united-arab-emirates">United Arab Emirates</option>
                        <option value="united-kingdom">United Kingdom</option>
                        <option value="united-states">United States</option>
                        <option value="vietnam">Vietnam</option>
                        <option value="zimbabwe">Zimbabwe</option>
                    </select>
                </div>
                <div class="ptg-calc-row">
                    <label for="calc-destination">Destination country</label>
                    <select id="calc-destination" name="destination" required>
                        <option value="">Select destination...</option>
                        <option value="argentina">Argentina</option>
                        <option value="australia">Australia</option>
                        <option value="austria">Austria</option>
                        <option value="bahrain">Bahrain</option>
                        <option value="bangladesh">Bangladesh</option>
                        <option value="belgium">Belgium</option>
                        <option value="brazil">Brazil</option>
                        <option value="bulgaria">Bulgaria</option>
                        <option value="cambodia">Cambodia</option>
                        <option value="canada">Canada</option>
                        <option value="chile">Chile</option>
                        <option value="china">China</option>
                        <option value="colombia">Colombia</option>
                        <option value="costa-rica">Costa Rica</option>
                        <option value="croatia">Croatia</option>
                        <option value="cyprus">Cyprus</option>
                        <option value="czech-republic">Czech Republic</option>
                        <option value="denmark">Denmark</option>
                        <option value="ecuador">Ecuador</option>
                        <option value="egypt">Egypt</option>
                        <option value="ethiopia">Ethiopia</option>
                        <option value="finland">Finland</option>
                        <option value="france">France</option>
                        <option value="germany">Germany</option>
                        <option value="ghana">Ghana</option>
                        <option value="greece">Greece</option>
                        <option value="hong-kong">Hong Kong</option>
                        <option value="hungary">Hungary</option>
                        <option value="india">India</option>
                        <option value="indonesia">Indonesia</option>
                        <option value="ireland">Ireland</option>
                        <option value="israel">Israel</option>
                        <option value="italy">Italy</option>
                        <option value="japan">Japan</option>
                        <option value="jordan">Jordan</option>
                        <option value="kenya">Kenya</option>
                        <option value="kuwait">Kuwait</option>
                        <option value="luxembourg">Luxembourg</option>
                        <option value="malaysia">Malaysia</option>
                        <option value="malta">Malta</option>
                        <option value="mauritius">Mauritius</option>
                        <option value="mexico">Mexico</option>
                        <option value="morocco">Morocco</option>
                        <option value="myanmar">Myanmar</option>
                        <option value="nepal">Nepal</option>
                        <option value="netherlands">Netherlands</option>
                        <option value="new-zealand">New Zealand</option>
                        <option value="nigeria">Nigeria</option>
                        <option value="norway">Norway</option>
                        <option value="oman">Oman</option>
                        <option value="pakistan">Pakistan</option>
                        <option value="peru">Peru</option>
                        <option value="philippines">Philippines</option>
                        <option value="poland">Poland</option>
                        <option value="portugal">Portugal</option>
                        <option value="qatar">Qatar</option>
                        <option value="romania">Romania</option>
                        <option value="saudi-arabia">Saudi Arabia</option>
                        <option value="singapore">Singapore</option>
                        <option value="slovakia">Slovakia</option>
                        <option value="south-africa">South Africa</option>
                        <option value="south-korea">South Korea</option>
                        <option value="spain">Spain</option>
                        <option value="sri-lanka">Sri Lanka</option>
                        <option value="sweden">Sweden</option>
                        <option value="switzerland">Switzerland</option>
                        <option value="taiwan">Taiwan</option>
                        <option value="tanzania">Tanzania</option>
                        <option value="thailand">Thailand</option>
                        <option value="turkey">Turkey</option>
                        <option value="united-arab-emirates">United Arab Emirates</option>
                        <option value="united-kingdom">United Kingdom</option>
                        <option value="united-states">United States</option>
                        <option value="vietnam">Vietnam</option>
                        <option value="zimbabwe">Zimbabwe</option>
                    </select>
                </div>
                <div class="ptg-calc-row">
                    <label for="calc-weight">Pet weight (kg, including crate)</label>
                    <input id="calc-weight" name="weight" type="number" min="0.5" max="120" step="0.5" placeholder="e.g. 12" required>
                </div>
                <div class="ptg-calc-row">
                    <label for="calc-pet-type">Pet type</label>
                    <select id="calc-pet-type" name="petType">
                        <option value="dog">Dog</option>
                        <option value="cat">Cat</option>
                        <option value="other">Other small mammal / bird</option>
                    </select>
                </div>
                <div class="ptg-calc-row ptg-calc-checks">
                    <label class="ptg-check"><input type="checkbox" id="calc-vacc" name="vacc" checked> <span>Include vaccinations &amp; rabies titre test</span></label>
                    <label class="ptg-check"><input type="checkbox" id="calc-agent" name="agent"> <span>Use a relocation agent (door-to-door service)</span></label>
                </div>
                <div class="ptg-calc-actions">
                    <button type="submit" class="btn btn-primary">Estimate cost</button>
                    <button type="reset" class="btn btn-outline-secondary">Reset</button>
                </div>
            </form>

            <div id="calc-result" class="ptg-calc-result" hidden>
                <h2>Estimated cost range</h2>
                <p class="ptg-calc-range" id="calc-range" aria-live="polite"></p>
                <p class="ptg-calc-tier" id="calc-tier"></p>
                <h3>Breakdown</h3>
                <table class="ptg-calc-table">
                    <thead><tr><th>Component</th><th class="ptg-num">Low (USD)</th><th class="ptg-num">High (USD)</th></tr></thead>
                    <tbody id="calc-breakdown"></tbody>
                    <tfoot><tr><th>Total</th><th class="ptg-num" id="calc-total-low"></th><th class="ptg-num" id="calc-total-high"></th></tr></tfoot>
                </table>
                <p class="ptg-calc-disclaimer">All figures are indicative ranges based on 2025-2026 industry pricing. Actual costs vary by airline, season, agent, and routing. Always obtain a written quote before committing.</p>
                <p class="ptg-calc-cta"><a class="btn btn-primary" href="/contact/">Get a written quote for your route</a></p>
            </div>

            <div id="calc-error" class="ptg-calc-error" hidden role="alert"></div>
        </div>

        {{ with .Params.faqs }}
        <div class="mb-5" id="faq-section">
            <div class="section-heading text-start"><h2>Frequently Asked Questions</h2></div>
            <div class="accordion" id="faqAccordion">
                {{ range $i, $faq := . }}
                <div class="accordion-item">
                    <h2 class="accordion-header" id="faq-head-{{ $i }}">
                        <button class="{{ if $i }}accordion-button collapsed{{ else }}accordion-button{{ end }}" type="button"
                            data-bs-toggle="collapse" data-bs-target="#faq-body-{{ $i }}"
                            aria-expanded="{{ if $i }}false{{ else }}true{{ end }}" aria-controls="faq-body-{{ $i }}">
                            {{ $faq.question }}
                        </button>
                    </h2>
                    <div id="faq-body-{{ $i }}" class="{{ if $i }}accordion-collapse collapse{{ else }}accordion-collapse collapse show{{ end }}"
                        aria-labelledby="faq-head-{{ $i }}" data-bs-parent="#faqAccordion">
                        <div class="accordion-body">{{ $faq.answer }}</div>
                    </div>
                </div>
                {{ end }}
            </div>
        </div>
        {{ end }}

    </div>
</section>

<script id="ptg-calc-data" type="application/json">
{
    "agent_usd": [500, 2500],
    "countries": {
        "argentina": {"name": "Argentina", "quarantine_usd": [0, 0], "region": "SA"},
        "australia": {"name": "Australia", "quarantine_usd": [2000, 3500], "region": "OC"},
        "austria": {"name": "Austria", "quarantine_usd": [0, 0], "region": "EU-W"},
        "bahrain": {"name": "Bahrain", "quarantine_usd": [0, 200], "region": "ME"},
        "bangladesh": {"name": "Bangladesh", "quarantine_usd": [200, 500], "region": "AS-S"},
        "belgium": {"name": "Belgium", "quarantine_usd": [0, 0], "region": "EU-W"},
        "brazil": {"name": "Brazil", "quarantine_usd": [0, 300], "region": "SA"},
        "bulgaria": {"name": "Bulgaria", "quarantine_usd": [0, 0], "region": "EU-E"},
        "cambodia": {"name": "Cambodia", "quarantine_usd": [200, 500], "region": "AS-SE"},
        "canada": {"name": "Canada", "quarantine_usd": [0, 0], "region": "NA"},
        "chile": {"name": "Chile", "quarantine_usd": [0, 200], "region": "SA"},
        "china": {"name": "China", "quarantine_usd": [400, 800], "region": "AS-E"},
        "colombia": {"name": "Colombia", "quarantine_usd": [0, 0], "region": "SA"},
        "costa-rica": {"name": "Costa Rica", "quarantine_usd": [0, 200], "region": "NA"},
        "croatia": {"name": "Croatia", "quarantine_usd": [0, 0], "region": "EU-E"},
        "cyprus": {"name": "Cyprus", "quarantine_usd": [0, 0], "region": "EU-W"},
        "czech-republic": {"name": "Czech Republic", "quarantine_usd": [0, 0], "region": "EU-E"},
        "denmark": {"name": "Denmark", "quarantine_usd": [0, 0], "region": "EU-W"},
        "ecuador": {"name": "Ecuador", "quarantine_usd": [0, 200], "region": "SA"},
        "egypt": {"name": "Egypt", "quarantine_usd": [0, 300], "region": "AF-N"},
        "ethiopia": {"name": "Ethiopia", "quarantine_usd": [0, 300], "region": "AF-S"},
        "finland": {"name": "Finland", "quarantine_usd": [0, 0], "region": "EU-W"},
        "france": {"name": "France", "quarantine_usd": [0, 0], "region": "EU-W"},
        "germany": {"name": "Germany", "quarantine_usd": [0, 0], "region": "EU-W"},
        "ghana": {"name": "Ghana", "quarantine_usd": [0, 300], "region": "AF-S"},
        "greece": {"name": "Greece", "quarantine_usd": [0, 0], "region": "EU-W"},
        "hong-kong": {"name": "Hong Kong", "quarantine_usd": [0, 0], "region": "AS-E"},
        "hungary": {"name": "Hungary", "quarantine_usd": [0, 0], "region": "EU-E"},
        "india": {"name": "India", "quarantine_usd": [200, 500], "region": "AS-S"},
        "indonesia": {"name": "Indonesia", "quarantine_usd": [300, 600], "region": "AS-SE"},
        "ireland": {"name": "Ireland", "quarantine_usd": [0, 0], "region": "EU-W"},
        "israel": {"name": "Israel", "quarantine_usd": [0, 200], "region": "ME"},
        "italy": {"name": "Italy", "quarantine_usd": [0, 0], "region": "EU-W"},
        "japan": {"name": "Japan", "quarantine_usd": [0, 300], "region": "AS-E"},
        "jordan": {"name": "Jordan", "quarantine_usd": [0, 200], "region": "ME"},
        "kenya": {"name": "Kenya", "quarantine_usd": [0, 300], "region": "AF-S"},
        "kuwait": {"name": "Kuwait", "quarantine_usd": [0, 200], "region": "ME"},
        "luxembourg": {"name": "Luxembourg", "quarantine_usd": [0, 0], "region": "EU-W"},
        "malaysia": {"name": "Malaysia", "quarantine_usd": [300, 600], "region": "AS-SE"},
        "malta": {"name": "Malta", "quarantine_usd": [0, 0], "region": "EU-W"},
        "mauritius": {"name": "Mauritius", "quarantine_usd": [400, 800], "region": "AF-S"},
        "mexico": {"name": "Mexico", "quarantine_usd": [0, 0], "region": "NA"},
        "morocco": {"name": "Morocco", "quarantine_usd": [0, 200], "region": "AF-N"},
        "myanmar": {"name": "Myanmar", "quarantine_usd": [200, 500], "region": "AS-SE"},
        "nepal": {"name": "Nepal", "quarantine_usd": [200, 500], "region": "AS-S"},
        "netherlands": {"name": "Netherlands", "quarantine_usd": [0, 0], "region": "EU-W"},
        "new-zealand": {"name": "New Zealand", "quarantine_usd": [1800, 3000], "region": "OC"},
        "nigeria": {"name": "Nigeria", "quarantine_usd": [0, 300], "region": "AF-S"},
        "norway": {"name": "Norway", "quarantine_usd": [0, 0], "region": "EU-W"},
        "oman": {"name": "Oman", "quarantine_usd": [0, 200], "region": "ME"},
        "pakistan": {"name": "Pakistan", "quarantine_usd": [200, 500], "region": "AS-S"},
        "peru": {"name": "Peru", "quarantine_usd": [0, 200], "region": "SA"},
        "philippines": {"name": "Philippines", "quarantine_usd": [200, 500], "region": "AS-SE"},
        "poland": {"name": "Poland", "quarantine_usd": [0, 0], "region": "EU-E"},
        "portugal": {"name": "Portugal", "quarantine_usd": [0, 0], "region": "EU-W"},
        "qatar": {"name": "Qatar", "quarantine_usd": [0, 200], "region": "ME"},
        "romania": {"name": "Romania", "quarantine_usd": [0, 0], "region": "EU-E"},
        "saudi-arabia": {"name": "Saudi Arabia", "quarantine_usd": [0, 200], "region": "ME"},
        "singapore": {"name": "Singapore", "quarantine_usd": [0, 200], "region": "AS-SE"},
        "slovakia": {"name": "Slovakia", "quarantine_usd": [0, 0], "region": "EU-E"},
        "south-africa": {"name": "South Africa", "quarantine_usd": [0, 300], "region": "AF-S"},
        "south-korea": {"name": "South Korea", "quarantine_usd": [200, 500], "region": "AS-E"},
        "spain": {"name": "Spain", "quarantine_usd": [0, 0], "region": "EU-W"},
        "sri-lanka": {"name": "Sri Lanka", "quarantine_usd": [200, 500], "region": "AS-S"},
        "sweden": {"name": "Sweden", "quarantine_usd": [0, 0], "region": "EU-W"},
        "switzerland": {"name": "Switzerland", "quarantine_usd": [0, 0], "region": "EU-W"},
        "taiwan": {"name": "Taiwan", "quarantine_usd": [800, 2000], "region": "AS-E"},
        "tanzania": {"name": "Tanzania", "quarantine_usd": [0, 300], "region": "AF-S"},
        "thailand": {"name": "Thailand", "quarantine_usd": [300, 600], "region": "AS-SE"},
        "turkey": {"name": "Turkey", "quarantine_usd": [0, 200], "region": "EU-E"},
        "united-arab-emirates": {"name": "United Arab Emirates", "quarantine_usd": [0, 200], "region": "ME"},
        "united-kingdom": {"name": "United Kingdom", "quarantine_usd": [0, 0], "region": "EU-W"},
        "united-states": {"name": "United States", "quarantine_usd": [0, 0], "region": "NA"},
        "vietnam": {"name": "Vietnam", "quarantine_usd": [200, 500], "region": "AS-SE"},
        "zimbabwe": {"name": "Zimbabwe", "quarantine_usd": [0, 300], "region": "AF-S"}
    },
    "crate_buckets": [
        {"cost_usd": [80, 200], "label": "S/M (up to 8 kg)", "max_kg": 8},
        {"cost_usd": [150, 300], "label": "M/L (8-20 kg)", "max_kg": 20},
        {"cost_usd": [250, 450], "label": "L (20-40 kg)", "max_kg": 40},
        {"cost_usd": [400, 750], "label": "XL (40-70 kg)", "max_kg": 70},
        {"cost_usd": [600, 1200], "label": "Giant (70 kg+)", "max_kg": 999}
    ],
    "currency": "USD",
    "disclaimer": "All figures are indicative ranges based on 2025-2026 industry pricing. Actual costs vary by airline, season, agent, and routing. Always obtain a written quote before committing.",
    "ground_transport_usd": [100, 400],
    "last_updated": "2026-05-01",
    "regions": {
        "AF-N": "North Africa",
        "AF-S": "Sub-Saharan Africa",
        "AS-E": "East Asia",
        "AS-S": "South Asia",
        "AS-SE": "Southeast Asia",
        "EU-E": "Central & Eastern Europe",
        "EU-W": "Western Europe",
        "ME": "Middle East",
        "NA": "North America",
        "OC": "Oceania",
        "SA": "South America"
    },
    "tier_air_freight_usd": {"1": [800, 1800], "2": [1800, 3500], "3": [3500, 6500], "4": [5500, 9500]},
    "tier_descriptions": {
        "1": "Short-haul within the same region",
        "2": "Medium intercontinental",
        "3": "Long intercontinental",
        "4": "Oceania-bound (Australia or New Zealand)"
    },
    "vaccinations_titre_usd": [250, 650],
    "vet_paperwork_usd": [200, 500]
}
</script>

<style>
.ptg-calc { background: #f8f9fa; border: 1px solid #e5e7eb; border-radius: 12px; padding: 1.5rem; margin: 2rem 0; }
.ptg-calc-form { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.25rem; }
.ptg-calc-row { display: flex; flex-direction: column; gap: 0.4rem; }
.ptg-calc-row.ptg-calc-checks { grid-column: 1 / -1; flex-direction: row; flex-wrap: wrap; gap: 1.25rem; }
.ptg-calc label { font-weight: 600; font-size: 0.92rem; color: #1f2937; }
.ptg-calc input[type="number"], .ptg-calc select { padding: 0.55rem 0.75rem; border: 1px solid #d1d5db; border-radius: 8px; font-size: 0.95rem; background: #fff; }
.ptg-calc input[type="number"]:focus, .ptg-calc select:focus { outline: 2px solid #2563eb; outline-offset: 1px; }
.ptg-check { display: flex; align-items: center; gap: 0.5rem; font-weight: 500; }
.ptg-calc-actions { grid-column: 1 / -1; display: flex; gap: 0.75rem; margin-top: 0.5rem; }
.ptg-calc-result { margin-top: 1.75rem; padding-top: 1.5rem; border-top: 1px solid #e5e7eb; }
.ptg-calc-range { font-size: 1.6rem; font-weight: 700; color: #2563eb; margin: 0.5rem 0; }
.ptg-calc-tier { color: #4b5563; font-size: 0.95rem; margin-bottom: 1rem; }
.ptg-calc-table { width: 100%; border-collapse: collapse; margin: 0.75rem 0 1rem; font-size: 0.92rem; }
.ptg-calc-table th, .ptg-calc-table td { padding: 0.55rem 0.75rem; border-bottom: 1px solid #e5e7eb; text-align: left; }
.ptg-calc-table .ptg-num { text-align: right; font-variant-numeric: tabular-nums; }
.ptg-calc-table tfoot th { border-top: 2px solid #1f2937; border-bottom: none; font-size: 1rem; }
.ptg-calc-disclaimer { font-size: 0.82rem; color: #6b7280; font-style: italic; margin: 0.75rem 0 1rem; }
.ptg-calc-cta { margin-top: 1rem; }
.ptg-calc-error { margin-top: 1rem; padding: 0.75rem 1rem; background: #fee2e2; border: 1px solid #fecaca; color: #991b1b; border-radius: 8px; }
@media (max-width: 640px) { .ptg-calc-form { grid-template-columns: 1fr; } }
</style>

<script>
(function () {
    var data = JSON.parse(document.getElementById('ptg-calc-data').textContent);
    var form = document.getElementById('ptg-calc-form');
    var resultBox = document.getElementById('calc-result');
    var errorBox = document.getElementById('calc-error');
    var oceanic = ['OC'];

    function getTier(regionA, regionB) {
        if (oceanic.indexOf(regionA) !== -1 || oceanic.indexOf(regionB) !== -1) return 4;
        if (regionA === regionB) return 1;
        var superRegion = function (r) {
            if (r === 'NA' || r === 'SA') return 'AM';
            if (r === 'EU-W' || r === 'EU-E') return 'EU';
            if (r === 'AS-S' || r === 'AS-SE' || r === 'AS-E') return 'AS';
            if (r === 'AF-N' || r === 'AF-S') return 'AF';
            return r;
        };
        return superRegion(regionA) === superRegion(regionB) ? 2 : 3;
    }

    function getCrateBucket(kg) {
        for (var i = 0; i < data.crate_buckets.length; i++) {
            if (kg <= data.crate_buckets[i].max_kg) return data.crate_buckets[i];
        }
        return data.crate_buckets[data.crate_buckets.length - 1];
    }

    function formatUSD(n) {
        return '$' + Math.round(n).toLocaleString('en-US');
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        errorBox.hidden = true;
        resultBox.hidden = true;

        var origin = form.origin.value;
        var dest = form.destination.value;
        var weight = parseFloat(form.weight.value);
        var inclVacc = form.vacc.checked;
        var inclAgent = form.agent.checked;

        if (!origin || !dest) {
            errorBox.textContent = 'Please select both origin and destination countries.';
            errorBox.hidden = false;
            return;
        }
        if (origin === dest) {
            errorBox.textContent = 'Origin and destination cannot be the same.';
            errorBox.hidden = false;
            return;
        }
        if (!weight || weight < 0.5 || weight > 120) {
            errorBox.textContent = 'Please enter a pet weight between 0.5 and 120 kg.';
            errorBox.hidden = false;
            return;
        }

        var originData = data.countries[origin];
        var destData = data.countries[dest];
        var tier = getTier(originData.region, destData.region);
        var airFreight = data.tier_air_freight_usd[String(tier)];
        var crate = getCrateBucket(weight);
        var vetPaperwork = data.vet_paperwork_usd;
        var vaccinations = inclVacc ? data.vaccinations_titre_usd : [0, 0];
        var groundTransport = data.ground_transport_usd;
        var agentFee = inclAgent ? data.agent_usd : [0, 0];
        var quarantine = destData.quarantine_usd;

        var rows = [
            ['Air freight (' + data.tier_descriptions[String(tier)] + ')', airFreight],
            ['IATA-compliant crate (' + crate.label + ')', crate.cost_usd],
            ['Vet checks &amp; export paperwork', vetPaperwork]
        ];
        if (inclVacc) rows.push(['Vaccinations + rabies titre test', vaccinations]);
        rows.push(['Ground transport (origin + destination)', groundTransport]);
        if (quarantine[1] > 0) rows.push(['Quarantine in ' + destData.name, quarantine]);
        if (inclAgent) rows.push(['Relocation agent (door-to-door)', agentFee]);

        var totalLow = 0, totalHigh = 0;
        var tbody = document.getElementById('calc-breakdown');
        tbody.innerHTML = '';
        rows.forEach(function (row) {
            totalLow += row[1][0];
            totalHigh += row[1][1];
            var tr = document.createElement('tr');
            tr.innerHTML = '<td>' + row[0] + '</td><td class="ptg-num">' + formatUSD(row[1][0]) + '</td><td class="ptg-num">' + formatUSD(row[1][1]) + '</td>';
            tbody.appendChild(tr);
        });

        document.getElementById('calc-total-low').textContent = formatUSD(totalLow);
        document.getElementById('calc-total-high').textContent = formatUSD(totalHigh);
        document.getElementById('calc-range').textContent = formatUSD(totalLow) + ' - ' + formatUSD(totalHigh) + ' USD';
        document.getElementById('calc-tier').textContent = originData.name + ' to ' + destData.name + ' (Tier ' + tier + ': ' + data.tier_descriptions[String(tier)] + ')';
        resultBox.hidden = false;
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });

    form.addEventListener('reset', function () {
        resultBox.hidden = true;
        errorBox.hidden = true;
    });
}());
</script>
{{ end }}
"""

CONTENT = """---
title: "Pet Transport Cost Calculator | Estimate Your International Move"
description: "Free pet transport cost calculator. Estimate the price of shipping your dog or cat between 75 countries, with breakdowns for air freight, crate, vet, vaccinations, and quarantine."
date: "2026-05-01"
lastmod: "2026-05-01"
layout: "cost-calculator"
url: "/pet-transport/resources/pet-transport-cost-calculator/"
faqs:
  - question: "How accurate is this pet transport cost estimate?"
    answer: "The estimate gives an indicative range based on 2025-2026 industry pricing across 75 countries. Real quotes vary by airline, season, agent, and routing. Treat the figure as a budgeting starting point and always obtain a written quote from a registered pet transporter before committing."
  - question: "What does the cost include?"
    answer: "Air freight, an IATA-compliant crate sized to your pet, vet checks and export paperwork, optional vaccinations and rabies titre test, ground transport at origin and destination, mandatory quarantine fees if the destination requires it, and an optional relocation agent for door-to-door service."
  - question: "What is not included in the estimate?"
    answer: "Boarding before flight, emergency vet care, customs duties on personal effects, premium airline pet cabins (where allowed), and unusual routing surcharges. Snub-nosed (brachycephalic) breeds may face higher airline costs or be refused entirely - confirm with the carrier."
  - question: "Why is shipping a pet to Australia or New Zealand so expensive?"
    answer: "Australia and New Zealand have the world's strictest biosecurity rules. Mandatory 10-day government quarantine, limited approved arrival airlines, additional pre-export blood tests, and an approved pet shipping agent for the import permit all add cost. Budget USD 5,500-9,500 minimum, plus AUD 4,000+ for Australian quarantine."
  - question: "Can I use the cost calculator for cargo and cabin pets?"
    answer: "The calculator estimates manifest cargo (the most common option for international moves). In-cabin pet travel is only allowed by some airlines for small pets on short-haul routes; expect lower air freight cost but the same vet, paperwork, and quarantine costs."
  - question: "Are agent fees mandatory?"
    answer: "No. You can self-handle the move if you're comfortable with airline cargo bookings, customs paperwork, and import permits. Australia, New Zealand, the UK, and several Asian destinations effectively require an agent because of permit and arrival logistics. For other routes, an agent typically adds USD 500-2,500 but saves significant time and stress."
---
Use this tool to estimate the cost of moving your dog or cat internationally between any of the 75 countries we cover. The calculator combines air freight, crate, vet paperwork, vaccinations, ground transport, quarantine fees, and optional agent costs into a single budgeting range.

The estimate is indicative. Real-world quotes depend on your departure and arrival airports, the specific carrier you book, the time of year, and your pet's breed (snub-nosed dogs and cats face airline restrictions and higher fees). Always get a written quote from a registered pet transporter before committing.

## How the calculator works

We sort routes into four pricing tiers:

- **Tier 1** - Same region (e.g. UK to France, US to Canada): USD 800-1,800 air freight
- **Tier 2** - Medium intercontinental (e.g. Europe to Middle East, US to Brazil): USD 1,800-3,500
- **Tier 3** - Long intercontinental (e.g. UK to Singapore, US to Japan): USD 3,500-6,500
- **Tier 4** - Anything to or from Australia or New Zealand: USD 5,500-9,500

Crate cost is sized to your pet's weight (including the crate itself). Quarantine cost is loaded automatically from the destination country's official rules. The vaccinations and titre test option adds rabies serology - mandatory for rabies-free destinations like the UK, EU, Australia, New Zealand, and Hawaii.
"""

base = os.path.dirname(os.path.abspath(__file__))
layout_path = os.path.join(base, "site", "layouts", "resources", "cost-calculator.html")
content_path = os.path.join(base, "site", "content", "resources", "pet-transport-cost-calculator.md")

with open(layout_path, "w", encoding="utf-8") as f:
    f.write(LAYOUT)
print(f"Written: {layout_path} ({len(LAYOUT)} chars)")

with open(content_path, "w", encoding="utf-8") as f:
    f.write(CONTENT)
print(f"Written: {content_path} ({len(CONTENT)} chars)")
