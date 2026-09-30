---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/
  description: Client-side JavaScript challenges that run on every request to identify automated traffic.
  full_title: JavaScript Detections · Cloudflare challenges docs
  head_html: <title>JavaScript Detections · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="Client-side JavaScript challenges that run on every request to identify automated traffic."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/index.md"><meta property="og:title" content="JavaScript Detections · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Client-side JavaScript challenges that run on every request to identify automated traffic."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Challenges"><meta name="pcx_tags" content="JavaScript,CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/#page","headline":"JavaScript Detections \u00b7 Cloudflare challenges docs","description":"Client-side JavaScript challenges that run on every request to identify automated traffic.","url":"https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","CSP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/challenge-types/javascript-detections/
  schema: 1
---
<p>JavaScript Detections is a type of challenge separate from Cloudflare’s Challenge Pages or Turnstile. JavaScript Detections helps Cloudflare's <a href="/bots/">bot solutions</a> identify automated requests.</p>
<p>While Challenge Pages and Turnstile rely on client-side signals to determine the authenticity of a request, Bot Management’s JavaScript Detections relies on client-side signals and runs on every single request made to your website.</p>
<h2 id="process">Process</h2>
<p>JavaScript Detections is implemented on your website via a lightweight, invisible JavaScript code snippet that follows Cloudflare's <a href="https://www.cloudflare.com/privacypolicy/">privacy standards</a>.</p>
<p>JavaScript is injected only in response to requests for HTML pages or page views, excluding AJAX calls. API and mobile application traffic is unaffected.</p>
<p>JavaScript Detections has a lifespan of 15 minutes. However, the code is injected again before the session expires. After page load, the script is deferred and utilizes a separate thread (where available) to ensure that performance impact is minimal. The snippets of JavaScript will contain a source pointing to the Challenge Platform, with paths that start with <code>/cdn-cgi/challenge-platform/…</code></p>
<p>Once JavaScript Detections is injected on the HTML page, the visitor's browser will run the JavaScript code snippet and a <code>cf_clearance</code> cookie is issued to the visitor. The information in JavaScript Detections is stored in the <code>cf_clearance</code> cookie and is used to populate <code>js_detection.passed</code>.</p>
<ul>
<li>If the visitor is verified and a <code>cf_clearance</code> cookie is issued, it will contain the outcome: <code>cf.bot_management.js_detection.passed</code> = <code>true</code></li>
<li>If the verification fails, the cookie will contain the outcome: <code>cf.bot_management.js_detection.passed</code> = <code>false</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4041.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4040.md")
</aside>
<p>When the visitor encounters a WAF custom rule on your website, the rule will check the outcome of the <code>cf_clearance</code> cookie. The outcome of the <code>cf_clearance</code> cookie determines whether the request passes, or is blocked or challenged.</p>
<p>Refer to the steps below to enable and enforce JavaScript Detections.</p>
<h2 id="1-enable-javascript-detections"><ol>
<li>Enable JavaScript Detections</li>
</ol></h2>
<p>For Bot Fight Mode customers, <a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> is automatically enabled and cannot be disabled.</p>
<p>For Super Bot Fight Mode and Bot Management for Enterprise customers, <a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> is optional.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4042.md")
</div>
<p>For more details on how to set up bot protection, refer to the <a href="/bots/get-started/">Bots documentation</a>.</p>
<h2 id="2-enforce-execution-of-javascript-detections"><ol start="2">
<li>Enforce execution of JavaScript Detections</li>
</ol></h2>
<p>Once you enable JavaScript detections, you must use the <code>cf.bot_management.js_detection.passed</code> field to create <a href="/waf/custom-rules/">WAF custom rules</a> (or the <code>request.cf.botManagement.jsDetection.passed</code> variable in <a href="/workers/">Workers</a>).</p>
<p>When adding this field to WAF custom rules, it is used on endpoints expecting browser traffic (avoiding native mobile applications or websocket endpoints), after a user's first request to your application (Cloudflare needs at least one HTML request before injecting JavaScript detection), and with the Managed Challenge action, because there are legitimate reasons a user might not have passed a JavaScript Detection challenge (network issues, ad blockers, disabled JavaScript in browser, native mobile applications).</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>You must have an <a href="/bots/plans/bm-subscription/">Enterprise Bot Management</a> subscription.</li>
<li>You must have JavaScript Detections enabled on your zone.</li>
<li>You must have <a href="/cloudflare-challenges/challenge-types/javascript-detections/#if-you-have-a-content-security-policy-csp">updated your Content Security Policy headers</a> for JavaScript detections.</li>
<li>You must not run this field on websocket endpoints.</li>
<li>You must use the field in a custom rules expression that expects only browser traffic.</li>
<li>The action should always be a managed challenge in case a legitimate user has not received the challenge for network or browser reasons.</li>
<li>The path specified in the rule builder should never be the first HTML page a user visits when browsing your site.</li>
</ul>
<p>The <code>cf.bot_management.js_detection.passed</code> field should never be used in a WAF custom rule that matches a visitor's first request to a site. It is necessary to have at least one HTML request before Cloudflare can inject JavaScript detection.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4045.md")
</div></div>
<p>Refer to the <a href="/waf/custom-rules/create-dashboard/">WAF documentation</a> for more information on creating a custom rule.</p>
<h2 id="api">API</h2>
<p>If you enable JavaScript Detections via the dashboard, Cloudflare will insert a script tag in all HTML pages served on your website. If you would prefer to limit where JavaScript Detections is served, you can do so with the JavaScript Detections API script.</p>
<p>The JavaScript Detections API allows you more granular control over when and where JavaScript Detections is injected on your website, as well as an option for callback handling (for logging or other additional actions).</p>
<p>You can explicitly add a script reference to <code>/cdn-cgi/challenge-platform/scripts/jsd/api.js</code> and your own code calling <code>window.cloudflare.jsd.executeOnce</code> on specific HTML pages of your website.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4039.md")
</aside>
<p>The following script must be added to every page that you wish to have JavaScript Detections enabled:</p>
<pre tabindex="0"><code class="language-html">&lt;script&gt;&#10;&#10;function jsdOnload(){&#10;  window.cloudflare.jsd.executeOnce(&#10;    {&#10;      callback: function(result){&#10;        console.log(&#x27;jsd outcome&#x27;, result);&#10;      }&#10;    }&#10;  );&#10;}&#10;&lt;/script&gt;&#10;&lt;script src=&quot;/cdn-cgi/challenge-platform/scripts/jsd/api.js?onload=jsdOnload&quot; async&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4038.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4037.md")
</aside>
<h2 id="considerations">Considerations</h2>
<p>JavaScript Detections does not guarantee a specific bot score.</p>
<ul>
<li>If the JavaScript Detections injection or execution fails and <code>cf.bot_management.js_detection.passed</code> = <code>false</code>, a separate Bot Management heuristic can still yield a <code>1</code> or higher bot score, independent of JavaScript Detections.</li>
<li>If the JavaScript Detections passes, the final bot score may still be <code>1</code> due to other detection heuristics (for example, known malicious IP, signature detection, and more), resulting in <code>js_detection.passed</code> = <code>true</code>, but <code>score</code> = <code>1</code>.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<h3 id="if-you-enabled-bot-management-before-june-2020">If you enabled Bot Management before June 2020</h3>
<p>Customers who enabled Enterprise Bot Management before June 2020 do not have JavaScript Detections enabled by default (unless specifically requested). These customers can still enable the feature in the Cloudflare dashboard.</p>
<h3 id="if-it-is-the-first-request-to-your-website">If it is the first request to your website</h3>
<p>The first request from a new client to your website or application will generally not have JavaScript Detections data (<code>cf.bot_management.js_detection.passed</code> = <code>false</code>). This is because Cloudflare needs at least one HTML request before injecting JavaScript Detection and issuing the <code>cf_clearance</code> cookie.</p>
<p>Subsequent requests can include a <code>cf_clearance</code> cookie if JavaScript ran successfully.</p>
<h3 id="if-you-have-a-content-security-policy-csp">If you have a Content Security Policy (CSP)</h3>
<p>If you have a <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span>, you need to take additional steps to implement JavaScript Detections:</p>
<ul>
<li>Ensure that anything under <code>/cdn-cgi/challenge-platform/</code> is allowed. Your CSP should allow scripts served from your origin domain (<code>script-src self</code>).</li>
<li>For <code>nonce</code> script tags:
<ul>
<li>
<p>If your CSP uses a <code>nonce</code> for script tags, Cloudflare will add these nonces to the scripts it injects by parsing your CSP response header.</p>
</li>
<li>
<p>If your CSP does not use <code>nonce</code> for script tags and <strong>JavaScript Detections</strong> is enabled, you may see a console error such as <code>Refused to execute inline script because it violates the following Content Security Policy directive: &quot;script-src 'self'&quot;. Either the 'unsafe-inline' keyword, a hash ('sha256-b123b8a70+4jEj+d6gWI9U6IilUJIrlnRJbRR/uQl2Jc='), or a nonce ('nonce-...') is required to enable inline execution.</code> We highly discourage the use of <code>unsafe-inline</code> and instead recommend the use CSP <code>nonces</code> in script tags which we parse and support in our CDN.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4036.md")
</aside>
<h3 id="if-you-have-etags">If you have ETags</h3>
<p>Enabling JavaScript Detections (JSD) will strip <a href="/cache/reference/etag-headers/">ETags</a> from HTML responses where JSD is injected.</p>
<h3 id="if-your-origin-sends-a-no-transform-header">If your origin sends a <code>no-transform</code> header</h3>
<p>If the origin response includes a <code>Cache-Control: no-transform</code> directive, Cloudflare does not inject the JavaScript Detections script. The <code>cf.bot_management.js_detection.passed</code> field will show as <code>missing</code> for these requests.</p>
<p>To use JavaScript Detections, remove the <code>no-transform</code> directive from <code>Cache-Control</code> response headers on pages where you want JavaScript Detections to run. For more information, refer to <a href="/cache/concepts/cache-control/#interaction-with-other-cloudflare-features">Cache-Control directives</a>.</p>
