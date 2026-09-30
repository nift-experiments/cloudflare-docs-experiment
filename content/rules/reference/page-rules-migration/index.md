---
cp9:
  canonical: https://developers.cloudflare.com/rules/reference/page-rules-migration/
  description: Migrate from Page Rules to modern Cloudflare Rules alternatives.
  full_title: Page Rules migration guide · Cloudflare Rules docs
  head_html: <title>Page Rules migration guide · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from Page Rules to modern Cloudflare Rules alternatives."><link rel="canonical" href="https://developers.cloudflare.com/rules/reference/page-rules-migration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/reference/page-rules-migration/index.md"><meta property="og:title" content="Page Rules migration guide · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from Page Rules to modern Cloudflare Rules alternatives."><meta property="og:url" content="https://developers.cloudflare.com/rules/reference/page-rules-migration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/reference/page-rules-migration/#page","headline":"Page Rules migration guide \u00b7 Cloudflare Rules docs","description":"Migrate from Page Rules to modern Cloudflare Rules alternatives.","url":"https://developers.cloudflare.com/rules/reference/page-rules-migration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/reference/page-rules-migration/
  schema: 1
---
<p>Cloudflare is continuously improving its platform to deliver more powerful and scalable tools for managing your configurations. To help you take full advantage of these improvements, we recommend using <a href="/rules/">modern Rules features</a> for new implementations. These products address the limitations of Page Rules while providing greater flexibility, scalability, and ease of use.</p>
<p>For a quick start, explore the one-click templates available in the Cloudflare dashboard in <strong>Rules</strong> &gt; <strong>Overview</strong>. These templates simplify common configurations like redirects, rewrites and header modifications, making setup faster and easier.</p>
<h2 id="page-rules-migration">Page Rules migration</h2>
<p>To make the transition seamless, Cloudflare will handle the migration of your existing Page Rules automatically. This process is planned for late 2025 or beyond, with no action required on your part. You will receive advance notification before any changes are made.</p>
<p>If you wish to explore the benefits of modern Rules features sooner, you can begin adopting them today. Doing so allows you to:</p>
<ul>
<li>Take advantage of modern features and capabilities sooner.</li>
<li>Customize and refine your rules to match your evolving needs.</li>
</ul>
<p>To assist with this process, we provide you with a comprehensive mapping between Page Rules settings and modern Rules products in this guide.</p>
<h2 id="why-transition">Why transition?</h2>
<p>Cloudflare Page Rules has several fundamental limitations, such as triggering solely based on URL patterns and being limited to 125 rules per zone for performance reasons. These rules are also complex to debug when multiple page rules apply to the same incoming request.</p>
<p>In 2022, we announced in our blog post <a href="https://blog.cloudflare.com/future-of-page-rules">The future of Page Rules</a> that Page Rules would be replaced with a suite of dedicated products, each built to be best-of-breed and put more power into the hands of our users. The new Rules products — <a href="/rules/configuration-rules/">Configuration Rules</a>, <a href="/rules/compression-rules/">Compression Rules</a>, <a href="/rules/origin-rules/">Origin Rules</a>, <a href="/rules/url-forwarding/">Redirects</a>, and <a href="/rules/transform/">Transform Rules</a> — are now generally available (GA) and have already been adopted by tens of thousands of Cloudflare customers.</p>
<p>Improvements in modern Rules features include:</p>
<ul>
<li><strong>New engine</strong>: New Rules features are powered by the <a href="/ruleset-engine/">Ruleset Engine</a>, which offers versatile configuration with a robust language that supports many HTTP request and response fields.</li>
<li><strong>Improved scalability</strong>: Thanks to the improved scalability, Cloudflare plans now have increased quotas.</li>
<li><strong>Easier troubleshooting</strong>: Rule execution is more predictable, since each rule operates independently, simplifying troubleshooting. Additionally, <a href="/rules/trace-request/">Cloudflare Trace</a> helps understand rule interactions.</li>
<li><strong>Improved consistency</strong>: New Rules features also ensure consistency, with common fields and capabilities shared across products, offering a seamless experience and predictable Terraform configurations.</li>
</ul>
<h2 id="key-differences">Key differences</h2>
<p>The evaluation and execution order of Rules features is different from Page Rules:</p>
<ul>
<li><strong>Rule matching logic</strong>: Page Rules apply the first matching rule (first match wins). In contrast, modern Rules are stackable, meaning multiple matching rules can combine and apply to the same request (last match wins). For example, if multiple cache rules match the same URL, the features in those rules will all apply in order.</li>
<li><strong>Action separation</strong>: A Page Rule may include multiple actions for different products that are applied in a sequence selected by the customer within the Page Rule itself. Modern Rules features are evaluated <a href="/rules/origin-rules/#execution-order">in a fixed sequence</a>, with customers defining the rule order within a product <a href="/ruleset-engine/reference/phases-list/">phase</a>.</li>
<li><strong>Precedence</strong>: Modern Rules features take precedence over Page Rules. For instance, if both define caching settings for the same path, Cache Rules will override Page Rules.</li>
<li><strong>Caching behavior</strong>: In Cache Rules, selecting <strong>Eligible for cache</strong> automatically enables <strong>Cache Everything</strong> by default. To maintain the exact behavior of Page Rules, you may need to <a href="/cache/how-to/cache-rules/page-rules-migration/">adjust your configuration</a>.</li>
<li><strong>Interactions with Workers</strong>: Requests handled by Workers will suppress Page Rules actions, but they will not suppress actions from modern Rules features.</li>
</ul>
<h2 id="convert-page-rules-urls-to-filter-expressions">Convert Page Rules URLs to filter expressions</h2>
<p>Modern Rules use filter expressions instead of URL patterns. These expressions, built with the Rules language, allow greater precision by leveraging <a href="/ruleset-engine/rules-language/fields/">fields</a>, <a href="/ruleset-engine/rules-language/functions/">functions</a>, and <a href="/ruleset-engine/rules-language/operators/">operators</a>.</p>
<p>The following example demonstrates the use of the <a href="/ruleset-engine/rules-language/fields/reference/http.request.full_uri/"><code>http.request.full_uri</code></a> field and the <code>wildcard</code> operator for <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard matching</a>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/12811.md")
</div>
<p><a href="/rules/url-forwarding/single-redirects/create-dashboard/">Single Redirects</a> and <a href="/rules/transform/url-rewrite/create-dashboard/">URL Rewrite Rules</a> also offer a simplified view called <strong>Wildcard pattern</strong>, allowing you to specify URL patterns (<code>http*://example.com/*/downloads/*.txt*</code>) without specifying the full filter expression (<code>http.request.full_uri wildcard &quot;http*://example.com/*/downloads/*.txt*&quot;</code>).</p>
<h3 id="important-considerations">Important considerations</h3>
<ul>
<li><strong>Protocol scheme</strong>: Page Rules URL matching does not include the URI scheme (for example, <code>http://</code> or <code>https://</code>) unless explicitly included in the rule. Filter expressions using <code>http.request.full_uri</code> field, however, require matching the full URI, including the protocol scheme. To make your filter expression scheme-agnostic, use <code>http*://</code> as a wildcard for both <code>http://</code> and <code>https://</code>.</li>
<li><strong>Query strings</strong>: Page Rules ignore query strings unless they are part of the rule URL. Filter expressions include the query string automatically, as part of the <code>http.request.full_uri</code> field. To ensure query strings do not affect your matching, append a <code>*</code> wildcard at the end of your filter expression, such as <code>.txt*</code>.</li>
</ul>
<h2 id="feature-correspondence-table">Feature correspondence table</h2>
<p>To help you map existing Page Rules to modern Rules products, this table outlines how Page Rules settings translate to modern Rules and provides examples for common configurations.</p>
<p>Also, to streamline common configurations, the Cloudflare dashboard now includes dozens of one-click templates, available in <strong>Rules</strong> &gt; <strong>Overview</strong>. These templates enable you to deploy commonly used features — such as redirects, rewrites, and header modifications — instantly, with pre-filled filter expressions and actions. Explore these templates in the dashboard for a faster setup.</p>
<table>
<thead>
<tr>
<th>Page Rules setting</th>
<th>New implementation uses...</th>
<th>Migration/Replacement instructions</th>
</tr>
</thead>
<tbody>
<tr>
<td>Always Use HTTPS</td>
<td>Redirect Rules (Single Redirects)</td>
<td><a href="#migrate-always-use-https">Migrate Always Use HTTPS</a></td>
</tr>
<tr>
<td>Browser Cache TTL</td>
<td>Cache Rules</td>
<td><a href="#migrate-browser-cache-ttl">Migrate Browser Cache TTL</a></td>
</tr>
<tr>
<td>Browser Integrity Check</td>
<td>Configuration Rules</td>
<td><a href="#migrate-browser-integrity-check">Migrate Browser Integrity Check</a></td>
</tr>
<tr>
<td>Bypass Cache on Cookie</td>
<td>Cache Rules</td>
<td><a href="#migrate-bypass-cache-on-cookie">Migrate Bypass Cache on Cookie</a></td>
</tr>
<tr>
<td>Cache By Device Type</td>
<td>Cache Rules</td>
<td><a href="#migrate-cache-by-device-type">Migrate Cache By Device Type</a></td>
</tr>
<tr>
<td>Cache Deception Armor</td>
<td>Cache Rules</td>
<td><a href="#migrate-cache-deception-armor">Migrate Cache Deception Armor</a></td>
</tr>
<tr>
<td>Cache Level</td>
<td>Cache Rules</td>
<td><a href="#migrate-cache-level-cache-everything">Migrate Cache Level</a></td>
</tr>
<tr>
<td>Cache on Cookie</td>
<td>Cache Rules</td>
<td><a href="#migrate-cache-on-cookie">Migrate Cache on Cookie</a></td>
</tr>
<tr>
<td>Cache TTL by status code</td>
<td>Cache Rules</td>
<td><a href="#migrate-cache-ttl-by-status-code">Migrate Cache TTL by status code</a></td>
</tr>
<tr>
<td>Custom Cache Key</td>
<td>Cache Rules</td>
<td><a href="#migrate-custom-cache-key">Migrate Custom Cache Key</a></td>
</tr>
<tr>
<td>Disable Apps</td>
<td>Configuration Rules</td>
<td><a href="#migrate-disable-apps">Migrate Disable Apps</a></td>
</tr>
<tr>
<td>Disable Performance</td>
<td>N/A (deprecated)</td>
<td><a href="#replace-disable-performance">Replace Disable Performance</a></td>
</tr>
<tr>
<td>Disable Railgun</td>
<td>N/A (deprecated)</td>
<td>N/A</td>
</tr>
<tr>
<td>Disable Security</td>
<td>N/A (deprecated)</td>
<td><a href="#replace-disable-security">Replace Disable Security</a></td>
</tr>
<tr>
<td>Disable Zaraz</td>
<td>Configuration Rules</td>
<td><a href="#migrate-disable-zaraz">Migrate Disable Zaraz</a></td>
</tr>
<tr>
<td>Edge Cache TTL</td>
<td>Cache Rules</td>
<td><a href="#migrate-edge-cache-ttl">Migrate Edge Cache TTL</a></td>
</tr>
<tr>
<td>Email Obfuscation</td>
<td>Configuration Rules</td>
<td><a href="#migrate-email-obfuscation">Migrate Email Obfuscation</a></td>
</tr>
<tr>
<td>Forwarding URL</td>
<td>Redirect Rules (Single Redirects)</td>
<td><a href="#migrate-forwarding-url">Migrate Forwarding URL</a></td>
</tr>
<tr>
<td>Host Header Override</td>
<td>Origin Rules</td>
<td><a href="#migrate-host-header-override">Migrate Host Header Override</a></td>
</tr>
<tr>
<td>IP Geolocation Header</td>
<td>Transform Rules (Managed Transforms)</td>
<td><a href="#migrate-ip-geolocation-header">Migrate IP Geolocation Header</a></td>
</tr>
<tr>
<td>Opportunistic Encryption</td>
<td>Configuration Rules</td>
<td><a href="#migrate-opportunistic-encryption">Migrate Opportunistic Encryption</a></td>
</tr>
<tr>
<td>Origin Cache Control</td>
<td>Cache Rules</td>
<td><a href="#migrate-origin-cache-control">Migrate Origin Cache Control</a></td>
</tr>
<tr>
<td>Origin Error Page Pass-thru</td>
<td>Cache Rules</td>
<td><a href="#migrate-origin-error-page-pass-thru">Migrate Origin Error Page Pass-thru</a></td>
</tr>
<tr>
<td>Polish</td>
<td>Configuration Rules</td>
<td><a href="#migrate-polish">Migrate Polish</a></td>
</tr>
<tr>
<td>Query String Sort</td>
<td>Cache Rules</td>
<td><a href="#migrate-query-string-sort">Migrate Query String Sort</a></td>
</tr>
<tr>
<td>Resolve Override</td>
<td>Origin Rules</td>
<td><a href="#migrate-resolve-override">Migrate Resolve Override</a></td>
</tr>
<tr>
<td>Respect Strong ETags</td>
<td>Cache Rules</td>
<td><a href="#migrate-respect-strong-etags">Migrate Respect Strong ETags</a></td>
</tr>
<tr>
<td>Response Buffering</td>
<td>N/A (deprecated)</td>
<td>N/A</td>
</tr>
<tr>
<td>Rocket Loader</td>
<td>Configuration Rules</td>
<td><a href="#migrate-rocket-loader">Migrate Rocket Loader</a></td>
</tr>
<tr>
<td>Security Level</td>
<td>Configuration Rules</td>
<td><a href="#migrate-security-level">Migrate Security Level</a></td>
</tr>
<tr>
<td>True Client IP Header</td>
<td>Transform Rules (Managed Transforms)</td>
<td><a href="#migrate-true-client-ip-header">Migrate True Client IP Header</a></td>
</tr>
<tr>
<td>SSL</td>
<td>Configuration Rules</td>
<td><a href="#migrate-ssl">Migrate SSL</a></td>
</tr>
<tr>
<td>Web Application Firewall</td>
<td>N/A (deprecated)</td>
<td>N/A</td>
</tr>
</tbody>
</table>
<h3 id="migrate-always-use-https">Migrate Always Use HTTPS</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12815.md")
</div></div>
<h3 id="migrate-automatic-https-rewrites">Migrate Automatic HTTPS Rewrites</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12819.md")
</div></div>
<h3 id="migrate-browser-cache-ttl">Migrate Browser Cache TTL</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12823.md")
</div></div>
<h3 id="migrate-browser-integrity-check">Migrate Browser Integrity Check</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12827.md")
</div></div>
<h3 id="migrate-bypass-cache-on-cookie">Migrate Bypass Cache on Cookie</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12831.md")
</div></div>
<h3 id="migrate-cache-by-device-type">Migrate Cache By Device Type</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12835.md")
</div></div>
<h3 id="migrate-cache-deception-armor">Migrate Cache Deception Armor</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12839.md")
</div></div>
<h3 id="migrate-cache-level-cache-everything">Migrate Cache Level (Cache Everything)</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12843.md")
</div></div>
<h3 id="migrate-cache-on-cookie">Migrate Cache on Cookie</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12847.md")
</div></div>
<h3 id="migrate-cache-ttl-by-status-code">Migrate Cache TTL by status code</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12851.md")
</div></div>
<h3 id="migrate-custom-cache-key">Migrate Custom Cache Key</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12855.md")
</div></div>
<h3 id="migrate-disable-apps">Migrate Disable Apps</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12859.md")
</div></div>
<h3 id="replace-disable-performance">Replace Disable Performance</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12802.md")
</aside>
<p>This Page Rules setting turned off Polish and Rocket Loader. You can still turn on or off relevant Cloudflare features one by one using Configuration Rules.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12863.md")
</div></div>
<h3 id="replace-disable-security">Replace Disable Security</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12801.md")
</aside>
<p>This Page Rules setting turns off Email Obfuscation, Rate Limiting (previous version), Scrape Shield, URL (Zone) Lockdown, and WAF managed rules (previous version). You can still turn on or off relevant Cloudflare features one by one using Configuration Rules and WAF custom rules.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12866.md")
</div></div>
<h3 id="migrate-disable-zaraz">Migrate Disable Zaraz</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12870.md")
</div></div>
<h3 id="migrate-edge-cache-ttl">Migrate Edge Cache TTL</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12874.md")
</div></div>
<h3 id="migrate-email-obfuscation">Migrate Email Obfuscation</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12878.md")
</div></div>
<h3 id="migrate-forwarding-url">Migrate Forwarding URL</h3>
<p><strong>Example #1: Redirect <code>www</code> to root domain</strong></p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12883.md")
</div></div>
<p><strong>Example #2: Redirect all pages under old path to new path</strong></p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12888.md")
</div></div>
<h3 id="migrate-host-header-override">Migrate Host Header Override</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12892.md")
</div></div>
<h3 id="migrate-ip-geolocation-header">Migrate IP Geolocation Header</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12896.md")
</div></div>
<h3 id="migrate-opportunistic-encryption">Migrate Opportunistic Encryption</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12900.md")
</div></div>
<h3 id="migrate-origin-cache-control">Migrate Origin Cache Control</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12904.md")
</div></div>
<h3 id="migrate-origin-error-page-pass-thru">Migrate Origin Error Page Pass-thru</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12908.md")
</div></div>
<h3 id="migrate-polish">Migrate Polish</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12912.md")
</div></div>
<h3 id="migrate-query-string-sort">Migrate Query String Sort</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12916.md")
</div></div>
<h3 id="migrate-resolve-override">Migrate Resolve Override</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12920.md")
</div></div>
<h3 id="migrate-respect-strong-etags">Migrate Respect Strong ETags</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12924.md")
</div></div>
<h3 id="migrate-rocket-loader">Migrate Rocket Loader</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12928.md")
</div></div>
<h3 id="migrate-security-level">Migrate Security Level</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12932.md")
</div></div>
<h3 id="migrate-true-client-ip-header">Migrate True Client IP Header</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12936.md")
</div></div>
<h3 id="migrate-ssl">Migrate SSL</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12940.md")
</div></div>
<h2 id="settings-that-will-not-be-migrated">Settings that will not be migrated</h2>
<p>The following Page Rules settings will not be migrated to other types of rules:</p>
<ul>
<li><strong>Disable Performance</strong> (this setting is deprecated)</li>
<li><strong>Disable Railgun</strong> (this setting is deprecated, since Railgun is no longer available)</li>
<li><strong>Disable Security</strong> (this setting is deprecated)</li>
<li><strong>Response Buffering</strong> (this setting is deprecated)</li>
<li><strong>Web Application Firewall</strong> (this setting is deprecated, since the previous version of WAF managed rules is deprecated)</li>
</ul>
<p>All other Page Rules settings will be migrated during 2025.</p>
<h2 id="more-resources">More resources</h2>
<p>If you have feedback to share, refer to our <a href="https://community.cloudflare.com/t/important-page-rules-deprecation/656021">Community thread</a>.</p>
