<p>After you onboard your domain, Cloudflare will act as the <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">reverse proxy</a> and <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-dns-provider">DNS provider</a> for your site.</p>
<p>This guide applies to existing domains that were purchased from another provider, and will use a <a href="/dns/zone-setups/full-setup">full DNS setup</a>, which is the most common configuration. To set this up, you will have to complete a few steps at Cloudflare, but also update some settings at your domain registrar<sup><a href="#footnote-1">1</a></sup>, and at your previous DNS provider (if you were using one).</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="cloudflare-registrar">Cloudflare Registrar</h3>
@markup("md", "content/.markup/bodies/8914.md")
</aside>
<h2 id="1-add-your-domain"><ol>
<li>Add your domain</li>
</ol></h2>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Onboard a domain</strong>.</li>
<li>Enter your website's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/8915.md")
</div> (for example, `example.com`), choose how you would like to add your DNS records, and select **Continue**.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8913.md")
</aside>
<ol start="4">
<li>Select a <a href="https://www.cloudflare.com/plans/#compare-features">plan</a>.</li>
</ol>
<h2 id="2-review-dns-records"><ol start="2">
<li>Review DNS records</li>
</ol></h2>
<p>Your DNS records must be accurate for your domain to work properly. If you don't know what DNS records are, consider the video below for a quick explanation.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/07e42365d5c40f2a46a6bde2844f370f/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F7e8cdb06-7280-4139-8f13-256e03027f00%2Fpublic" title="Review your DNS records" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<ol>
<li></li>
</ol>
<p>Since the quick scan is not guaranteed to find all existing DNS records, you need to review your records, paying special attention to the following:</p>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-zone-apex/">Zone apex records (<code>example.com</code>)</a></p>
  <details class="nb-details"><summary>More about zone apex records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/8916.md")
</div></details>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-subdomain/">Subdomain records (<code>www.example.com</code> or <code>blog.example.com</code>)</a></p>
<details class="nb-details"><summary>More about subdomain records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/8917.md")
</div></details>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/email-records/">Email records</a></p>
<details class="nb-details"><summary>More about email records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/8918.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8912.md")
</aside>
<ol start="2">
<li>If you find any missing records, <a href="/dns/manage-dns-records/how-to/create-dns-records/">manually add</a> those records.</li>
<li>Depending on your site setup, you may want to adjust the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/8919.md")
</div> for certain `A`, `AAAA`, or `CNAME` records. Each record has a proxy status toggle:
   - **Proxied** (orange cloud): web traffic goes through the Cloudflare network, which provides caching, DDoS protection, and other security features.
   - **DNS only** (gray cloud): Cloudflare returns the DNS record value but does not proxy traffic. Use this for CNAME records that verify your domain for third-party services.
<ol start="4">
<li>Select <strong>Continue</strong>.</li>
</ol>
<h2 id="3-update-nameservers"><ol start="3">
<li>Update nameservers</li>
</ol></h2>
<p>Your domain will be assigned two authoritative Cloudflare nameservers. Nameservers are specialized servers that store your domain's DNS records and &quot;answer&quot; requests from browsers by providing the specific IP address needed to connect to your website.</p>
<p>Usually, you need to add these nameservers at your registrar. Refer to <a href="/dns/nameservers/update-nameservers/">Update nameservers</a> for more information.</p>
<details class="nb-details" open><summary>Provider-specific instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8920.md")
</div></details>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="dnssec">DNSSEC</h3>
@markup("md", "content/.markup/bodies/8911.md")
</aside>
<h2 id="4-complete-ssl-tls-setup"><ol start="4">
<li>Complete SSL/TLS setup</li>
</ol></h2>
<p>To prevent insecure connections and visitor browser errors, review your <a href="/ssl/get-started/">SSL/TLS certificates</a>. Many Cloudflare services will automatically protect and speed up your web traffic after your nameservers are updated and your DNS records are proxied. For further guidance, refer to <a href="/dns/proxy-status/">Proxy status</a>.</p>
<p>If you encounter unexpected results when changing your nameservers, refer to the <a href="/dns/zone-setups/full-setup/troubleshooting/">DNS Full Setup troubleshooting</a>.</p>
<h2 id="further-options">Further options</h2>
<h3 id="other-dns-setups">Other DNS setups</h3>
- To use Cloudflare as a reverse proxy but maintain your DNS provider, refer to [partial setup](/dns/zone-setups/partial-setup/).
- To use one or more DNS providers, refer to [DNS Zone transfers](/dns/zone-setups/zone-transfers/).
- Enterprise customers can onboard lower-level subdomains using [Subdomain setup](/dns/zone-setups/subdomain-setup/).
<h3 id="minimize-downtime">Minimize downtime</h3>
<ul>
<li></li>
</ul>
<p>If your domain is particularly sensitive to downtime, review our suggestions to <a href="/fundamentals/performance/minimize-downtime/">minimize downtime</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The provider you purchased your domain from</li>
<li id="footnote-2">Enterprise customers can onboard these using [Subdomain setup](/dns/zone-setups/subdomain-setup/).</li>
<li id="footnote-3">A security feature that protects DNS records from spoofing</li></ol></section>
