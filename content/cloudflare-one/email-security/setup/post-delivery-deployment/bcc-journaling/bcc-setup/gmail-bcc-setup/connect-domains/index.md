---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/
  description: Connect your domains in Email Security.
  full_title: Connect your domains · Cloudflare One docs
  head_html: <title>Connect your domains · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect your domains in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/index.md"><meta property="og:title" content="Connect your domains · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect your domains in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/#page","headline":"Connect your domains \u00b7 Cloudflare One docs","description":"Connect your domains in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/
  schema: 1
---
<p>To connect your domains, you will need to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#enable-gmail-bcc-integration">enable your Gmail BCC integration</a>. Once you have enabled your Gmail BCC integration, the Cloudflare dashboard will redirect you to the <strong>Set up Email security</strong> page.</p>
<p>On the <strong>Set up Email security</strong> page:</p>
<ol>
<li><strong>Connect domains</strong>: Select at least one domain. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Add manual domains</strong>: Select <strong>Add domain name</strong> to manually enter additional domains. Then, select <strong>Continue</strong>.</li>
<li>(<strong>Optional</strong>) <strong>Adjust hop count</strong>: Enter the number of <span class="nb-glossary-tooltip" title="Hops">hops</span>. Then, select <strong>Continue</strong>. Configuring the hop count will determine where you want Cloudflare to sit in the email processing chain.</li>
<li>(<strong>Optional</strong>, select <strong>Skip for now</strong> to skip this step) <strong>Move messages</strong>: Refer to <a href="/cloudflare-one/email-security/settings/auto-moves/">Auto-moves</a> to configure auto-moves. Then, select <strong>Continue</strong>.</li>
<li><strong>Select your processing location</strong>: Configure where you want Cloudflare to process your email. <strong>Global</strong> will be the default option. If you choose <strong>Global</strong>, <code>&lt;account tag&gt;@CF-emailsecurity.com</code> will be your regional service address. Once you have chosen your processing location, select <strong>Continue</strong>. Refer to <a href="/cloudflare-one/email-security/reference/regional-processing/">Regional processing</a> to learn more.</li>
<li><strong>Review details</strong>: Review your connected domains and service addresses. Then, select <strong>Go to domains.</strong></li>
</ol>
<p>Your domains are now added successfully.</p>
<p>On the <strong>Domains</strong> page, select the three dots &gt; <strong>View integration</strong>. The dashboard will display your <a href="/cloudflare-one/email-security/settings/domain-management/domain/">domain information</a>.</p>
<p>Under <strong>Source</strong>, the dashboard will display <strong>Google integration</strong>, along with the <strong>Integration name</strong>.</p>
<h2 id="add-additional-domains">Add additional domains</h2>
<p>To add additional domains:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Connect an integration</strong> &gt; <strong>BCC/Journaling</strong> &gt; <strong>Integrate with Google</strong> &gt; <strong>Authorize</strong>.</li>
<li><strong>Connect domains</strong>: Select the domains you want to add, then select <strong>Next</strong>.</li>
<li>(Optional) Select <strong>Add manual domains</strong>: Enter additional domains manually, then select <strong>Next</strong>.</li>
<li>(Optional) Select <strong>Adjust hop count</strong>: Enter the number of <span class="nb-glossary-tooltip" title="Hops">hops</span>.</li>
<li><strong>Review details</strong>: Review your selected domains, then use the following email to configure the service address with your third-party email provider:</li>
</ol>
<pre tabindex="0"><code class="language-txt">&lt;account tag&gt;@CF-emailsecurity.com&#10;</code></pre>
<ol start="7">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="verify-successful-deployment">Verify successful deployment</h2>
<p>To verify that the deployment has been successful and that your emails are being scanned:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Under <strong>Your domains</strong>, locate your domain, and verify that <strong>Status</strong> (which describes the state of the configuration) displays <strong>Active</strong>.</li>
</ol>
