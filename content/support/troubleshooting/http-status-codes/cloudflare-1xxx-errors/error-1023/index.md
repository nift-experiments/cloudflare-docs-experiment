<h2 id="error-1023-could-not-find-host">Error 1023: Could not find host</h2>
<p>This error indicates that the host could not be found due to a configuration issue or propagation delay.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>If the owner just signed up for Cloudflare it can take a few minutes for the website's information to be distributed to our global network. Something is wrong with the site's configuration.</li>
<li>Usually, this happens when accounts have been signed up with a partner organization (for example, hosting provider) and the provider's DNS fails.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14733.md")
</aside>
<h3 id="resolution">Resolution</h3>
<p>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> with the following details:</p>
<ul>
<li>Your domain name.</li>
<li>A screenshot of the <code>1023</code> error including the <a href="/fundamentals/reference/cloudflare-ray-id/"><strong>Ray ID</strong></a> mentioned in the error message.</li>
<li>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">HAR file</a> captured while duplicating the error.</li>
</ul>
