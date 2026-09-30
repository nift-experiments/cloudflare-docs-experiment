<p>The Any Hostname feature removes the requirement to specify hostnames during widget creation, allowing widgets to function on any domain.</p>
<p>By default, hostname validation is a security feature that prevents unauthorized use of your widgets. The Any Hostname entitlement removes this restriction, making the hostname field optional during widget creation.</p>
<p>When enabled, widgets can be created without the required hostname specification and used on any domain without pre-configuration. Hostname validation protection is also removed.</p>
<h2 id="implementation">Implementation</h2>
<p>To reduce security risks when using Any Hostname, monitor widget usage through <a href="/turnstile/turnstile-analytics/">Turnstile Analytics</a> to identify unexpected patterns, implement server-side validation with hostname checking in your application code, and use <code>action</code> and <code>cData</code> parameters to track widget usage sources and identify where widgets are being deployed.</p>
<p>When using the Any Hostname feature, it is essential to implement additional validation in your server-side code to maintain security controls. Always validate the <code>hostname</code> field in Siteverify responses.</p>
<pre><code class="language-js">async function validateTurnstileWithHostname(token, expectedHostnames = []) {&#10;  const response = await fetch(&#x27;https://challenges.cloudflare.com/turnstile/v0/siteverify&#x27;, {&#10;    method: &#x27;POST&#x27;,&#10;    headers: { &#x27;Content-Type&#x27;: &#x27;application/json&#x27; },&#10;    body: JSON.stringify({&#10;      secret: process.env.TURNSTILE_SECRET,&#10;      response: token&#10;    })&#10;  });&#10;&#10;  const result = await response.json();&#10;&#10;  if (!result.success) {&#10;    return { valid: false, error: &#x27;Token validation failed&#x27; };&#10;  }&#10;&#10;  // Additional hostname validation when using Any Hostname&#10;  if (expectedHostnames.length &gt; 0 &amp;&amp; !expectedHostnames.includes(result.hostname)) {&#10;    return { &#10;      valid: false, &#10;      error: &#x27;Hostname not in allowed list&#x27;,&#10;      hostname: result.hostname &#10;    };&#10;  }&#10;&#10;  return { valid: true, data: result };&#10;}&#10;</code></pre>
<p>You should regularly review Turnstile Analytics for unexpected usage patterns and monitor the hostname field in Siteverify responses. You can set up alerts for widget usage on unexpected domains.</p>
<p>Use <code>action</code> and <code>cData</code> parameters to track widget usage sources.</p>
<pre><code class="language-html">&lt;!-- Widget with tracking information --&gt;&#10;&lt;div class=&quot;cf-turnstile&quot; &#10;     data-sitekey=&quot;your-site-key&quot;&#10;     data-action=&quot;customer-portal&quot;&#10;     data-cdata=&quot;tenant-123&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<hr />
<h2 id="use-cases">Use cases</h2>
<p>The Any Hostname feature is particularly valuable for customers with:</p>
<ul>
<li>Large domain portfolios with many domains to manage individually.</li>
<li>Dynamic subdomain creation and frequently create subdomains or customer-specific domains.</li>
<li>Multi-tenant applications such as SaaS platforms serving multiple customer domains.</li>
<li>Development environments that test across various staging and development domains.</li>
</ul>
