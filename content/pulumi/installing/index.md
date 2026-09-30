---
cp9:
  canonical: https://developers.cloudflare.com/pulumi/installing/
  description: Install the Pulumi CLI on Mac, Linux, or Windows and verify your installation.
  full_title: Get started · Pulumi docs
  head_html: <title>Get started · Pulumi docs</title><meta name="generator" content="Nift"><meta name="description" content="Install the Pulumi CLI on Mac, Linux, or Windows and verify your installation."><link rel="canonical" href="https://developers.cloudflare.com/pulumi/installing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pulumi/installing/index.md"><meta property="og:title" content="Get started · Pulumi docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install the Pulumi CLI on Mac, Linux, or Windows and verify your installation."><meta property="og:url" content="https://developers.cloudflare.com/pulumi/installing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pulumi"><meta name="algolia_product_filter" content="Pulumi"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pulumi"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pulumi/installing/#page","headline":"Get started \u00b7 Pulumi docs","description":"Install the Pulumi CLI on Mac, Linux, or Windows and verify your installation.","url":"https://developers.cloudflare.com/pulumi/installing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pulumi/installing/
  schema: 1
---
<p>Follow the recommended steps for your operating system below. For official instructions on installing Pulumi and other install options, refer to <a href="https://www.pulumi.com/docs/install/">Install Pulumi</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/595.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/594.md")
</aside>
<h2 id="installation">Installation</h2>
<h3 id="mac">Mac</h3>
<p>Install via Homebrew package manager.</p>
<pre tabindex="0"><code class="language-sh">brew install pulumi/tap/pulumi&#10;</code></pre>
<h3 id="linux">Linux</h3>
<p>Use the installation script.</p>
<pre tabindex="0"><code class="language-sh">curl -fsSL https://get.pulumi.com | sh&#10;</code></pre>
<h3 id="windows">Windows</h3>
<ol>
<li>Download the latest installer from the <a href="https://github.com/pulumi/pulumi-winget/releases/latest">Pulumi Repository</a></li>
<li>Double click the MSI file and complete the wizard.</li>
</ol>
<h2 id="verify-installation">Verify installation</h2>
<p>To verify your installation, run the following in the terminal:</p>
<pre tabindex="0"><code class="language-sh">pulumi version&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/593.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Follow the <a href="/pulumi/tutorial/hello-world/">Hello World tutorial</a> to write a simple Pulumi program. It takes about 10 minutes to complete.</p>
