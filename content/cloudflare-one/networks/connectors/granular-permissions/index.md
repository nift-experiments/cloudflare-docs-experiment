---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/
  description: Scope Cloudflare member permissions to individual Cloudflare Tunnel instances and Cloudflare Mesh nodes.
  full_title: Granular permissions for Tunnels and Mesh nodes · Cloudflare One docs
  head_html: <title>Granular permissions for Tunnels and Mesh nodes · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Scope Cloudflare member permissions to individual Cloudflare Tunnel instances and Cloudflare Mesh nodes."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/index.md"><meta property="og:title" content="Granular permissions for Tunnels and Mesh nodes · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scope Cloudflare member permissions to individual Cloudflare Tunnel instances and Cloudflare Mesh nodes."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/#page","headline":"Granular permissions for Tunnels and Mesh nodes \u00b7 Cloudflare One docs","description":"Scope Cloudflare member permissions to individual Cloudflare Tunnel instances and Cloudflare Mesh nodes.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/granular-permissions/
  schema: 1
---
<p>You can scope Cloudflare member permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes, instead of granting account-wide access to every Tunnel and Mesh node. This enables least-privilege delegation for private networking operations — for example, letting a support operator stream logs from a single Tunnel without exposing the rest of your account.</p>
<p>Granular permissions are a parallel layer to <a href="/fundamentals/manage-members/roles/#account-scoped-roles">account-scoped roles</a> — they do not replace them. Members who already hold an account-level role like <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> continue to have write access to every Tunnel and Mesh node in the account.</p>
<h2 id="how-it-works">How it works</h2>
<p>For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong>:</p>
<ul>
<li>An account-level role that covers the resource (for example, <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code>), <strong>or</strong></li>
<li>A <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped role</a> bound to that specific Tunnel or Mesh node.</li>
</ul>
<p><a href="#resource-enumeration">Resource enumeration endpoints</a> (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</p>
<h2 id="grant-a-granular-permission">Grant a granular permission</h2>
<p>Granular permissions are assigned through the standard <a href="/fundamentals/manage-members/manage/">member management</a> flow.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/5130.md")
</div>
<p>You can attach multiple granular policies to the same member to cover different Tunnels and Mesh nodes with different roles.</p>
<h2 id="resource-enumeration">Resource enumeration</h2>
<p>Listing endpoints are authorization-aware. When a principal calls a listing endpoint, the response is filtered to the resources they have at least read access to.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Method</th>
<th>Returns</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/accounts/{account_id}/cfd_tunnel</code></td>
<td><code>GET</code></td>
<td>Cloudflare Tunnel instances the principal can read or manage.</td>
</tr>
<tr>
<td><code>/accounts/{account_id}/warp_connector</code></td>
<td><code>GET</code></td>
<td>Cloudflare Mesh nodes the principal can read or manage.</td>
</tr>
<tr>
<td><code>/accounts/{account_id}/teamnet/routes</code></td>
<td><code>GET</code></td>
<td>Routes attached to Tunnels the principal can read or manage.</td>
</tr>
</tbody>
</table>
<p>Members with an account-level role that covers Tunnels and Mesh continue to see all resources in the account.</p>
<h2 id="backward-compatibility">Backward compatibility</h2>
<ul>
<li>Existing account-level roles and API tokens continue to function as before.</li>
<li>Existing automation that authenticates with an account-level token (for example, Terraform pipelines using a <code>Cloudflare Access</code> token) is unaffected.</li>
<li>Granular permissions are opt-in. Granting one to a member adds capability; it never removes capability that the member already has from an account-level role.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/manage-members/roles/">Roles reference</a> — the full list of Cloudflare roles, including resource-scoped roles for Tunnels and Mesh nodes.</li>
<li><a href="/fundamentals/manage-members/scope/">Role scopes</a> — how policy scopes work across account, domain, and resource layers.</li>
<li><a href="/fundamentals/manage-members/manage/">Manage account members</a> — the member invite and edit flow.</li>
<li><a href="/tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/mesh/">Cloudflare Mesh</a></li>
</ul>
