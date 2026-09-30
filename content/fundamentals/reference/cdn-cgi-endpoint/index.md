<p>When you <a href="/fundamentals/manage-domains/add-site/">add a domain to Cloudflare</a>, Cloudflare adds a <code>/cdn-cgi/</code> endpoint (<code>www.example.com/cdn-cgi/</code>) to that domain.</p>
<p>This endpoint is managed and served by Cloudflare. It cannot be modified or customized. The endpoint is not used by every Cloudflare product, but you may find some products use the endpoint in its URL.</p>
<p>A few examples include (but are not limited to):</p>
<ul>
<li><a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#identify-the-cloudflare-data-center-serving-your-request">Identify the Cloudflare data center serving your request</a>, which is helpful for troubleshooting (<code>https://&lt;YOUR_DOMAIN&gt;/cdn-cgi/trace</code>).</li>
<li><a href="/bots/additional-configurations/javascript-detections/">JavaScript detection</a> used by Cloudflare bot products (<code>example.com/cdn-cgi/challenge-platform/</code>)</li>
<li><a href="/images/optimization/transformations/overview/">Image transformations</a> in the new URLs you would use for images (<code>example.com/cdn-cgi/image/</code>)</li>
<li><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email address obfuscation</a> used to hide email addresses from malicious bots (<code>example.com/cdn-cgi/l/email-protection</code>)</li>
<li><a href="/web-analytics/get-started/#sites-proxied-through-cloudflare">Web analytics</a> for a website proxied through Cloudflare (<code>example.com/cdn-cgi/rum</code>). This endpoint returns a <code>204</code> HTTP status code.</li>
<li><a href="/speed/optimization/content/speed-brain/">Speed Brain</a> adds an HTTP header called <code>Speculation-Rules</code> to web page responses. This header contains a URL that hosts an opinionated Speculation-Rules configuration, which instructs the browser to initiate prefetch requests for anticipated future navigations.</li>
</ul>
<h2 id="recommended-exclusions">Recommended exclusions</h2>
<h3 id="exclude-from-security-scanners">Exclude from security scanners</h3>
<p>Some scanners may display an error because certain <code>/cdn-cgi/</code> endpoints do not have an <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">HSTS setting</a> applied to it or for similar reasons. Because the endpoint is managed by Cloudflare, you can ignore the error and do not need to worry about it.</p>
<p>To prevent scanner errors, omit the <code>/cdn-cgi/</code> endpoint from your security scans.</p>
<h3 id="disallow-using-robots-txt">Disallow using robots.txt</h3>
<p><code>/cdn-cgi/</code> also can cause issues with various web crawlers.</p>
<p>Search engine crawlers can encounter <a href="/support/troubleshooting/general-troubleshooting/troubleshooting-crawl-errors/">errors when crawling these endpoints</a> and — though these errors do not impact site rankings — they may surface in your webmaster dashboard.</p>
<p>SEO and other web crawlers may also mistakenly crawl these endpoints, thinking that they are part of your site's content.</p>
<p>As a best practice, update your <code>robots.txt</code> file to include <code>Disallow: /cdn-cgi/</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8808.md")
</aside>
