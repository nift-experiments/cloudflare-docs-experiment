<p>To set up Cloudflare for SaaS for <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying</a> - as opposed to the <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">normal setup</a> - perform the following steps.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you start creating custom hostnames:</p>
<ol>
<li><a href="/fundamentals/manage-domains/add-site/">Add</a> your zone to Cloudflare (this should be within the account associated with your IP prefixes).</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/enable/">Enable</a> Cloudflare for SaaS for your zone.</li>
<li>Review the <a href="/ssl/reference/certificate-and-hostname-priority/#hostname-priority">Hostname prioritization guidelines</a>. Wildcard custom hostnames behave differently than an exact hostname match.</li>
<li>(optional) Review the following documentation:</li>
</ol>
<ul>
<li><a href="/fundamentals/api/">API documentation</a> (if you have not worked with the Cloudflare API before).</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/">Certificate validation</a>.</li>
</ul>
<hr />
<h2 id="initial-setup">Initial setup</h2>
<p>When you first <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/enable/">enable</a> Cloudflare for SaaS, you need to perform a few steps prior to creating any custom hostnames.</p>
<br />
<h3 id="1-get-ip-range"><ol>
<li>Get IP range</li>
</ol></h3>
<p>With apex proxying, you can either <a href="/byoip/">bring your own IP range</a> or use a set of IP addresses provided by Cloudflare.</p>
<p>For more details on this step, reach out to your account team.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4179.md")
</aside>
<h3 id="2-create-fallback-origin"><ol start="2">
<li>Create fallback origin</li>
</ol></h3>
<p>The fallback origin is where Cloudflare will route traffic sent to your custom hostnames (must be proxied).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4178.md")
</aside>
<p>To create your fallback origin:</p>
<ol>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create</a> a proxied <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record pointing to the IP address of your fallback origin (where Cloudflare will send custom hostname traffic).</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/4180.md")
</div>
<ol start="2">
<li>Designate that record as your fallback origin.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4183.md")
</div></div>
<ol start="3">
<li>Once you have added the fallback origin, confirm that its status is <strong>Active</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4177.md")
</aside>
<hr />
<h2 id="per-hostname-setup">Per-hostname setup</h2>
<p>You need to perform the following steps for each custom hostname.</p>
<h3 id="1-plan-for-validation"><ol>
<li>Plan for validation</li>
</ol></h3>
<p>Before you create a hostname, you need to plan for:</p>
<ol>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/">Certificate validation</a>: Upon successful validation, the certificates are deployed to Cloudflare’s global network.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">Hostname validation</a>: Upon successful validation, Cloudflare proxies traffic for this hostname.</li>
</ol>
<p>You must complete both these steps for the hostname to work as expected.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4176.md")
</aside>
<h3 id="2-create-custom-hostname"><ol start="2">
<li>Create custom hostname</li>
</ol></h3>
<p>After planning for certification and hostname validation, you can create the custom hostname.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="zone-name-restriction">Zone name restriction</h3>
@markup("md", "content/.markup/bodies/4175.md")
</aside>
<p>To create a custom hostname:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4186.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4172.md")
</aside>
<h3 id="3-have-customer-create-dns-record"><ol start="3">
<li>Have customer create DNS record</li>
</ol></h3>
<p>To finish the custom hostname setup, your customer can set up either an A or CNAME record at their authoritative DNS provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4171.md")
</aside>
<h4 id="a-record">A record</h4>
<p>If your customer uses an A record at their authoritative DNS provider, they need to point their hostname to the IP prefix allocated for your account. You should also make sure that they point to the specific IPs that you want to use for apex proxying - if you have Static IPs or BYOIP, and your customer points to any of the IPs associated to your account, validation will run.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4170.md")
</aside>
<p>Your customer's A record might look like the following:</p>
<pre><code class="language-txt">example.com.  60  IN  A   192.0.2.1&#10;</code></pre>
<h4 id="cname-record">CNAME record</h4>
<p>If your customer uses a CNAME record at their authoritative DNS, they need to point their hostname to your <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#2-optional-create-cname-target">CNAME target</a> <sup><a href="#footnote-1">1</a></sup>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4169.md")
</aside>
<p>Your customer's CNAME record might look like the following:</p>
<pre><code class="language-txt">mystore.com CNAME customers.saasprovider.com&#10;</code></pre>
<p>If you have <a href="/data-localization/regional-services/">regional services</a> set up for your custom hostnames, Cloudflare always uses the processing region associated with your DNS target record (instead of the processing region of any <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">custom origins</a>).</p>
<h4 id="service-continuation">Service continuation</h4>
<p>If your customer is also using Cloudflare for their domain, they should keep their DNS record pointing to your SaaS provider in place for as long as they want to use your service.</p>
<p>For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/">Remove custom hostnames</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1"></li></ol></section>
