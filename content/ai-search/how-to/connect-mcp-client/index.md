---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/how-to/connect-mcp-client/
  description: Expose your indexed content as a search tool for any MCP client or agent using the built-in MCP endpoint.
  full_title: Connect your AI Search to an MCP client · Cloudflare AI Search docs
  head_html: <title>Connect your AI Search to an MCP client · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Expose your indexed content as a search tool for any MCP client or agent using the built-in MCP endpoint."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/how-to/connect-mcp-client/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/how-to/connect-mcp-client/index.md"><meta property="og:title" content="Connect your AI Search to an MCP client · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose your indexed content as a search tool for any MCP client or agent using the built-in MCP endpoint."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/how-to/connect-mcp-client/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/how-to/connect-mcp-client/#page","headline":"Connect your AI Search to an MCP client \u00b7 Cloudflare AI Search docs","description":"Expose your indexed content as a search tool for any MCP client or agent using the built-in MCP endpoint.","url":"https://developers.cloudflare.com/ai-search/how-to/connect-mcp-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/how-to/connect-mcp-client/
  schema: 1
---
<p>Every AI Search instance can expose a built-in <a href="https://modelcontextprotocol.io/">Model Context Protocol (MCP)</a> endpoint. The endpoint provides a <code>search</code> tool over your indexed content, so any MCP client or agent, such as an AI assistant or IDE, can search your knowledge base without any code.</p>
<p>This guide creates an AI Search instance that indexes a documentation site, then exposes it as a search tool that any MCP client can call.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3029.md")
</div></details>
<p>To index a website, you also need a domain <a href="/fundamentals/manage-domains/add-site/">onboarded to your Cloudflare account</a>. Otherwise, you can upload your own files to <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>.</p>
<h2 id="1-create-an-ai-search-instance"><ol>
<li>Create an AI Search instance</li>
</ol></h2>
<p>If you already have an instance with indexed content, skip to <a href="#2-enable-the-mcp-endpoint">step 2</a>.</p>
<p>Create an instance with the <a href="/ai-search/wrangler-commands/">Wrangler CLI</a>. This example indexes a documentation site, using the Cloudflare Developer Docs at <code>developers.cloudflare.com</code>, so an assistant can answer questions from it. Connect the site as a <a href="/ai-search/configuration/data-source/website/">website data source</a> so AI Search crawls and indexes it automatically:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler ai-search create docs-search --type web-crawler --source developers.cloudflare.com&#10;</code></pre>
<p>Replace <code>developers.cloudflare.com</code> with a domain you have <a href="/fundamentals/manage-domains/add-site/">onboarded to your Cloudflare account</a>, since you can only crawl sites you own. To index content without crawling a site, run <code>npx wrangler ai-search create docs-search --type builtin</code> and upload files to <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a> instead.</p>
<p>Check indexing progress:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler ai-search stats docs-search&#10;</code></pre>
<p>Once indexing completes, your instance has content to expose over MCP.</p>
<h2 id="2-enable-the-mcp-endpoint"><ol start="2">
<li>Enable the MCP endpoint</li>
</ol></h2>
<p>Your instance's public endpoint serves the MCP endpoint.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3030.md")
</div>
<h2 id="3-describe-your-search-tool"><ol start="3">
<li>Describe your search tool</li>
</ol></h2>
<p>An MCP client reads a tool's description to decide when to call it. Under <strong>Settings</strong> &gt; <strong>Public Endpoint</strong>, set the <strong>Tool Description</strong> to explain what your content covers and the questions it answers. For example:</p>
<pre tabindex="0"><code class="language-txt">Search the Cloudflare Developer Documentation for product concepts,&#10;configuration, and API references. Use this when users ask how to build&#10;or configure Cloudflare products.&#10;</code></pre>
<p>A specific description helps agents call your search tool at the right time. Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint settings</a> for the full configuration.</p>
<h2 id="4-connect-your-mcp-client"><ol start="4">
<li>Connect your MCP client</li>
</ol></h2>
<p>Add the MCP URL to your client as a remote MCP server. Many clients use an <code>mcpServers</code> configuration like the following:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;ai-search&quot;: {&#10;			&quot;url&quot;: &quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The exact configuration depends on your client. Some clients require a transport field on the server entry, such as <code>&quot;type&quot;: &quot;http&quot;</code> for a remote HTTP server, so refer to your MCP client's documentation for how to add a remote server. Once connected, the client can call the <code>search</code> tool to retrieve relevant content from your instance.</p>
<p>To test the endpoint directly or build your own client, refer to <a href="/ai-search/api/search/mcp/">MCP</a> for the request format.</p>
<h2 id="security-considerations">Security considerations</h2>
<p>The public endpoint does not require authentication, so anyone with the URL can query your indexed content.</p>
<p>To require authentication, add a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a> and protect it with <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a>. MCP clients then authenticate with an Access <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a> sent as request headers.</p>
<p>If you keep the endpoint open:</p>
<ul>
<li>Only index content that is safe to expose publicly.</li>
<li>Enable rate limiting under <strong>Settings</strong> &gt; <strong>Public Endpoint</strong>.</li>
<li>Restrict allowed origins under <strong>Authorized hosts</strong>. This only affects browser clients.</li>
</ul>
<p>Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint settings</a> for details.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-mcp-endpoint-reference-ai-search-api-search-mcp"><a href="/ai-search/api/search/mcp/">MCP endpoint reference</a></h3><p>The MCP endpoint tools and request format.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-public-endpoint-settings-ai-search-configuration-retrieval-public-endpoint"><a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint settings</a></h3><p>Rate limiting, CORS, and tool description.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cloudflare-access-ai-search-configuration-retrieval-public-endpoint-cloudflare-access"><a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a></h3><p>Require MCP clients to authenticate before they can search.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-ai-search-as-an-agent-tool-agents-tools-ai-search"><a href="/agents/tools/ai-search/">AI Search as an agent tool</a></h3><p>Query AI Search in code from a Cloudflare Agent.</p></div>
