---
cp9:
  canonical: https://developers.cloudflare.com/waf/troubleshooting/faq/
  description: Answers to common questions about WAF configuration and behavior.
  full_title: FAQ · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>FAQ · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Answers to common questions about WAF configuration and behavior."><link rel="canonical" href="https://developers.cloudflare.com/waf/troubleshooting/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/troubleshooting/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Answers to common questions about WAF configuration and behavior."><meta property="og:url" content="https://developers.cloudflare.com/waf/troubleshooting/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/troubleshooting/faq/#page","headline":"FAQ \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Answers to common questions about WAF configuration and behavior.","url":"https://developers.cloudflare.com/waf/troubleshooting/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/troubleshooting/faq/
  schema: 1
---
<h2 id="general-questions">General questions</h2>
<h3 id="why-does-a-security-event-display-a-cloudflare-ip-address-even-though-other-fields-match-the-client-details">Why does a security event display a Cloudflare IP address even though other fields match the client details?</h3>
<p>This happens when a request goes through a Cloudflare Worker.</p>
<p>In this case, Cloudflare considers the client details, including its IP address, for triggering security settings. However, the IP displayed in <a href="/waf/analytics/security-events/">Security Events</a> will be a Cloudflare IP address.</p>
<h3 id="do-i-need-to-escape-certain-characters-in-expressions">Do I need to escape certain characters in expressions?</h3>
<p>Yes, you may have to escape certain characters in expressions. The exact escaping will depend on the string syntax you use:</p>
<ul>
<li>If you use the raw string syntax (for example, <code>r#&quot;this is a string&quot;#</code>), you will only need to escape characters that have a special meaning in regular expressions.</li>
<li>If you use the quoted string syntax (for example, <code>&quot;this is a string&quot;</code>), you need to perform additional escaping, such as escaping special characters <code>&quot;</code> and <code>\</code> using <code>\&quot;</code> and <code>\\</code>, both in literal strings and in regular expressions.</li>
</ul>
<p>For more information on string syntaxes and escaping, refer to <a href="/ruleset-engine/rules-language/values/#string-values-and-regular-expressions">String values and regular expressions</a>.</p>
<h3 id="why-is-my-regular-expression-pattern-not-working">Why is my regular expression pattern not working?</h3>
<p>If you are using a regular expression, it is recommended that you test it with a tool such as <a href="https://regex101.com/?flavor=rust&amp;regex=">Regular Expressions 101</a> or <a href="https://rustexp.lpil.uk">Rustexp</a>.</p>
<h3 id="why-are-some-rules-bypassed-when-i-did-not-create-an-exception">Why are some rules bypassed when I did not create an exception?</h3>
<p>If you have <a href="/ssl/">SSL/TLS certificates</a> managed by Cloudflare, every time a certificate is issued or renewed, a <a href="/ssl/edge-certificates/changing-dcv-method/dcv-flow/">domain control validation (DCV)</a> must happen. When a certificate is in <code>pending_validation</code> state and there are valid DCV tokens in place, some Cloudflare security features such as <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/managed-rules/">Managed Rules</a> will be automatically disabled on specific DCV paths (for example, <code>/.well-known/pki-validation/</code> and <code>/.well-known/acme-challenge/</code>).</p>
<p>These automatic bypasses do not appear in <a href="/rules/trace-request/">Trace</a> results.</p>
<h3 id="why-have-i-been-blocked">Why have I been blocked?</h3>
<p>Cloudflare may block requests when it detects activity that could be unsafe. Common reasons include:</p>
<ul>
<li>Security protection against malicious traffic, DDoS attacks, or other threats.</li>
<li>Excessive requests in a short time (rate limiting).</li>
<li>Bot-like or automated traffic.</li>
<li>IP addresses listed on public blocklists, such as <a href="https://projecthoneypot.org/">Project Honey Pot</a>.</li>
</ul>
<p>If you are a site visitor:</p>
<ul>
<li>Contact the site owner, providing details of your actions when the block occurred and the Cloudflare Ray ID displayed at the bottom of the error page.</li>
<li>Avoid suspicious inputs or automated scripts.</li>
<li>Check your IP reputation through <a href="https://projecthoneypot.org/">Project Honey Pot</a>.</li>
</ul>
<p>If you are the site owner:</p>
<ul>
<li>Adjust security settings to balance protection with accessibility.</li>
<li>Monitor blocked requests in your Cloudflare dashboard.</li>
<li>Allowlist trusted IPs or fine-tune WAF/bot rules to reduce false positives.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15318.md")
</aside>
<h2 id="bots">Bots</h2>
<h3 id="how-does-the-waf-handle-traffic-from-known-bots">How does the WAF handle traffic from known bots?</h3>
<h4 id="caution-about-potentially-blocking-bots">Caution about potentially blocking bots</h4>
<p>When you create a custom rule with a <em>Block</em>, <em>Non-Interactive Challenge</em>, <em>Managed Challenge</em>, or <em>Interactive Challenge</em> action, you might unintentionally block traffic from known bots. Specifically, this might affect search engine optimization (SEO) and website monitoring when trying to enforce a mitigation action based on URI, path, host, ASN, or country.</p>
<p>Refer to the <a href="/cloudflare-challenges/troubleshooting/#allowlist-traffic-from-mitigation-actions">Challenges documentation</a> for more information.</p>
<h4 id="bots-currently-detected">Bots currently detected</h4>
<p><a href="https://radar.cloudflare.com/verified-bots">Cloudflare Radar</a> lists a <strong>sample</strong> of known bots that the WAF currently detects. When traffic comes from these bots and others not listed, the <code>cf.client.bot</code> field is set to <code>true</code>.</p>
<p>To submit a friendly bot to be verified, go to the <a href="https://radar.cloudflare.com/traffic/verified-bots"><strong>Verified bots</strong></a> page in Cloudflare Radar and select <strong>Add a bot</strong>.</p>
<p>For more information on verified bots, refer to <a href="/bots/concepts/bot/">Bots</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15317.md")
</aside>
