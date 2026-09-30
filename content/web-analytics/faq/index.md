---
cp9:
  canonical: https://developers.cloudflare.com/web-analytics/faq/
  description: Answers to common questions about Cloudflare Web Analytics.
  full_title: FAQs · Cloudflare Web Analytics docs
  head_html: <title>FAQs · Cloudflare Web Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Answers to common questions about Cloudflare Web Analytics."><link rel="canonical" href="https://developers.cloudflare.com/web-analytics/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web-analytics/faq/index.md"><meta property="og:title" content="FAQs · Cloudflare Web Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Answers to common questions about Cloudflare Web Analytics."><meta property="og:url" content="https://developers.cloudflare.com/web-analytics/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Web Analytics"><meta name="algolia_product_filter" content="Cloudflare Web Analytics"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Cloudflare Web Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web-analytics/faq/#page","headline":"FAQs \u00b7 Cloudflare Web Analytics docs","description":"Answers to common questions about Cloudflare Web Analytics.","url":"https://developers.cloudflare.com/web-analytics/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web-analytics/faq/
  schema: 1
---
<p>Below you will find answers to our most commonly asked questions. If you cannot find the answer you are looking for, refer to the <a href="https://community.cloudflare.com/">community page</a> to explore more resources.</p>
<ul>
<li><a href="#errors">Errors</a></li>
<li><a href="#setup">Setup</a></li>
<li><a href="#functionality">Functionality</a></li>
</ul>
<h2 id="errors">Errors</h2>
<h3 id="when-i-add-the-beacon-to-my-website-and-load-the-webpage-i-see-an-error-that-includes-is-not-allowed-by-access-control-allow-origin-cors-what-is-happening">When I add the beacon to my website and load the webpage, I see an error that includes <code>is not allowed by Access-Control-Allow-Origin</code> (CORS). What is happening?</h3>
<p>This error usually occurs when the hostname of the site loading the analytics does not match the name of the analytics site configured in the dashboard. Double-check that they are identical.</p>
<p>Cloudflare matches hostnames based on a postfix. For example, if you set up analytics for <code>example.com</code>, we will allow analytics from <code>www.example.com</code>, <code>blog.staging.example.com</code>, and <code>fooexample.com</code>. However, we will not allow analytics from <code>example.com.br</code>.</p>
<p>You may also see this error if the site does not send a <code>Referer</code> or <code>Origin</code> header. The <code>Referer</code> header is required (do not try to use the <code>Referrer-policy</code> header instead). We have a change in-flight now that only the <code>Origin</code> header will be required – we believe there is no way to disable that in the browser.</p>
<h3 id="the-analytics-beacon-is-blocked-by-ad-blockers-including-adblockplus-brave-duckduckgo-extension-etc-why-is-that">The analytics beacon is blocked by ad-blockers (including adblockplus, Brave, DuckDuckGo extension, etc). Why is that?</h3>
<p>Cloudflare is aware that the analytics beacon is blocked by these services.</p>
<p>While Cloudflare Web Analytics uses a JavaScript beacon, Cloudflare’s edge analytics cannot be blocked because we can measure every request that is received. Edge analytics are available to any customer who proxies traffic through Cloudflare. Currently, users on Pro, Business, and Enterprise plans get advanced web analytics powered by our edge logs.</p>
<h3 id="why-am-i-not-seeing-all-the-metrics-for-single-page-application-spa-or-multiple-page-application-mpa">Why am I not seeing all the metrics for single-page application (SPA) or multiple-page application (MPA)?</h3>
<p>Every route change that occurs in the single-page app will send the measurement of the route before the route is changed to the beacon endpoint. The measurement for the last route change will be sent whenever the user leaves the tab or closes the browser window. That will trigger <code>visibilityState</code> to a hidden state. Whenever that happens, Beacon JS sends the payload using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon">Navigator.sendBeacon method</a> that should not be cancelled even when the browser window is closed. However, due to compatibility, old browsers would fallback to using AJAX (<code>XmlHttpRequest</code>), which can be cancelled when the browser window is closed, so the last payload that gets sent to the beacon endpoint can be lost. Also, due to various network conditions, there can be data loss when the payload is sent to the beacon endpoint.</p>
<h3 id="for-the-same-site-why-would-i-see-more-data-reported-with-an-automatic-setup">For the same site, why would I see more data reported with an automatic setup?</h3>
<p>Unless you are using Rules to control which pages to be measured, using <a href="/web-analytics/get-started/#sites-proxied-through-cloudflare">automatic setup</a> will inject the JS snippet on all pages (sub-domains) under the zone.</p>
<p>If you used a <a href="/web-analytics/get-started/#sites-not-proxied-through-cloudflare">manual setup</a> instead, only those pages that render the JS snippet will be reported.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/102.md")
</aside>
<h3 id="my-website-is-proxied-through-cloudflare-but-web-analytic-s-automatic-setup-is-not-working">My website is proxied through Cloudflare, but Web Analytic's automatic setup is not working.</h3>
<p>If you have a <code>Cache-Control</code> header set to <code>public, no-transform</code>, Cloudflare proxy will not be able to modify the original payload of the website. Therefore, the Beacon script will not be automatically injected to your site, and Web Analytics will not work. Refer to <a href="/cache/concepts/cache-control/">Origin cache control</a> for more information.</p>
<h3 id="why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgi-rum">Why am I getting a <code>405 Method Not Allowed</code> error from <code>/cdn-cgi/rum</code>?</h3>
<p>The <code>/cdn-cgi/rum</code> endpoint only accepts <code>POST</code> requests for data ingestion. If you send a request using any other HTTP method (for example, <code>GET</code>, <code>PUT</code>, or <code>DELETE</code>), the endpoint returns a <code>405 Method Not Allowed</code> response with an <code>Allow: POST, OPTIONS</code> header (<code>OPTIONS</code> is allowed for <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS">CORS</a> support).</p>
<p>The Web Analytics beacon (<code>beacon.min.js</code>) always uses <code>POST</code> when reporting metrics. If you see <code>405</code> errors in your logs, the requests are not coming from the beacon itself.</p>
<p>They are most likely coming from an automated testing tool making erroneous requests, in which case you should correct it to use <code>POST</code> or ignore the errors.</p>
<p>We do not support custom integrations directly with the endpoint: all requests should originate from our beacon JavaScript.</p>
<h3 id="why-am-i-seeing-syntax-errors-from-the-beacon-script-in-internet-explorer">Why am I seeing syntax errors from the beacon script in Internet Explorer?</h3>
<p>Internet Explorer 11 was the final version of Internet Explorer and it was <a href="https://techcommunity.microsoft.com/blog/windows-itpro-blog/internet-explorer-11-desktop-app-retirement-faq/2366549">declared completely end-of-life (EOL) in 2022</a>.</p>
<p>Our beacon script targets modern syntax which Internet Explorer does not support. This will cause a non-user-visible error when the script attempts to execute. The only functional impact is that beacons are not collected from these old browsers.</p>
<p>For customers using automatic-injection, Cloudflare adds <code>type=&quot;module&quot;</code> to the <code>&lt;script&gt;</code> tag to prevent loading in Internet Explorer and similarly old, deprecated browsers.</p>
<p>For customers using the manual embed approach, you will need to add <code>type=&quot;module&quot;</code> to the <code>&lt;script&gt;</code> tag manually. Our dashboard has been updated to include this attribute in the installation instructions.</p>
<hr />
<h2 id="setup">Setup</h2>
<h3 id="i-am-proxying-my-site-through-cloudflare-should-i-manually-add-the-js-beacon">I am proxying my site through Cloudflare. Should I manually add the JS beacon?</h3>
<p>You can, but you do not have to. Cloudflare Web Analytics is designed primarily for customers who do not use Cloudflare's proxy to measure their web traffic.</p>
<p>Existing Cloudflare customers can access analytics collected from our edge on the <strong>Analytics</strong> tab of the dashboard. You can also enable Web Analytics to measure performance using JavaScript.</p>
<p>Using a domain proxied through Cloudflare with <a href="/web-analytics/get-started/#sites-proxied-through-cloudflare">automatic setup</a> will report stats back to your own domain's <code>/cdn-cgi/rum</code> endpoint. If you have installed JS snippet yourself (a <a href="/web-analytics/get-started/#sites-not-proxied-through-cloudflare">manual setup</a>), it will report back to <code>cloudflareinsights.com/cdn-cgi/rum</code> endpoint.</p>
<h3 id="can-i-add-web-analytics-to-my-site-using-a-tag-manager-like-google-tag-manager-gtm">Can I add Web Analytics to my site using a tag manager like Google Tag Manager (GTM)?</h3>
<p>Yes. Instead of embedding the script using a tag manager as shown here:</p>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://static.cloudflareinsights.com/beacon.min.js&quot;&#10;	data-cf-beacon=&#x27;{&quot;token&quot;: &quot;$SITE_TOKEN&quot;}&#x27;&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<p>Add the following script:</p>
<pre tabindex="0"><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://static.cloudflareinsights.com/beacon.min.js?token=$SITE_TOKEN&quot;&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<h3 id="what-do-i-need-to-add-to-my-content-security-policy-csp">What do I need to add to my Content Security Policy (CSP)?</h3>
<p>If your site implements a Content Security Policy (CSP), you'll need to add some entries to this HTTP header to allow browsers to download the beacon script and transmit beacons to Cloudflare.</p>
<p><strong>Warning:</strong> be sure to validate any CSP changes on a test environment before releasing an update to your production environment. You may wish to use <a href="https://developers.cloudflare.com/client-side-security/rules/">Content Security Rules</a> or trial with <code>Content-Security-Policy-Report-Only</code> first.</p>
<p>You'll first need to permit our script to execute by adding it to your <code>script-src</code> directive:</p>
<pre tabindex="0"><code>script-src [...existing values...] https://static.cloudflareinsights.com/beacon.min.js&#10;</code></pre>
<p><em>Note: if you have a query string in the script as per the example above for Google Tag Manager, then you'll need to include this in the URL too, e.g. <code>script-src [...existing values...] https://static.cloudflareinsights.com/beacon.min.js?token=$SITE_TOKEN</code></em></p>
<p>Secondly, you'll need to permit the endpoint we transmit the beacon data to.</p>
<p>For automatic injection, this will be the same domain, so ensure your <code>connect-src</code> includes <code>'self'</code>:</p>
<pre tabindex="0"><code>connect-src [...existing values...] &#x27;self&#x27;&#10;</code></pre>
<p>For manual embedding, this script instead connects to <code>cloudflareinsights.com</code>, so ensure that's included instead:</p>
<pre tabindex="0"><code>connect-src [...existing values...] cloudflareinsights.com&#10;</code></pre>
<h3 id="how-can-i-enforce-subresource-integrity-sri-with-the-js-beacon">How can I enforce Subresource Integrity (SRI) with the JS beacon?</h3>
<p>If you're using the automated injection (i.e. not the manually-embedded script approach mentioned above), Cloudflare automatically includes an <code>integrity</code> attribute in the <code>&lt;script&gt;</code>. This ensures the script will only execute if a local hash of its downloaded contents match the integrity hash supplied in the HTML.</p>
<p>Unfortunately, if you're using the manually-embedded script approach, there is no current way to safely apply an <code>integrity</code> attribute because we do not support version-pinning our beacon script. We do this because it ensures we can release periodic updates to maintain security, address bugs and ensure</p>
<h3 id="can-i-use-the-same-js-snippet-for-a-different-domain">Can I use the same JS Snippet for a different domain?</h3>
<p>No. However, if the apex domain (also known as &quot;root domain&quot; or &quot;naked domain&quot;) is the same, you can use the same site tag. For example, if you have provided us a hostname <code>example.com</code> when registering a site, you can use the JS snippet from that site for <code>abc.example.com</code> and <code>def.example.com</code> since they use the same apex domain. When payload gets sent to the beacon endpoint, we validate the hostname with postfix matching, so if your domain shares the same apex domain, that would work.</p>
<h3 id="can-i-use-automatic-setup-with-a-dns-only-domain-cname-setup">Can I use automatic setup with a DNS-only domain (CNAME setup)?</h3>
<p>No, you can only use the <a href="/web-analytics/get-started/#sites-proxied-through-cloudflare">automatic setup</a> with JS snippet injection if traffic to your domain is proxied through Cloudflare (orange-clouded).</p>
<p>If you have a DNS-only domain, you will have to do a <a href="/web-analytics/get-started/#sites-not-proxied-through-cloudflare">manual setup</a> instead.</p>
<h3 id="what-prevents-the-js-snippet-from-being-added-to-a-page">What prevents the JS Snippet from being added to a page?</h3>
<p>For Cloudflare to automatically add the JavaScript snippet, your pages need to have valid HTML.</p>
<p>For example, Cloudflare would not be able to enable Web Analytics on a page like this:</p>
<pre tabindex="0"><code class="language-html">Hello world.&#10;</code></pre>
<p>For Web Analytics to correctly insert the JavaScript snippet, you would need valid HTML output, such as:</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;title&gt;Title&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;&#10;		&lt;p&gt;Hello world.&lt;/p&gt;&#10;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h3 id="can-i-use-real-user-monitoring-rum-with-cloudflare-workers">Can I use Real User Monitoring (RUM) with Cloudflare Workers?</h3>
<p>Cloudflare's Real User Monitoring (RUM) operates exclusively on the initial client request and cannot collect metrics from Worker subrequests. This is a fundamental architectural limitation designed to ensure accurate performance measurements and prevent duplicate or misleading analytics data.</p>
<hr />
<h2 id="functionality">Functionality</h2>
<h3 id="is-the-data-sampled">Is the data sampled?</h3>
<p>We retain unsampled beacon data for the past 7 days, after this point data is aggregated down to around 10%.</p>
<p>When aggregating metrics in the Cloudflare Dashboard or querying the GraphQL API, a level of sampling (between 0.0001% and 100%) will be dynamically selected based on the filters applied and the volume of matching rows. This ensures a high confidence in the accuracy of figures while maintaining a reasonable response time. You can <a href="https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/">read more about this approach on the Cloudflare blog</a>.</p>
<p>Note: the GraphQL API exposes a <code>sampleInterval</code> field to indicate which level of sampling has been applied to the query.</p>
<ul>
<li>The beacon script will fire on every pageview.</li>
<li>The data ingestion pipeline does not apply sampling—every received beacon will be recorded.</li>
<li>We store the unsampled data for 7 days.</li>
<li>We also aggregate it down so it's around 10% of the original volume for long-term storage.</li>
<li>Sites with very low traffic volumes are sampled to greater percentages to maintain high confidence in aggregate figures.</li>
</ul>
<h3 id="can-i-see-server-side-analytics-by-url">Can I see server-side analytics by URL?</h3>
<p>Web Analytics only displays client-side analytics. All Cloudflare customers who proxy their traffic also get analytics based on traffic at their edge.</p>
<p>Currently, users on Pro, Business, and Enterprise plans get advanced HTTP traffic analytics, which is the only way to see features like a breakdown of traffic by URL based on server-side analytics.</p>
<h3 id="what-is-the-period-of-time-i-can-access-data-in-web-analytics">What is the period of time I can access data in Web Analytics?</h3>
<p>Currently, you can access data for the previous six months.</p>
<h3 id="does-cloudflare-web-analytics-support-utm-parameters">Does Cloudflare Web Analytics support UTM parameters?</h3>
<p>Not yet. UTM parameters are special query string parameters that can help track where traffic is coming from.
Currently, Cloudflare Web Analytics do not log query strings to avoid collecting potentially sensitive data, but we may add support for this in the future.</p>
<h3 id="does-web-analytics-support-custom-events">Does Web Analytics support custom events?</h3>
<p>Not yet, but we may add support for this in the future.</p>
<h3 id="can-i-track-more-than-one-website-with-web-analytics">Can I track more than one website with Web Analytics?</h3>
<p>Yes. Right now there is a soft limit of ten sites per account, but that can be adjusted by contacting Cloudflare support.</p>
<h3 id="when-does-the-beacon-send-metrics-to-the-cdn-cgi-rum-endpoint">When does the beacon send metrics to the <code>/cdn-cgi/rum/</code> endpoint?</h3>
<p>For traditional websites, not Single Page Applications (SPAs), the Web Analytics beacon reports to the <code>/cdn-cgi/rum/</code> endpoint when the page has finished loading (load event) and when the user leaves the page. For Single Page Applications, additional metrics are sent for every route change to capture the page load event.</p>
