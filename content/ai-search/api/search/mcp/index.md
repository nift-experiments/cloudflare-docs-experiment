---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/search/mcp/
  description: Expose AI Search content to AI agents through the Model Context Protocol (MCP) endpoint.
  full_title: MCP · Cloudflare AI Search docs
  head_html: <title>MCP · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Expose AI Search content to AI agents through the Model Context Protocol (MCP) endpoint."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/search/mcp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/search/mcp/index.md"><meta property="og:title" content="MCP · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose AI Search content to AI agents through the Model Context Protocol (MCP) endpoint."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/search/mcp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/search/mcp/#page","headline":"MCP \u00b7 Cloudflare AI Search docs","description":"Expose AI Search content to AI agents through the Model Context Protocol (MCP) endpoint.","url":"https://developers.cloudflare.com/ai-search/api/search/mcp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/search/mcp/
  schema: 1
---
<p>The Model Context Protocol (MCP) endpoint allows AI agents to discover and interact with your AI Search content. This endpoint follows the <a href="https://modelcontextprotocol.io/">MCP specification</a> and provides tools for querying your indexed content.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Enable public endpoints for your AI Search instance:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your AI Search instance.
3. Go to **Settings** > **Public Endpoint**.
4. Turn on **Enable Public Endpoint**.
5. Copy the public endpoint URL.
<h2 id="namespace-mcp-endpoints">Namespace MCP endpoints</h2>
<p>You can enable a public endpoint on a single instance or on a whole <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">namespace</a>. A namespace endpoint serves <code>/mcp</code> as well, and searches across the instances you allow in that namespace. Its hostname is prefixed with <code>ns-</code>:</p>
<pre tabindex="0"><code class="language-txt">https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>The tools and request format are the same for both. The examples on this page use the instance hostname.</p>
<h2 id="available-tools">Available tools</h2>
<p>The AI Search MCP endpoint exposes a <code>search</code> tool that queries your indexed content.</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>search</code></td>
<td>Finds exactly what you're looking for</td>
</tr>
</tbody>
</table>
<p>You can customize this in your AI Search instance settings. For more details, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint configuration</a>.</p>
<h2 id="test-the-mcp-endpoint">Test the MCP endpoint</h2>
<p>Send a request to the <code>/mcp</code> endpoint with the <code>Accept: application/json, text/event-stream</code> header:</p>
<pre tabindex="0"><code class="language-bash">curl https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Accept: application/json, text/event-stream&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;jsonrpc&quot;: &quot;2.0&quot;,&#10;    &quot;id&quot;: 1,&#10;    &quot;method&quot;: &quot;tools/call&quot;,&#10;    &quot;params&quot;: {&#10;      &quot;name&quot;: &quot;search&quot;,&#10;      &quot;arguments&quot;: {&#10;        &quot;query&quot;: &quot;How do I configure AI Search?&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h2 id="bring-your-own-domain">Bring your own domain</h2>
<p>You can serve the MCP endpoint from a hostname that you own, such as <code>https://search.example.com/mcp</code>, instead of the generated one. The hostname must belong to a zone on the same Cloudflare account. To attach a custom domain:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance or namespace.
3. Go to **Public Endpoints** and enable the public endpoint. A custom domain requires an active public endpoint.
4. Go to **Custom Domains** and attach your hostname.
<p>A custom domain routes requests through your own zone, so you can then put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of the endpoint. MCP clients authenticate with an Access <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>, sent as <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers, so only the agents you issue tokens to can reach the endpoint. Access only protects the custom hostname, so set <code>default_domain_enabled</code> to <code>false</code> as well. Otherwise the default <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code> hostname keeps answering unauthenticated requests.</p>
<p>To attach a domain through the API instead, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a>.</p>
