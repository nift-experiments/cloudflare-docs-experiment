<p>The Cloudflare dashboard provides the following settings to manage URL normalization:</p>
<h2 id="normalization-type">Normalization type</h2>
<p>Default value: <em>RFC-3986</em></p>
<p>Selects the type of normalization to perform:</p>
<ul>
<li><em>RFC-3986</em> – Applies URL normalization strictly according to <a href="https://datatracker.ietf.org/doc/html/rfc3986">RFC 3986</a>.</li>
<li><em>Cloudflare</em> – In addition to what is defined in RFC 3986, applies <a href="/rules/normalization/how-it-works/#cloudflare-normalization">extra URL normalization techniques</a>.</li>
</ul>
<h2 id="normalize-incoming-urls">Normalize incoming URLs</h2>
<p>Default value: <em>On</em></p>
<p>Configures the URLs of all incoming traffic to Cloudflare:</p>
<ul>
<li>When enabled, all incoming URLs are normalized before they pass to subsequent Cloudflare features that can receive a URL as input, such as Page Rules, WAF custom rules, Workers, and Access.</li>
<li>When disabled, incoming URLs are not normalized before passing to subsequent Cloudflare features.</li>
</ul>
<h2 id="normalize-urls-to-origin">Normalize URLs to origin</h2>
<p>Default value: <em>Off</em></p>
<p>Configures URLs sent to the origin:</p>
<ul>
<li>When enabled, requests sent to the origin are normalized.</li>
<li>When disabled, requests sent to the origin are not modified.</li>
</ul>
<p>You can only view and enable this option when <strong>Normalize incoming URLs</strong> is enabled.</p>
<p>For examples of how these settings affect URL normalization, refer to the <a href="/rules/normalization/examples/">URL normalization examples</a>.</p>
