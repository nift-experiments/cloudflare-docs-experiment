---
cp9:
  canonical: https://developers.cloudflare.com/agents/communication-channels/slack/
  description: Connect agents to Slack workspaces so they can respond to direct messages, mentions, and threaded conversations.
  full_title: Slack · Cloudflare Agents docs
  head_html: <title>Slack · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect agents to Slack workspaces so they can respond to direct messages, mentions, and threaded conversations."><link rel="canonical" href="https://developers.cloudflare.com/agents/communication-channels/slack/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/communication-channels/slack/index.md"><meta property="og:title" content="Slack · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect agents to Slack workspaces so they can respond to direct messages, mentions, and threaded conversations."><meta property="og:url" content="https://developers.cloudflare.com/agents/communication-channels/slack/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/communication-channels/slack/#page","headline":"Slack \u00b7 Cloudflare Agents docs","description":"Connect agents to Slack workspaces so they can respond to direct messages, mentions, and threaded conversations.","url":"https://developers.cloudflare.com/agents/communication-channels/slack/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/communication-channels/slack/
  schema: 1
---
<p>Slack is a communication channel for agents that need to participate in team conversations. A Slack-connected agent can receive events from Slack, route each message to the right agent instance, and respond back to direct messages or channel mentions.</p>
<p>Use Slack when you want an agent to:</p>
<ul>
<li>Respond to direct messages from Slack users.</li>
<li>Reply when mentioned in public channels.</li>
<li>Maintain context inside Slack threads.</li>
<li>Serve multiple Slack workspaces from one deployment.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Slack sends events to your Worker through the <a href="https://api.slack.com/apis/events-api">Slack Events API</a>. Your Worker verifies each request, identifies the installed workspace, and routes the event to an agent instance.</p>
<p>Common Slack events include:</p>
<table>
<thead>
<tr>
<th>Event</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>message.im</code></td>
<td>Direct messages to the bot</td>
</tr>
<tr>
<td><code>app_mention</code></td>
<td>Mentions in channels</td>
</tr>
</tbody>
</table>
<p>For multi-workspace Slack apps, store each workspace installation separately and route events by team or enterprise ID. Each workspace can map to an isolated agent instance with its own Durable Object-backed state.</p>
<h2 id="build-a-slack-agent">Build a Slack agent</h2>
<p>For a complete walkthrough, including Slack app setup, OAuth, event subscriptions, and deployment, use the Slack agent example.</p>
<div class="nb-card nb-link-card"><h3 id="card-slack-agent-agents-examples-slack-agent"><a href="/agents/examples/slack-agent/">Slack agent</a></h3><p>Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK.</p></div>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-slack-events-api-https-api-slack-com-apis-events-api"><a href="https://api.slack.com/apis/events-api">Slack Events API</a></h3><p>Receive events when users message, mention, or interact with a Slack app.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-slack-app-authentication-https-api-slack-com-authentication"><a href="https://api.slack.com/authentication">Slack app authentication</a></h3><p>Configure OAuth, bot tokens, signing secrets, and request verification for Slack apps.</p></div>
