<p>Cloudflare automatically attaches headers to every request made through Browser Run. These headers make it easy for destination servers to identify that these requests came from Cloudflare.</p>
<h2 id="user-agent">User-Agent</h2>
<p>The default User-Agent depends on how you access Browser Run:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Default User-Agent</th>
<th>Customizable</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/browser-run/quick-actions/">Quick Actions</a></td>
<td><code>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36</code></td>
<td>Yes, using the <code>userAgent</code> parameter</td>
</tr>
<tr>
<td><a href="/browser-run/quick-actions/crawl-endpoint/">Crawl endpoint</a></td>
<td><code>CloudflareBrowserRenderingCrawler/1.0</code></td>
<td>No</td>
</tr>
<tr>
<td><a href="/browser-run/cdp/">CDP</a> (<a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>)</td>
<td>The default User-Agent of the underlying Chrome version</td>
<td>Yes, via Puppeteer/Playwright configuration</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3585.md")
</aside>
<h2 id="non-configurable-headers">Non-configurable headers</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3584.md")
</aside>
<table>
<thead>
<tr>
<th>Header</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-brapi-request-id</code></td>
<td>A unique identifier for the Browser Run request when using <a href="/browser-run/quick-actions/">Quick Actions</a></td>
</tr>
<tr>
<td><code>cf-brapi-devtools</code></td>
<td>A unique identifier for the Browser Run request when using <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, or <a href="/browser-run/cdp/">CDP</a></td>
</tr>
<tr>
<td><code>cf-biso-devtools</code></td>
<td>A flag indicating the request originated from Cloudflare's rendering infrastructure</td>
</tr>
<tr>
<td><code>Signature-agent</code></td>
<td><a href="https://web-bot-auth.cloudflare-browser-rendering-085.workers.dev">The location of the bot public keys</a>, used to sign the request and verify it came from Cloudflare</td>
</tr>
<tr>
<td><code>Signature</code> and <code>Signature-input</code></td>
<td>A digital signature, used to validate requests, as shown in <a href="https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture">this architecture document</a></td>
</tr>
</tbody>
</table>
<h3 id="about-web-bot-auth">About Web Bot Auth</h3>
<p>The <code>Signature</code> headers use an authentication method called <a href="/bots/reference/bot-verification/web-bot-auth/">Web Bot Auth</a>. Web Bot Auth leverages cryptographic signatures in HTTP messages to verify that a request comes from an automated bot. To verify a request originated from Cloudflare Browser Run, use the keys found on <a href="https://web-bot-auth.cloudflare-browser-rendering-085.workers.dev/.well-known/http-message-signatures-directory">this directory</a> to verify the <code>Signature</code> and <code>Signature-Input</code> found in the headers from the incoming request. A successful verification proves that the request originated from Cloudflare Browser Run and has not been tampered with in transit.</p>
<h3 id="bot-detection">Bot detection</h3>
<p>Browser Run uses different bot detection IDs depending on the method. <a href="/browser-run/quick-actions/">Quick Actions</a> (excluding the <a href="/browser-run/quick-actions/crawl-endpoint/">crawl endpoint</a>), <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, and <a href="/browser-run/cdp/">CDP</a> share one ID, while the crawl endpoint has its own.</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Bot detection ID</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/browser-run/quick-actions/">Quick Actions</a>, <a href="/browser-run/puppeteer/">Puppeteer</a>, <a href="/browser-run/playwright/">Playwright</a>, <a href="/browser-run/cdp/">CDP</a></td>
<td><code>119853733</code></td>
</tr>
<tr>
<td><a href="/browser-run/quick-actions/crawl-endpoint/">Crawl endpoint</a></td>
<td><code>128292352</code></td>
</tr>
</tbody>
</table>
<p>If you are attempting to scan your own zone and want Browser Run to access your website freely without your bot protection configuration interfering, you can create a WAF skip rule to <a href="/browser-run/faq/#can-i-allowlist-browser-run-on-my-own-website">allowlist Browser Run</a>.</p>
