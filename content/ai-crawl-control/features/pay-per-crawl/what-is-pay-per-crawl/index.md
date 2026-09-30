<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pay-per-crawl-beta">Pay per crawl beta</h3>
@markup("md", "content/.markup/bodies/2753.md")
</aside>
<p>AI crawlers often consume vast amounts of web content. Some provide mutual benefit to content owners by indexing content for search engines, but others engage in activities such as content scraping without permission.</p>
<p>The resulting landscape leaves content owners with limited options for managing AI crawlers or receiving compensation for automated access to their intellectual property.</p>
<h2 id="what-is-pay-per-crawl">What is Pay Per Crawl?</h2>
<p>Pay per crawl is a feature of AI Crawl Control that enables site owners to control and monetize AI crawler access to content by setting a price per zone.</p>
<p>Each time an AI crawler requests content, they either present payment intent via request headers for successful <code>HTTP 200</code> access, or receive an <code>HTTP 402 Payment Required</code> response with pricing. Cloudflare acts as the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/2754.md")
</div> for pay per crawl and also provides the underlying technical infrastructure.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2752.md")
</aside>
<p>Ultimately, pay per crawl enables:</p>
<ul>
<li>Site owners to take control of their content, and charge a fee every time an AI crawler accesses a page in their <a href="/fundamentals/concepts/accounts-and-zones/#zones">Cloudflare zone</a>. For more details, refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/">use pay per crawl as a site owner</a>.</li>
<li>AI crawler owners to pay to access content on sites protected by pay per crawl. For more details, refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/">use pay per crawl as an AI owner</a>.</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-pay-per-crawl-diagram.png" alt="Pay per crawl components" /></p>
<h2 id="additional-resources">Additional resources</h2>
<p>Refer to the following resources.</p>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/">Use pay per crawl as a site owner</a>.</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/set-up-cloudflare-account/">Use pay per crawl as an AI owner</a>.</li>
<li><a href="/ai-crawl-control/configuration/ai-crawl-control-with-waf/">AI Crawl Control with Cloudflare WAF</a>.</li>
<li><a href="/ai-crawl-control/configuration/ai-crawl-control-with-bots/">AI Crawl Control with Cloudflare Bots</a>.</li>
</ul>
