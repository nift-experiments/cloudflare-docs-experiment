---
cp9:
  canonical: https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/
  description: This tutorial shows how to enable TLS 1.3, Automatic HTTPS Rewrites, and Strict SSL mode using the updated v5 provider.
  full_title: Configure HTTPS settings · Cloudflare Terraform docs
  head_html: <title>Configure HTTPS settings · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial shows how to enable TLS 1.3, Automatic HTTPS Rewrites, and Strict SSL mode using the updated v5 provider."><link rel="canonical" href="https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/index.md"><meta property="og:title" content="Configure HTTPS settings · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial shows how to enable TLS 1.3, Automatic HTTPS Rewrites, and Strict SSL mode using the updated v5 provider."><meta property="og:url" content="https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/#page","headline":"Configure HTTPS settings \u00b7 Cloudflare Terraform docs","description":"This tutorial shows how to enable TLS 1.3, Automatic HTTPS Rewrites, and Strict SSL mode using the updated v5 provider.","url":"https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/tutorial/configure-https-settings/
  schema: 1
---
<p>After setting up basic DNS records, you can configure zone settings using Terraform. This tutorial shows how to enable <a href="/ssl/edge-certificates/additional-options/tls-13/">TLS 1.3</a>, <a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a>, and <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Strict SSL mode</a> using the updated v5 provider.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Completed tutorials <a href="/terraform/tutorial/initialize-terraform/">1</a> and <a href="/terraform/tutorial/track-history/">2</a></li>
<li>Valid SSL certificate on your origin server (use the <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA</a> to generate one for strict SSL mode)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14761.md")
</aside>
<h2 id="1-create-zone-setting-configuration"><ol>
<li>Create zone setting configuration</li>
</ol></h2>
<p>Create a new branch and add zone settings:</p>
<pre tabindex="0"><code class="language-bash">git checkout -b step3-zone-settings&#10;</code></pre>
<p>Add the following to your <code>main.tf</code> file:</p>
<pre tabindex="0"><code class="language-hcl">&#35; Enable TLS 1.3&#10;resource &quot;cloudflare_zone_setting&quot; &quot;tls_1_3&quot; {&#10;  zone_id    = var.zone_id&#10;  setting_id = &quot;tls_1_3&quot;&#10;  value      = &quot;on&quot;&#10;}&#10;&#10;&#35; Enable automatic HTTPS rewrites&#10;resource &quot;cloudflare_zone_setting&quot; &quot;automatic_https_rewrites&quot; {&#10;  zone_id    = var.zone_id&#10;  setting_id = &quot;automatic_https_rewrites&quot;&#10;  value      = &quot;on&quot;&#10;}&#10;&#10;&#35; Set SSL mode to strict&#10;resource &quot;cloudflare_zone_setting&quot; &quot;ssl&quot; {&#10;  zone_id    = var.zone_id&#10;  setting_id = &quot;ssl&quot;&#10;  value      = &quot;strict&quot;&#10;}&#10;</code></pre>
<h2 id="2-preview-and-apply-the-changes"><ol start="2">
<li>Preview and apply the changes</li>
</ol></h2>
<p>Review the proposed changes:</p>
<pre tabindex="0"><code class="language-sh">terraform plan&#10;</code></pre>
<p>Expected output</p>
<pre tabindex="0"><code class="language-sh">Plan: 3 to add, 0 to change, 0 to destroy.&#10;&#10;Terraform will perform the following actions:&#10;&#10;  &#35; cloudflare_zone_setting.automatic_https_rewrites will be created&#10;  &#43; resource &quot;cloudflare_zone_setting&quot; &quot;automatic_https_rewrites&quot; {&#10;      &#43; setting_id = &quot;automatic_https_rewrites&quot;&#10;      &#43; value      = &quot;on&quot;&#10;      &#43; zone_id    = &quot;your-zone-id&quot;&#10;    }&#10;&#10;  &#35; cloudflare_zone_setting.ssl will be created&#10;  &#43; resource &quot;cloudflare_zone_setting&quot; &quot;ssl&quot; {&#10;      &#43; setting_id = &quot;ssl&quot;&#10;      &#43; value      = &quot;strict&quot;&#10;      &#43; zone_id    = &quot;your-zone-id&quot;&#10;    }&#10;&#10;  &#35; cloudflare_zone_setting.tls_1_3 will be created&#10;  &#43; resource &quot;cloudflare_zone_setting&quot; &quot;tls_1_3&quot; {&#10;      &#43; setting_id = &quot;tls_1_3&quot;&#10;      &#43; value      = &quot;on&quot;&#10;      &#43; zone_id    = &quot;your-zone-id&quot;&#10;    }&#10;</code></pre>
<p>Commit and merge the changes:</p>
<pre tabindex="0"><code class="language-bash">git add main.tf&#10;git commit -m &quot;Step 3 - Enable TLS 1.3, automatic HTTPS rewrites, and strict SSL&quot;&#10;git checkout main&#10;git merge step3-zone-settings&#10;git push&#10;</code></pre>
<p>Before applying the changes, try to connect with TLS 1.3. Technically, you should not be able to with default settings. To follow along with this test, you will need to <a href="https://everything.curl.dev/source/build/tls/boringssl#build-boringssl">compile <code>curl</code> against BoringSSL</a>.</p>
<pre tabindex="0"><code class="language-sh">curl -v --tlsv1.3 https://www.example.com 2&gt;&amp;1 | grep &quot;SSL connection\|error&quot;&#10;</code></pre>
<p>As shown above, you should receive an error because TLS 1.3 is not yet enabled on your zone. Enable it by running <code>terraform apply</code> and try again.</p>
<p>Apply the configuration:</p>
<pre tabindex="0"><code class="language-sh">terraform apply&#10;</code></pre>
<p>Type <code>yes</code> when prompted.</p>
<h2 id="3-verify-the-settings"><ol start="3">
<li>Verify the settings</li>
</ol></h2>
<p>Try the same command as before. The command will now succeed.</p>
<pre tabindex="0"><code class="language-sh">curl -v --tlsv1.3 https://www.example.com 2&gt;&amp;1 | grep &quot;SSL connection\|error&quot;&#10;</code></pre>
