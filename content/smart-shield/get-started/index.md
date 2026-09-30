<p>Smart Shield reduces the load on your origin server and improves content delivery by consolidating requests through Cloudflare's caching infrastructure. It is available to all customers as an opt-in configuration.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You must have a Cloudflare account and <a href="/fundamentals/manage-domains/add-site/">onboard your domain</a>.</li>
<li>Verify that DNS records for the domain you want to protect are set to <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/349.md")
</div>. Smart Shield operates within Cloudflare's reverse proxy, so traffic from DNS-only records is not routed through it.
<h2 id="steps">Steps</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Smart Shield</strong>.</li>
<li>(Optional) Explore the different <a href="#packages-and-availability">available packages</a>.</li>
<li>Select <strong>Get started for free</strong> or choose a different package and select <strong>Continue</strong> to proceed to the guided onboarding flow.</li>
</ol>
<p>After setup, you can monitor origin performance and cache effectiveness through the <a href="/speed/observatory/">Observatory</a> dashboard.</p>
<h2 id="packages-and-availability">Packages and availability</h2>
<p>Pro, Business, and Enterprise customers have access to <a href="/smart-shield/configuration/health-checks/">Health Checks</a> for monitoring origin availability across all packages.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/352.md")
</div></div>
<h2 id="further-reading">Further reading</h2>
<ul class="directory-listing"><li><a href="/smart-shield/concepts/network-diagram/">Network diagram</a></li><li><a href="/smart-shield/concepts/connection-reuse/">Connection reuse</a></li></ul>
