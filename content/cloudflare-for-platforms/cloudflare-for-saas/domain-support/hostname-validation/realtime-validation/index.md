<p>When you use a real-time validation method, Cloudflare verifies your customer's hostname when your customers adds their <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record">DNS routing record</a> to their authoritative DNS.</p>
<h2 id="use-when">Use when</h2>
<p>Real-time validation methods put less burden on your customers because it does not require any additional actions.</p>
<p>However, it may cause some downtime since Cloudflare takes a few seconds to iterate over DNS records. This downtime also can increase - due to the increasing <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/">validation backoff schedule</a> - if your customer takes additional time to add their DNS routing record.</p>
<p>To minimize this downtime, you can continually send no-change <a href="/api/resources/custom_hostnames/methods/edit/"><code>PATCH</code> requests</a> for the specific custom hostname until it validates (which resets the validation backoff schedule).</p>
<p>To avoid any chance of downtime, use a <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/">pre-validation method</a></p>
<h2 id="how-to">How to</h2>
<p>Real-time validation occurs automatically when your customer adds their <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record">DNS routing record</a>.</p>
<p>The exact record depends on your Cloudflare for SaaS setup.</p>
<h3 id="normal-setup-cname-target">Normal setup (CNAME target)</h3>
<p>Most customers will have a <code>CNAME</code> target, which requires their customers to create a <code>CNAME</code> record similar to:</p>
<pre><code class="language-txt">mystore.com CNAME customers.saasprovider.com&#10;</code></pre>
<h3 id="apex-proxying">Apex proxying</h3>
<p>With <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying</a>, SaaS customers need to create an <code>A</code> record for their hostname that points to the IP prefix allocated to the SaaS provider's account.</p>
<pre><code class="language-txt">example.com.  60  IN  A   192.0.2.1&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4114.md")
</aside>
