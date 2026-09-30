---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/
  description: Cloudflare analyzes the JavaScript code of the scripts loaded by your website visitors, using threat intelligence and machine learning (including LLMs) to detect malicious behavior.
  full_title: Malicious script and connection detection · Client-side security docs
  head_html: <title>Malicious script and connection detection · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare analyzes the JavaScript code of the scripts loaded by your website visitors, using threat intelligence and machine learning (including LLMs) to detect malicious behavior."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/index.md"><meta property="og:title" content="Malicious script and connection detection · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare analyzes the JavaScript code of the scripts loaded by your website visitors, using threat intelligence and machine learning (including LLMs) to detect malicious behavior."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="LLM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/#page","headline":"Malicious script and connection detection \u00b7 Client-side security docs","description":"Cloudflare analyzes the JavaScript code of the scripts loaded by your website visitors, using threat intelligence and machine learning (including LLMs) to detect malicious behavior.","url":"https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["LLM"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/how-it-works/malicious-script-detection/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3988.md")
</aside>
<p>Cloudflare uses three complementary mechanisms to determine if a script, or a connection made by a script, is malicious. Each mechanism checks at a different level — the script's code, the URL it is hosted at, or the domain it is served from:</p>
<ul>
<li><strong>Malicious script detection</strong> — Analyzes the actual JavaScript code for malicious behavior.</li>
<li><strong>Malicious URL checks</strong> — Looks up script URLs against threat intelligence feeds.</li>
<li><strong>Malicious domain checks</strong> — Looks up script domains against threat intelligence feeds.</li>
</ul>
<p>Any updates to the threat feeds will trigger new checks for previously detected scripts or connections so that the client-side resource monitoring dashboards always reflect the latest categorization.</p>
<h2 id="malicious-script-detection">Malicious script detection</h2>
<p>Cloudflare analyzes the JavaScript code of the scripts loaded by your website visitors. This analysis uses machine learning, including an LLM powered by Workers AI, to reduce the false positive rate and focus on highlighting true positives such as <a href="https://sansec.io/what-is-magecart">Magecart-type attacks</a>, where injected code skims payment card data from checkout forms.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3987.md")
</aside>
<p>The analysis assigns a JS integrity score between 1 and 99 to each script version. Lower scores indicate higher risk: a score of 1 means definitely malicious, and 99 means definitely not malicious.</p>
<p>Cloudflare classifies a script as malicious when its score falls below the threshold, which is currently set to 10. Scripts that score below this threshold appear as malicious in the monitoring dashboards.</p>
<p>In addition to the integrity score, Cloudflare will also provide individual scores for different malicious code detections (scores from 1 to 99):</p>
<ul>
<li><strong>Magecart</strong></li>
<li><strong>Crypto mining</strong></li>
<li><strong>Malware</strong></li>
</ul>
<p>You can <a href="/client-side-security/alerts/configure/">configure Malicious Script Alerts</a> to receive an alert notification as soon as Cloudflare detects JavaScript code classified as malicious in your domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3986.md")
</aside>
<h2 id="malicious-url-checks">Malicious URL checks</h2>
<p>Cloudflare will search for the URLs of your JavaScript dependencies in threat intelligence feeds to determine if any of those scripts should be categorized as malicious.</p>
<p>The client-side resource monitoring dashboards display the scripts that were considered malicious at the top of the scripts list.</p>
<p>You can <a href="/client-side-security/alerts/configure/">configure Malicious URL Alerts</a> to receive an alert notification as soon as Cloudflare detects a script from a malicious URL in your domain.</p>
<p>Depending on your current configuration, Cloudflare can also search for malicious URLs in the URLs of outgoing connections made by scripts in your domain. To enable this check, you must <a href="/client-side-security/reference/settings/#connection-target-details">allow resource monitoring to use the full URLs of outgoing connections</a> instead of only the hostname in the settings page.</p>
<h2 id="malicious-domain-checks">Malicious domain checks</h2>
<p>Cloudflare will search for the domains of your client-side JavaScript dependencies in threat feeds to determine if any of those scripts is being served from a known malicious domain.</p>
<p>A domain previously reported as malicious can later be reported as non-malicious if, after further analysis, the domain is deemed safe.</p>
<p>Cloudflare will also check the target domains of connections made by scripts in your domain's pages, following the same approach described for scripts.</p>
<p>You can <a href="/client-side-security/alerts/configure/">configure Malicious Domain Alerts</a> to receive an alert notification as soon as Cloudflare detects a malicious script loaded from a known malicious domain in your domain.</p>
<hr />
<h2 id="malicious-script-and-connection-categories">Malicious script and connection categories</h2>
<p>Scripts and connections considered malicious are categorized based on data from threat intelligence feeds. The current categories are the following:</p>
<ul>
<li>Security threats</li>
<li>Command-and-Control (C2) &amp; Botnet</li>
<li>Crypto mining</li>
<li>Spyware</li>
<li>Phishing</li>
<li>Malware</li>
<li>Domain Generation Algorithm (DGA) domain</li>
<li>Typosquatting &amp; Impersonation</li>
</ul>
<p>Each script or connection considered malicious can belong to several categories.</p>
