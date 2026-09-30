---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/
  description: Yandex in Zero Trust integrations.
  full_title: Yandex · Cloudflare One docs
  head_html: <title>Yandex · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Yandex in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/index.md"><meta property="og:title" content="Yandex · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Yandex in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/#page","headline":"Yandex \u00b7 Cloudflare One docs","description":"Yandex in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/yandex/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SSO"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/yandex/
  schema: 1
---
<p>Yandex is a web search engine that also offers identity provider (IdP) services.</p>
<h2 id="set-up-yandex">Set up Yandex</h2>
<p>To set up Yandex for Cloudflare Access:</p>
<ol>
<li>
<p>Log in to your Yandex account.</p>
</li>
<li>
<p>Select <strong>Open a new OAuth Application</strong>.</p>
</li>
<li>
<p>Select <strong>New client</strong>.</p>
</li>
<li>
<p>Complete the required fields.</p>
</li>
<li>
<p>Choose <strong>Yandex.Passport API</strong> to set the basic scopes.</p>
</li>
<li>
<p>Select the <strong>Access to email address</strong>, <strong>Access to user avatar,</strong> and <strong>Access to username, first name and surname, gender</strong> options.</p>
</li>
<li>
<p>Select <strong>Platform</strong> and select <strong>Web Services.</strong></p>
</li>
<li>
<p>In the <strong>Callback URL #1</strong> field, enter the following URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/yandex/yandex-3.png" alt="Yandex Platform interface with Web services checked and callback URI in open form field" /></p>
<ol start="9">
<li>
<p>Select <strong>Add</strong>.</p>
</li>
<li>
<p>Scroll to the <strong>Platforms</strong> card, and select <strong>Submit</strong>.</p>
<p><strong>Yandex OAuth</strong> card titled <strong>Cloudflare Access App</strong> displays.</p>
</li>
<li>
<p>Copy the <strong>ID</strong> and <strong>Password</strong>.</p>
</li>
<li>
<p>In Cloudflare One, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select Yandex.</p>
</li>
<li>
<p>Paste the ID and password in the appropriate fields.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="example-api-config">Example API Config</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;yandex&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
