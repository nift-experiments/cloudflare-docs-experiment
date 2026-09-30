---
cp9:
  canonical: https://developers.cloudflare.com/agents/communication-channels/email/
  description: Connect agents to email so they can send outbound messages, process inbound mail, and handle follow-up replies.
  full_title: Email · Cloudflare Agents docs
  head_html: <title>Email · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect agents to email so they can send outbound messages, process inbound mail, and handle follow-up replies."><link rel="canonical" href="https://developers.cloudflare.com/agents/communication-channels/email/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/communication-channels/email/index.md"><meta property="og:title" content="Email · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect agents to email so they can send outbound messages, process inbound mail, and handle follow-up replies."><meta property="og:url" content="https://developers.cloudflare.com/agents/communication-channels/email/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/communication-channels/email/#page","headline":"Email \u00b7 Cloudflare Agents docs","description":"Connect agents to email so they can send outbound messages, process inbound mail, and handle follow-up replies.","url":"https://developers.cloudflare.com/agents/communication-channels/email/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/communication-channels/email/
  schema: 1
---
<p>Email is a communication channel for agents that need to interact with users or systems through inboxes instead of chat UIs. Agents can send outbound email, receive inbound email, route replies back to an existing session, and use email content as part of an agent workflow.</p>
<p>Use email when you want an agent to:</p>
<ul>
<li>Send notifications, summaries, receipts, or follow-up messages.</li>
<li>Process inbound messages through <a href="/email-service/">Cloudflare Email Service</a>.</li>
<li>Continue a conversation from a reply.</li>
<li>Route support, sales, or operational workflows through an agent.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Outbound email uses a <code>send_email</code> binding in your Worker. Inbound email uses an Email Service routing rule that sends messages to your Worker, where the agent can parse the sender, recipients, headers, and body before deciding how to respond.</p>
<p>For reply handling, include a stable identifier in the reply address, message metadata, or headers so the Worker can route follow-up messages to the right agent instance.</p>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Implement <code>onEmail()</code> to handle inbound email, and use <code>sendEmail()</code> or <code>replyToEmail()</code> when the agent needs to send a response.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1982.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>Add a <code>send_email</code> binding for outbound email, then configure an Email Service routing rule to send inbound mail to your Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1983.md")
</div>
<p>The <code>remote = true</code> option lets you call the real Email Service API during local development with <code>wrangler dev</code>.</p>
<h2 id="build-an-email-agent">Build an email agent</h2>
<p>For a complete walkthrough, including domain setup, bindings, inbound routing, and secure replies, use the email agent example.</p>
<div class="nb-card nb-link-card"><h3 id="card-email-agent-agents-examples-email-agent"><a href="/agents/examples/email-agent/">Email agent</a></h3><p>Build an agent that sends, receives, routes, and replies to email using Cloudflare Email Service and the Agents SDK.</p></div>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-email-service-email-service"><a href="/email-service/">Email Service</a></h3><p>Route, receive, and send email with Cloudflare Email Service.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-send-email-from-workers-email-service-api-send-emails-workers-api"><a href="/email-service/api/send-emails/workers-api/">Send email from Workers</a></h3><p>Use the Workers API to send outbound email.</p></div>
