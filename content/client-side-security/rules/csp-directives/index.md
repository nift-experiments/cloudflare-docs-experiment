---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/rules/csp-directives/
  description: CSP directives supported by content security rules
  full_title: Supported CSP directives · Client-side security docs
  head_html: <title>Supported CSP directives · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="CSP directives supported by content security rules"><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/rules/csp-directives/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/rules/csp-directives/index.md"><meta property="og:title" content="Supported CSP directives · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="CSP directives supported by content security rules"><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/rules/csp-directives/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="Headers,CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/rules/csp-directives/#page","headline":"Supported CSP directives \u00b7 Client-side security docs","description":"CSP directives supported by content security rules","url":"https://developers.cloudflare.com/client-side-security/rules/csp-directives/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","CSP"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/rules/csp-directives/
  schema: 1
---
<p><a href="/client-side-security/rules/">Content security rules</a> support most <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> directives, covering both monitored and unmonitored resources. You can use a content security rule to control other types of resources besides scripts and their connections, even though Cloudflare is not monitoring these resources.</p>
<p>Each CSP directive can contain multiple values, including:</p>
<ul>
<li>Schemes</li>
<li>Hostnames</li>
<li>URIs</li>
<li>Special keywords between single quotes (for example, <code>'none'</code>)</li>
<li>Hashes between single quotes (for example, <code>'sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC'</code>)</li>
</ul>
<p>Hostname and URI values support a <code>*</code> wildcard for the leftmost subdomain.</p>
<p>The following table lists the supported CSP directives and special values you can use in content security rules:</p>
<table>
<thead>
<tr>
<th>Directive</th>
<th>Name in the dashboard</th>
<th>Supported special values</th>
<th>Monitored</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>script-src</code></td>
<td>Scripts</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td><a href="/client-side-security/detection/monitor-connections-scripts/">Yes</a></td>
</tr>
<tr>
<td><code>connect-src</code></td>
<td>Connections</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td><a href="/client-side-security/detection/monitor-connections-scripts/">Yes</a></td>
</tr>
<tr>
<td><code>default-src</code></td>
<td>Default</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>img-src</code></td>
<td>Images</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>style-src</code></td>
<td>Styles</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>font-src</code></td>
<td>Fonts</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>object-src</code></td>
<td>Objects</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>media-src</code></td>
<td>Media</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>child-src</code></td>
<td>Child</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>form-action</code></td>
<td>Form actions</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>worker-src</code></td>
<td>Workers</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>base-uri</code></td>
<td>Base URI</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>manifest-src</code></td>
<td>Manifests</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>frame-src</code></td>
<td>Frames</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>frame-ancestors</code></td>
<td>Frame ancestors</td>
<td><code>'none'</code><br/><code>'self'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>upgrade-insecure-requests</code></td>
<td>Upgrade insecure requests</td>
<td>N/A</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="more-resources">More resources</h2>
<p>For more information on CSP directives and their values, refer to the following resources in the MDN documentation:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy">Content-Security-Policy response header</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP">CSP guide</a></li>
</ul>
