---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/features/guardrails/
  description: Restrict HTTP and HTTPS requests by destination hostname.
  full_title: Guardrails · Cloudflare Browser Run docs
  head_html: <title>Guardrails · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict HTTP and HTTPS requests by destination hostname."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/features/guardrails/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/features/guardrails/index.md"><meta property="og:title" content="Guardrails · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict HTTP and HTTPS requests by destination hostname."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/features/guardrails/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/features/guardrails/#page","headline":"Guardrails \u00b7 Cloudflare Browser Run docs","description":"Restrict HTTP and HTTPS requests by destination hostname.","url":"https://developers.cloudflare.com/browser-run/features/guardrails/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/features/guardrails/
  schema: 1
---
<p>Guardrails limit a Browser Run session's HTTP and HTTPS requests to permitted hostnames.</p>
<p>This allows you to:</p>
<ul>
<li><strong>Keep automation focused</strong> — Limit each session to hostnames needed for its task.</li>
<li><strong>Support page dependencies</strong> — Include required third-party APIs, scripts, images, and fonts.</li>
<li><strong>Run self-contained pages</strong> — Prevent external HTTP and HTTPS requests.</li>
</ul>
<p>Session guardrails apply to browser sessions created with <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, or <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a>. They are unavailable for <a href="/browser-run/quick-actions/">Quick Actions</a>.</p>
<h2 id="set-up-guardrails">Set up guardrails</h2>
<p>Add the hostname the browser will visit and any hostnames required for redirects, APIs, scripts, images, or fonts. For common or shared hostnames, use a domain set instead of listing each hostname individually.</p>
<p>Set guardrails when you start a new session. The policy remains fixed for the lifetime of that session.</p>
<p>Choose a property based on how you maintain the allowlist:</p>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Use when</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>allowedDomains</code></td>
<td><code>string[]</code></td>
<td>Your workflow needs a short, stable list with exact hostname control.</td>
<td>50 entries</td>
</tr>
<tr>
<td><code>allowedDomainSets</code></td>
<td><code>string[]</code></td>
<td>Many sessions share a longer list, or your team maintains one centrally.</td>
<td>Four entries</td>
</tr>
</tbody>
</table>
<p>Both properties are optional and form one allowlist. If you omit both, HTTP and HTTPS requests remain unrestricted.</p>
<h3 id="check-policy-requirements">Check policy requirements</h3>
<p>Before starting a session, make sure your guardrail policy meets these requirements:</p>
<ul>
<li>Add no more than 50 entries to <code>allowedDomains</code>.</li>
<li>Add no more than four entries to <code>allowedDomainSets</code>.</li>
<li>Write hostname patterns without a scheme, port, or path.</li>
<li>Use no more than one wildcard in each hostname pattern.</li>
</ul>
<p>If a policy does not meet these requirements, Browser Run rejects the session request with a <code>400</code> response.</p>
<h3 id="start-a-guarded-session-with-puppeteer">Start a guarded session with Puppeteer</h3>
<p>This function starts a session that permits <code>example.com</code>, its subdomains, and hostnames from the <code>common-cdns</code> domain set.</p>
<p>The example assumes a browser binding named <code>MYBROWSER</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3713.md")
</div>
<p><a href="/browser-run/playwright/">Playwright</a> accepts the same <code>guardrails</code> object through its <code>launch()</code> options.</p>
<h3 id="rest-api">REST API</h3>
<p>Use the REST API to acquire a guarded session outside Workers. This request assumes <code>$ACCOUNT_ID</code> is set and <code>$CLOUDFLARE_API_TOKEN</code> has Browser Rendering Write permission.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="compatibility">Compatibility</h3>
@markup("md", "content/.markup/bodies/3712.md")
</aside>
<h2 id="add-allowed-hostnames">Add allowed hostnames</h2>
<p>Use <code>allowedDomains</code> to specify which hostnames the browser can request.</p>
<p>Each entry must contain only a hostname. Do not include a protocol such as <code>https://</code>, a port such as <code>:443</code>, or a path such as <code>/api</code>.</p>
<ul>
<li><code>example.com</code> allows only <code>example.com</code>.</li>
<li><code>*.example.com</code> allows subdomains such as <code>www.example.com</code> and <code>api.example.com</code>, but not <code>example.com</code>.</li>
</ul>
<p>You can use one <code>*</code> wildcard in each entry to match variations of a hostname:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Matches</th>
<th>Does not match</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td><code>example.com</code></td>
<td><code>www.example.com</code>, <code>evil-example.com</code></td>
</tr>
<tr>
<td><code>*.example.com</code></td>
<td><code>www.example.com</code>, <code>api.v1.example.com</code></td>
<td><code>example.com</code>, <code>evilexample.com</code></td>
</tr>
<tr>
<td><code>*example.com</code></td>
<td><code>example.com</code>, <code>www.example.com</code>, <code>evilexample.com</code></td>
<td><code>example.net</code></td>
</tr>
<tr>
<td><code>api.*.example.com</code></td>
<td><code>api.v1.example.com</code>, <code>api.staging.example.com</code></td>
<td><code>api.example.com</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="prefer-subdomain-wildcards">Prefer subdomain wildcards</h3>
@markup("md", "content/.markup/bodies/3711.md")
</aside>
<h2 id="use-a-domain-set">Use a domain set</h2>
<p>Domain sets help you reuse shared hostname lists across sessions. The <code>allowedDomainSets</code> property accepts the <code>common-cdns</code> set name and HTTPS URLs.</p>
<h3 id="allow-common-cdn-hostnames">Allow common CDN hostnames</h3>
<p>Use the Cloudflare-maintained <code>common-cdns</code> set when your page depends on assets served by common content delivery network (CDN) hostnames:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;allowedDomains&quot;: [&quot;example.com&quot;],&#10;	&quot;allowedDomainSets&quot;: [&quot;common-cdns&quot;]&#10;}&#10;</code></pre>
<p>Cloudflare maintains the <code>common-cdns</code> set and may change it over time. Use <code>allowedDomains</code> or a hosted hostname list when you need a fixed set of permitted hostnames.</p>
<h3 id="use-a-hosted-hostname-list">Use a hosted hostname list</h3>
<p>Use an HTTPS URL for hostname patterns specific to your pages and dependencies:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;allowedDomainSets&quot;: [&quot;https://example.com/browser-run-hostnames.txt&quot;]&#10;}&#10;</code></pre>
<p>For example, <code>browser-run-hostnames.txt</code> could contain:</p>
<pre tabindex="0"><code class="language-txt">example.com&#10;&#42;.example.com&#10;&#10;&#35; Third-party API&#10;api.example.net&#10;</code></pre>
<p>The hosted list must meet these requirements:</p>
<table>
<thead>
<tr>
<th>Requirement</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Protocol</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Content type</td>
<td><code>text/plain</code></td>
</tr>
<tr>
<td>Line format</td>
<td>One hostname pattern per line</td>
</tr>
<tr>
<td>Comments</td>
<td>Lines starting with <code>#</code> and blank lines are ignored</td>
</tr>
<tr>
<td>Validation</td>
<td>One invalid line rejects the entire hosted list</td>
</tr>
</tbody>
</table>
<p>Cloudflare caches a hosted list for up to one hour. Updates after the cache refresh affect only newly started sessions, not existing sessions.</p>
<h2 id="block-all-web-requests">Block all web requests</h2>
<p>An empty <code>allowedDomains</code> array blocks all HTTP and HTTPS requests. Use it for self-contained pages, such as rendering inline HTML to a screenshot or PDF.</p>
<p>Inline content can render, but the browser cannot request external APIs or assets. Do not include any domain sets with this policy.</p>
<p>Use this policy object as the <code>guardrails</code> value across supported integrations:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;allowedDomains&quot;: []&#10;}&#10;</code></pre>
<h2 id="verify-blocked-requests">Verify blocked requests</h2>
<p>Use Puppeteer to request a hostname outside the allowlist. This example checks the response status and guardrail headers.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3714.md")
</div>
<p>A blocked request returns a <code>403</code> response with these headers:</p>
<table>
<thead>
<tr>
<th>Header</th>
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-mitigated</code></td>
<td><code>guardrails</code></td>
<td>Confirms guardrails blocked the request</td>
</tr>
<tr>
<td><code>cf-brapi-guardrails-reason</code></td>
<td><code>not-in-allowlist</code></td>
<td>Requested hostname was not permitted</td>
</tr>
</tbody>
</table>
<h2 id="use-guardrails-with-live-view">Use guardrails with Live View</h2>
<p>Session guardrails remain active when you use <a href="/browser-run/features/live-view/">Live View</a>. The <code>{ mode: &quot;readonly&quot; }</code> Live View setting controls viewer interaction and does not change the session hostname allowlist.</p>
