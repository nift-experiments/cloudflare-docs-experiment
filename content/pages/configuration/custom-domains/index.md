---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/custom-domains/
  description: Add custom domains and subdomains to your Cloudflare Pages project.
  full_title: Custom domains · Cloudflare Pages docs
  head_html: <title>Custom domains · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Add custom domains and subdomains to your Cloudflare Pages project."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/custom-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/custom-domains/index.md"><meta property="og:title" content="Custom domains · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add custom domains and subdomains to your Cloudflare Pages project."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/custom-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/custom-domains/#page","headline":"Custom domains \u00b7 Cloudflare Pages docs","description":"Add custom domains and subdomains to your Cloudflare Pages project.","url":"https://developers.cloudflare.com/pages/configuration/custom-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/custom-domains/
  schema: 1
---
<p>When deploying your Pages project, you may wish to point custom domains (or subdomains) to your site.</p>
<h2 id="add-a-custom-domain">Add a custom domain</h2>
<p>To add a custom domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project > **Custom domains**.
3. Select **Set up a domain**.
4. Provide the domain that you would like to serve your Cloudflare Pages site on and select **Continue**.
<p><img src="/assets/upstream/images/pages/platform/domains.png" alt="Adding a custom domain for your Pages project through the Cloudflare dashboard" /></p>
<h3 id="add-a-custom-apex-domain">Add a custom apex domain</h3>
<p>If you are deploying to an apex domain (for example, <code>example.com</code>), then you will need to add your site as a Cloudflare zone and <a href="#configure-nameservers">configure your nameservers</a>.</p>
<h4 id="configure-nameservers">Configure nameservers</h4>
<p>To use a custom apex domain (for example, <code>example.com</code>) with your Pages project, <a href="/dns/zone-setups/full-setup/setup/">configure your nameservers to point to Cloudflare's nameservers</a>. If your nameservers are successfully pointed to Cloudflare, Cloudflare will proceed by creating a CNAME record for you.</p>
<h3 id="add-a-custom-subdomain">Add a custom subdomain</h3>
<p>If you are deploying to a subdomain, it is not necessary for your site to be a Cloudflare zone. You will need to <a href="#add-a-custom-cname-record">add a custom CNAME record</a> to point the domain to your Cloudflare Pages site. To deploy your Pages project to a custom apex domain, that custom domain must be a zone on the Cloudflare account you have created your Pages project on.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11069.md")
</aside>
<h4 id="add-a-custom-cname-record">Add a custom CNAME record</h4>
<p>If you do not want to point your nameservers to Cloudflare, you must create a custom CNAME record to use a subdomain with Cloudflare Pages. After logging in to your DNS provider, add a CNAME record for your desired subdomain, for example, <code>shop.example.com</code>. This record should point to your custom Pages subdomain, for example, <code>&lt;YOUR_SITE&gt;.pages.dev</code>.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CNAME</code></td>
<td><code>shop.example.com</code></td>
<td><code>&lt;YOUR_SITE&gt;.pages.dev</code></td>
</tr>
</tbody>
</table>
<p>If your site is already managed as a Cloudflare zone, the CNAME record will be added automatically after you confirm your DNS record.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11068.md")
</aside>
<h2 id="delete-a-custom-domain">Delete a custom domain</h2>
<p>To detach a custom domain from your Pages project, you must modify your zone's DNS records.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11070.md")
</div>
<p>After completing these steps, your Pages project will only be accessible through the <code>*.pages.dev</code> subdomain you chose when creating your project.</p>
<h2 id="disable-access-to-pages-dev-subdomain">Disable access to <code>*.pages.dev</code> subdomain</h2>
<p>To disable access to your project's provided <code>*.pages.dev</code> subdomain:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11071.md")
</div>
<h2 id="caching">Caching</h2>
<p>For guidelines on caching, refer to <a href="/pages/configuration/serving-pages/#caching-and-performance">Caching and performance</a>.</p>
<h2 id="known-issues">Known issues</h2>
<h3 id="caa-records">CAA records</h3>
<p>Certification Authority Authorization (CAA) records allow you to restrict certificate issuance to specific Certificate Authorities (CAs).</p>
<p>This can cause issues when adding a <a href="/pages/configuration/custom-domains/">custom domain</a> to your Pages project if you have CAA records that do not allow Cloudflare to issue a certificate for your custom domain.</p>
<p>To resolve this, add the necessary CAA records to allow Cloudflare to issue a certificate for your custom domain.</p>
<pre tabindex="0"><code>example.com.            300     IN      CAA     0 issue &quot;letsencrypt.org&quot;&#10;example.com.            300     IN      CAA     0 issue &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;example.com.            300     IN      CAA     0 issue &quot;ssl.com&quot;&#10;example.com.            300     IN      CAA     0 issuewild &quot;letsencrypt.org&quot;&#10;example.com.            300     IN      CAA     0 issuewild &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;example.com.            300     IN      CAA     0 issuewild &quot;ssl.com&quot;&#10;</code></pre>
<p>Refer to the <a href="/ssl/faq/#caa-records">Certification Authority Authorization (CAA) FAQ</a> for more information.</p>
<h3 id="change-dns-entry-away-from-pages-and-then-back-again">Change DNS entry away from Pages and then back again</h3>
<p>Once a custom domain is set up, if you change the DNS entry to point to something else (for example, your origin), the custom domain will become inactive. If you then change that DNS entry to point back at your custom domain, anybody using that DNS entry to visit your website will get errors until it becomes active again. If you want to redirect traffic away from your Pages project temporarily instead of changing the DNS entry, it would be better to use an <a href="/rules/origin-rules/">Origin rule</a> or a <a href="/rules/url-forwarding/single-redirects/create-dashboard/">redirect rule</a> instead.</p>
<h2 id="relevant-resources">Relevant resources</h2>
<ul>
<li><a href="/pages/configuration/debugging-pages/">Debugging Pages</a> - Review common errors when deploying your Pages project.</li>
</ul>
