---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/
  description: GitHub in Zero Trust integrations.
  full_title: GitHub · Cloudflare One docs
  head_html: <title>GitHub · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="GitHub in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/index.md"><meta property="og:title" content="GitHub · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="GitHub in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="GitHub"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/#page","headline":"GitHub \u00b7 Cloudflare One docs","description":"GitHub in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/github/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GitHub"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/github/
  schema: 1
---
<p>Cloudflare One allows your team to connect to your applications using their GitHub login. You do not need to have a GitHub organization to use the integration.</p>
<h2 id="set-up-github-access">Set up GitHub Access</h2>
<p>To configure GitHub access in both GitHub and Cloudflare One:</p>
<ol>
<li>
<p>Log in to <a href="https://github.com/">GitHub</a>.</p>
</li>
<li>
<p>Go to your account &gt; <strong>Settings</strong> &gt; <strong>Developer Settings</strong>.</p>
</li>
<li>
<p>In <strong>Developer Settings</strong>, select <strong>OAuth Apps</strong> and select <strong>New OAuth app</strong>.</p>
</li>
<li>
<p>On the <strong>Register a new OAuth application</strong> page, enter an <strong>Application name</strong>. Your users will see this application name on the login page.</p>
</li>
<li>
<p>In the <strong>Homepage URL</strong> field, enter your team domain:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="6">
<li>In the GitHub <strong>Authorization callback URL</strong> field, enter the following URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="7">
<li>
<p>Select <strong>Register application</strong>.</p>
</li>
<li>
<p>Make note of the <strong>Client ID</strong>.</p>
</li>
<li>
<p>Select <strong>Generate a new client secret</strong> and copy the client secret to a safe place.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new identity provider</strong> and select <strong>GitHub</strong>.</p>
</li>
<li>
<p>In <strong>App ID</strong>, enter the <strong>Client ID</strong> obtained from GitHub (refer to step 8).</p>
</li>
<li>
<p>In <strong>Client secret</strong>, enter the <strong>Client secret</strong> obtained from GitHub (refer to step 9).</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Finish setup</strong> to launch a GitHub authorization page. You will be asked to grant the following permissions to Cloudflare Access:</p>
<ul>
<li>Organizations and teams (read-only)</li>
<li>Email addresses (read-only)</li>
</ul>
</li>
<li>
<p>Select <strong>Authorize</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> &gt; <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to your GitHub login method. If you have GitHub two-factor authentication enabled, you will need to first login to GitHub directly and return to Access.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshooting-organization-policies">Troubleshooting organization policies</h3>
@markup("md", "content/.markup/bodies/5058.md")
</aside>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;github&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
