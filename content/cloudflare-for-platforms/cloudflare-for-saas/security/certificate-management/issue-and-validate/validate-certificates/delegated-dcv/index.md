<p>Delegated DCV allows SaaS providers to delegate the DCV process to Cloudflare.</p>
<p>DCV Delegation requires your customers to place a one-time record at their authoritative DNS that allows Cloudflare to auto-renew all future certificate orders, so that there is no manual intervention from you or your customers at the time of the renewal.</p>
<hr />
<h2 id="setup">Setup</h2>
<p>To set up Delegated DCV:</p>
<ol>
<li>Add a <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/">custom hostname</a> for your zone, choosing <code>TXT</code> as the <strong>Certificate validation method</strong>.</li>
<li>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames"><strong>Custom Hostnames</strong></a> page, go to <strong>DCV Delegation for Custom Hostnames</strong>.</li>
<li>Copy the hostname value.</li>
<li>For each hostname, the domain owner needs to place a <code>CNAME</code> record at their authoritative DNS. In this example, the SaaS zone is <code>example.com</code>.</li>
</ol>
<pre><code class="language-txt">_acme-challenge.example.com CNAME example.com.&lt;COPIED_HOSTNAME&gt;.&#10;</code></pre>
<p>Once this is complete, Cloudflare will place two TXT DCV records - one for <code>example.com</code> and one for <code>*.example.com</code> - at the <code>example.com.&lt;COPIED_HOSTNAME&gt;</code> hostname. The CNAME record will need to stay in place in order to allow Cloudflare to continue placing the records for the renewals.</p>
<p>If desired, you could also manually fetch the DCV tokens and share them with your customers.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="remove-conflicting-acme-challenge-txt-records">Remove conflicting `_acme-challenge` TXT records</h3>
@markup("md", "content/.markup/bodies/4161.md")
</aside>
<h2 id="moved-domains">Moved domains</h2>
<p>If you <a href="/fundamentals/manage-domains/move-domain/">move your SaaS zone to another account</a>, you will need to update the <code>CNAME</code> record with a new hostname value.</p>
