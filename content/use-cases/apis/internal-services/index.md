---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/apis/internal-services/
  description: Expose internal APIs and microservices securely without opening inbound firewall ports.
  full_title: Connect your internal network services · Cloudflare use cases
  head_html: <title>Connect your internal network services · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Expose internal APIs and microservices securely without opening inbound firewall ports."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/apis/internal-services/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/apis/internal-services/index.md"><meta property="og:title" content="Connect your internal network services · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose internal APIs and microservices securely without opening inbound firewall ports."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/apis/internal-services/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Cloudflare Tunnel,Access"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/apis/internal-services/#page","headline":"Connect your internal network services \u00b7 Cloudflare use cases","description":"Expose internal APIs and microservices securely without opening inbound firewall ports.","url":"https://developers.cloudflare.com/use-cases/apis/internal-services/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/apis/internal-services/
  schema: 1
---
<p>Internal services and microservices often need to communicate without exposing endpoints to the public Internet. Cloudflare Tunnel creates outbound-only connections with no inbound firewall rules, while Access enforces Zero Trust policies for every request between services.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="cloudflare-tunnel">Cloudflare Tunnel</h3>
<p>Connect infrastructure to Cloudflare without opening inbound firewall ports. <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Learn more about Cloudflare Tunnel</a>.</p>
<ul>
<li><strong>No public exposure</strong> - Internal Application Programming Interfaces (APIs) remain private; Tunnel establishes an outbound-only connection with no inbound firewall rules needed</li>
</ul>
<h3 id="access">Access</h3>
<p>Zero Trust access control for applications and infrastructure. <a href="/cloudflare-one/access-controls/policies/">Learn more about Access</a>.</p>
<ul>
<li><strong>Zero Trust policies</strong> - Verify identity and enforce per-service policies for every request between services</li>
<li><strong>Centralized policy management</strong> - Manage access rules for all internal services from a single control plane</li>
</ul>
<h3 id="service-tokens">Service Tokens</h3>
<p>Non-interactive credentials for machine-to-machine authentication. <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Learn more about Service Tokens</a>.</p>
<ul>
<li><strong>Service-to-service auth</strong> - Authenticate internal services with non-interactive credentials managed in Cloudflare One</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">Create a Cloudflare Tunnel</a></li>
<li><a href="/cloudflare-one/access-controls/policies/">Cloudflare Access get started</a></li>
<li><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Create service tokens</a></li>
</ol>
