---
cp9:
  canonical: https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/
  description: Update firewall rules for URL normalization.
  full_title: Required firewall rule changes to enable URL normalization · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Required firewall rule changes to enable URL normalization · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="Update firewall rules for URL normalization."><link rel="canonical" href="https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/index.md"><meta property="og:title" content="Required firewall rule changes to enable URL normalization · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update firewall rules for URL normalization."><meta property="og:url" content="https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/#page","headline":"Required firewall rule changes to enable URL normalization \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"Update firewall rules for URL normalization.","url":"https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/troubleshooting/required-changes-to-enable-url-normalization/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8691.md")
</aside>
<p>On 2021-04-08, Cloudflare announced <a href="/rules/normalization/">URL normalization</a>, a feature that protects zones by normalizing HTTP request URI paths.</p>
<p>Malicious users can craft specific URIs that could be interpreted differently by firewall systems and origin systems. When you enable <strong>Normalize incoming URLs</strong>, all rules filtering on the URI path will receive the URL in a canonical form, which provides an extra layer of protection against these malicious users.</p>
<p>Cloudflare gradually enabled URL normalization for all Cloudflare zones except for those that could be impacted by this change. We determined the impacted zones by analyzing all firewall rules, looking for patterns in HTTP fields that would no longer match when using URL normalization techniques.</p>
<p>These fields are the following:</p>
<ul>
<li><code>http.request.uri.path</code></li>
<li><code>http.request.full_uri</code></li>
<li><code>http.request.uri</code></li>
</ul>
<p>Cloudflare did not enable URL normalization automatically for zones that would be impacted by these changes to prevent any change in behavior of your existing firewall rules.</p>
<h2 id="why-url-normalization-is-important">Why URL normalization is important</h2>
<p>Cloudflare strongly recommends that you enable <strong>Normalize incoming URLs</strong> in <strong>Rules</strong> &gt; <strong>Overview</strong> &gt; <strong>URL Normalization</strong> to strengthen your zone's security posture. Not doing so leaves your zone at greater risk of a successful attack. Malicious parties could craft the URL in a way that the rules are not accounting for.</p>
<p>For example, a firewall rule with an expression such as <code>http.request.uri.path contains &quot;/login&quot;</code> could be bypassed if the malicious actor has encoded the <code>l</code> character as <code>%6C</code>. In this scenario, and with URL normalization disabled, traffic would not be matched by the firewall rule.</p>
<p>Refer to <a href="/rules/normalization/how-it-works/">How URL normalization works</a> for more information and additional examples.</p>
<hr />
<h2 id="recommended-procedure">Recommended procedure</h2>
<p>It is recommended that you:</p>
<ol>
<li>Update any firewall rules impacted by the URL normalization changes.</li>
<li>Enable URL normalization.</li>
</ol>
<p>These steps will ensure a stronger security posture on your zone(s).</p>
<h3 id="1-review-and-update-firewall-rules"><ol>
<li>Review and update firewall rules</li>
</ol></h3>
<p>Before enabling URL normalization, you should review the affected firewall rules on your zone(s) and take one of the following approaches:</p>
<ul>
<li>
<p>Edit these firewall rules to remove the parts which will no longer trigger once normalized — for example, any rules that look for <code>//</code> or <code>../</code> in URL paths. Administrators previously created these rules to perform a limited URL normalization, and these rules can now be safely disabled and then deleted.</p>
</li>
<li>
<p>If you wish to identify visitors with non-normalized URI paths with these firewall rules, you should update them to use the original (or raw) non-normalized fields. These fields are the following:</p>
<ul>
<li><code>raw.http.request.uri.path</code></li>
<li><code>raw.http.request.full_uri</code></li>
<li><code>raw.http.request.uri</code></li>
</ul>
</li>
</ul>
<h3 id="2-enable-url-normalization"><ol start="2">
<li>Enable URL normalization</li>
</ol></h3>
<p>Once you have updated the affected firewall rules, enable URL normalization in <strong>Rules</strong> &gt; <strong>Overview</strong> &gt; <strong>URL Normalization</strong>.</p>
<p>A Cloudflare user must have the <a href="/fundamentals/manage-members/roles/">Firewall role</a> or one of the Administrator roles to access URL normalization settings in the dashboard.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/rules/normalization/">URL normalization</a></li>
<li><a href="/rules/transform/">Transform Rules</a></li>
</ul>
