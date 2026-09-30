---
cp9:
  canonical: https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/
  description: The easiest way to begin using APO is directly from Cloudflare's WordPress plugin. Before you can use APO, you must first install and activate the plugin and then activate APO.
  full_title: Activate the Cloudflare WordPress plugin · Cloudflare Automatic Platform Optimization docs
  head_html: <title>Activate the Cloudflare WordPress plugin · Cloudflare Automatic Platform Optimization docs</title><meta name="generator" content="Nift"><meta name="description" content="The easiest way to begin using APO is directly from Cloudflare&#x27;s WordPress plugin. Before you can use APO, you must first install and activate the plugin and then activate APO."><link rel="canonical" href="https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/index.md"><meta property="og:title" content="Activate the Cloudflare WordPress plugin · Cloudflare Automatic Platform Optimization docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The easiest way to begin using APO is directly from Cloudflare&#x27;s WordPress plugin. Before you can use APO, you must first install and activate the plugin and then activate APO."><meta property="og:url" content="https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Automatic Platform Optimization"><meta name="algolia_product_filter" content="Automatic Platform Optimization"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Automatic Platform Optimization"><meta name="pcx_tags" content="WordPress"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/#page","headline":"Activate the Cloudflare WordPress plugin \u00b7 Cloudflare Automatic Platform Optimization docs","description":"The easiest way to begin using APO is directly from Cloudflare's WordPress plugin. Before you can use APO, you must first install and activate the plugin and then activate APO.","url":"https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["WordPress"]}</script>
  markdown: true
  noindex: false
  route: /automatic-platform-optimization/get-started/activate-cf-wp-plugin/
  schema: 1
---
<p>After you <a href="/automatic-platform-optimization/get-started/change-nameservers/">change your nameservers</a>, activate the Cloudflare WordPress plugin.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before activating the Cloudflare WordPress plugin, review the following prerequisites.</p>
<h3 id="plan-type">Plan type</h3>
<p>For users on the free plan, <a href="#purchase-apo">purchase APO</a> before installing the WordPress plugin.</p>
<p>For users on a Pro plan or higher, continue to <a href="#install-and-activate-the-cloudflare-wordpress-plugin">Install and activate</a> the Cloudflare WordPress plugin.</p>
<h3 id="plugin-compatibility">Plugin compatibility</h3>
<p>Cloudflare recommends turning off plugins such as WP Rocket Cache Plugin, W3 Total Cache, or similar plugins when first setting up APO. After confirming APO is working, we recommend testing whether turning on the plugins listed above improves results or causes unexpected behavior. In many cases, using APO along with other caching plugins can cause unexpected results.</p>
<p>We also recommend clearing the server cache for the WP Rocket Cache plugin, W3 Total Cache, or similar plugins after APO activation.</p>
<p>For more details, refer to <a href="/automatic-platform-optimization/about/plugin-compatibility/">Plugin compatibility</a>.</p>
<h3 id="limitations">Limitations</h3>
<p>The Cloudflare APO WordPress plugin does not support multisite WordPress installation.</p>
<h2 id="purchase-apo">Purchase APO</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Speed</strong> &gt; <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Content Optimization</strong>.</li>
<li>For <strong>Automatic Platform Optimization for WordPress</strong>, select <strong>Purchase</strong>.</li>
<li>Enter your payment information and select <strong>Confirm payment</strong>.</li>
</ol>
<h2 id="install-and-activate-the-cloudflare-wordpress-plugin">Install and activate the Cloudflare WordPress plugin</h2>
<p>The easiest way to begin using APO is directly from Cloudflare’s WordPress plugin. Before you can use APO, you must first install and activate the plugin and then activate APO.</p>
<ol>
<li>Navigate and log in to your WordPress account.</li>
<li>Select <strong>Plugins</strong> &gt; <strong>Add new</strong>.</li>
<li>In the search field, enter <code>Cloudflare</code>.</li>
<li>Locate the Cloudflare plugin and select <strong>Install now</strong>.</li>
<li>After the plugin finishes installing, select <strong>Activate</strong>. The Cloudflare plugin now displays in your Plugins list.</li>
</ol>
<h2 id="activate-apo">Activate APO</h2>
<p>To create the connection between WordPress and Cloudflare, you will create an API token from your Cloudflare dashboard and add it to WordPress. To set up APO on a subdomain, refer to <a href="/automatic-platform-optimization/reference/subdomain-subdirectories/">Subdomains and subdirectories</a>.</p>
<h2 id="create-the-api-token-from-cloudflare">Create the API token from Cloudflare</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Locate <strong>WordPress</strong> from the list and select <strong>Use template</strong>.</li>
<li>Select <strong>Continue to summary</strong> at the bottom of the page.</li>
<li>On the <strong>WordPress API token summary</strong> page, select <strong>Create Token</strong>. Your API token displays.</li>
<li>Select the <strong>Copy</strong> button to copy your token. You will need to paste the token in the next section.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3345.md")
</aside>
<h2 id="add-your-api-token-to-wordpress">Add your API token to WordPress</h2>
<ol>
<li>Open your WordPress account and navigate to Plugins.</li>
<li>Locate the Cloudflare plugin and select <strong>Settings</strong>.</li>
<li>Select the option to sign in with an existing account.</li>
<li>Enter your email address and paste the token you copied in Step 7 of Create the API token from Cloudflare.</li>
<li>Select <strong>Save API Credentials</strong>.</li>
<li>For <strong>Apply Recommended Cloudflare Settings for WordPress</strong>, select <strong>Apply</strong>.</li>
<li>For <strong>Automatic Platform Optimization</strong>, switch the toggle to <strong>On</strong> to enable APO.</li>
</ol>
<p>To verify APO is working, see <a href="/automatic-platform-optimization/get-started/verify-apo-works/">Verify APO works</a>.</p>
