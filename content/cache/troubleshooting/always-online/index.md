<p>Observe the following best practices when enabling Always Online with Internet Archive integration.</p>
<ul>
<li><strong>Allow requests from the Internet Archive IP addresses.</strong> Origin servers receive requests from the Internet Archive IPs. Make sure you are not blocking requests from the Internet Archive IP range: <code>207.241.224.0/20</code> and <code>208.70.24.0/21</code>.</li>
<li><strong>The Internet Archive does not consider your origin server's cache-control header.</strong> When the Internet Archive is crawling sites, it will crawl sites regardless of their cache-control, since the Internet Archive does not cache assets, but archives them.</li>
<li><strong>Consider potential conflicts with Cloudflare features that transform URIs.</strong> Always Online with Internet Archive integration may cause issues with Cache Rules and other Cloudflare features that transform URIs due to the way the Internet Archive crawls pages to archive. Specifically, some redirects that take place at the edge may cause the Internet Archive's crawler not to archive the target URL. Before enabling Origin Cache Control, review <a href="/cache/concepts/default-cache-behavior/">how Cloudflare caches resources by default</a> as well as any Cache Rules you have configured so that you can avoid these issues. If you experience problems, disable Always Online.</li>
<li><strong>Do not block Known Bots or Verified Bots via a WAF custom rule.</strong> If you block either of these bot lists, the Internet Archive will not be able to crawl.</li>
</ul>
<p>Do not use Always Online with:</p>
<ul>
<li>API traffic.</li>
<li>An <a href="/waf/tools/ip-access-rules/">IP Access rule</a> or a <a href="/waf/custom-rules/">WAF custom rule</a> that blocks the United States or</li>
<li>Bypass Cache cache rules. Always Online ignores Bypass Cache cache rules and serves Always Online cached assets.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>There are limitations with the Always Online functionality:</p>
<ol>
<li>Always Online is not immediately active for sites recently added due to:
<ul>
<li>DNS record propagation, which can take 24-72 hours</li>
<li>Always Online has not initially crawled the website</li>
</ul>
</li>
<li>Cloudflare cannot show private content behind logins or handle form submission (POSTs) if your origin web server is offline.</li>
</ol>
<p>Always Online does not trigger for HTTP response codes such as <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-404/">404</a>, <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/">503</a>, or <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/">500</a> errors such as database connection errors or internal server errors. This is because these status codes indicate the origin is reachable and responding — Always Online only activates when Cloudflare cannot connect to your origin at all (resulting in Cloudflare-generated <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520–527</a> status codes). If your origin returns a 5xx error, the origin is online by definition and Always Online will not intervene.</p>
<h2 id="frequently-asked-questions">Frequently asked questions</h2>
<ol>
<li>
<p>How can I know if a page has been crawled?</p>
<ul>
<li>You can go to the <a href="https://web.archive.org/">Internet Archive</a> and search for the page URL to see if it has been crawled or not.</li>
<li>You can also check this via the <a href="https://archive.org/help/wayback_api.php">Internet Archive Availability API</a>.</li>
</ul>
</li>
<li>
<p>Why were not pages x, y, and z crawled?</p>
<ul>
<li>Since Cloudflare only requests to crawl the most popular pages on the site, it is possible that there will be missing pages. If you really want to archive a page, then you can visit the <a href="https://web.archive.org/save">Internet Archive</a> save page and ask them to crawl a particular page.</li>
</ul>
</li>
<li>
<p>What IP addresses do we need to allowlist to make sure crawling works?</p>
<ul>
<li>IP Range: <code>207.241.224.0/20</code> and <code>208.70.24.0/21</code>. Note that this ip range belongs to Internet Archive and NOT Cloudflare, since it is the Internet Archive that does the crawling.</li>
</ul>
</li>
<li>
<p>What user agent should the origin expect to see?</p>
<ul>
<li>Currently the Internet Archive uses: <code>Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/605.1.15</code>.</li>
</ul>
</li>
</ol>
