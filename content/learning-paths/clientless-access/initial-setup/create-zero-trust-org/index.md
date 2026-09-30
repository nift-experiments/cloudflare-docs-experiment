---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/
  description: Set up a Zero Trust organization.
  full_title: Create a Zero Trust organization · Cloudflare Learning Paths
  head_html: <title>Create a Zero Trust organization · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Set up a Zero Trust organization."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/index.md"><meta property="og:title" content="Create a Zero Trust organization · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up a Zero Trust organization."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Access,Cloudflare Tunnel,Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/#page","headline":"Create a Zero Trust organization \u00b7 Cloudflare Learning Paths","description":"Set up a Zero Trust organization.","url":"https://developers.cloudflare.com/learning-paths/clientless-access/initial-setup/create-zero-trust-org/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/clientless-access/initial-setup/create-zero-trust-org/
  schema: 1
---
<p>To start using Zero Trust features, create a Zero Trust organization in your Cloudflare account.</p>
<h2 id="sign-up-for-zero-trust">Sign up for Zero Trust</h2>
<p>To create a Zero Trust organization:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong>.</p>
</li>
<li>
<p>On the onboarding screen, choose a <span class="nb-glossary-tooltip" title="team name">team name</span>. The team name is a unique, internal identifier for your Zero Trust organization. Users will enter this team name when they enroll their device manually, and it will be the subdomain for your App Launcher (as relevant). Your business name is the typical entry.</p>
<p>You can find your team name in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Zero Trust</strong> &gt; <strong>Settings</strong>.</p>
</li>
<li>
<p>Complete your onboarding by selecting a subscription plan and entering your payment details. If you chose the <strong>Zero Trust Free plan</strong>, this step is still needed but you will not be charged.</p>
</li>
</ol>
<p>When you create your organization, Cloudflare automatically adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method, so your users can sign in with their Cloudflare account credentials right away. You can add a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a> or connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> at any time.</p>
<h2 id="optional-manage-zero-trust-in-terraform">(Optional) Manage Zero Trust in Terraform</h2>
<p>You can use the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest">Cloudflare Terraform provider</a> to manage your Zero Trust organization alongside your other IT infrastructure. To get started with Terraform, refer to our <a href="/terraform/tutorial/">Terraform tutorial series</a>.</p>
<p>To add Zero Trust to your Terraform configuration:</p>
<ol>
<li>
<p><a href="#sign-up-for-zero-trust">Sign up for Zero Trust</a> on the Cloudflare dashboard.</p>
</li>
<li>
<p>Add the following permission to your <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token"><code>cloudflare_api_token</code></a>:</p>
<ul>
<li><code>Access: Organizations, Identity Providers, and Groups Write</code></li>
</ul>
</li>
<li>
<p>Add the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_organization"><code>cloudflare_zero_trust_organization</code></a> resource:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-terraform">resource &quot;cloudflare_zero_trust_organization&quot; &quot;&lt;your-team-name&gt;&quot; {&#10;	account_id                         = var.cloudflare_account_id&#10;	name                               = &quot;Acme Corporation&quot;&#10;	auth_domain                        = &quot;&lt;your-team-name&gt;.cloudflareaccess.com&quot;&#10;}&#10;</code></pre>
<p>Replace <code>&lt;your-team-name&gt;</code> with the Zero Trust organization name selected during <a href="#sign-up-for-zero-trust">onboarding</a>. You can also view your team name in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Settings</strong> &gt; <strong>Team name and domain</strong>.</p>
<p>You can now update Zero Trust organization settings using Terraform.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/9666.md")
</aside>
