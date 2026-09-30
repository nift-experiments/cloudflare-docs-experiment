---
cp9:
  canonical: https://developers.cloudflare.com/notifications/get-started/configure-webhooks/
  description: Send notifications to webhook endpoints.
  full_title: Configure webhooks · Cloudflare Notifications docs
  head_html: <title>Configure webhooks · Cloudflare Notifications docs</title><meta name="generator" content="Nift"><meta name="description" content="Send notifications to webhook endpoints."><link rel="canonical" href="https://developers.cloudflare.com/notifications/get-started/configure-webhooks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/notifications/get-started/configure-webhooks/index.md"><meta property="og:title" content="Configure webhooks · Cloudflare Notifications docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send notifications to webhook endpoints."><meta property="og:url" content="https://developers.cloudflare.com/notifications/get-started/configure-webhooks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Notifications"><meta name="algolia_product_filter" content="Notifications"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Notifications"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/notifications/get-started/configure-webhooks/#page","headline":"Configure webhooks \u00b7 Cloudflare Notifications docs","description":"Send notifications to webhook endpoints.","url":"https://developers.cloudflare.com/notifications/get-started/configure-webhooks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /notifications/get-started/configure-webhooks/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10854.md")
</aside>
<p>There are a variety of services you can connect to Cloudflare using webhooks to receive notifications from your Cloudflare account. Refer to the table below to learn how to connect your Cloudflare account to <a href="#popular-webhook-services">popular webhook services</a>.</p>
<h2 id="configure-webhooks">Configure webhooks</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Destinations</strong>.</li>
<li>In the <strong>Webhooks</strong> card, select <strong>Create</strong>.</li>
<li>Give your webhook a name to use for identification later.</li>
<li>In the <strong>URL</strong> field, enter the URL of the third-party service that you have previously set up and want to connect to your Cloudflare account.</li>
<li>If needed, insert the <strong>Secret</strong>. Secrets are how webhooks are encrypted and vary according to the service you are connecting to Cloudflare.</li>
<li>Select <strong>Save and Test</strong> to finish setting up your webhook.</li>
</ol>
<p>The new webhook will appear in the <strong>Webhooks</strong> card.</p>
<h2 id="edit-webhooks">Edit webhooks</h2>
<p>You can only edit the name of webhooks and/or delete them.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Destinations</strong>.</li>
<li>In the <strong>Webhooks</strong> card, select <strong>Edit</strong> on the webhook that you want to edit.</li>
<li>Update the webhook's name and select <strong>Save</strong>.</li>
</ol>
<p>You can delete a webhook after selecting <strong>Edit</strong> or by selecting <strong>Delete</strong> in the list of webhooks displayed in the <strong>Destinations</strong> card.</p>
<h2 id="firewall-settings">Firewall settings</h2>
<p>Webhook notifications are sent from <a href="https://www.cloudflare.com/ips/">Cloudflare's IP ranges</a>. If your webhook endpoint is protected by a firewall, you must allowlist these IP addresses to receive notifications.</p>
<p>To programmatically retrieve the current list of Cloudflare IP addresses, use the <a href="/api/resources/cloudflare_ips/methods/list/">Cloudflare API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10853.md")
</aside>
<h2 id="generic-webhooks">Generic webhooks</h2>
<p>If you use a service that is not covered by Cloudflare's currently available webhooks, you can <a href="#configure-webhooks">configure your own</a>, and enter a valid webhook URL.</p>
<p>It is always recommended to use a secret for generic webhooks. Cloudflare will send your secret in the <code>cf-webhook-auth</code> header of every request made. If this header is not present, or is not your specified value, you should reject the webhook.</p>
<p>After selecting <strong>Save and Test</strong>, your webhook should now be configured as a destination that you can use to attach to policies.</p>
<p>When Cloudflare sends you a webhook, it will have the following schema:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;text&quot;: &quot;Hello World! This is a test message sent from https://cloudflare.com. If you can see this, your webhook is configured properly.&quot;&#10;}&#10;</code></pre>
<p>For the full payload structure and examples for different alert types, refer to the <a href="/notifications/reference/webhook-payload-schema/">webhook payload schema reference</a>.</p>
<h3 id="limitations-of-generic-webhooks">Limitations of generic webhooks</h3>
<p>Cloudflare generic webhook notifications will only be dispatched to a publicly resolvable IP address on port 80 or 443.</p>
<p>If you want to receive the generic webhook notification on a private IP address or different port, you can either receive and forward the notification using <a href="/workers/">Workers</a> or set up a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> to route to your connected application.</p>
<h3 id="use-generic-webhooks-with-workers">Use generic webhooks with Workers</h3>
<p>You can use Cloudflare Workers with a generic webhook to deliver notifications to any service that accepts webhooks.</p>
<p>Cloudflare has an <a href="https://github.com/cloudflare/cf-webhook-relay/">example tool</a> to help you understand how you can use <a href="/workers/">Workers</a> and generic webhooks. The example provided transforms a generic webhook response in order for it to be delivered to Rocket.Chat. The code provided is heavily commented to guide you in the process of adapting the example to your needs.</p>
<h2 id="popular-webhook-services">Popular webhook services</h2>
<h3 id="google-chat">Google Chat</h3>
<p>For <a href="https://developers.google.com/chat/how-tos/webhooks">Google Chat</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is part of the URL. Cloudflare parses this information automatically and there is no input needed from the user.</li>
<li><strong>URL</strong>: URL varies depending on the Google Chat channel's address.</li>
</ul>
<h3 id="slack">Slack</h3>
<p>For <a href="https://api.slack.com/messaging/webhooks">Slack</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is part of the URL. Cloudflare parses this information automatically and there is no input needed from the user.</li>
<li><strong>URL</strong>: URL varies depending on the Slack channel's address.</li>
</ul>
<h3 id="datadog">DataDog</h3>
<p>For <a href="https://docs.datadoghq.com/api/latest/events/#post-an-event">DataDog</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is required and has to be entered by the user. This is what DataDog refers to as <a href="https://app.datadoghq.com/account/settings#api">API Key</a></li>
<li><strong>URL</strong>: <code>https://api.datadoghq.com/api/v1/events</code></li>
</ul>
<h3 id="discord">Discord</h3>
<p>For <a href="https://discord.com/developers/docs/resources/webhook#execute-webhook">Discord</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is part of the URL. Cloudflare parses this information automatically and there is no input needed from the user.</li>
<li><strong>URL</strong>: URL varies depending on the Discord channel's address.</li>
</ul>
<h3 id="opsgenie">OpsGenie</h3>
<p>For <a href="https://support.atlassian.com/opsgenie/docs/create-a-default-api-integration">OpsGenie</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is the <code>API Key</code> for OpsGenie's REST API.</li>
<li><strong>URL</strong>: <code>https://api.opsgenie.com/v2/alerts</code></li>
</ul>
<h3 id="splunk">Splunk</h3>
<p>For <a href="https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector">Splunk</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is required and has to be entered by the user. This is what Splunk refers to as <code>token</code>. Refer to <a href="https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#How_the_Splunk_platform_uses_HTTP_Event_Collector_tokens_to_get_data_in">Splunk’s documentation</a> for details.</li>
<li><strong>URL</strong>:
<ol>
<li>We only support three Splunk endpoints: services/collector, services/collector/raw, and services/collector/event.</li>
<li>If SSL is enabled on the token, the port must be 443. If SSL is not enabled on the token, the port must be 8088.</li>
<li>SSL must be enabled on the server.</li>
<li><strong>Enable indexer acknowledgement</strong> must be disabled on the Splunk HTTP Event Collector.</li>
</ol>
</li>
</ul>
<h3 id="feishu">Feishu</h3>
<p>For <a href="https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot">Feishu</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is part of the URL. Cloudflare parses this information automatically and there is no input needed from the user.</li>
<li><strong>URL</strong>: The URL varies depending on the Custom Robot.</li>
</ul>
<h3 id="teams">Teams</h3>
<p>For <a href="https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook">Teams</a>:</p>
<ul>
<li><strong>Secret</strong>: The secret is part of the URL. Cloudflare parses this information automatically and there is no input needed from the user.</li>
<li><strong>URL</strong>: URL is provided by Teams when the Incoming Webhook connector is created.</li>
</ul>
<h3 id="servicenow">ServiceNow</h3>
<p>For <a href="https://docs.servicenow.com/bundle/tokyo-application-development/page/administer/integrationhub-store-spokes/task/govnotify-wbhk.html">ServiceNow</a>:</p>
<ul>
<li><strong>Secret</strong>: User decides. Ensure that the secret entered in Cloudflare Notifications matches with ServiceNow. Refer to <a href="https://docs.servicenow.com/bundle/washingtondc-integrate-applications/page/administer/integrationhub/concept/rest-trigger.html">ServiceNow's documentation</a> for details.</li>
<li><strong>URL</strong>: <code>https://{servicenow_instance}.com/{base_api_path}</code></li>
</ul>
<h3 id="generic-webhook">Generic webhook</h3>
<p>For a Generic webhook:</p>
<ul>
<li><strong>Secret</strong>: User decides.</li>
<li><strong>URL</strong>: User decides.</li>
</ul>
<h3 id="configuration-of-secrets">Configuration of secrets</h3>
<p>When creating a Google Chat, Slack, Discord, or Feishu webhook, the secret is part of the URL. You can choose to remove the secret from the URL and explicitly set the value of <code>secret</code> rather than letting Cloudflare automatically extract it.</p>
<p>This can be useful when defining your webhook infrastructure as code using Terraform since the URL will not be modified by Cloudflare.</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_notification_policy_webhooks&quot; &quot;example&quot; {&#10;  account_id = &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  name       = &quot;Slack Webhook&quot;&#10;  url        = &quot;https://hooks.slack.com/services/T00000000/B00000000&quot;&#10;  secret     = &quot;&lt;secret&gt;&quot;&#10;}&#10;</code></pre>
