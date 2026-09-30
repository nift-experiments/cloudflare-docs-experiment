---
cp9:
  canonical: https://developers.cloudflare.com/terraform/installing/
  description: Install Terraform and configure the Cloudflare provider on your operating system.
  full_title: Install Terraform · Cloudflare Terraform docs
  head_html: <title>Install Terraform · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Install Terraform and configure the Cloudflare provider on your operating system."><link rel="canonical" href="https://developers.cloudflare.com/terraform/installing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/installing/index.md"><meta property="og:title" content="Install Terraform · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install Terraform and configure the Cloudflare provider on your operating system."><meta property="og:url" content="https://developers.cloudflare.com/terraform/installing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/installing/#page","headline":"Install Terraform \u00b7 Cloudflare Terraform docs","description":"Install Terraform and configure the Cloudflare provider on your operating system.","url":"https://developers.cloudflare.com/terraform/installing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/installing/
  schema: 1
---
<p>Terraform ships as a single binary file. The examples below include installation information for popular operating systems.</p>
<p>For official instructions on installing Terraform, refer to <a href="https://developer.hashicorp.com/terraform/tutorials/certification-associate-tutorials/install-cli">Install Terraform</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/255.md")
</aside>
<h2 id="mac">Mac</h2>
<p>The easiest way to install Terraform on macOS is with Homebrew.</p>
<pre tabindex="0"><code class="language-sh">brew tap hashicorp/tap&#10;brew install hashicorp/tap/terraform&#10;</code></pre>
<h2 id="linux">Linux</h2>
<p>You can install the <code>terraform</code> binary via your distribution's package manager. For example:</p>
<pre tabindex="0"><code class="language-sh">sudo apt install terraform&#10;</code></pre>
<p>Alternatively, you can fetch a specific version directly and place the binary in your <code>PATH</code>:</p>
<pre tabindex="0"><code class="language-sh">wget -q https://releases.hashicorp.com/terraform/1.4.5/terraform_1.4.5_linux_amd64.zip&#10;&#10;unzip terraform_1.4.5_linux_amd64.zip&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Archive:  terraform_1.4.5_linux_amd64.zip&#10;  inflating: terraform&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">sudo mv terraform /usr/local/bin/terraform&#10;&#10;terraform version&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Terraform v1.4.5&#10;</code></pre>
<h2 id="windows">Windows</h2>
<ol>
<li>Download the 32 or 64-bit executable from the <a href="https://developer.hashicorp.com/terraform/downloads">Download Terraform</a> page.</li>
<li>Unzip and place <code>terraform.exe</code> somewhere in your path.</li>
</ol>
<h2 id="other">Other</h2>
<p>For additional installers, refer to the <a href="https://developer.hashicorp.com/terraform/downloads">Download Terraform</a> page.</p>
