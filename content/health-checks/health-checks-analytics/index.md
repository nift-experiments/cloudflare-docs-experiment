---
cp9:
  canonical: https://developers.cloudflare.com/health-checks/health-checks-analytics/
  description: View Health Checks status history and response time analytics.
  full_title: Health Checks Analytics · Cloudflare Health Checks docs
  head_html: <title>Health Checks Analytics · Cloudflare Health Checks docs</title><meta name="generator" content="Nift"><meta name="description" content="View Health Checks status history and response time analytics."><link rel="canonical" href="https://developers.cloudflare.com/health-checks/health-checks-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/health-checks/health-checks-analytics/index.md"><meta property="og:title" content="Health Checks Analytics · Cloudflare Health Checks docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View Health Checks status history and response time analytics."><meta property="og:url" content="https://developers.cloudflare.com/health-checks/health-checks-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Health Checks"><meta name="algolia_product_filter" content="Health Checks"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Health Checks"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/health-checks/health-checks-analytics/#page","headline":"Health Checks Analytics \u00b7 Cloudflare Health Checks docs","description":"View Health Checks status history and response time analytics.","url":"https://developers.cloudflare.com/health-checks/health-checks-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /health-checks/health-checks-analytics/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/993.md")
</aside>
<p>Once you have set up a standalone Health Check including notification emails, use Health Check Analytics to debug possible origin issues.</p>
<p>To access health check analytics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Health Check Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<p>You can evaluate origin uptime, latency, failure reason, and specific event logs:</p>
<ul>
<li><strong>Health Checks By Uptime</strong>: Shows the percentage of uptime for individual origins over time.</li>
<li><strong>Health Checks By Failure Reason</strong>: Shows a breakdown of failures by the specific reason. Refer to <a href="#common-error-codes">common error code causes and solutions below</a>.</li>
<li><strong>Health Checks By Latency</strong>: Shows average latency – measured in round trip time — for individual origins over time.</li>
<li><strong>Event Log</strong>: Shows individual health check data.
<ul>
<li>Select each record for additional details on <strong>Round trip time</strong>, the <strong>Failure Reason</strong>, the <strong>Average Waterfall</strong> (showing chronological data about request stages), <strong>Response status code</strong>, and more.</li>
<li>Note that <strong>Global</strong> is not a configured region; it represents the aggregated data from all enabled regions.</li>
</ul>
</li>
</ul>
<h2 id="common-error-codes">Common error codes</h2>
<h3 id="tcp-connection-failed">TCP connection failed</h3>
<h4 id="cause">Cause</h4>
<p>Health Checks failed to establish a TCP connection to your origin server.</p>
<h4 id="solution">Solution</h4>
<p>This typically occurs when there is a network failure between Cloudflare and your origin, and/or a firewall refuses to allow our connection. Ensure your network and firewall configurations are not interfering with traffic.</p>
<h3 id="http-timeout-occurred">HTTP timeout occurred</h3>
<h4 id="cause-1">Cause</h4>
<p>The origin failed to return an HTTP response within the timeout configured. This happens if you have the timeout set to a low number. For example, one to two seconds.</p>
<h4 id="solution-1">Solution</h4>
<p>Cloudflare recommends increasing the HTTP response timeout to allow the origin server to respond.</p>
<h3 id="response-code-mismatch-error">Response code mismatch error</h3>
<h4 id="cause-2">Cause</h4>
<p>Cloudflare receives an HTTP status code that does not match the values defined in the <code>expected_codes</code> property of your Health Check configuration.</p>
<h4 id="solution-2">Solution</h4>
<p>Response codes must match the <code>expected_codes</code>. Confirm the values are correct by comparing the expected response codes and the status code received in the Event Log.</p>
<h4 id="alternate-cause">​​Alternate cause</h4>
<p>You may also see this issue if you have a Health Check configured to use HTTP connections and your origin server is redirecting to HTTPS. In this case, the response code will often be <code>301</code>, <code>302</code>, or <code>303</code>.</p>
<h4 id="solution-3">Solution</h4>
<p>Change your Cloudflare Health Check configuration to use HTTPS or set the value of <code>follow_redirect</code> to <code>true</code> so that Cloudflare can resolve the correct status code.</p>
<h3 id="response-body-mismatch-error">Response body mismatch error</h3>
<h4 id="cause-3">Cause</h4>
<p>The response body returns from your origin server and does not include the (case-insensitive) value of <code>expected_body</code> configured in your Health Check.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/992.md")
</aside>
<h4 id="solution-4">Solution</h4>
<p>Ensure the <code>expected_body</code> is in the first 10 KB of the response body.
​​</p>
<h3 id="tls-untrusted-certificate-error">TLS untrusted certificate error</h3>
<h4 id="cause-4">Cause</h4>
<p>The certificate is not trusted by a public Certificate Authority (CA).</p>
<h4 id="solution-5">Solution</h4>
<p>If you’re using a self-signed certificate, Cloudflare recommends either using a publicly trusted certificate or setting the <code>allow_insecure</code> property on your Health Check to <code>true</code>.</p>
<h3 id="tls-name-mismatch-error">TLS name mismatch error</h3>
<h4 id="cause-5">Cause</h4>
<p>Our Health Check (client) was not able to match a name on the server certificate to the hostname of the request.</p>
<h4 id="solution-6">Solution</h4>
<p>Inspect your Health Check configuration to confirm that the <code>header</code> value set in the Cloudflare Health Check is correct.</p>
<h3 id="tls-protocol-error">TLS protocol error</h3>
<h4 id="cause-6">Cause</h4>
<p>This error can occur if you are using an older version of TLS or your origin server is not configured for HTTPS.</p>
<h4 id="solution-7">Solution</h4>
<p>Ensure that your origin server supports TLS 1.2 or greater and is configured for HTTPS.</p>
<h3 id="tls-unrecognized-name-error">TLS unrecognized name error</h3>
<h4 id="cause-7">Cause</h4>
<p>The server did not recognize the name provided by the client. When a host header is set, this is set as the ServerName in the initial TLS handshake. If it is not set, Cloudflare will not provide a ServerName, which can cause this error.</p>
<h4 id="solution-8">Solution</h4>
<p>Set the host header in your Health Check object.</p>
<h3 id="no-route-to-host-error">​​No route to host error</h3>
<h4 id="cause-8">Cause</h4>
<p>The IP address cannot be reached from Cloudflare’s network. Common causes are ISP or hosting provider network issues (e.g. BGP level), or that the IP does not exist.</p>
<h4 id="solution-9">Solution</h4>
<p>Ensure IP is accurate, and check if there is an ISP or hosting provider network issue.</p>
<h3 id="tcp-timeout">TCP Timeout</h3>
<h4 id="cause-9">Cause</h4>
<p>Data transmission was not acknowledged and the retransmit of data did not succeed.</p>
<h4 id="solution-10">Solution</h4>
<p>Confirm whether the SYN-ACK for the handshake takes place at your origin and contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a>.</p>
<h3 id="network-unreachable">​​Network Unreachable</h3>
<h4 id="cause-10">Cause</h4>
<p>Cloudflare cannot connect to the origin web server due to network unavailability. This is usually caused by a network issue or incorrect origin IP.</p>
<h4 id="solution-11">Solution</h4>
<p>Check the IP entered for the origin in Cloudflare’s Health Checks configuration or the IP returned via DNS for the origin hostname.</p>
<h3 id="http-invalid-response">HTTP Invalid Response</h3>
<h4 id="cause-11">Cause</h4>
<p>Usually caused by an HTTP 502 error or bad gateway.</p>
<h4 id="solution-12">Solution</h4>
<p>Ensure the origin web server responds to requests and that no applications have crashed or are under high load.</p>
<h3 id="dns-unknown-host">DNS Unknown Host</h3>
<h4 id="cause-12">Cause</h4>
<p>The origin web server hostname does not exist.</p>
<h4 id="solution-13">Solution</h4>
<p>Confirm the origin web server resolves to an IP address.</p>
<h3 id="connection-reset-by-peer">Connection Reset by Peer</h3>
<h4 id="cause-13">Cause</h4>
<p>A network error occurred while the client received data from the origin web server.</p>
<h4 id="solution-14">Solution</h4>
<p>Confirm whether the origin web server is experiencing a high amount of traffic or an error.</p>
<h3 id="monitor-configuration-error">Monitor Configuration Error</h3>
<h4 id="cause-14">Cause</h4>
<p>There was a configuration error in the Health Check and no checks were run against the origin.</p>
<h4 id="solution-15">Solution</h4>
<p>Review your Health Check configuration to ensure it matches an expected request to your origin.</p>
<h3 id="dns-internal">​​DNS Internal</h3>
<h4 id="cause-15">Cause</h4>
<p>The origin web server's hostname resolves to a non-publicly-routable or restricted IP address (for example, a localhost address). No checks are run against this origin.</p>
<h4 id="solution-16">Solution</h4>
<p>Confirm the origin web server hostname resolves to a publicly routable IP address. Note that if the hostname resolves to a public Cloudflare anycast IP (because the hostname is proxied through Cloudflare), the health check will run but will probe Cloudflare's edge rather than your actual origin server. To monitor your origin server directly, configure the health check to use the origin IP address or a non-proxied hostname.</p>
<h3 id="other-failure">Other Failure</h3>
<h4 id="cause-16">Cause</h4>
<p>If the failure cannot be classified as any other type of failure mentioned above.</p>
<h4 id="solution-17">Solution</h4>
<p>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a>.</p>
<h2 id="set-up-alerts">Set up alerts</h2>
<p>You can configure alerts to notify you of any changes in your health check status.</p>
<details><summary>Health Checks status notification</summary><strong>Who is it for?</strong><p>Customers who want to be warned about changes to server health as determined by <a href="/health-checks/">health checks</a>.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search for and add health checks from your list of health checks.</li>
<li>You can choose a trigger to fire the notification when your server becomes <strong>unhealthy</strong>, <strong>healthy</strong>, or <strong>either healthy or unhealthy</strong>.</li>
</ul>
<strong>Included with</strong><p>Professional plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Review your <a href="/health-checks/health-checks-analytics/#common-error-codes">health check analytics</a>.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
