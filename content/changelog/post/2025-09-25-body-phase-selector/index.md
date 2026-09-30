<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 25, 2025</time><h2 id="post-title">Refine DLP Scans with New Body Phase Selector</h2>
<div class="changelog-badges"><span>gateway</span><span>dlp</span></div><div class="changelog-body"><p>You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.</p>
<p>In the Gateway HTTP policy builder, you will find a new selector called <em>Body Phase</em>. This allows you to define the direction of traffic the DLP engine will inspect:</p>
<ul>
<li><em>Request Body</em>: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.</li>
<li><em>Response Body</em>: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.</li>
</ul>
<p>For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the <strong>Body Phase</strong> to <em>Request Body</em>, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.</p>
<p>All policies without this selector will continue to scan both request and response bodies to ensure continued protection.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#body-phase">Gateway HTTP policy selectors</a>.</p>
</div></article></div>
