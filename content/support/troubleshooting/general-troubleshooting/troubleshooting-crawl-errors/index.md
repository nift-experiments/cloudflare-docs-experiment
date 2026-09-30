<p>Cloudflare allows search engine crawlers and bots. If you observe crawl issues or Cloudflare challenges presented to the search engine crawler or bot, <a href="/support/contacting-cloudflare-support/">contact Cloudflare support</a> with the information you gather when troubleshooting the crawl errors via the methods outlined in this guide.</p>
<hr />
<h2 id="disable-anti-bot-modules">Disable Anti-bot modules</h2>
<p>Search engine crawlers' requests, when proxied through Cloudflare, can be blocked by anti-bot modules installed on your origin server. Try disabling any anti-bot modules to prevent your origin from blocking these requests.</p>
<hr />
<h2 id="adjust-google-and-bing-crawl-rates">Adjust Google and Bing crawl rates</h2>
<p>To optimize CDN performance, Google and Bing assign special crawl rates to websites that use CDN services in order. Special crawl rates do not negatively affect Search Engine Optimization (SEO) and Search Engine Results Pages (SERPs). To change your crawl rates for Bing and Google, follow the guides below:</p>
<ul>
<li>Change the Google crawl rate by <a href="https://support.google.com/webmasters/answer/48620?hl=en">reviewing Google’s documentation</a>.</li>
<li>Change your Bing crawl rate via guidance from Bing’s documentation:
<ul>
<li><a href="https://www.bing.com/webmasters/help/?topicid=55a30303">Bing Crawl Control</a></li>
<li><a href="https://blogs.bing.com/webmaster/2009/08/10/crawl-delay-and-the-bing-crawler-msnbot">Crawl Delay and the Bing Crawler</a></li>
</ul>
</li>
</ul>
<hr />
<h2 id="prevent-crawl-errors">Prevent crawl errors</h2>
<p>Review the following recommendations to prevent crawler errors:</p>
<ul>
<li>
<p>Monitor the performance and availability of your website using a third-party tool:</p>
<ul>
<li><a href="http://www.statuscake.com/">StatusCake</a></li>
<li><a href="http://www.pingdom.com/">Pingdom</a></li>
<li><a href="http://www.monitor.us/">Monitor.Us</a></li>
<li><a href="https://updown.io/">Updown</a></li>
</ul>
</li>
<li>
<p>Do not block Google crawler IP addresses via <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/tools/ip-access-rules/">IP Access rules</a>. If you are using <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, make sure they do not apply to the Google crawler.</p>
<p>Confirm an IP address belongs to Google by consulting Google’s documentation on <a href="https://support.google.com/webmasters/bin/answer.py?answer=80553">verifying googlebot IP addresses</a>.</p>
</li>
<li>
<p>Do not block the United States via <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/tools/ip-access-rules/">IP Access rules</a>.</p>
</li>
<li>
<p>Do not block Google User-Agents in your <code>.htaccess</code> file, server configuration, <a href="http://support.google.com/webmasters/bin/answer.py?answer=35303"><code>robots.txt</code></a>, or web application.</p>
</li>
</ul>
<p>Google uses a <a href="https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers">variety of User-Agents</a> to crawl your website. You can <a href="https://support.google.com/webmasters/answer/6062598?hl=en">test your <code>robots.txt</code> via Google</a>.</p>
<ul>
<li>Do not allow crawling of files in the <code>/cdn-cgi/</code> directory. This path is used internally by Cloudflare and Google encounters errors when crawling it. Disallow crawls of <code>cdn-cgi</code> via <code>robots.txt</code>:</li>
</ul>
<p><code>Disallow: /cdn-cgi/</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14698.md")
</aside>
<ul>
<li>Ensure your <a href="http://support.google.com/webmasters/bin/answer.py?hl=en&amp;answer=1061943"><code>robots.txt</code> file allows the AdSense crawler</a>.</li>
<li><a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Restore original visitor IP addresses</a> in your server logs.</li>
</ul>
<hr />
<h2 id="troubleshoot-crawl-errors">Troubleshoot crawl errors</h2>
<p>Troubleshooting steps for the most commonly reported crawl errors are mentioned below.</p>
<h3 id="http-4xx-errors">HTTP 4XX Errors</h3>
<p><a href="/support/troubleshooting/http-status-codes/4xx-client-error/">HTTP 4XX errors</a> are the most common type of crawl error. Cloudflare delivers these errors from your web server to Google. These errors are caused for various reasons such as a missing page on your web server or a malformed link in your HTML. The solution depends upon the problem encountered.</p>
<h3 id="http-5xx-errors">HTTP 5XX Errors</h3>
<p><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">HTTP 5XX errors</a> indicate that either Cloudflare or your origin web server experienced an internal error. To correlate occurrences of crawl errors with site outages, monitor your origin web server's health. Monitoring your website health both through Cloudflare and directly to your origin web server IPs determines whether errors occurred due to Cloudflare or your origin web server.</p>
<h3 id="dns-errors">DNS Errors</h3>
<p>Troubleshooting steps vary depending on whether your domain is on Cloudflare via a Full or CNAME setup. To verify which setup your domain uses, open a terminal and execute the following command (replace <code>www.example.com</code> with your Cloudflare domain):</p>
<p><code>dig +short SOA</code> <code>www.example.com</code></p>
<p>For domains on a <a href="/dns/zone-setups/partial-setup/">Partial (CNAME) setup</a>, the result response contains cdn.cloudflare.net. For example:</p>
<p><code>example.com.cdn.cloudflare.net.</code></p>
<p>For domains on a <a href="/dns/zone-setups/full-setup/">Full setup</a>, the result response contains the <code>cloudflare.com</code> domain in the nameservers listed. For example:</p>
<p><code>josh.ns.cloudflare.com. dns.cloudflare.com. 2013050901 10000 2400 604800 3600</code></p>
<p>Once you’ve confirmed how your domain was setup with Cloudflare, proceed with the troubleshooting steps appropriate to your domain setup.</p>
<p><strong>CNAME</strong></p>
<p>Contact your hosting provider to investigate DNS errors and provide the date Google encountered DNS errors. Additionally, review the <a href="http://www.cloudflare.com/system-status">Cloudflare System Status</a> page for any network outages on the date the errors were encountered by Google.</p>
<p><strong>Full</strong></p>
<p><a href="/support/contacting-cloudflare-support/">Contact Cloudflare support</a> and provide the date and time that Google observed the errors.</p>
<h3 id="requesting-troubleshooting-assistance">Requesting troubleshooting assistance</h3>
<p>If the above troubleshooting steps do not resolve your crawl errors, follow the steps below to export crawler errors as a <code>.csv</code> file from your Google Webmaster Tools Dashboard. Include this <code>.csv</code> file when <a href="/support/contacting-cloudflare-support/">contacting Cloudflare Support</a>.</p>
<ol>
<li>Log in to your Google Webmaster Tools account and navigate to the <strong>Health</strong> section of the affected domain.</li>
<li>Click <strong>Crawl Errors</strong> in the left hand navigation.</li>
<li>Click <strong>Download</strong> to export the list of errors as a <code>.csv</code> file.</li>
<li>Provide the downloaded <code>.csv</code> file to Cloudflare support.</li>
</ol>
<hr />
<h2 id="related-resources">Related resources</h2>
<p><a href="https://support.google.com/webmasters/answer/7440203#not_found_404">Google’s documentation on crawl errors and troubleshooting</a></p>
