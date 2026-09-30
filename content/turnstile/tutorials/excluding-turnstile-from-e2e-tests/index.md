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
<pre><code class="language-typescript">// Detect test environments using IP addresses or headers&#10;function isTestEnvironment(request) {&#10;  const testIPs = [&#x27;127.0.0.1&#x27;, &#x27;::1&#x27;];&#10;  const isTestIP = testIPs.includes(request.ip);&#10;  const hasTestHeader = request.headers[&#x27;x-test-environment&#x27;] === &#x27;secret-token&#x27;;&#10;&#10;  return isTestIP || hasTestHeader;&#10;}&#10;&#10;// Use the appropriate credentials based on the environment&#10;function getTurnstileCredentials(request) {&#10;  if (isTestEnvironment(request)) {&#10;    return {&#10;      sitekey: &#x27;1x00000000000000000000AA&#x27;,&#10;      secretKey: &#x27;1x0000000000000000000000000000000AA&#x27;&#10;    };&#10;  }&#10;&#10;  return {&#10;    sitekey: process.env.TURNSTILE_SITE_KEY,&#10;    secretKey: process.env.TURNSTILE_SECRET_KEY&#10;  };&#10;}&#10;</code></pre>
<h2 id="server-side-integration">Server-side integration</h2>
<p>When rendering your page, inject the appropriate sitekey based on the environment:</p>
<pre><code class="language-typescript">app.get(&#x27;/your-form&#x27;, (req, res) =&gt; {&#10;  const { sitekey } = getTurnstileCredentials(req);&#10;  res.render(&#x27;form&#x27;, { sitekey });&#10;});&#10;</code></pre>
<h2 id="client-side-integration">Client-side integration</h2>
<p>Your template can then use the injected sitekey:</p>
<pre><code class="language-html">&lt;div class=&quot;turnstile&quot; data-sitekey=&quot;&lt;%= sitekey %&gt;&quot;&gt;&lt;/div&gt;&#10;</code></pre>
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
<pre><code class="language-typescript">// Set test header for all test requests&#10;beforeEach(() =&gt; {&#10;  cy.intercept(&#x27;*&#x27;, (req) =&gt; {&#10;    req.headers[&#x27;x-test-environment&#x27;] = &#x27;secret-token&#x27;;&#10;  });&#10;});&#10;&#10;// Your test can now interact with the form normally&#10;it(&#x27;submits form successfully&#x27;, () =&gt; {&#10;  cy.visit(&#x27;/your-form&#x27;);&#10;  cy.get(&#x27;form&#x27;).submit();&#10;  // Turnstile will automatically pass verification&#10;});&#10;</code></pre>
<h2 id="conclusion">Conclusion</h2>
<p>By using Turnstile's test credentials and proper environment detection, you can create reliable E2E tests while maintaining security in production. Remember to always keep test credentials separate from production and implement proper safeguards in your deployment process.</p>
