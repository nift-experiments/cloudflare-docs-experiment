<p>Cloudflare DNS offers a few different <a href="/dns/zone-setups/">setup options</a>. A primary setup (also known as full) is the most common and the only one available for Free or Pro plans. For details, refer to <a href="/dns/zone-setups/full-setup/">About</a>. For more introductory context, refer to <a href="/dns/concepts/">Concepts</a>.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure that you:</p>
<ul>
<li>Create a Cloudflare account — If you have not already, <a href="/fundamentals/account/create-account/">sign up for a Cloudflare account</a>.</li>
<li>Own a domain name — You need a registered domain (for example, <code>example.com</code>). If you do not have one, you can <a href="https://dash.cloudflare.com/?to=/:account/domains/register">register a domain at-cost through Cloudflare Registrar</a>. Domains purchased through Cloudflare Registrar automatically use Cloudflare for authoritative DNS, so you can skip the rest of this tutorial.</li>
</ul>
<h2 id="1-add-your-domain-to-cloudflare"><ol>
<li>Add your domain to Cloudflare</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7951.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7948.md")
</aside>
<details class="nb-details"><summary>DNS records quick scan</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7953.md")
</div></details>
<h2 id="2-review-your-dns-records"><ol start="2">
<li>Review your DNS records</li>
</ol></h2>
<p>Your DNS records must be accurate for your domain to work properly. If you don't know what DNS records are, consider the video below for a quick explanation.</p>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/7e8cdb06-7280-4139-8f13-256e03027f00/public" alt="Review your DNS records"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/07e42365d5c40f2a46a6bde2844f370f/iframe?preload=true&amp;letterboxColor=transparent" title="Review your DNS records" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7946.md")
</aside>
<h3 id="common-records">Common records</h3>
<p>Since the quick scan is not guaranteed to find all existing DNS records, you need to review your records, paying special attention to the following:</p>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-zone-apex/">Zone apex records (<code>example.com</code>)</a></p>
  <details class="nb-details"><summary>More about zone apex records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/7954.md")
</div></details>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-subdomain/">Subdomain records (<code>www.example.com</code> or <code>blog.example.com</code>)</a></p>
<details class="nb-details"><summary>More about subdomain records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/7955.md")
</div></details>
<ul>
<li>
<p><a href="/dns/manage-dns-records/how-to/email-records/">Email records</a></p>
<details class="nb-details"><summary>More about email records</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/7956.md")
</div></details>
<h3 id="proxy-status">Proxy status</h3>
<p>Each A, AAAA, and CNAME record has a <a href="/dns/proxy-status/">proxy status</a> toggle:</p>
<ul>
<li><strong>Proxied</strong> (orange cloud): web traffic goes through the Cloudflare network, which provides caching, DDoS protection, and other security features.</li>
<li><strong>DNS only</strong> (gray cloud): Cloudflare returns the DNS record value but does not proxy traffic. Use this for CNAME records that verify your domain for third-party services.</li>
</ul>
<h2 id="3-change-your-nameservers"><ol start="3">
<li>Change your nameservers</li>
</ol></h2>
<p>Your domain will be assigned two authoritative Cloudflare nameservers. Nameservers are specialized servers that store your domain's DNS records and &quot;answer&quot; requests from browsers by providing the specific IP address needed to connect to your website.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7945.md")
</aside>
<h3 id="3-1-get-nameserver-names">3.1. Get nameserver names</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7959.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7944.md")
</aside>
<h3 id="3-2-log-in-to-your-registrar">3.2. Log in to your registrar</h3>
<p>Log in to the admin account for your domain registrar. If you do not know your provider, use <a href="https://lookup.icann.org/">ICANN Lookup</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7943.md")
</aside>
<h3 id="3-3-turn-off-dnssec">3.3. Turn off DNSSEC</h3>
<p>If your domain has <a href="/dns/dnssec/">DNSSEC</a><sup><a href="#footnote-1">1</a></sup> active, you must <a href="/dns/dnssec/#disable-dnssec">turn it off</a> at your registrar before replacing nameservers. Changing nameservers while DNSSEC is active can cause your domain to become unreachable. You can <a href="/dns/dnssec/#enable-dnssec">re-enable DNSSEC through Cloudflare</a> after your domain is active.</p>
<details class="nb-details"><summary>Provider-specific DNSSEC instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7960.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7942.md")
</aside>
<h3 id="3-4-update-your-registrar">3.4. Update your registrar</h3>
<ol>
<li>
<p>Remove your existing authoritative nameservers.</p>
</li>
<li>
<p>Add the nameservers provided by Cloudflare. If their names are not <strong>copied exactly</strong>, your DNS will not resolve correctly.</p>
</li>
</ol>
<details class="nb-details"><summary>Provider-specific instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7961.md")
</div></details>
<p>To avoid common issues, refer to our <a href="/dns/zone-setups/full-setup/troubleshooting/">Nameserver replacement checklist</a>.</p>
<h3 id="3-5-verify-changes">3.5. Verify changes</h3>
<p>Wait up to 24 hours while your registrar updates your nameservers.</p>
<p>When your domain is <strong>Active</strong>:</p>
<ul>
<li>You will receive an email from Cloudflare.</li>
<li>Your domain will have a <a href="/dns/zone-setups/reference/domain-status/">status</a> of <strong>Active</strong> on the <strong>Domains</strong> page of your account.</li>
<li>Online tools such as <a href="https://www.whatsmydns.net/">https://www.whatsmydns.net/</a> will show your Cloudflare-assigned nameservers (most of these tools use cached query results, so it may take longer for them to show the updated nameservers).</li>
<li>CLI commands will show your Cloudflare-assigned nameservers</li>
</ul>
<pre><code class="language-txt">&#42;macOS/Linux*&#10;&#10;whois &lt;DOMAIN_NAME&gt;&#10;dig ns &lt;DOMAIN_NAME&gt; @1.1.1.1&#10;dig ns &lt;DOMAIN_NAME&gt; @8.8.8.8&#10;dig &lt;DOMAIN_NAME&gt; +trace&#10;&#10;&#42;Windows*&#10;&#10;nslookup -type=ns &lt;DOMAIN_NAME&gt; 1.1.1.1&#10;nslookup -type=ns &lt;DOMAIN_NAME&gt; 8.8.8.8&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7941.md")
</aside>
<h2 id="4-re-enable-dnssec"><ol start="4">
<li>Re-enable DNSSEC</li>
</ol></h2>
<p>If you turned off DNSSEC before updating your nameservers, you can now <a href="/dns/dnssec/">re-enable DNSSEC through Cloudflare</a> to protect your domain from spoofing.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A security feature that protects DNS records from spoofing</li></ol></section>
