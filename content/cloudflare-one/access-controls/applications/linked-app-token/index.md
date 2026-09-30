---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/linked-app-token/
  description: Forward Access JWTs between linked applications.
  full_title: Linked App Token · Cloudflare One docs
  head_html: <title>Linked App Token · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Forward Access JWTs between linked applications."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/linked-app-token/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/linked-app-token/index.md"><meta property="og:title" content="Linked App Token · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Forward Access JWTs between linked applications."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/linked-app-token/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One,Access"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/linked-app-token/#page","headline":"Linked App Token \u00b7 Cloudflare One docs","description":"Forward Access JWTs between linked applications.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/linked-app-token/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/linked-app-token/
  schema: 1
---
<p>The <strong>Linked App Token</strong> policy selector allows an Access policy on one application to accept tokens issued for another application. This is useful when one application needs to make authenticated requests to another on behalf of a user — for example, an MCP server calling internal APIs, or a microservice forwarding user identity to a downstream service.</p>
<p>Linked App Token supports two flows:</p>
<ul>
<li><a href="#self-hosted-to-self-hosted"><strong>Self-hosted to self-hosted</strong></a> — A self-hosted application forwards its Access JWT to another self-hosted application. This is the simplest setup and requires no additional OAuth configuration.</li>
<li><a href="#saas-to-self-hosted"><strong>SaaS to self-hosted</strong></a> — An Access for SaaS application (such as an <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/#saas-managed-third-party-mcp-server">MCP server using OAuth</a>) sends its OAuth access token to a self-hosted application.</li>
</ul>
<h2 id="self-hosted-to-self-hosted">Self-hosted to self-hosted</h2>
<p>In this flow, Application A is a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access application</a> that needs to make requests to Application B, another self-hosted Access application. When a user authenticates to Application A, Cloudflare Access sends the user's JWT to Application A in the <code>Cf-Access-Jwt-Assertion</code> header. Application A can then forward that token to Application B in the <code>Cf-Access-Token</code> header. Access will validate the token against the Linked App Token rule on Application B's policy and allow the request if the token was issued for Application A.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Self-hosted to self-hosted linked app token flow&#10;    User --&gt; appA[&quot;Application A &lt;br&gt; (self-hosted)&quot;]&#10;    appA -- &quot;Cf-Access-Token: &amp;lt;JWT&amp;gt;&quot; --&gt; appB[&quot;Application B &lt;br&gt; (self-hosted)&quot;]&#10;    idp[Identity provider] &lt;--&gt; appA&#10;</code></pre>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Two <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access applications</a></li>
</ul>
<h3 id="1-create-a-linked-app-token-policy"><ol>
<li>Create a Linked App Token policy</li>
</ol></h3>
<p>Create a policy on Application B (the downstream application that will receive forwarded requests):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4682.md")
</div></div>
<h3 id="2-forward-the-access-jwt"><ol start="2">
<li>Forward the Access JWT</li>
</ol></h3>
<p>When Cloudflare Access authenticates a user to Application A, it sends a signed JWT in the <code>Cf-Access-Jwt-Assertion</code> request header. Application A must forward this token to Application B in the <code>Cf-Access-Token</code> header:</p>
<pre tabindex="0"><code class="language-txt">Cf-Access-Token: &lt;JWT from Cf-Access-Jwt-Assertion&gt;&#10;</code></pre>
<p>When Access receives the request to Application B, it will:</p>
<ol>
<li>Extract the token from the <code>Cf-Access-Token</code> header.</li>
<li>Validate that the token was issued for Application A (matching the <code>app_uid</code> in the Linked App Token rule).</li>
<li>If valid, Access issues a new <code>Cf-Access-Jwt-Assertion</code> scoped to Application B's AUD tag, forwards it to Application B's origin, and attributes the request to the original user in the audit log.</li>
</ol>
<h2 id="saas-to-self-hosted">SaaS to self-hosted</h2>
<p>In this example an <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS application</a> (for example, an MCP server that implements <a href="https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization">OAuth</a>) needs to make requests to a self-hosted Access application. The SaaS app obtains an OAuth access token from Cloudflare Access and sends it to the self-hosted application in the <code>Authorization: Bearer</code> header.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: SaaS to self-hosted linked app token flow&#10;    User --&gt; appA[&quot;Application A &lt;br&gt; (Access for SaaS)&quot;]&#10;    appA -- &quot;Authorization: Bearer &amp;lt;token&amp;gt;&quot; --&gt; appB[&quot;Application B &lt;br&gt; (self-hosted)&quot;]&#10;    idp[Identity provider] &lt;--&gt; appA&#10;</code></pre>
<h3 id="prerequisites-1">Prerequisites</h3>
<ul>
<li>A <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access application</a></li>
<li>An <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS OIDC application</a></li>
</ul>
<h3 id="1-create-a-linked-app-token-policy-1"><ol>
<li>Create a Linked App Token policy</li>
</ol></h3>
<p>Create a policy on the self-hosted application (Application B):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4685.md")
</div></div>
<h3 id="2-configure-token-forwarding"><ol start="2">
<li>Configure token forwarding</li>
</ol></h3>
<p>The SaaS application must forward the OAuth <code>access_token</code> to the self-hosted application in an HTTP header:</p>
<pre tabindex="0"><code class="language-txt">Authorization: Bearer ACCESS_TOKEN&#10;</code></pre>
<p>The end-to-end flow is:</p>
<ol>
<li>The user authenticates against the Access for SaaS app via OAuth.</li>
<li>Upon success, the application receives an <code>access_token</code>.</li>
<li>The application makes a request to the self-hosted application with the token in the <code>Authorization: Bearer</code> header.</li>
<li>Cloudflare Access inspects the token and validates it against the <code>linked_app_token</code> rule. If valid, the request is allowed.</li>
</ol>
<h2 id="known-limitations">Known limitations</h2>
<ul>
<li>The Linked App Token policy can only be added to <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted applications</a>. It cannot be added to <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">SaaS applications</a> or other application types.</li>
<li>This feature works best with applications that rely on the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">Cloudflare Access JWT</a> for authentication and identity. If the downstream application implements its own authentication layer after Cloudflare Access, requests that pass Access validation may still be rejected by the application itself.</li>
<li>When the upstream application uses <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">Managed OAuth</a>, the client receives an <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#token-format">opaque access token</a>, not a JWT. The client cannot forward this token directly to downstream applications as a <code>Cf-Access-Token</code> header. Instead, the upstream application's origin must read the <code>Cf-Access-Jwt-Assertion</code> header (which contains the resolved JWT) and forward it as <code>Cf-Access-Token</code> to the downstream application. If you want clients to access multiple endpoints without a proxy, consider using a <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#multi-domain-applications">multi-domain Access application</a> instead.</li>
</ul>
