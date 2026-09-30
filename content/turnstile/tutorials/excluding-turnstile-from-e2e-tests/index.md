---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/
  description: This tutorial explains how to handle Turnstile in your end-to-end (E2E) tests by using Turnstile's dedicated testing keys.
  full_title: Exclude Turnstile from E2E tests · Cloudflare Turnstile docs
  head_html: <title>Exclude Turnstile from E2E tests · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to handle Turnstile in your end-to-end (E2E) tests by using Turnstile&#x27;s dedicated testing keys."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/index.md"><meta property="og:title" content="Exclude Turnstile from E2E tests · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to handle Turnstile in your end-to-end (E2E) tests by using Turnstile&#x27;s dedicated testing keys."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Node.js,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/#page","headline":"Exclude Turnstile from E2E tests \u00b7 Cloudflare Turnstile docs","description":"This tutorial explains how to handle Turnstile in your end-to-end (E2E) tests by using Turnstile's dedicated testing keys.","url":"https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Node.js","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/tutorials/excluding-turnstile-from-e2e-tests/
  schema: 1
---
<p>This tutorial explains how to handle Turnstile in your end-to-end (E2E) tests by using Turnstile's dedicated testing keys.</p>
<h2 id="overview">Overview</h2>
<p>When running E2E tests, you often want to bypass or simplify the Turnstile verification process. Cloudflare provides official test credentials that always pass verification, making them perfect for testing environments:</p>
<ul>
<li>Test sitekey: <code>1x00000000000000000000AA</code></li>
<li>Test secret key: <code>1x0000000000000000000000000000000AA</code></li>
</ul>
<p>For more details, refer to the <a href="/turnstile/troubleshooting/testing/">testing documentation</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14988.md")
</aside>
<h2 id="implementation">Implementation</h2>
<p>The key to implementing test-environment detection is identifying test requests server-side. Here is a simple approach:</p>
<pre tabindex="0"><code class="language-typescript">// Detect test environments using IP addresses or headers&#10;function isTestEnvironment(request) {&#10;  const testIPs = [&#x27;127.0.0.1&#x27;, &#x27;::1&#x27;];&#10;  const isTestIP = testIPs.includes(request.ip);&#10;  const hasTestHeader = request.headers[&#x27;x-test-environment&#x27;] === &#x27;secret-token&#x27;;&#10;&#10;  return isTestIP || hasTestHeader;&#10;}&#10;&#10;// Use the appropriate credentials based on the environment&#10;function getTurnstileCredentials(request) {&#10;  if (isTestEnvironment(request)) {&#10;    return {&#10;      sitekey: &#x27;1x00000000000000000000AA&#x27;,&#10;      secretKey: &#x27;1x0000000000000000000000000000000AA&#x27;&#10;    };&#10;  }&#10;&#10;  return {&#10;    sitekey: process.env.TURNSTILE_SITE_KEY,&#10;    secretKey: process.env.TURNSTILE_SECRET_KEY&#10;  };&#10;}&#10;</code></pre>
<h2 id="server-side-integration">Server-side integration</h2>
<p>When rendering your page, inject the appropriate sitekey based on the environment:</p>
<pre tabindex="0"><code class="language-typescript">app.get(&#x27;/your-form&#x27;, (req, res) =&gt; {&#10;  const { sitekey } = getTurnstileCredentials(req);&#10;  res.render(&#x27;form&#x27;, { sitekey });&#10;});&#10;</code></pre>
<h2 id="client-side-integration">Client-side integration</h2>
<p>Your template can then use the injected sitekey:</p>
<pre tabindex="0"><code class="language-html">&lt;div class=&quot;turnstile&quot; data-sitekey=&quot;&lt;%= sitekey %&gt;&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h2 id="best-practices">Best practices</h2>
<ol>
<li>
<p><strong>Environment detection</strong></p>
<ul>
<li>Use multiple factors to identify test environments (IP, headers, etc.).</li>
<li>Keep your test environment identifiers secure if you need to test from the public web.</li>
</ul>
</li>
<li>
<p><strong>Credential management</strong></p>
<ul>
<li>Store production credentials securely (for example, in environment variables).</li>
<li>Never commit credentials to version control.</li>
<li>Use different credentials for each environment.</li>
</ul>
</li>
<li>
<p><strong>Deployment safety</strong></p>
<ul>
<li>Add checks to prevent test credentials in production.</li>
<li>Include credential validation in your CI/CD pipeline.</li>
<li>Monitor for accidental test credential usage.</li>
</ul>
</li>
</ol>
<h2 id="testing-considerations">Testing considerations</h2>
<ul>
<li>Test credentials will always pass verification.</li>
<li>They are perfect for automated testing environments.</li>
<li>They help avoid rate limiting during testing.</li>
<li>They make tests more predictable and faster.</li>
</ul>
<h2 id="example-test-setup">Example test setup</h2>
<p>For Cypress or similar E2E testing frameworks:</p>
<pre tabindex="0"><code class="language-typescript">// Set test header for all test requests&#10;beforeEach(() =&gt; {&#10;  cy.intercept(&#x27;*&#x27;, (req) =&gt; {&#10;    req.headers[&#x27;x-test-environment&#x27;] = &#x27;secret-token&#x27;;&#10;  });&#10;});&#10;&#10;// Your test can now interact with the form normally&#10;it(&#x27;submits form successfully&#x27;, () =&gt; {&#10;  cy.visit(&#x27;/your-form&#x27;);&#10;  cy.get(&#x27;form&#x27;).submit();&#10;  // Turnstile will automatically pass verification&#10;});&#10;</code></pre>
<h2 id="conclusion">Conclusion</h2>
<p>By using Turnstile's test credentials and proper environment detection, you can create reliable E2E tests while maintaining security in production. Remember to always keep test credentials separate from production and implement proper safeguards in your deployment process.</p>
