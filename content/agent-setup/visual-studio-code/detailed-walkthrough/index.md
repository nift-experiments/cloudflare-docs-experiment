---
cp9:
  canonical: https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/
  description: A screenshot-by-screenshot guide to connecting Visual Studio Code to the Cloudflare API through the Cloudflare MCP server, then creating, verifying, and deleting a DNS record with natural language.
  full_title: Visual Studio Code detailed walkthrough · Agent setup docs
  head_html: <title>Visual Studio Code detailed walkthrough · Agent setup docs</title><meta name="generator" content="Nift"><meta name="description" content="A screenshot-by-screenshot guide to connecting Visual Studio Code to the Cloudflare API through the Cloudflare MCP server, then creating, verifying, and deleting a DNS record with natural language."><link rel="canonical" href="https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/index.md"><meta property="og:title" content="Visual Studio Code detailed walkthrough · Agent setup docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A screenshot-by-screenshot guide to connecting Visual Studio Code to the Cloudflare API through the Cloudflare MCP server, then creating, verifying, and deleting a DNS record with natural language."><meta property="og:url" content="https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agent setup"><meta name="algolia_product_filter" content="Agent setup"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agent setup"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/#page","headline":"Visual Studio Code detailed walkthrough \u00b7 Agent setup docs","description":"A screenshot-by-screenshot guide to connecting Visual Studio Code to the Cloudflare API through the Cloudflare MCP server, then creating, verifying, and deleting a DNS record with natural language.","url":"https://developers.cloudflare.com/agent-setup/visual-studio-code/detailed-walkthrough/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agent-setup/visual-studio-code/detailed-walkthrough/
  schema: 1
---
<p>This walkthrough connects Visual Studio Code directly to the Cloudflare API using the <a href="https://github.com/cloudflare/mcp-server-cloudflare">Cloudflare MCP server</a>. By the end, you can create a DNS record by typing a sentence, without leaving the editor.</p>
<p>The Cloudflare MCP server at <code>mcp.cloudflare.com</code> exposes the Cloudflare API to any MCP-capable agent. The Visual Studio Code Copilot agent connects to it, and you run API calls from natural language.</p>
<p>For the condensed version, refer to the <a href="/agent-setup/visual-studio-code/">Visual Studio Code quick start</a>.</p>
<h2 id="before-you-start">Before you start</h2>
<ul>
<li>Visual Studio Code, fully up to date. A version mismatch between the editor and the Copilot extension is the most common source of agent-mode errors.</li>
<li>GitHub Copilot. Any GitHub account works, and the free tier is enough.</li>
<li>A Cloudflare account you are comfortable pointing an agent at. Use a demo account. The reason becomes clear at the authorization step.</li>
</ul>
<h2 id="connect-visual-studio-code-to-the-cloudflare-api">Connect Visual Studio Code to the Cloudflare API</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1840.md")
</div>
<p>You now have an AI agent with read and write access to Cloudflare services in the account, driven entirely from Visual Studio Code.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/agent-setup/visual-studio-code/">Visual Studio Code quick start</a> — condensed setup, tips, FAQ, and troubleshooting.</li>
<li><a href="https://github.com/cloudflare/mcp-server-cloudflare">Cloudflare MCP server</a> — domain-specific MCP servers.</li>
<li><a href="/api/">Cloudflare API</a> — the full REST API reference.</li>
</ul>
