---
cp9:
  canonical: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/
  description: Configure WordPress.com with Cloudflare services.
  full_title: WordPress.com and Cloudflare · Cloudflare Support docs
  head_html: <title>WordPress.com and Cloudflare · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure WordPress.com with Cloudflare services."><link rel="canonical" href="https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/index.md"><meta property="og:title" content="WordPress.com and Cloudflare · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure WordPress.com with Cloudflare services."><meta property="og:url" content="https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/#page","headline":"WordPress.com and Cloudflare \u00b7 Cloudflare Support docs","description":"Configure WordPress.com with Cloudflare services.","url":"https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/third-party-software/content-management-system-cms/wordpresscom-and-cloudflare/
  schema: 1
---
<h2 id="getting-started-with-wordpress-com-and-cloudflare">Getting started with WordPress.com and Cloudflare</h2>
<p>Cloudflare and WordPress.com are partnering to offer customers Cloudflare's performance and security solutions with WordPress.com's web-hosting platform. Getting started is easy.</p>
<p>1. Add your WordPress site to Cloudflare. Do the following:</p>
<ul>
<li><a href="/fundamentals/account/create-account/">Create a Cloudflare account</a>.</li>
<li><a href="/fundamentals/manage-domains/add-site/">Onboard your domain</a> to Cloudflare.</li>
</ul>
<p>During this process, Cloudflare scans your existing WordPress.com DNS records and displays them. The records will look similar to the examples below.</p>
<ul>
<li><code>A example.com 192.0.78.12</code></li>
<li><code>A example.com 192.0.78.13</code></li>
</ul>
<p>WordPress.com does not guarantee the IP address will never change. For maximum uptime, you should complete the following:</p>
<p>2. Find your <code>&lt;site&gt;.wordpress.com</code> domain from the <a href="https://wordpress.com/domains/manage">Manage Domains</a> page. The domain will look like <code>examplecom.wordpress.com</code>, i.e. your domain with non-alphanumeric characters removed.</p>
<p>3. Enter the domain into your browser's address bar to make sure the domain is correct.</p>
<p>4. Add the record <code>CNAME @ examplecom.wordpress.com</code>.</p>
<p>5. Remove the A records.</p>
<p><img src="/assets/upstream/images/support/add-cname-wp.png" alt="Example of completed CNAME record setup." /></p>
<p>Congratulations! Your site is now accelerated and protected by Cloudflare.</p>
<hr />
<h2 id="enabling-additional-cloudflare-products">Enabling additional Cloudflare products</h2>
<h2 id="cloudflare-web-analytics-free"><strong>Cloudflare Web Analytics (Free)</strong></h2>
<p>Cloudflare Web Analytics gives web creators the information they need in a simple, clean way that doesn't sacrifice their visitors' privacy. One of the goals of the partnership is to bring a privacy-first analytics solution to WordPress.com sites.</p>
<h3 id="cloudflare">Cloudflare</h3>
<p>1. <a href="https://dash.cloudflare.com/">Open your dashboard</a> and select the Account menu &gt; <strong>Account Home</strong>.</p>
<p>2. On the Account homepage, select <strong>Analytics &amp; Logs &gt; Web Analytics</strong>.</p>
<p>3. Enter the hostname to use with Web Analytics. Typically the hostname is your top-level domain, like <code>example.com</code>.</p>
<p>4. Click <strong>Next</strong>.</p>
<p>5. Select <strong>Click to copy</strong> under <strong>Copy JS Snippet</strong>.</p>
<h3 id="wordpress">WordPress</h3>
<p>1. Open WordPress and select your site.</p>
<p>2. Select <strong>Tools</strong> &gt; <strong>Marketing</strong>.</p>
<p>3. Locate the Cloudflare section.</p>
<p>4. Paste the code snippet you copied from Cloudflare into the <strong>Tracking ID</strong> field. The field will extract the Tracking ID from the snippet.</p>
<p>5. Toggle <strong>Add to Cloudflare</strong> to enable the tracking.</p>
<p>WordPress.com automatically adds the javascript to each page of your site. You can view the new insights from your Cloudflare dashboard under <strong>Web Analytics</strong>.</p>
<h2 id="automatic-platform-optimization-for-wordpress-com-5-month-included-with-pro-and-business-plans"><strong>Automatic Platform Optimization for WordPress.com ($5/month, included with Pro and Business plans)</strong></h2>
<p>Cloudflare's <a href="https://www.cloudflare.com/automatic-platform-optimization/wordpress/">Automatic Platform Optimization</a> for WordPress.com is the easiest way to drastically speed up your WordPress.com site. With the <a href="https://wordpress.org/plugins/cloudflare/">APO plugin</a>, Cloudflare accelerates your WordPress.com site by intelligently caching dynamic content, which means fast performance for your visitors no matter where they are. For more information, refer to <a href="/automatic-platform-optimization/">Automatic Platform Optimization</a> and to the <a href="https://blog.cloudflare.com/automatic-platform-optimizations-starting-with-wordpress/">blog</a>.</p>
<h3 id="requirements"><strong>Requirements</strong></h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14689.md")
</aside>
<ul>
<li>Cloudflare free plan + $5/month APO add-on or a Pro or Business plan subscription (includes APO)</li>
<li>WordPress.com Business plan or above (requires plugins)</li>
</ul>
<h3 id="install-and-enable-apo"><strong>Install and enable APO</strong></h3>
<p>1. From WordPress, install the <a href="https://wordpress.org/plugins/cloudflare/">Cloudflare WordPress plugin</a> on your WordPress website or update to the latest version (3.8.2 or higher).</p>
<p>2. <a href="https://wordpress.org/plugins/cloudflare/#installation">Authenticate the plugin</a> to connect to Cloudflare if you have not already done so.</p>
<p>3. From the Home screen of the Cloudflare section, turn on Automatic Platform Optimization.</p>
<p>For more details, refer to <a href="/automatic-platform-optimization/">Understanding Automatic Platform Optimization (APO) with WordPress</a>.</p>
<hr />
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="how-do-i-verify-that-cloudflare-is-now-my-dns-provider-on-record"><strong>How do I verify that Cloudflare is now my DNS provider on record?</strong></h3>
<p>1. Visit <a href="https://dnschecker.org/#A/s-steiner.com">https://dnschecker.org</a>.</p>
<p>2. From the dropdown under <strong>DNS Check, s</strong>elect NS record.</p>
<p>3. In the text field, enter your domain name and click <strong>Search</strong>.</p>
<p>4. Verify that your Cloudflare nameservers display.</p>
<h3 id="how-can-i-confirm-apo-is-up-and-running"><strong>How can I confirm APO is up and running?</strong></h3>
<p>In a terminal, use the following cURL. The header <code>'accept: text/html'</code> is important</p>
<pre tabindex="0"><code class="language-sh">curl -svo /dev/null -A &quot;CF&quot; &#x27;https://example.com/&#x27; -H &#x27;accept: text/html&#x27; 2&gt;&amp;1 | grep &#x27;cf-cache-status\|cf-edge\|cf-apo-via&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&lt; cf-cache-status: HIT&#10;&lt; cf-apo-via: cache&#10;&lt; cf-edge-cache: cache,platform=wordpress&#10;</code></pre>
<p>As always, <code>cf-cache-status</code> displays if the asset hit the cache or was considered dynamic and served from the origin.</p>
<ul>
<li>The <code>cf-apo-via</code> header returns the APO status for the given request.</li>
<li>The <code>cf-edge-cache</code> header means the WordPress plugin is installed and enabled.</li>
</ul>
<h3 id="how-can-i-verify-apo-and-the-wordpress-com-integration-works">How can I verify APO and the WordPress.com integration works?</h3>
<p>1. Publish a change on your WordPress website.</p>
<p>2. Refresh the page twice.</p>
<p>3. You should see a change. The page should be cached with <code>cf-cache-status: HIT</code> and <code>cf-apo-via: cache</code> in a response header.</p>
