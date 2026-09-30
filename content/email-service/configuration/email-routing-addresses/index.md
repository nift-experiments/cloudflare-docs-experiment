---
cp9:
  canonical: https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/
  description: Create and manage routing rules, destination addresses, and the catch-all rule in Email Service.
  full_title: Email routing rules and addresses · Cloudflare Email Service docs
  head_html: <title>Email routing rules and addresses · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage routing rules, destination addresses, and the catch-all rule in Email Service."><link rel="canonical" href="https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/index.md"><meta property="og:title" content="Email routing rules and addresses · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage routing rules, destination addresses, and the catch-all rule in Email Service."><meta property="og:url" content="https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#page","headline":"Email routing rules and addresses \u00b7 Cloudflare Email Service docs","description":"Create and manage routing rules, destination addresses, and the catch-all rule in Email Service.","url":"https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/configuration/email-routing-addresses/
  schema: 1
---
<p>In Email Routing, a routing rule pairs an email pattern with a destination — either a verified email address or a Worker. You can route emails to either:</p>
<ul>
<li>Verified email addresses</li>
<li>Workers with the <code>email</code> handler</li>
</ul>
<p>This allows you to route emails to your preferred inbox, or apply logic with Workers before deciding what should happen to your emails. You can have multiple routing rules to route email from specific senders to specific mailboxes.</p>
<h2 id="destination-addresses">Destination addresses</h2>
<p>A destination address is the verified email address that Email Routing forwards messages to. Before you can create a routing rule, you must add and verify at least one destination address.</p>
<p>Destination addresses are shared at the account level and can be reused with any other domain in your account.</p>
<p>You can also send to verified destination addresses directly through the <a href="/email-service/api/send-emails/rest-api/">REST API</a> or the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a>, free of charge on any plan — including when only Email Routing is configured. Sends to verified destination addresses do not count toward your monthly quota or daily sending limits. Refer to <a href="/email-service/platform/pricing/">Pricing</a> for details.</p>
<h3 id="add-a-destination-address">Add a destination address</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong> &gt; <strong>Destination Addresses</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Under <strong>Destination addresses</strong>, enter the email address you want to use as a destination in the inline form and submit it.</li>
<li>Cloudflare sends a verification email to that address. Open the email and select <strong>Verify email address</strong> to activate it.</li>
</ol>
<p>Until a destination address is verified, any routing rule that points to it stays disabled.</p>
<h3 id="manage-destination-addresses">Manage destination addresses</h3>
<p>The <strong>Destination Addresses</strong> page lists every address on your account, including those pending verification. From this page you can resend a verification email or delete a destination address.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8621.md")
</aside>
<h2 id="routing-rules">Routing rules</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong> &gt; <strong>Routing Rules</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Create routing rule</strong>.</li>
<li>In <strong>Email pattern</strong>, enter the local part of the email address you want to use (for example, <code>my-new-email</code>), and select your domain.</li>
<li>In the <strong>Action</strong> drop-down menu, choose what this routing rule should do. Refer to <a href="#routing-rule-actions">Routing rule actions</a> for more information.</li>
<li>In <strong>Destination</strong>, choose the verified address or Worker you want your emails to be forwarded to — for example, <code>your-name@gmail.com</code>. To add a new destination address, refer to <a href="#add-a-destination-address">Add a destination address</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8620.md")
</aside>
<h3 id="routing-rule-actions">Routing rule actions</h3>
<p>When creating a routing rule, you must specify an <strong>Action</strong>:</p>
<ul>
<li><em>Send to an email</em>: Emails will be routed to your destination address.</li>
<li><em>Send to a Worker</em>: Emails will be processed by the logic in your <a href="/email-service/api/route-emails/email-handler/">Worker</a>.</li>
<li><em>Drop</em>: Deletes emails matching the rule without routing them. This can be useful if you want to make an email address appear valid for privacy reasons.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8619.md")
</aside>
<h3 id="disable-a-routing-rule">Disable a routing rule</h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Routing Rules</strong>.</li>
<li>Identify the routing rule you want to pause, and toggle the status button to <strong>Disabled</strong>.</li>
</ol>
<p>Your routing rule is now disabled. It will not forward emails to a destination address or Worker. To forward emails again, toggle the routing rule status button to <strong>Active</strong>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="renaming-a-worker">Renaming a Worker</h3>
@markup("md", "content/.markup/bodies/8618.md")
</aside>
<h3 id="edit-a-routing-rule">Edit a routing rule</h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Routing Rules</strong>.</li>
<li>Identify the routing rule you want to edit, and select <strong>Edit</strong>.</li>
<li>Make the appropriate changes to the rule.</li>
</ol>
<h3 id="delete-a-routing-rule">Delete a routing rule</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong> &gt; <strong>Routing Rules</strong>.</li>
<li>Identify the routing rule you want to delete.</li>
<li>Select <strong>Delete</strong> and confirm the action.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8617.md")
</aside>
<h3 id="catch-all-rule">Catch-all rule</h3>
<p>When you enable this feature, Email Routing forwards every email sent to your domain, including misspelled local parts, to a single destination. For example, if you created a rule for <code>info@example.com</code> and a sender accidentally types <code>ifno@example.com</code>, the email will still be handled if you have the <strong>Catch-all rule</strong> enabled.</p>
<p>To enable the catch-all rule:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Routing Rules</strong>.</li>
<li>Enable <strong>Catch-all rule</strong>, so it shows as <strong>Active</strong>.</li>
<li>In the <strong>Action</strong> drop-down menu, select what to do with these emails. Refer to <a href="#routing-rule-actions">Routing rule actions</a> for more information.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="subaddressing">Subaddressing</h3>
<p>Email Routing supports subaddressing, also known as plus addressing, as defined in <a href="https://www.rfc-editor.org/rfc/rfc5233">RFC 5233</a>. This enables using the &quot;+&quot; separator to augment your routing rules with arbitrary detail information.</p>
<p>You can enable subaddressing at <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong> &gt; <strong>Settings</strong>.</p>
<p>Once enabled, you can use subaddressing with any of your routing rules. For example, if you send an email to <code>user+detail@example.com</code> it will be matched by the <code>user@example.com</code> routing rule. The <code>+detail</code> part does not affect rule matching, but it is preserved in <code>message.to</code> and can be inspected by a <a href="/email-service/api/route-emails/email-handler/">Worker</a>, an <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">Agent application</a>, or via the activity log.</p>
<p>If a routing rule for <code>user+detail@example.com</code> already exists, it takes precedence over the rule for <code>user@example.com</code>. This prevents breaking existing routing rules and allows certain sub-addresses to be captured by a specific rule.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/route-emails/email-handler/">Email handler</a> — process emails programmatically with the <code>email()</code> handler.</li>
<li><a href="/email-service/platform/email-routing-rest-api/">Email Routing REST API</a> — manage routing rules and destination addresses programmatically.</li>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — manage DNS records for Email Routing.</li>
<li><a href="/email-service/examples/email-routing/">Email routing examples</a> — advanced patterns including spam filtering and email storage.</li>
</ul>
