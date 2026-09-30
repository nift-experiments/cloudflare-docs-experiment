<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you start creating custom hostnames:</p>
<ol>
<li><a href="/fundamentals/manage-domains/add-site/">Add</a> your zone to Cloudflare on a Free plan.</li>
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
<h3 id="1-create-fallback-origin"><ol>
<li>Create fallback origin</li>
</ol></h3>
<p>The fallback origin is where Cloudflare will route traffic sent to your custom hostnames (must be proxied).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4079.md")
</aside>
<p>To create your fallback origin:</p>
<ol>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create</a> a proxied <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> record pointing to the IP address of your fallback origin (where Cloudflare will send custom hostname traffic).</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/4080.md")
</div>
<ol start="2">
<li>Designate that record as your fallback origin.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4083.md")
</div></div>
<ol start="3">
<li>Once you have added the fallback origin, confirm that its status is <strong>Active</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4078.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4077.md")
</aside>
<h3 id="2-optional-create-cname-target"><ol start="2">
<li>(Optional) Create CNAME target</li>
</ol></h3>
<p>The CNAME target — optional, but highly encouraged — provides a friendly and more flexible place for customers to <a href="#3-have-customer-create-cname-record">route their traffic</a>. You may want to use a subdomain such as <code>customers.&lt;SAAS_PROVIDER&gt;.com</code>.</p>
<p><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create</a> a proxied CNAME that points your CNAME target to your fallback origin (can be a wildcard such as <code>*.customers.saasprovider.com</code>).</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/4084.md")
</div>
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
@markup("md", "content/.markup/bodies/4076.md")
</aside>
<h3 id="2-create-custom-hostname"><ol start="2">
<li>Create custom hostname</li>
</ol></h3>
<p>After planning for certification and hostname validation, you can create the custom hostname.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="zone-name-restriction">Zone name restriction</h3>
@markup("md", "content/.markup/bodies/4075.md")
</aside>
<p>To create a custom hostname:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4087.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4072.md")
</aside>
<h3 id="check-when-a-custom-hostname-is-ready">Check when a custom hostname is ready</h3>
<p>A custom hostname uses separate validation flows for hostname activation and certificate issuance.</p>
<table>
<thead>
<tr>
<th>API field</th>
<th>What it means</th>
<th>Ready value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>result.status</code></td>
<td>Cloudflare has validated the hostname and can proxy traffic for it.</td>
<td><code>active</code></td>
</tr>
<tr>
<td><code>result.ssl.status</code></td>
<td>Cloudflare has issued and deployed the certificate for the hostname.</td>
<td><code>active</code></td>
</tr>
</tbody>
</table>
<p>Treat a custom hostname as ready for production traffic when:</p>
<ul>
<li><code>result.status</code> is <code>active</code>.</li>
<li><code>result.ssl.status</code> is <code>active</code>.</li>
<li>The hostname's DNS record points to your SaaS target.</li>
</ul>
<p>A successful TLS handshake can happen before <code>result.ssl.status</code> changes to <code>active</code> if Cloudflare can present another matching certificate. Use the <a href="/api/resources/custom_hostnames/methods/get/">Custom hostname details endpoint</a> as the source of truth for onboarding state. For more information, refer to <a href="/ssl/reference/certificate-and-hostname-priority/">Certificate and hostname priority</a>.</p>
<h3 id="3-have-customer-create-cname-record"><ol start="3">
<li>Have customer create CNAME record</li>
</ol></h3>
<p>To finish the custom hostname setup, your customer needs to set up a CNAME record at their authoritative DNS that points to your <a href="#2-optional-create-cname-target">CNAME target</a> <sup><a href="#footnote-1">1</a></sup>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4071.md")
</aside>
<p>Your customer's CNAME record might look like the following:</p>
<pre><code class="language-txt">mystore.example.com CNAME customers.saasprovider.com&#10;</code></pre>
<p>This record would route traffic in the following way:</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: How traffic routing works with a CNAME target&#10;A[Request to &lt;code&gt;mystore.example.com&lt;/code&gt;] --&gt; B[&lt;code&gt;customers.saasprovider.com&lt;/code&gt;]&#10;B --&gt; C[&lt;code&gt;proxy-fallback.saasprovider.com&lt;/code&gt;]&#10;</code></pre>
<br />
<p>Requests to <code>mystore.example.com</code> would go to your CNAME target (<code>customers.saasprovider.com</code>), which would then route to your fallback origin (<code>proxy-fallback.saasprovider.com</code>).</p>
<p>If you have <a href="/data-localization/regional-services/">regional services</a> set up for your custom hostnames, Cloudflare always uses the processing region associated with your DNS target record (instead of the processing region of any <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">custom origins</a>).</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4070.md")
</aside>
<h4 id="service-continuation">Service continuation</h4>
<p>If your customer is also using Cloudflare for their domain, they should keep their DNS record pointing to your SaaS provider in place for as long as they want to use your service.</p>
<p>For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/">Remove custom hostnames</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1"></li></ol></section>
