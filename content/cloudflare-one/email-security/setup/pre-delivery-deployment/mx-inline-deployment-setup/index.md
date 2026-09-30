---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/
  description: How Set up MX/Inline deployment works in Email Security.
  full_title: Set up MX/Inline deployment · Cloudflare One docs
  head_html: <title>Set up MX/Inline deployment · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Set up MX/Inline deployment works in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/index.md"><meta property="og:title" content="Set up MX/Inline deployment · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Set up MX/Inline deployment works in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#page","headline":"Set up MX/Inline deployment \u00b7 Cloudflare One docs","description":"How Set up MX/Inline deployment works in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/
  schema: 1
---
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Email security, you will need to have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a></li>
<li>A domain to protect</li>
</ul>
<h2 id="initiate-mx-inline-configuration">Initiate MX/Inline configuration</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Overview</strong>. Select one of the following options:</li>
</ol>
<ul>
<li>If you have not purchased Email security, select <strong>Contact sales</strong>.</li>
<li>If you have not associated any integration, <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#associate-an-integration">associate an integration</a>, then select <strong>Set up</strong>.</li>
<li>If you have associated an integration, but have not connected a domain, select <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#connect-a-domain"><strong>Connect a domain</strong></a>.</li>
</ul>
<ol start="4">
<li>Select <strong>MX/Inline</strong>.</li>
<li>To start the MX/Inline configuration, you will need to have completed the prerequisite setup on your email provider's platform. Once you have completed this step, select <strong>I confirm that I have completed all the necessary requirements</strong>. Then, select <strong>Start configuration</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4944.md")
</aside>
<h2 id="associate-an-integration">Associate an integration</h2>
<p>MX/Inline does not require an integration for protection to be effective. However, it is a best practice to connect an integration.</p>
<p>To associate an integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Cloud &amp; SaaS Integrations</strong> &gt; <strong>Integrations</strong></li>
<li>Select <strong>Connect an integration</strong>.</li>
<li>Select an application: Choose between <strong>Google Workspace CASB + EMAIL</strong>, or <strong>Microsoft CASB + EMAIL</strong>.
<ul>
<li>Refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#1-create-a-service-account-in-your-gcp-project">Enable Gmail BCC integration</a> if you select <strong>Google Workspace CASB + EMAIL</strong>.</li>
<li>Refer to <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/#enable-microsoft-integration">Enable Microsoft integration</a> if you select <strong>Microsoft CASB + EMAIL</strong>.</li>
</ul>
</li>
<li>After you have associated an integration, go to <strong>Email security</strong> &gt; <strong>Set up</strong>.</li>
<li>Follow the instructions to <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#connect-a-domain">connect a domain</a>.</li>
</ol>
<h2 id="connect-a-domain">Connect a domain</h2>
<p>If you have verified zones on Cloudflare, continue with the following steps:</p>
<ol>
<li><strong>Connect a domain</strong>: Select your domain. Then, select <strong>Continue</strong>.</li>
<li><strong>Select position</strong>: This step allows you to choose where Email security fits into your mail flow and configure position settings:
<ul>
<li><strong>Select position</strong>: Choose between:
<ul>
<li><strong>Sit first (hop count = 1)</strong>: Email security is the first server that receives the email. There are no other email scanners or services between the Internet and Cloudflare.</li>
<li><strong>Sit in the middle (hop count &gt; 1)</strong>: Email security sits anywhere other than the first position. Other servers receive emails <em>before</em> Email security. There are other email scanners or email services in between.</li>
</ul>
</li>
<li><strong>Position settings</strong>: Refine how Email security receives and forwards emails:
<ul>
<li><strong>Forwarding address</strong>: This is your mail flow next hop after Email security. This value is auto-filled, but you can still change it.</li>
<li><strong>Outbound TLS</strong>: Choose between:
<ol>
<li><strong>Forward all messages over TLS</strong> (recommended).</li>
<li><strong>Forward all messages using opportunistic TLS</strong>.</li>
</ol>
</li>
</ul>
</li>
<li>Select <strong>Continue</strong>.</li>
</ul>
</li>
<li>(<strong>Optional</strong>, select <strong>Skip for now</strong> to skip this step) <strong>Configure quarantine policy</strong>: Select dispositions to automatically prevent certain types of incoming messages from reaching a recipient's inbox.</li>
<li>(Optional) <strong>Update MX records</strong>:
<ul>
<li>Email security can automatically update MX records for domains that proxy traffic through Cloudflare. Under <strong>Your mail processing location</strong>, select your mail processing location. You can refer to <a href="/cloudflare-one/email-security/reference/regional-processing/">Regional processing</a> for more information.</li>
<li>You can also choose to allow Cloudflare to update MX records by selecting <strong>I confirm that I allow Cloudflare to update to the new MX records</strong>. When Email security updates MX records, we replace your original MX records with Email security MX records.</li>
<li>Select <strong>Continue</strong>.</li>
</ul>
</li>
<li><strong>Review details</strong>: Review your domain, then select <strong>Go to domains</strong>.</li>
</ol>
<h2 id="users-who-do-not-have-domains-with-cloudflare">Users who do not have domains with Cloudflare</h2>
<p>If you do not have domains with Cloudflare, the dashboard will display two options:</p>
<ul>
<li><a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#enter-domain-manually">Enter domain manually</a>.</li>
<li><a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#add-a-domain-to-cloudflare">Add a domain to Cloudflare</a>.</li>
</ul>
<h2 id="enter-domain-manually">Enter domain manually</h2>
<ol>
<li><strong>Add domains</strong>: Manually enter domain names.</li>
<li><strong>Review all domains</strong>: Review all your domains, then select <strong>Continue</strong>.</li>
<li><strong>Verify your domains</strong>: It may take up to 24 hours for your domains to be verified. Select <strong>Done</strong>.</li>
<li>Once your domains have been verified, the dashboard will display a message like this: <strong>You have verified domains ready to connect to Email security</strong>. This means that you can now set up Email security via MX/Inline.</li>
<li>Select <strong>Set up</strong>, then select <strong>MX/Inline</strong>.</li>
<li>Follow the steps to <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/#initiate-mxinline-configuration">initiate MX/Inline configuration</a>.</li>
</ol>
<h3 id="add-a-domain-to-cloudflare">Add a domain to Cloudflare</h3>
<p>Selecting <strong>Add a domain to Cloudflare</strong> will redirect you to a new page where you will connect your domain to Cloudflare. Once you have entered an existing domain, select <strong>Continue</strong>.</p>
<p>Then, follow the steps to <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/">Set up MX/Inline</a>.</p>
<h2 id="verify-successful-deployment">Verify successful deployment</h2>
<p>To verify that the deployment has been successful and that your emails are being scanned:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, select <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Under <strong>Your domains</strong>, locate your domain, and verify that <strong>Status</strong> (which describes the state of the configuration) displays <strong>Active</strong>.</li>
</ol>
