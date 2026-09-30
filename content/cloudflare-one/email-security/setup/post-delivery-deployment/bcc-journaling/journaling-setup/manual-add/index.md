---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/
  description: Manually add domains for BCC or journaling email scanning.
  full_title: Manually add domains · Cloudflare One docs
  head_html: <title>Manually add domains · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Manually add domains for BCC or journaling email scanning."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/index.md"><meta property="og:title" content="Manually add domains · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manually add domains for BCC or journaling email scanning."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/#page","headline":"Manually add domains \u00b7 Cloudflare One docs","description":"Manually add domains for BCC or journaling email scanning.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/manual-add/
  schema: 1
---
<p>This page will teach you how to manually add domains via BCC/Journaling on the Cloudflare dashboard.</p>
<p>This setup is ideal if your email provider is not Microsoft 365 or Google Workspace, or you do not want to directly integrate your account. Beware that manually add does not support <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> or <a href="/cloudflare-one/email-security/directories/">directory synchronization</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Email security, you will need to have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a></li>
<li>A domain to protect</li>
</ul>
<h2 id="manually-add-domains">Manually add domains</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Select <strong>Overview</strong>. If you have not purchased Email security, select <strong>Contact Sales</strong>. Otherwise, select <strong>Set up</strong> &gt; <strong>BCC/Journaling</strong>.</li>
<li>Select <strong>Manual add</strong>.</li>
</ol>
<h2 id="users-with-domains-on-cloudflare">Users with domains on Cloudflare</h2>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <span class="nb-glossary-tooltip" title="Hops">hops</span>, and then select <strong>Continue</strong>.</li>
<li><strong>Select your processing location</strong>: Configure where you want Cloudflare to process your email. <strong>Global</strong> will be the default option. If you choose <strong>Global</strong>, <code>&lt;account tag&gt;@CF-emailsecurity.com</code> will be your regional service address. Once you have chosen your processing location, select <strong>Continue</strong>.</li>
<li><strong>Review details</strong>: Review your connected domains and regional service address. Then, select <strong>Go to domains.</strong></li>
</ol>
<h2 id="users-who-do-not-have-domains-with-cloudflare">Users who do not have domains with Cloudflare</h2>
<p>If you do not have domains with Cloudflare, the Cloudflare dashboard will display two options:</p>
<ul>
<li>Add a domain to Cloudflare.</li>
<li>Enter domain manually.</li>
</ul>
<h3 id="add-a-domain-to-cloudflare">Add a domain to Cloudflare</h3>
<p>Selecting <strong>Add a domain to Cloudflare</strong> will redirect you to a new page where you will connect your domain to Cloudflare. Once you have entered an existing domain, select <strong>Continue</strong>.</p>
<h3 id="enter-domain-manually">Enter domain manually</h3>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <span class="nb-glossary-tooltip" title="Hops">hops</span>, and then select <strong>Continue</strong>.</li>
<li><strong>Configure service address with your third party email provider</strong>: Copy and paste the service address into your third-party email provider to allow BCC/Journaling: <code>&lt;account tag&gt;@CF-emailsecurity.com</code>.</li>
<li><strong>Review details</strong>: Review your connected domains. Then, select <strong>Go to domains.</strong></li>
</ol>
<h2 id="enable-auto-moves">Enable auto-moves</h2>
<p>To enable auto-move events, you will have to associate an integration.</p>
<p>To associate an integration:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong> &gt; Select <strong>View</strong>.</li>
<li>On the <strong>Domain management</strong> page, locate your domain, select the three dots, then select <strong>Associate an integration</strong>.</li>
<li>Select <strong>Connect an integration</strong>. Follow the steps to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">enable the Microsoft 365 integration</a>.</li>
<li>Select the three dots, then select <strong>Associate an integration</strong>. Select the integration, then select <strong>Associate</strong>.</li>
</ol>
<p>Now that your domain has an associated integration, enable <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move events</a> on your domain.</p>
