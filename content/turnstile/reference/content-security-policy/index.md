<p>If your website uses a <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP">Content Security Policy (CSP)</a> header, you must configure it to allow Turnstile's scripts and iframes. Without the correct CSP directives, Turnstile may fail to load.</p>
<p>Cloudflare recommends using the nonce-based approach documented with <a href="https://w3c.github.io/webappsec-csp/#framework-directive-source-list">CSP3</a>. Include your nonce in the <code>api.js</code> script tag and Turnstile will propagate it to dynamically loaded resources. Turnstile works with <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy#strict-dynamic"><code>strict-dynamic</code></a>.</p>
<p>Alternatively, add the following values to your CSP header:</p>
<ul>
<li><strong>script-src</strong>: <code>https://challenges.cloudflare.com</code></li>
<li><strong>frame-src</strong>: <code>https://challenges.cloudflare.com</code></li>
</ul>
<p>We recommend validating your CSP with <a href="https://csp-evaluator.withgoogle.com/">Google's CSP Evaluator</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14997.md")
</aside>
<h2 id="pre-clearance-support">Pre-clearance support</h2>
<p>If you are using <a href="/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile">Turnstile in pre-clearance mode</a>, Turnstile sets the <code>cf_clearance</code> cookie by doing a fetch request to a special endpoint in <a href="/fundamentals/reference/cdn-cgi-endpoint/"><code>/cdn-cgi/</code></a> of your domain.</p>
<p>For this request to succeed, your <code>connect-src</code> directive must include <code>'self'</code>.</p>
