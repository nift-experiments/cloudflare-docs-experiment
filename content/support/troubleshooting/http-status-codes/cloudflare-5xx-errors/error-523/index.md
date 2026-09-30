<h2 id="error-523-origin-is-unreachable">Error 523: origin is unreachable</h2>
<p>This error occurs when Cloudflare cannot contact your origin web server.</p>
<h3 id="common-causes">Common causes</h3>
<p>This typically occurs when a network device between Cloudflare and the origin web server does not have a route to the origin's IP address.</p>
<p>In AWS environments, a common cause is an overly broad route such as <code>172.0.0.0/8</code> in a VPC route table. Cloudflare uses public IP ranges in <code>172.64.0.0/13</code>, and a broad route can accidentally capture traffic intended for Cloudflare.</p>
<h3 id="resolution">Resolution</h3>
<p>Contact your hosting provider and share the necessary <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">error details</a> to exclude the following common causes at your origin web server:</p>
<ul>
<li>Confirm the correct origin IP address is listed for A or AAAA records within your Cloudflare DNS app.</li>
<li>Troubleshoot Internet routing issues between your origin and Cloudflare, or with the origin itself.</li>
<li>In AWS, review VPC route tables and make sure you are not sending <code>172.64.0.0/13</code> toward a private destination. If required, add a more specific route for <code>172.64.0.0/13</code> to your Internet Gateway.</li>
</ul>
<p>If none of the above leads to a resolution, request the following information from your hosting provider or site administrator:</p>
<ul>
<li>An <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#perform-a-traceroute">MTR or traceroute</a> from your origin web server to a <a href="http://www.cloudflare.com/ips">Cloudflare IP address</a> that most commonly connected to your origin web server before the issue occurred. Identify a connecting Cloudflare IP from the logs of the origin web server.</li>
</ul>
