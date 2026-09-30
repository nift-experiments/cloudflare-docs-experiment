<h2 id="error-1018-could-not-find-host">Error 1018: Could not find host</h2>
<p>This error indicates that the host could not be found.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>The Cloudflare domain was recently activated and there is a delay propagating the domain's settings to the Cloudflare edge network.</li>
<li>The Cloudflare domain was created via a Cloudflare partner (for example, a hosting provider) and the provider's DNS failed.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14735.md")
</aside>
<h3 id="resolution">Resolution</h3>
<p>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> with the following details:</p>
<ul>
<li>Your domain name.</li>
<li>A screenshot of the <code>1018</code> error including the <a href="/fundamentals/reference/cloudflare-ray-id/"><strong>Ray ID</strong></a> mentioned in the error message.</li>
<li>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">HAR file</a> captured while duplicating the error.</li>
</ul>
