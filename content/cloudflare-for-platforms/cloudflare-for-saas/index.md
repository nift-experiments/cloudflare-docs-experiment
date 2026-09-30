<p>Cloudflare for SaaS allows you to extend the security and performance benefits of Cloudflare's network to your customers via their own custom or vanity domains.</p>
<br />
<p>As a SaaS provider, you may want to support subdomains under your own zone in addition to letting your customers use their own domain names with your services. For example, a customer may want to use their vanity domain <code>app.customer.com</code> to point to an application hosted on your Cloudflare zone <code>service.saas.com</code>. Cloudflare for SaaS allows you to increase security, performance, and reliability of your customers' domains.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4065.md")
</aside>
<h2 id="benefits">Benefits</h2>
<p>When you use Cloudflare for SaaS, it helps you to:</p>
<ul>
<li>Provide custom domain support.</li>
<li>Keep your customers' traffic encrypted.</li>
<li>Keep your customers online.</li>
<li>Facilitate fast load times of your customers' domains.</li>
<li>Gain insight through traffic analytics.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>If your customers already have their applications on Cloudflare, they cannot control some Cloudflare features for hostnames managed by your Custom Hostnames configuration, including:</p>
<ul>
<li>Argo</li>
<li>Early Hints</li>
<li>Client-side security (formerly known as Page Shield)</li>
<li>Spectrum</li>
<li>Wildcard DNS</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>As the SaaS provider, you can extend Cloudflare's products to customer-owned custom domains by adding them to your zone <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">as custom hostnames</a>. Through a suite of easy-to-use products, Cloudflare for SaaS routes traffic from custom hostnames to an origin, set up on your domain. Cloudflare for SaaS is highly customizable. Three possible configurations are shown below.</p>
<h3 id="standard-cloudflare-for-saas-configuration">Standard Cloudflare for SaaS configuration:</h3>
<p>Custom hostnames are routed to a default origin server called fallback origin. This configuration is available on all plans.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/use-cases/Standard.png" alt="Standard case" /></p>
<h3 id="cloudflare-for-saas-with-apex-proxying">Cloudflare for SaaS with Apex Proxying:</h3>
<p>This allows you to support apex domains even if your customers are using a DNS provider that does not allow a CNAME at the apex. This is available as an add-on for Enterprise plans. For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">Apex Proxying</a>.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/use-cases/Advanced.png" alt="Advanced case" /></p>
<h3 id="cloudflare-for-saas-with-byoip">Cloudflare for SaaS with BYOIP:</h3>
<p>This allows you to support apex domains even if your customers are using a DNS provider that does not allow a CNAME at the apex. Also, you can point to your own IPs if you want to bring an IP range to Cloudflare (instead of Cloudflare provided IPs). This is available as an add-on for Enterprise plans.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/use-cases/Pro.png" alt="Pro Case" /></p>
<h2 id="availability">Availability</h2>
<p>Cloudflare for SaaS is bundled with non-Enterprise plans and available as an add-on for Enterprise plans. For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/plans/">Plans</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-link-button" href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Get started</a>
<a class="nb-link-button" href="https://blog.cloudflare.com/introducing-ssl-for-saas/">Learn more</a></p>
