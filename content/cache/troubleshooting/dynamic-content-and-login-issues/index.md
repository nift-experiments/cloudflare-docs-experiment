---
cp9:
  canonical: https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/
  description: Troubleshoot login failures, missing session cookies, and challenge loops caused by caching dynamic content.
  full_title: Dynamic content and login issues · Cloudflare Cache (CDN) docs
  head_html: <title>Dynamic content and login issues · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot login failures, missing session cookies, and challenge loops caused by caching dynamic content."><link rel="canonical" href="https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/index.md"><meta property="og:title" content="Dynamic content and login issues · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot login failures, missing session cookies, and challenge loops caused by caching dynamic content."><meta property="og:url" content="https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="Cookies,Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/#page","headline":"Dynamic content and login issues \u00b7 Cloudflare Cache (CDN) docs","description":"Troubleshoot login failures, missing session cookies, and challenge loops caused by caching dynamic content.","url":"https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies","Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cache/troubleshooting/dynamic-content-and-login-issues/
  schema: 1
---
<p>Dynamic pages such as login forms, checkout flows, and authenticated application routes can break when they are cached too aggressively.</p>
<p>Common symptoms include:</p>
<ul>
<li>Users can load the login page, but the sign-in form fails after submission.</li>
<li>Sessions do not persist after a successful sign-in.</li>
<li>The origin sends a <code>Set-Cookie</code> header, but the browser never stores the cookie.</li>
<li>A challenge page appears, but after solving it the user returns to the login page or loses form state.</li>
</ul>
<h2 id="cached-login-page-strips-session-cookies">Cached login page strips session cookies</h2>
<p>One common cause is a <a href="/cache/how-to/cache-rules/">Cache Rule</a> or legacy Page Rule configured to cache dynamic HTML.</p>
<p>This usually happens when all of the following are true:</p>
<ul>
<li>The page is configured as <strong>Eligible for cache</strong> or <strong>Cache Everything</strong>.</li>
<li>The response is dynamic HTML such as <code>/login</code> or <code>/account</code>.</li>
<li>The origin sends a <code>Set-Cookie</code> header.</li>
<li>An <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge TTL</a> or status-code TTL overrides origin cache directives.</li>
</ul>
<p>In this configuration, Cloudflare can cache the response and remove the <code>Set-Cookie</code> header before the response is stored at the edge. As a result, the browser receives the login page but never gets the session cookie required for the next request.</p>
<h3 id="how-to-confirm">How to confirm</h3>
<p>Check the response for the login page or other dynamic route.</p>
<p>If you see both of the following, the page is probably cached when it should not be:</p>
<ul>
<li><code>CF-Cache-Status: HIT</code> or <code>CF-Cache-Status: EXPIRED</code></li>
<li>No <code>Set-Cookie</code> header in the response, even though your origin usually sets one</li>
</ul>
<p>You may also see framework-specific failures after form submission, for example:</p>
<ul>
<li>A redirect back to the login page</li>
<li>A <code>403</code> or <code>500</code> after sign-in</li>
<li>CSRF validation errors</li>
<li>Missing server-side session state</li>
</ul>
<p>This issue is common with frameworks that rely on a session or CSRF cookie on the first page load, including JavaServer Faces, ASP.NET, PHP session handlers, Django, Rails, and Laravel.</p>
<h3 id="resolution">Resolution</h3>
<p>Do not cache login pages or other authenticated HTML.</p>
<p>Instead:</p>
<ol>
<li>Restrict <strong>Eligible for cache</strong> or <strong>Cache Everything</strong> to static paths only.</li>
<li>Add a more specific Cache Rule that bypasses or disables caching for routes such as <code>/login</code>, <code>/account</code>, <code>/cart</code>, <code>/checkout</code>, and application API paths.</li>
<li>If the origin must control caching, remove any Edge TTL override that forces the page to be cached.</li>
<li>Verify the fixed response now returns <code>CF-Cache-Status: DYNAMIC</code>, <code>MISS</code>, or <code>BYPASS</code>, and preserves <code>Set-Cookie</code>.</li>
</ol>
<p>For more information on cookie behavior, refer to <a href="/cache/concepts/cache-behavior/#interaction-of-set-cookie-response-header-with-cache">Interaction of Set-Cookie response header with Cache</a>.</p>
<h2 id="challenge-loops-on-login-or-form-flows">Challenge loops on login or form flows</h2>
<p>Security challenges can also interrupt dynamic flows.</p>
<p>Two common patterns are:</p>
<ul>
<li>A challenge is triggered on the initial <code>GET</code> request for the login page. The user solves the challenge, but the application loses the original session or CSRF context.</li>
<li>A challenge is triggered on the <code>POST</code> request that submits the login form or other sensitive action. The browser may have to repeat the request after the challenge, which can break the original form submission.</li>
</ul>
<h3 id="how-to-confirm-1">How to confirm</h3>
<p>Check whether a <a href="/waf/custom-rules/">WAF custom rule</a>, <a href="/waf/managed-rules/">managed rule</a>, or <a href="/waf/rate-limiting-rules/">rate limiting rule</a> applies to the login path.</p>
<p>If the issue only affects routes such as <code>/login</code>, <code>/signin</code>, <code>/checkout</code>, or <code>/api/auth/*</code>, and the application works when the challenge is disabled for those paths, the challenge is likely interrupting the flow.</p>
<h3 id="resolution-1">Resolution</h3>
<p>Use one of the following approaches:</p>
<ol>
<li>Exclude the login or form submission path from the challenge rule.</li>
<li>Narrow the rule expression so it applies to suspicious traffic only.</li>
<li>If you must protect the route, use a less disruptive control on the page load and apply stronger actions elsewhere in the flow.</li>
</ol>
<p>When debugging, also verify that rules are not matching Cloudflare-generated paths such as <code>/cdn-cgi/*</code>.</p>
<p>For more information on challenge-related behavior, refer to <a href="/rules/reference/troubleshooting/">Rules troubleshooting</a> and <a href="/waf/troubleshooting/">Cloudflare WAF troubleshooting</a>.</p>
