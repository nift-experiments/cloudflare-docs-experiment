---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/troubleshooting/testing/
  description: Test your Turnstile implementation with test site keys.
  full_title: Test your Turnstile implementation · Cloudflare Turnstile docs
  head_html: <title>Test your Turnstile implementation · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Test your Turnstile implementation with test site keys."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/troubleshooting/testing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/troubleshooting/testing/index.md"><meta property="og:title" content="Test your Turnstile implementation · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test your Turnstile implementation with test site keys."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/troubleshooting/testing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/troubleshooting/testing/#page","headline":"Test your Turnstile implementation \u00b7 Cloudflare Turnstile docs","description":"Test your Turnstile implementation with test site keys.","url":"https://developers.cloudflare.com/turnstile/troubleshooting/testing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/troubleshooting/testing/
  schema: 1
---
<p>Use dummy sitekeys and secret keys to test your Turnstile implementation without triggering real challenges that would interfere with automated testing suites.</p>
<p>Automated testing suites (like Selenium, Cypress, or Playwright) are detected as bots by Turnstile, which can cause:</p>
<ul>
<li>Tests to fail when Turnstile blocks automated browsers</li>
<li>Unpredictable test results due to challenge variations</li>
<li>Interference with form submission testing</li>
<li>Difficulty testing complete user flows</li>
</ul>
<p>Dummy keys solve this by providing predictable, controlled responses that work with automated testing tools.</p>
<h2 id="test-sitekeys">Test sitekeys</h2>
<table>
<thead>
<tr>
<th>Sitekey</th>
<th>Behavior</th>
<th>Widget Type</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1x00000000000000000000AA</code></td>
<td>Always passes</td>
<td>Visible</td>
<td>Test successful form submissions</td>
</tr>
<tr>
<td><code>2x00000000000000000000AB</code></td>
<td>Always fails</td>
<td>Visible</td>
<td>Test error handling and retry logic</td>
</tr>
<tr>
<td><code>1x00000000000000000000BB</code></td>
<td>Always passes</td>
<td>Invisible</td>
<td>Test invisible widget success flows</td>
</tr>
<tr>
<td><code>2x00000000000000000000BB</code></td>
<td>Always fails</td>
<td>Invisible</td>
<td>Test invisible widget error handling</td>
</tr>
<tr>
<td><code>3x00000000000000000000FF</code></td>
<td>Forces interactive challenge</td>
<td>Visible</td>
<td>Test user interaction scenarios</td>
</tr>
</tbody>
</table>
<h2 id="test-secret-keys">Test secret keys</h2>
<p>Use these secret keys for server-side validation testing:</p>
<table>
<thead>
<tr>
<th>Secret key</th>
<th>Behavior</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1x0000000000000000000000000000000AA</code></td>
<td>Always passes validation</td>
<td>Test successful token validation</td>
</tr>
<tr>
<td><code>2x0000000000000000000000000000000AA</code></td>
<td>Always fails validation</td>
<td>Test validation error handling</td>
</tr>
<tr>
<td><code>3x0000000000000000000000000000000AA</code></td>
<td>Returns &quot;token already spent&quot; error</td>
<td>Test duplicate token handling</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="implementation">Implementation</h2>
<h3 id="local-development">Local development</h3>
<p>Test keys work on any domain, including:</p>
<ul>
<li><code>localhost</code></li>
<li><code>127.0.0.1</code></li>
<li><code>0.0.0.0</code></li>
<li>Any development domain</li>
</ul>
<p>Cloudflare recommends that sitekeys used in production do not allow local domains (<code>localhost</code> or <code>127.0.0.1</code>), but users can choose to add local domains to the list of allowed domains under <a href="/turnstile/additional-configuration/hostname-management/">Hostname Management</a>. Dummy sitekeys can be used from any domain, including on <code>localhost</code>.</p>
<h3 id="client-side-testing">Client-side testing</h3>
<p>Replace your production sitekey with a test sitekey.</p>
<pre tabindex="0"><code class="language-html">&lt;!-- Development/Testing --&gt;&#10;&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;1x00000000000000000000AA&quot;&gt;&lt;/div&gt;&#10;&#10;&lt;!-- Production --&gt;&#10;&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;your-real-sitekey&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h3 id="server-side-testing">Server-side testing</h3>
<p>Replace your production secret key with a test secret key.</p>
<pre tabindex="0"><code class="language-js">// Environment-based configuration&#10;const SECRET_KEY = process.env.NODE_ENV === &#x27;production&#x27; &#10;  ? process.env.TURNSTILE_SECRET_KEY &#10;  : &#x27;1x0000000000000000000000000000000AA&#x27;;&#10;&#10;// Use in validation&#10;const validation = await validateTurnstile(token, SECRET_KEY);&#10;</code></pre>
<h3 id="environment-configuration">Environment configuration</h3>
<p>Set up different keys for different environments.</p>
<pre tabindex="0"><code class="language-shell">&#10;&#35; .env.development&#10;TURNSTILE_SITEKEY=1x00000000000000000000AA&#10;TURNSTILE_SECRET_KEY=1x0000000000000000000000000000000AA&#10;&#10;&#35; .env.test  &#10;TURNSTILE_SITEKEY=2x00000000000000000000AB&#10;TURNSTILE_SECRET_KEY=2x0000000000000000000000000000000AA&#10;&#10;&#35; .env.production&#10;TURNSTILE_SITEKEY=your-real-sitekey&#10;TURNSTILE_SECRET_KEY=your-real-secret-key&#10;</code></pre>
<hr />
<h2 id="dummy-token-behavior">Dummy token behavior</h2>
<h3 id="token-generation">Token generation</h3>
<p>Test sitekeys generate a dummy token: <code>XXXX.DUMMY.TOKEN.XXXX</code></p>
<h3 id="token-validation">Token validation</h3>
<ul>
<li>Test secret keys: Only accept the dummy token, reject real tokens.</li>
<li>Production secret keys: Only accept real tokens, reject dummy tokens.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14992.md")
</aside>
<h3 id="validation-response">Validation response</h3>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;challenge_ts&quot;: &quot;2022-02-28T15:14:30.096Z&quot;,&#10;  &quot;hostname&quot;: &quot;localhost&quot;,&#10;  &quot;error-codes&quot;: [],&#10;  &quot;action&quot;: &quot;test&quot;,&#10;  &quot;cdata&quot;: &quot;test-data&quot;&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;error-codes&quot;: [&quot;invalid-input-response&quot;]&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;error-codes&quot;: [&quot;timeout-or-duplicate&quot;]&#10;}&#10;</code></pre>
<hr />
<h2 id="testing-scenarios">Testing scenarios</h2>
<table>
<thead>
<tr>
<th>Test sitekey</th>
<th>Test secret key</th>
<th><span style="width:200px">Test case</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1x00000000000000000000AA</code></td>
<td><code>1x0000000000000000000000000000000AA</code></td>
<td>This combination will always result in successful validation.</td>
</tr>
<tr>
<td><code>2x00000000000000000000AB</code></td>
<td><code>2x0000000000000000000000000000000AA</code></td>
<td>This combination will always fail.</td>
</tr>
<tr>
<td><code>1x00000000000000000000AA</code></td>
<td><code>3x0000000000000000000000000000000AA</code></td>
<td>This combination will always fail with &quot;timeout-or-duplicate&quot; error.</td>
</tr>
</tbody>
</table>
