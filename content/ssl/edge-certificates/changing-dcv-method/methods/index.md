<p>Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).</p>
<h2 id="perform-dcv">Perform DCV</h2>
<p>For details on each method available for DCV, refer to the following resources:</p>
<ul class="directory-listing"><li><a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated</a></li><li><a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT</a></li><li><a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP</a></li></ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14189.md")
</aside>
<hr />
<h2 id="verify-dcv-status">Verify DCV status</h2>
<p>To verify the <a href="/ssl/reference/certificate-statuses/">DCV status</a> of a certificate, either monitor the certificate's status on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page or use the <a href="/api/resources/ssl/subresources/verification/methods/get/">Verification Status endpoint</a>.</p>
<p>A status of <code>active</code> means that the certificate has been deployed to Cloudflare’s global network and will be served as soon as HTTP traffic is proxied to Cloudflare.</p>
<h2 id="update-dcv-methods">Update DCV methods</h2>
<p>You cannot update the DCV method for an active certificate. To update the DCV method for a subdomain, wait until the DCV expires and then change the DCV method.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Meaning that Cloudflare is your Authoritative DNS provider.</li>
<li id="footnote-2">Meaning that another DNS provider - not Cloudflare - maintains your Authoritative DNS.</li></ol></section>
