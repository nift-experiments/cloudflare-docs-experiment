<p>You can change the configuration settings described below in a configuration rule.</p>
<h2 id="automatic-https-rewrites">Automatic HTTPS Rewrites</h2>
<p><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a> prevents end users from seeing <code>Mixed content</code> errors by rewriting URLs from <code>http</code> to <code>https</code> for resources or links on your website that can be served with HTTPS.</p>
<p>Use this setting to turn on or off Automatic HTTPS Rewrites for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13005.md")
</div></details>
<h2 id="browser-integrity-check">Browser Integrity Check</h2>
<p><a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a> blocks access to pages based on specific HTTP headers commonly abused by spammers.</p>
<p>Use this setting to turn on or off Browser Integrity Check for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13006.md")
</div></details>
<h2 id="disable-real-user-monitoring-rum">Disable Real User Monitoring (RUM)</h2>
<p><a href="/web-analytics/">Cloudflare Web Analytics</a>, also known as Real User Monitoring (RUM), is Cloudflare's free, privacy-first analytics for your website.</p>
<p>Use this setting to turn off Web Analytics for matching requests.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/13004.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13007.md")
</div></details>
<h2 id="disable-zaraz">Disable Zaraz</h2>
<p><a href="/zaraz/">Cloudflare Zaraz</a> gives you complete control over third-party tools and services for your website, and allows you to offload them to the Cloudflare global network.</p>
<p>Use this setting to turn off Zaraz for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13008.md")
</div></details>
<h2 id="email-obfuscation">Email Obfuscation</h2>
<p><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Obfuscation</a> prevents spam by hiding email addresses from bots and harvesters while keeping them visible to human visitors to your site.</p>
<p>Use this setting to turn on or off Email Obfuscation for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13009.md")
</div></details>
<h2 id="fonts">Fonts</h2>
<p><a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a> rewrites Google Fonts to be delivered from a website's own origin, eliminating the need to rely on third-party font providers.</p>
<p>Use this setting to turn on or off Cloudflare Fonts for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13010.md")
</div></details>
<h2 id="hotlink-protection">Hotlink Protection</h2>
<p><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a> prevents your images from being used by other sites, potentially reducing the bandwidth consumed by your origin server.</p>
<p>Use this setting to turn on or off Hotlink Protection for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13011.md")
</div></details>
<h2 id="i-m-under-attack">I'm Under Attack</h2>
<p>When enabled, <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> performs additional security checks to help mitigate layer 7 DDoS attacks. Validated users access your website and suspicious traffic is blocked.</p>
<p>Use this setting to turn on or off Under Attack mode for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13012.md")
</div></details>
<h2 id="markdown-for-agents">Markdown for Agents</h2>
<p><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> automatically converts HTML to Markdown for requests that use content negotiation headers (<code>Accept: text/markdown</code>).</p>
<p>Use this setting to turn on or off Markdown for Agents for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13013.md")
</div></details>
<h2 id="opportunistic-encryption">Opportunistic Encryption</h2>
<p><a href="/ssl/edge-certificates/additional-options/opportunistic-encryption/">Opportunistic Encryption</a> allows browsers to access HTTP URIs over an encrypted TLS channel.</p>
<p>Use this setting to turn on or off Opportunistic Encryption for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13014.md")
</div></details>
<h2 id="polish">Polish</h2>
<p><a href="/images/polish/">Cloudflare Polish</a> is a one-click image optimization product that automatically optimizes images in your site.</p>
<p>Use this setting to configure Polish for matching requests:</p>
<ul>
<li>Off</li>
<li>Lossless</li>
<li>Lossy</li>
<li>WebP</li>
</ul>
<p>Refer to <a href="/images/polish/compression/#compression-options">Compression options</a> for more information on these values.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13015.md")
</div></details>
<h2 id="request-body-buffering">Request Body Buffering</h2>
<p>Use the Request Body Buffering setting to configure the request body buffering mode for matching requests:</p>
<ul>
<li><strong>Standard</strong> (default): Allows Cloudflare products to inspect a prefix of the request body when necessary for enabled functionality on your zone.</li>
<li><strong>Full</strong>: Buffers the entire request body before sending the request to your origin server.</li>
<li><strong>None</strong>: Strictly no buffering. The request body is streamed directly to the origin server without inspection.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13003.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13016.md")
</div></details>
<h2 id="response-body-buffering">Response Body Buffering</h2>
<p>Use the Response Body Buffering setting to configure the response body buffering mode for matching requests:</p>
<ul>
<li><strong>Standard</strong> (default): Allows Cloudflare products to inspect a prefix of the response body when necessary for enabled functionality on your zone.</li>
<li><strong>None</strong>: Strictly no buffering. The response body is streamed directly to the client without inspection.</li>
</ul>
<p>For features that inspect response content and troubleshooting guidance, refer to <a href="/rules/configuration-rules/response-body-inspection/">Response body inspection</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13002.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13017.md")
</div></details>
<h2 id="rocket-loader">Rocket Loader</h2>
<p><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a> prioritizes your website's content (such as text, images, and fonts) by deferring the loading of all your JavaScript code until after rendering.</p>
<p>Use this setting to turn on or off Rocket Loader for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13018.md")
</div></details>
<h2 id="ssl">SSL</h2>
<p><a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption modes</a> control the scheme (<code>http://</code> or <code>https://</code>) that Cloudflare uses to connect to your origin web server and how SSL certificates presented by your origin will be validated.</p>
<p>Use this setting to configure the SSL/TLS encryption mode for matching requests:</p>
<ul>
<li>Off</li>
<li>Flexible</li>
<li>Full</li>
<li>Strict</li>
<li>Origin Pull</li>
</ul>
<p>Refer to <a href="/ssl/origin-configuration/ssl-modes/#available-encryption-modes">Available encryption modes</a> for more information on these values.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13019.md")
</div></details>
