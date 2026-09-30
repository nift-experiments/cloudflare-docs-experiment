---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/
  description: Configure CASB webhooks to send posture finding instances from Cloudflare One to external HTTPS endpoints.
  full_title: Webhooks · Cloudflare One docs
  head_html: <title>Webhooks · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure CASB webhooks to send posture finding instances from Cloudflare One to external HTTPS endpoints."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/index.md"><meta property="og:title" content="Webhooks · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure CASB webhooks to send posture finding instances from Cloudflare One to external HTTPS endpoints."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/#page","headline":"Webhooks \u00b7 Cloudflare One docs","description":"Configure CASB webhooks to send posture finding instances from Cloudflare One to external HTTPS endpoints.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/cloud-and-saas/webhooks/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/5089.md")
</aside>
<p>Use CASB webhooks to send posture finding instances from Cloudflare One to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.</p>
<p>After you configure a webhook destination, you can test delivery from the <strong>Webhooks</strong> page and send posture finding instances directly from the finding details workflow.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You have access to Cloudflare One.</li>
<li>You have a public HTTPS endpoint that can receive <code>POST</code> requests.</li>
<li>You have any authentication values required by your destination, such as a bearer token, Basic auth credentials, static headers, or an HMAC signing secret.</li>
</ul>
<h2 id="create-a-webhook">Create a webhook</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Webhooks</strong>.</li>
<li>Select <strong>Create webhook</strong>.</li>
<li>Enter a <strong>Name</strong> for the webhook.</li>
<li>Enter the <strong>Destination URL</strong> for the system that will receive webhook requests.</li>
<li>Choose an <strong>Authentication method</strong>.</li>
<li>Enter the required credentials, headers, or signing secret.</li>
<li>(Optional) Select <strong>Test delivery</strong> to validate the destination before saving.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Cloudflare only accepts destination URLs that use <code>https://</code> and are publicly reachable. URLs that resolve to localhost, loopback, private, or other reserved addresses are rejected.</p>
<h2 id="authentication-methods">Authentication methods</h2>
<p>CASB webhooks support the following authentication methods:</p>
<ul>
<li><strong>None</strong>: Use this option if your destination does not require authentication.</li>
<li><strong>Basic Auth</strong>: Use this option when your destination expects HTTP Basic authentication.</li>
<li><strong>Bearer Auth</strong>: Use this option when your destination expects a bearer token.</li>
<li><strong>Static Headers</strong>: Use this option when your destination requires one or more fixed custom headers. Header names must be unique.</li>
<li><strong>HMAC-Signing</strong>: Use this option when your destination validates signed requests. You must provide a signing secret.</li>
</ul>
<h2 id="test-delivery">Test delivery</h2>
<p>Use <strong>Test delivery</strong> to send a test request to the configured destination before saving a new webhook or after updating an existing webhook.</p>
<p>A successful test indicates that Cloudflare reached the destination URL and that the destination returned a response.</p>
<p>Test delivery does not send a live finding instance from your environment.</p>
<h2 id="edit-turn-off-or-delete-a-webhook">Edit, turn off, or delete a webhook</h2>
<p>To update an existing webhook:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Integrations</strong> &gt; <strong>Webhooks</strong>.</li>
<li>Select the webhook you want to update.</li>
<li>Modify the webhook configuration.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To turn a webhook off or on, use the status toggle on the <strong>Webhooks</strong> page.</p>
<p>To delete a webhook, open the webhook menu and select <strong>Delete</strong>.</p>
<p>When you edit an existing webhook, Cloudflare does not display saved header values or signing secrets. To replace a stored value, enter a new value and save the webhook again.</p>
<h2 id="send-a-posture-finding-instance-to-a-webhook">Send a posture finding instance to a webhook</h2>
<p>After you configure one or more webhook destinations, you can send posture finding instances directly from the findings workflow.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Choose <strong>SaaS</strong> or <strong>Cloud</strong>.</li>
<li>Choose the finding you want to review, then select <strong>Manage</strong>.</li>
<li>Select an instance.</li>
<li>In the instance details panel, select <strong>Send webhook</strong>.</li>
<li>Choose the webhook destination or destinations you want to use.</li>
<li>Select <strong>Send webhooks</strong>.</li>
</ol>
<p>Cloudflare queues webhook sends in the background. A success message means that Cloudflare accepted the request for delivery.</p>
<p>For more information on finding workflows, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">Manage findings</a>.</p>
<p>To automatically send a webhook for matching findings without sending each one manually, refer to <a href="/cloudflare-one/cloud-and-saas-findings/policies/">Remediation Policies</a>.</p>
<h2 id="payload-format">Payload format</h2>
<p>CASB sends a JSON payload that describes the posture finding instance.</p>
<p>Webhook payloads include event metadata, finding details, asset details, and any additional metadata associated with the finding instance. The exact contents vary by integration and finding type.</p>
<p>Webhook payloads include a top-level <code>id</code>, <code>type</code>, <code>metadata</code>, and <code>data</code> object.</p>
<p>Depending on the finding, the <code>metadata</code> object can include event details such as the actor, destination, send time, and payload version.</p>
<p>The <code>data</code> object can include finding details, asset details, and additional metadata associated with the finding instance.</p>
<p>If your downstream system expects a custom schema, send the webhook to an intermediary service or workflow engine that transforms the payload before forwarding it to the final destination.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>CASB webhooks support posture finding instances only.</li>
<li>CASB webhooks do not send content findings.</li>
<li>Test delivery sends a test request, but does not send a live finding instance.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If a webhook test or delivery fails:</p>
<ul>
<li>Verify that the destination URL uses <code>https://</code>.</li>
<li>Verify that the destination is publicly reachable.</li>
<li>Confirm that your authentication values, headers, and signing secret are correct.</li>
<li>If the dashboard reports success but the destination does not process the event immediately, remember that finding instance sends are queued in the background.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/integrations/cloud-and-saas/troubleshooting/casb/">CASB troubleshooting</a>.</p>
