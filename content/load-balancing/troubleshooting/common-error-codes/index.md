---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/
  description: Common Load Balancing error codes and resolutions.
  full_title: Common error codes · Cloudflare Load Balancing docs
  head_html: <title>Common error codes · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Common Load Balancing error codes and resolutions."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/index.md"><meta property="og:title" content="Common error codes · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Common Load Balancing error codes and resolutions."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/#page","headline":"Common error codes \u00b7 Cloudflare Load Balancing docs","description":"Common Load Balancing error codes and resolutions.","url":"https://developers.cloudflare.com/load-balancing/troubleshooting/common-error-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/troubleshooting/common-error-codes/
  schema: 1
---
<p>The Cloudflare Load Balancing API adds global health to each pool and endpoint. It also gives you a view into what our network sees at a wider level. Cloudflare uses a quorum system to determine pool and endpoint health status. The quorum is taken from PoPs responsible for running health monitor requests in a region, and the majority result is used.</p>
<p>When troubleshooting failures, use the Cloudflare API for programmatic access to Cloudflare Load Balancing. The Health Monitor Events and Load Balancer Monitors routes are excellent tools for accessing load balancing event logs and reconfiguring Cloudflare monitors.</p>
<p>You can get a per-data center breakdown of the health of your endpoints from the Cloudflare API from the List Health Monitor Events command:</p>
<pre tabindex="0"><code class="language-txt">GET user/load_balancing_analytics/events&#10;</code></pre>
<p>If a health monitor request fails, the breakdown will include the reason.</p>
<p>Common troubleshooting causes and solutions are listed below.</p>
<hr />
<h2 id="tcp-connection-failed">TCP connection failed</h2>
<h3 id="cause">Cause</h3>
<p>Our health monitor requests failed to establish a TCP connection to your endpoint.</p>
<h3 id="solution">Solution</h3>
<p>This typically occurs when there is a network failure between Cloudflare and your endpoint, and/or a firewall refused to allow our connection. Ensure your network and firewall configurations are not interfering with load balancing traffic.</p>
<hr />
<h2 id="http-timeout-occurred">HTTP timeout occurred</h2>
<h3 id="cause-1">Cause</h3>
<p>The endpoint failed to return an HTTP response within the timeout configured. This happens if you have the timeout set to a low number — 1 or 2 seconds, for instance.</p>
<h3 id="solution-1">Solution</h3>
<p>We recommend increasing the HTTP response timeout to allow the endpoint to respond.</p>
<hr />
<h2 id="response-code-mismatch-error">Response code mismatch error</h2>
<h3 id="cause-2">Cause</h3>
<p>Cloudflare receives an HTTP status code that does not match the values defined in the <code>expected_codes</code> property of your Cloudflare monitor configuration.</p>
<h3 id="solution-2">Solution</h3>
<p>Response codes must match the <code>expected_codes</code>. Use the List Monitors API command to confirm the values are correct.</p>
<h3 id="alternate-cause">Alternate cause</h3>
<p>You may also see this issue if you have a monitor configured to use HTTP connections and your endpoint is redirecting to HTTPS. In this case, the response code will often be 301, 302, or 303.</p>
<h3 id="solution-3">Solution</h3>
<p>Either change your Cloudflare monitor configuration to use HTTPS, or set the value of <code>follow_redirect</code> to <code>true</code> so that we can resolve the correct status code.</p>
<hr />
<h2 id="response-body-mismatch-error">Response body mismatch error</h2>
<h3 id="cause-3">Cause</h3>
<p>The response body returns from your endpoint and does not include the (case-insensitive) value of <code>expected_body</code> configured in your monitor.</p>
<p>Note that we only read the first 10 KB of the response. If you return a larger response, and the expected_body is not in the first 10 KB, the health monitor request will fail.</p>
<h3 id="solution-4">Solution</h3>
<p>Ensure the expected_body is in the first 10 KB of the response body.</p>
<hr />
<h2 id="tls-untrusted-certificate-error">TLS untrusted certificate error</h2>
<h3 id="cause-4">Cause</h3>
<p>The certificate is not trusted by a public Certificate Authority (CA).</p>
<h3 id="solution-5">Solution</h3>
<p>If you're using a self-signed certificate, we recommend either using a publicly trusted certificate or setting the <code>allow_insecure</code> property on your monitor to <code>true</code>.</p>
<hr />
<h2 id="tls-name-mismatch-error">TLS name mismatch error</h2>
<h3 id="cause-5">Cause</h3>
<p>Our health monitor (client) was not able to match a name on the server certificate to the hostname of the request.</p>
<h3 id="solution-6">Solution</h3>
<p>Use the List Monitors command to confirm that the <code>header</code> value set in the Cloudflare monitor is correct and the Update Monitors command to make any necessary changes.</p>
<hr />
<h2 id="tls-protocol-error">TLS protocol error</h2>
<h3 id="cause-6">Cause</h3>
<p>This error can occur if you’re using an older version of TLS or your endpoint is not configured for HTTPS.</p>
<h3 id="solution-7">Solution</h3>
<p>Ensure that your endpoint supports TLS 1.0 or greater and is configured for HTTPS.</p>
<hr />
<h2 id="tls-unrecognized-name-error">TLS unrecognized name error</h2>
<h3 id="cause-7">Cause</h3>
<p>The server did not recognize the name provided by the client. When a host header is set, we set this as the ServerName in the initial TLS handshake. If not set, we will not provide a ServerName, which can cause this error.</p>
<h3 id="solution-8">Solution</h3>
<p>Set the host header in your monitor object.</p>
<hr />
<h2 id="no-route-to-host-error">No route to host error</h2>
<h3 id="cause-8">Cause</h3>
<p>The IP address cannot be reached from our network. Common causes are ISP or hosting provider network issues (e.g. BGP level), or that the IP does not exist.</p>
<h3 id="solution-9">Solution</h3>
<p>Make sure IP is accurate, and if it is check if there is an ISP or hosting provider network issue.</p>
<hr />
<h2 id="exceeded-quota-error">Exceeded quota error</h2>
<h3 id="cause-9">Cause</h3>
<p>You will receive this error if you attempt to create more objects (monitors, pools, or endpoints) than are included in your plan.</p>
<p>If using the dashboard, you will not be able to create additional objects.</p>
<p>If you're using the <strong>Cloudflare API</strong>, you will receive an error message.</p>
<h3 id="solution-10">Solution</h3>
<ul>
<li>Enterprise customers who need to create more objects (load balancers, pools, endpoints, or monitors) should reach out to their account team to discuss this issue.</li>
<li>Self-service customers can upgrade their Load Balancing subscription with more endpoints to increase load balancing capacity.</li>
</ul>
<hr />
<h2 id="tcp-timeout">TCP Timeout</h2>
<h3 id="cause-10">Cause</h3>
<p>Data transmission was not acknowledged and retransmit of data did not succeed.</p>
<h3 id="solution-11">Solution</h3>
<p>Confirm whether the SYN-ACK for the handshake takes place at your endpoint and <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a>.</p>
<hr />
<h2 id="tls-handshake-failure">TLS Handshake Failure</h2>
<h3 id="cause-11">Cause</h3>
<p>Indicates that the browser's connection to the web server is not secure.</p>
<h3 id="solution-12">Solution</h3>
<p>Change wifi networks, connect to a wired network, or verify the network connection is stable.</p>
<hr />
<h2 id="network-unreachable">Network Unreachable</h2>
<h3 id="cause-12">Cause</h3>
<p>Cloudflare cannot connect to the endpoint due to network unavailability. This is usually caused by a network issue or incorrect IP.</p>
<h3 id="solution-13">Solution</h3>
<p>Check either the IP entered for the endpoint in Cloudflare's Load Balancer configuration or the IP returned via DNS for the endpoint hostname.</p>
<hr />
<h2 id="http-invalid-response">HTTP Invalid Response</h2>
<h3 id="cause-13">Cause</h3>
<p>Usually caused by an HTTP 502 error or bad gateway.</p>
<h3 id="solution-14">Solution</h3>
<p>Ensure the endpoint responds to requests and that no applications have crashed or are under high load.</p>
<hr />
<h2 id="dns-unknown-host">DNS Unknown Host</h2>
<h3 id="cause-14">Cause</h3>
<p>The endpoint hostname does not exist.</p>
<h3 id="solution-15">Solution</h3>
<p>Confirm the endpoint resolves to an IP address.</p>
<hr />
<h2 id="connection-reset-by-peer">Connection Reset by Peer</h2>
<h3 id="cause-15">Cause</h3>
<p>A network error occurred while the client received data from the endpoint.</p>
<h3 id="solution-16">Solution</h3>
<p>Confirm whether the endpoint is experiencing a high amount of traffic or an error.</p>
<hr />
<h2 id="monitor-config-error">Monitor Config Error</h2>
<h3 id="cause-16">Cause</h3>
<p>There was a configuration error in the monitor and no checks are run against the pool endpoints.</p>
<h3 id="solution-17">Solution</h3>
<p>Review your monitor configuration to ensure it matches an expected request to your endpoint.</p>
<hr />
<h2 id="dns-internal">DNS Internal</h2>
<h3 id="cause-17">Cause</h3>
<p>The endpoint's hostname resolves to an internal or orange-clouded IP address. No checks are run against the pool endpoints.</p>
<h3 id="solution-18">Solution</h3>
<p>Cloudflare does not allow use of an endpoint hostname that is proxied by Cloudflare.</p>
<hr />
<h2 id="load-balancing-not-enabled">Load Balancing Not Enabled</h2>
<h3 id="cause-18">Cause</h3>
<p>Load Balancing is not enabled for your account or zone.</p>
<h3 id="solution-19">Solution</h3>
<p>For Enterprise customers, reach out to your Cloudflare Account Team. Free, Pro, and Business customers should <a href="/load-balancing/get-started/enable-load-balancing/">Enable Load Balancing</a>.</p>
<hr />
<h2 id="validation-failed-error">Validation failed error</h2>
<h3 id="cause-19">Cause</h3>
<p>You will receive an error if you try to set the host header value while configuring a load balancer endpoint.</p>
<h3 id="solution-20">Solution</h3>
<p>Cloudflare now restricts configured <a href="/load-balancing/additional-options/override-http-host-headers/">endpoint host headers</a> to fully qualified domain names (FQDNs) that are immediate subdomains of a zone associated with the account. For example, this host header would be the same zone as the load balancer itself, but pools may be used across multiple Load balancers.</p>
<hr />
<h2 id="object-referenced-by-other-objects">Object referenced by other objects</h2>
<h3 id="cause-20">Cause</h3>
<p>You will receive this error when you attempt to delete a pool that is referenced by a load balancer <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">geo steering</a> region, or by a <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">pool set</a>.</p>
<h3 id="solution-21">Solution</h3>
<p>For a geo steering reference, remove the pool from the load balancer's geo steering configuration. If your load balancer no longer uses geo steering, you will need to <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">re-enable geo steering</a> and then remove the pool.</p>
<p>For a pool set reference, remove the pool from every pool set that references it, including any <code>overrides.pool_weights</code> and <code>overrides.fallback_pool</code> entries.</p>
<hr />
<h2 id="other-failure">Other Failure</h2>
<h3 id="cause-21">Cause</h3>
<p>If the failure cannot be classified as any other type of failure mentioned above.</p>
<h3 id="solution-22">Solution</h3>
<p><a href="/support/contacting-cloudflare-support/">Contact Cloudflare Support</a>.</p>
