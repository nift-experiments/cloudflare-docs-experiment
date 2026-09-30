<p>Domains added to Cloudflare receive SSL certificates and can serve traffic over HTTPS. However, after starting to use Cloudflare, some customers notice missing content or page rendering issues when they first serve HTTPS traffic.</p>
<p>Typically, the problem is due to a request for HTTP resources from a web page served over HTTPS. For example, you type <code>https://example.com</code> in a browser and the page contains an image reference via HTTP in the HTML to <code>&lt;img src=&quot;http://example.com/resource.jpg&quot;&gt;</code>.</p>
<p>Normally, if your website loads all resources securely over HTTPS, visitors observe a lock icon in the address bar of their browser.</p>
<p>This indicates your site has a working SSL certificate and all resources loaded by the site are loaded over HTTPS. The green lock assures visitors that their connection is safe. One of the <a href="#symptoms-of-mixed-content-occurrence">symptoms of mixed content</a> is that different icons appear instead of the green lock icon.</p>
<hr />
<h2 id="symptoms-of-mixed-content-occurrence">Symptoms of mixed content occurrence</h2>
<p>Most modern browsers block HTTP requests on secure HTTPS pages. Blocked content can include images, JavaScript, CSS, or other content that affects how the page looks or behaves.</p>
<h3 id="browser-indications">Browser indications</h3>
<p>Each web browser uses different methods to warn visitors about mixed content on a website, potentially including:</p>
<ul>
<li>A yellow triangle or information symbol beside the URL bar</li>
<li>Messages mentioning &quot;secure content&quot;</li>
</ul>
<h3 id="console-logs"><strong>Console logs</strong></h3>
<p>For mixed content warnings, the web browser loads the resources but users do not see the lock icon in the URL. Warning messages appear within the browser’s debug tools:</p>
<p><img src="/assets/upstream/images/support/hc-import-mixed_content_warning.png" alt="Screenshot of mixed content warnings displayed in a browser console." /></p>
<p>For mixed content errors, the browser refuses to load the resources over an insecure connection:</p>
<p><img src="/assets/upstream/images/support/hc-import-mixed_content_error.png" alt="Screenshot of mixed content errors displayed in a browser console." /></p>
<p>Information on using the browser’s debug tools to locate these issues are found in the documentation for <a href="https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content">Chrome</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content">Firefox</a>. Alternatively, you can view your page source and find specific references of <em>http://</em> for paths to other resources.</p>
<hr />
<h2 id="resolution">Resolution</h2>
<h3 id="general-advice">General advice</h3>
<p>There are two methods to resolve mixed content errors.</p>
<ol>
<li>Load all resources via your HTML source without specifying the HTTP or HTTPS protocols.
For example, using <code>/domain.com/path/to.file</code> instead of <code>http://domain.com/path/to.file</code>.</li>
<li>Depending on your Content Management System, check for plugins that automatically rewrite HTTP resources to HTTPS. Cloudflare provides such a service via <a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites">Automatic HTTPS Rewrites</a>.</li>
</ol>
<h3 id="wordpress-users">WordPress users</h3>
<p>Cloudflare recommends WordPress users to install the <a href="https://wordpress.org/plugins/cloudflare/">Cloudflare WordPress plugin</a> and enable the <em>Automatic HTTPS rewrites</em> option within the plugin.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content">Debugging mixed content in Chrome</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content">Debugging mixed content in Firefox</a></li>
<li><a href="https://community.cloudflare.com/t/community-tip-fixing-mixed-content-errors/42476">Community Tip - Fixing mixed content errors</a></li>
</ul>
