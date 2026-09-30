---
cp9:
  canonical: https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/
  description: Expose a local Wrangler or Vite dev server over a public tunnel URL.
  full_title: Share a local dev server · Cloudflare Workers docs
  head_html: <title>Share a local dev server · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Expose a local Wrangler or Vite dev server over a public tunnel URL."><link rel="canonical" href="https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/index.md"><meta property="og:title" content="Share a local dev server · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose a local Wrangler or Vite dev server over a public tunnel URL."><meta property="og:url" content="https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/#page","headline":"Share a local dev server \u00b7 Cloudflare Workers docs","description":"Expose a local Wrangler or Vite dev server over a public tunnel URL.","url":"https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/local-development/local-dev-tunnels/
  schema: 1
---
<p>You can expose your local dev server over a <a href="/tunnel/">Cloudflare Tunnel</a> when you need to share a preview, test a webhook, or access your app from another device.</p>
<p>This page covers tunnel support in <a href="/workers/wrangler/commands/general/#dev">Wrangler</a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<h2 id="start-a-tunnel">Start a tunnel</h2>
<p>You can start a tunnel with Wrangler or the Cloudflare Vite plugin for the current session. This gives you either a random <code>*.trycloudflare.com</code> hostname via a <a href="/tunnel/get-started/#quick-tunnels-development">Quick tunnel</a>, or a stable hostname via a <a href="/tunnel/get-started/#create-a-tunnel">named tunnel</a>.</p>
<p><strong>Wrangler</strong></p>
<p>Run <code>wrangler dev</code>, then press <code>[t]</code> to start or close the tunnel. Wrangler will print the public tunnel URL or URLs for the current session.</p>
<p>To use a named tunnel, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler dev --tunnel-name=my-tunnel</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev --tunnel-name=my-tunnel" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler dev --tunnel-name=my-tunnel</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev --tunnel-name=my-tunnel" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler dev --tunnel-name=my-tunnel</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev --tunnel-name=my-tunnel" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Use <code>--tunnel</code> if you want the tunnel to open automatically when Wrangler starts.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler dev --tunnel</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev --tunnel" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler dev --tunnel</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev --tunnel" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler dev --tunnel</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev --tunnel" aria-label="Copy to clipboard">Copy</button></div></div>
<p><strong>Cloudflare Vite plugin</strong></p>
<p>Run <code>vite dev</code>, then press <code>t + Enter</code> to start or close the tunnel. Add <code>tunnel</code> to the plugin config if you want to configure a named tunnel or have the tunnel open automatically when Vite starts.</p>
<p>To use a named tunnel with stable hostnames:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16268.md")
</div>
<p>If you want the tunnel to open automatically when Vite starts, set <code>tunnel.autoStart</code> to <code>true</code>.</p>
<p>When using <code>vite preview</code>, Vite's preview host validation still applies:</p>
<ul>
<li>For Quick tunnel, add <code>.trycloudflare.com</code> to <code>preview.allowedHosts</code>.</li>
<li>For named tunnel, add the resolved hostnames or a matching domain suffix such as <code>.my-domain.com</code> to <code>preview.allowedHosts</code>.</li>
</ul>
<p>For example:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16269.md")
</div>
<h2 id="security-considerations">Security considerations</h2>
<p>Anyone with the tunnel URL can reach your dev server, so review what your app exposes before enabling a tunnel.</p>
<ul>
<li>Pay special attention to ungated preview or admin endpoints.</li>
<li>Review any <a href="/workers/local-development/#remote-bindings">remote bindings</a> connected to real resources.</li>
<li>Review any code that proxies requests to private or internal services.</li>
<li>If you are using the Cloudflare Vite plugin with <code>vite dev</code>, HMR and module serving may expose source files, file paths, or project structure over the tunnel. If you only need to share a built preview, prefer <code>vite preview</code> for public sharing.</li>
<li>Local dev-related routes, such as <code>/cdn-cgi/*</code>, remain restricted and are not exposed over the tunnel.</li>
<li>If you need a stable hostname or stricter access control, use a named tunnel protected by Cloudflare Access.</li>
</ul>
<h2 id="related-docs">Related docs</h2>
<ul>
<li><a href="/tunnel/">Cloudflare Tunnel</a></li>
</ul>
