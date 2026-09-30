<p>A Certificate Authority Authorization (CAA) DNS record specifies which certificate authorities (CAs) are allowed to issue certificates for a domain. This record reduces the chance of unauthorized certificate issuance and promotes standardization across your organization.
<br /></p>
<p>For additional security, set up <a href="/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">Certificate Transparency Monitoring</a> as well.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/14008.md")
</aside>
<h2 id="who-should-create-caa-records">Who should create CAA records?</h2>
<p>You should <a href="#create-caa-records">create CAA records</a> in Cloudflare if each of the following is true:</p>
<ul>
<li>You uploaded your own custom origin server certificate (not provisioned by Cloudflare).</li>
<li>That certificate was issued by a CA (not self-signed).</li>
<li>Your domain is on a <a href="/dns/zone-setups/full-setup/">full setup</a> (not a <a href="/dns/zone-setups/partial-setup">CNAME setup</a>).</li>
<li>When adding new <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Custom Hostname</a> and your customer has existing CAA records. In this case, ask your customer to remove the existing CAA records or add the missing CAA record.</li>
</ul>
<h2 id="caa-records-added-by-cloudflare">CAA records added by Cloudflare</h2>
<p>Cloudflare adds CAA records automatically when you have <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> and add any CAA records to your zone. These records make sure Cloudflare can still issue Universal certificates on your behalf.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14007.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="subdomain-zones-caveat">Subdomain zones caveat</h3>
@markup("md", "content/.markup/bodies/14006.md")
</aside>
<p>If Cloudflare has automatically added CAA records on your behalf, these records will not appear in the Cloudflare dashboard. However, if you run a command line query using <code>dig</code>, you can see any existing CAA records, including those added by Cloudflare (replacing <code>example.com</code> with your own domain on Cloudflare):</p>
<pre><code class="language-bash">➜  ~ dig example.com caa +short&#10;&#10;&#35; CAA records added by Google Trust Services&#10;0 issue &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;0 issuewild &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;&#10;&#35; CAA records added by Let&#x27;s Encrypt&#10;0 issue &quot;letsencrypt.org&quot;&#10;0 issuewild &quot;letsencrypt.org&quot;&#10;&#10;&#35; CAA records added by SSL.com&#10;0 issue &quot;ssl.com&quot;&#10;0 issuewild &quot;ssl.com&quot;&#10;&#10;&#35; CAA records added by Sectigo&#10;0 issue &quot;sectigo.com&quot;&#10;0 issuewild &quot;sectigo.com&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14005.md")
</aside>
<h2 id="create-caa-records">Create CAA records</h2>
<p>Create a CAA record for each Certificate Authority (CA) that you plan to use for your domain.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14011.md")
</div></div>
<p>Once you have finished creating all the records, you can review them in the list of records appearing under the DNS Records panel.</p>
<h2 id="certificate-authorities-and-required-caa-values">Certificate authorities and required CAA values</h2>
<p>If you have CAA records on your domain, they must permit the certificate authority (CA) that Cloudflare uses. For the required CAA values for each CA Cloudflare may use, refer to <a href="/ssl/reference/certificate-authorities/#caa-records">Certificate authorities</a>.</p>
<h3 id="cname-chain-caa-records">CNAME chain CAA records</h3>
<p>CAA records on a CNAME target also apply. If your hostname CNAMEs to a domain whose zone has restrictive CAA records, those records take precedence — even if your own domain has no CAA records.</p>
<p>Check CAA at all levels of your CNAME chain:</p>
<pre><code class="language-sh">dig yourdomain.com CAA +short&#10;dig cname-target.com CAA +short&#10;</code></pre>
