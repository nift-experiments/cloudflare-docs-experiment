<p>You can only crawl domains that you have onboarded onto the same Cloudflare account. Refer to <a href="/fundamentals/manage-domains/add-site/">Onboard a domain</a> for more information on adding a domain to your Cloudflare account.</p>
<p>If your website has pages behind authentication or pages that are only visible to logged-in users, you can configure custom HTTP headers to allow the AI Search crawler to access this protected content. You can add up to five custom HTTP headers to the requests AI Search sends when crawling your site.</p>
<p>This setting is labeled <strong>Extra headers</strong> in the dashboard, under <strong>Parser options</strong>. In the <a href="/ai-search/api/instances/rest-api/">REST API</a> and in Wrangler, it is the <code>source_params.web_crawler.parse_options.include_headers</code> field.</p>
<h2 id="configure-in-the-dashboard">Configure in the dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3095.md")
</div>
<p>The crawler sends every header you configure with each request it makes to your site. Adding or changing headers on an existing instance starts a new indexing job that reindexes every item.</p>
<h2 id="indexing-your-site-protected-by-cloudflare-access">Indexing your site protected by Cloudflare Access</h2>
<p>To allow AI Search to crawl a site protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>, you need to create service token credentials and configure them as custom headers.</p>
<p>Service tokens bypass user authentication, so ensure your Access policies are configured appropriately for the content you want to index. The service token will allow the AI Search crawler to access all content covered by the Service Auth policy.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3096.md")
</div>
