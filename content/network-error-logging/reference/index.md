<p>If a user is able to connect to Cloudflare and the site they connect to has NEL enabled, Cloudflare passes back two headers to the browser indicating that they should report any network failures to an endpoint specified in the headers. The browser will operate as usual, and if something happens that prevents the browser from connecting to the site, the browser will log the failure as a report and send it to the endpoint.</p>
<p>Network Error Logging failures can occur for different reasons which are outlined below.</p>
<h2 id="internet-service-provider-isp-outage">Internet Service Provider (ISP) outage</h2>
<p>An ISP outage appears to NEL users as failures from one particular last-mile network. By examining NEL data to look at the client autonomous system number (ASN) view, you can see which networks are causing the most impact.</p>
<p>For customers, this scenario appears as an influx of <code>tcp.timed_out errors</code>, as well as <code>tcp.failed</code>, <code>h2.protocol_error</code> and <code>h3.protocol_error</code>.</p>
<p>In the event of a last-mile outage, the best course of action is to contact the provider to investigate.</p>
<h2 id="transit-flap">Transit Flap</h2>
<p>Transit flaps look like momentary outages caused by transits re-establishing BGP sessions.</p>
<p>To customers, this will appear as <code>tcp.timed_out</code> reports from a variety of ASNs over a short period of time. This could happen for several reasons:</p>
<ul>
<li>Maintenance in the transit network necessitated a reset of the session.</li>
<li>Maintenance or reboots in Cloudflare necessitated a reset of the BGP session.</li>
<li>Packet loss in the network caused the session to flap.</li>
</ul>
<p>Heavy packet loss in the network will likely result in a series of flaps over time. Maintenance is typically one impact period that lasts no more than two minutes.</p>
<h2 id="infrastructure-outage">Infrastructure outage</h2>
<p>Infrastructure outages occur at shared peering points, such as Internet exchanges.</p>
<p>These outages appear to customers as an increase in <code>tcp.timed_out</code>, <code>tcp.failed</code>, and <code>tcp.aborted reports</code>. These failures will likely appear across multiple networks for an extended period of time.</p>
<p>Depending on the severity of the report volume, Cloudflare may declare an incident to track remediation. Alternatively, Cloudflare may deactivate peering from these shared points until the issue is resolved.</p>
<h2 id="cloudflare-outage">Cloudflare outage</h2>
<p>Cloudflare outages consist of issues within Cloudflare’s data-center fabric.</p>
<p>These outages appear to customers as an increase in <code>tcp.timed_out</code>, <code>tcp.failed</code>, and <code>tcp.aborted</code> reports and will likely appear across multiple networks for a short period of time.</p>
<p>By pivoting by data center, customers can track the impact across Cloudflare points of presence. Cloudflare-based incidents will always be tracked through a status page, which will indicate whether or not there are issues within the impacted region.</p>
<h2 id="provider-sending-traffic-through-scrubbing-center-blocking-traffic">Provider sending traffic through scrubbing center/blocking traffic</h2>
<p>This type of outage manifests as TLS errors, such as <code>tls.cert.authority_invalid</code>, <code>tls.cert.name_invalid,</code> or others and may also present with <code>tcp.aborted errors</code>.</p>
<p>Customers may uncover this behavior by looking at which last-mile ASNs are displaying increased failures, as it will typically be only one.</p>
<p>Customers can seek remediation by contacting the provider that they believe is scrubbing their traffic.</p>
<h2 id="certificate-issues">Certificate issues</h2>
<p>Certificate issues are also detectable through NEL. The <code>TLS.version</code>, <code>cipher_mismatch</code>, or other errors may present across multiple ISPs in multiple Cloudflare locations.</p>
<p>If this is detected in NEL, the issue can be remediated by deploying new certificates or using <a href="/ssl/edge-certificates/advanced-certificate-manager/">Cloudflare’s SSL management suite</a> to automatically deploy new certificates.</p>
