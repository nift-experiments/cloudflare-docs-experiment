---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/how-it-works/
  description: Cloudflare's client-side security tracks resources (such as scripts) loaded by your website visitors and provides alerts when it detects new, changed, or malicious resources.
  full_title: How client-side security works · Client-side security docs
  head_html: <title>How client-side security works · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare&#x27;s client-side security tracks resources (such as scripts) loaded by your website visitors and provides alerts when it detects new, changed, or malicious resources."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/how-it-works/index.md"><meta property="og:title" content="How client-side security works · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare&#x27;s client-side security tracks resources (such as scripts) loaded by your website visitors and provides alerts when it detects new, changed, or malicious resources."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="Headers,CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/how-it-works/#page","headline":"How client-side security works \u00b7 Client-side security docs","description":"Cloudflare's client-side security tracks resources (such as scripts) loaded by your website visitors and provides alerts when it detects new, changed, or malicious resources.","url":"https://developers.cloudflare.com/client-side-security/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","CSP"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/how-it-works/
  schema: 1
---
<p>Cloudflare's client-side security helps manage <span class="nb-glossary-tooltip" title="client-side resource">client-side resources</span> (which include scripts and their connections) loaded by your website visitors, and provides visibility on the <a href="https://www.cloudflare.com/learning/privacy/what-are-cookies/">cookies</a> recently detected in HTTP traffic. Client-side security can trigger alert notifications when resources change or are considered malicious.</p>
<p>Client-side security works by adding <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> HTTP headers to your site's responses. CSP is a browser-native mechanism that controls which resources a page is allowed to load and where to send reports when a resource violates the policy. Cloudflare uses two types of CSP headers for different purposes:</p>
<ul>
<li>For resource monitoring (scripts and connections)</li>
<li>To enforce content security rules or log violations of these rules</li>
</ul>
<h2 id="comparison-of-csp-headers">Comparison of CSP headers</h2>
<p>The following table compares the CSP HTTP headers used for monitoring resources and applying content security rules:</p>
<table>
<thead>
<tr>
<th>Resource monitoring HTTP header</th>
<th>Content security rules HTTP headers</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>content-security-policy-report-only</code></td>
<td><code>content-security-policy-report-only</code> (log rules)<br/><code>content-security-policy</code> (allow rules)</td>
</tr>
<tr>
<td>Automatic — on when monitoring is enabled</td>
<td>Manual — created via rules you define</td>
</tr>
<tr>
<td>Added to a sample of HTML responses</td>
<td>Added to 100% of matching responses (not sampled)</td>
</tr>
<tr>
<td>Reports all detected scripts and connections</td>
<td>CSP directives come from your allowlist</td>
</tr>
<tr>
<td>Browser sends violation reports to Cloudflare</td>
<td>Log rules report violations only<br/>Allow rules block disallowed resources</td>
</tr>
</tbody>
</table>
<h2 id="header-used-for-resource-monitoring">Header used for resource monitoring</h2>
<p>When you turn on resource monitoring, Cloudflare automatically adds a <code>content-security-policy-report-only</code> HTTP header to a sample of HTML responses. This report-only header does not block anything. It uses CSP directives that cause browsers to generate violation reports for detected scripts and connections. For details on the header format, refer to <a href="/client-side-security/reference/csp-header/">CSP HTTP header format</a>.</p>
<p>Based on these reports, Cloudflare builds a list of all scripts running on your application and the connections they make to third-party endpoints. Cloudflare also monitors ingress and egress HTTP traffic for cookies, whether set by origin servers or by the visitor's browser.</p>
<p>You cannot turn off the monitoring header while resource monitoring is enabled. Because the header is added to a sample of responses, there may be a <a href="/client-side-security/troubleshooting/#cloudflare-does-not-show-any-client-side-resources-after-activation">small delay</a> between deploying a script or cookie and having its data displayed in the resource monitoring dashboards.</p>
<p>The client-side resource monitoring dashboard shows the list of <a href="/client-side-security/reference/script-statuses/#available-statuses">active</a> scripts, connections, and cookies. The <strong>All Reported Scripts</strong> and <strong>All Reported Connections</strong> dashboards show the full list of detected scripts and connections in your domain, respectively, including infrequent and inactive ones.</p>
<h2 id="headers-related-to-content-security-rules">Headers related to content security rules</h2>
<p>When you create <a href="/client-side-security/rules/">content security rules</a>, Cloudflare generates CSP directives based on your allow and log rules:</p>
<ul>
<li><strong>Log rules</strong> add directives to the <code>content-security-policy-report-only</code> HTTP header, reporting violations without blocking resources.</li>
<li><strong>Allow rules</strong> add directives to the <code>content-security-policy</code> HTTP header, actively blocking resources not present in your allowlist.</li>
</ul>
<p>Unlike headers used for resource monitoring, these HTTP headers apply only to responses matching the expression you define in each rule and are not sampled. You have full control over these headers through your <a href="/client-side-security/rules/">content security rules</a> configuration.</p>
<p>Customers with Client-Side Security Advanced have access to additional classification mechanisms based on threat feeds to determine if a script, or a connection made by a script, is malicious. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<hr />
<h2 id="learn-more">Learn more</h2>
<p>For more background on client-side security and resource monitoring, refer to our <a href="https://blog.cloudflare.com/page-shield-generally-available/">blog post</a>.</p>
