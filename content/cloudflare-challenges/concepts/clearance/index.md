---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/
  description: How cf_clearance cookies prove a visitor passed a Cloudflare challenge.
  full_title: Clearance · Cloudflare challenges docs
  head_html: <title>Clearance · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="How cf_clearance cookies prove a visitor passed a Cloudflare challenge."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/index.md"><meta property="og:title" content="Clearance · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How cf_clearance cookies prove a visitor passed a Cloudflare challenge."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Challenges"><meta name="pcx_tags" content="Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#page","headline":"Clearance \u00b7 Cloudflare challenges docs","description":"How cfclearance cookies prove a visitor passed a Cloudflare challenge.","url":"https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/concepts/clearance/
  schema: 1
---
<h2 id="cf-clearance-cookies"><code>cf_clearance</code> cookies</h2>
<p>A <code>cf_clearance</code> cookie proves to Cloudflare that the visitor is a verified human and has passed Cloudflare's client-side verifications.</p>
<p>The cookie contains <strong>two types of clearance</strong> that work together:</p>
<ul>
<li><strong>Challenge clearance</strong>: Granted when a visitor solves a Challenge (for example, Interstitial Challenge Pages or Turnstile with pre-clearance enabled).</li>
<li><strong>Precursor clearance</strong>: Continuously updated based on session behavior.</li>
</ul>
<p>The cookie is securely tied to the specific visitor and device it was issued to, preventing reuse across machines.</p>
<p>As an additional layer of security, Cloudflare recommends that customers <a href="/waf/rate-limiting-rules/">add a rate limiting rule</a> based on the <code>cf_clearance</code> cookie value. This helps ensure that a single, valid cookie cannot be abused by one machine to send an excessive volume of requests.</p>
<h3 id="challenge-clearance">Challenge clearance</h3>
<p>Challenge clearance is granted when a visitor successfully completes a Challenge.</p>
<p>Each challenge type sets a clearance level. A higher-level clearance bypasses all Challenges at or below that level. A lower-level clearance only bypasses challenges at the same level.</p>
<table>
<thead>
<tr>
<th>Clearance level</th>
<th>Bypasses</th>
</tr>
</thead>
<tbody>
<tr>
<td>Interactive (high)</td>
<td>Interactive, Managed, and Non-Interactive Challenges</td>
</tr>
<tr>
<td>Managed (medium)</td>
<td>Managed and Non-Interactive Challenges</td>
</tr>
<tr>
<td>Non-Interactive (low)</td>
<td>Non-Interactive Challenges only</td>
</tr>
</tbody>
</table>
<p>If a visitor passes an Interactive Challenge (highest security level), they can bypass all other Challenges for as long as the clearance remains valid.</p>
<p>If a visitor receives clearance at a lower level (Managed or Non-Interactive) and later encounters a higher-level challenge, they must solve the higher-level challenge again.</p>
<p>The original clearance is replaced if a higher-level challenge is later solved.</p>
<p>Challenge clearance remains valid for the duration configured by the customer (Challenge Passage), <strong>unless Precursor determines the session is suspicious</strong>.</p>
<h3 id="precursor-clearance">Precursor clearance</h3>
<p>Precursor clearance is continuously re-evaluated throughout a visitor’s session. Rather than being tied to a single challenge event, it operates as an ongoing, client-side process that periodically reassesses behavior at regular intervals. As new signals are observed, the clearance is updated dynamically to reflect the current level of trust in the session.</p>
<p>If Precursor determines that a session is suspicious:</p>
<ul>
<li>The visitor’s effective Challenge clearance may be <strong>reduced or invalidated</strong>.</li>
<li>The visitor may be <strong>re-challenged</strong>, even if the cookie has not expired.</li>
</ul>
<p>This creates a model where clearance is both <strong>time-bound (Interstitial)</strong> and <strong>behavior-bound (Precursor)</strong>.</p>
<h2 id="pre-clearance-support-in-turnstile">Pre-clearance support in Turnstile</h2>
<p>Pre-clearance in <a href="/turnstile/">Turnstile</a> allows websites to streamline user experiences by using <code>cf_clearance</code> cookies. The <code>cf_clearance</code> cookie enables visitors to bypass WAF Challenges on all subsequent requests on the zone, including API requests, based on the security clearance level set by the customer. This can be particularly useful for trusted visitors, enhancing usability while maintaining security.</p>
<p>By default, Turnstile issues a one-time use token to the visitor when they solve a challenge via the widget. You must <a href="/turnstile/get-started/server-side-validation/">validate the token</a> by making a server-side call to the Siteverify API.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4031.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4030.md")
</aside>
<table>
<thead>
<tr>
<th>Challenge type</th>
<th>Issued clearance</th>
</tr>
</thead>
<tbody>
<tr>
<td>Challenge Page</td>
<td><code>cf_clearance</code> cookie (default)</td>
</tr>
<tr>
<td>Turnstile widget</td>
<td>Token (default) <br /> <code>cf_clearance</code> cookie (optional addition)</td>
</tr>
</tbody>
</table>
<p>When you enable pre-clearance support on Turnstile, a <code>cf_clearance</code> cookie is issued to the visitor in addition to the default Turnstile token.</p>
<p>You can integrate Cloudflare Challenges by allowing Turnstile to issue a <code>cf_clearance</code> cookie as pre-clearance to your visitor. The pre-clearance level is set upon widget creation or widget modification using the Turnstile API's clearance_level. Possible values for the configuration are:</p>
<ul>
<li><code>interactive</code></li>
<li><code>managed</code></li>
<li><code>jschallenge</code></li>
<li><code>no_clearance</code></li>
</ul>
<p>All widgets have pre-clearance mode set to <code>false</code> and the security clearance is set to <code>no_clearance</code> by default.</p>
<p>For Enterprise customers eligible to enable widgets without any pre-configured hostnames, Cloudflare recommends issuing pre-clearance cookies on widgets where at least one hostname is specified and is the same as the zone that you want to integrate with Turnstile.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/integrating-turnstile-with-the-cloudflare-waf-to-challenge-fetch-requests">blog post</a> for more details on how pre-clearance works with WAF.</p>
<h3 id="pre-clearance-level-options">Pre-clearance level options</h3>
<p><strong>Interactive</strong> (High) <code>interactive</code></p>
<p>Allows a user with a clearance cookie to not be challenged by Non-Interactive Challenge, Managed Challenge, or Interactive Challenge Firewall Rules.</p>
<p><strong>Managed</strong> (Medium) <code>managed</code></p>
<p>Allows a user with a clearance cookie to not be challenged by Non-Interactive Challenge or Managed Challenge Firewall Rules.</p>
<p><strong>Non-interactive</strong> (Low) <code>jschallenge</code></p>
<p>Allows a user with a clearance cookie to not be challenged by Non-Interactive Challenge Firewall Rules.</p>
<h3 id="clearance-cookie-duration">Clearance cookie duration</h3>
<p>Clearance cookies generated by the Turnstile widget will be valid for the time specified by the zone-level Challenge Passage value. To configure the Challenge Passage setting, refer to <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a>.</p>
<h3 id="setup">Setup</h3>
<p>To enable pre-clearance, you must ensure that the hostname of the Turnstile widget matches the zone with the WAF rules. During the Turnstile configuration setup in the Cloudflare dashboard, you have access to a list of registered zones. Select the appropriate hostname from this list.</p>
<p>The prerequisite is crucial for pre-clearance to function properly. If set up correctly, visitors who successfully solve Turnstile will receive a cookie with the security clearance level set by the customer. When encountering a WAF challenge on the same zone, they will bypass additional challenges for the configured clearance level and below.</p>
<p>For more details on managing hostnames, refer to the <a href="/turnstile/additional-configuration/hostname-management/">Hostname Management documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4029.md")
</aside>
<h4 id="enable-pre-clearance-on-a-new-site">Enable pre-clearance on a new site</h4>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4032.md")
</div>
<h4 id="enable-pre-clearance-on-an-existing-site">Enable pre-clearance on an existing site</h4>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4033.md")
</div>
