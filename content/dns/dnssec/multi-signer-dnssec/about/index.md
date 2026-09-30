---
cp9:
  canonical: https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/
  description: How multi-signer DNSSEC works with multiple DNS providers.
  full_title: About multi-signer DNSSEC · Cloudflare DNS docs
  head_html: <title>About multi-signer DNSSEC · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="How multi-signer DNSSEC works with multiple DNS providers."><link rel="canonical" href="https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/index.md"><meta property="og:title" content="About multi-signer DNSSEC · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How multi-signer DNSSEC works with multiple DNS providers."><meta property="og:url" content="https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/#page","headline":"About multi-signer DNSSEC \u00b7 Cloudflare DNS docs","description":"How multi-signer DNSSEC works with multiple DNS providers.","url":"https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dnssec/multi-signer-dnssec/about/
  schema: 1
---
<p>Multi-signer DNSSEC consists of two models that allow different authoritative DNS providers to serve the same zone and have DNSSEC enabled at the same time.</p>
<p>This means better compatibility with DNS features that require live-signing of DNS records (at query time), and also allows you to <a href="/dns/dnssec/dnssec-active-migration/">migrate zones to Cloudflare without having to disable DNSSEC</a>.</p>
<p>You can <a href="/dns/dnssec/multi-signer-dnssec/setup/">set up multi-signer DNSSEC</a> using either one of the models described in <a href="https://www.rfc-editor.org/rfc/rfc8901.html">RFC 8901</a>.</p>
<h2 id="how-it-works">How it works</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7747.md")
</aside>
<p>Multi-signer DNSSEC looks into the chain of trust that is necessary for DNSSEC validation and leverages that to guarantee that validation is completed even when multiple providers are involved.</p>
<p>An example case where validation would otherwise be an issue is if a resolver has cached a <a href="https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/">DNSKEY record set</a> from one provider but receives a response signed by another provider.</p>
<p>To avoid issues in that case, when you set up multi-signer DNSSEC, you adjust:</p>
<ol>
<li>The Zone Signing Keys (ZSK) that your DNS providers have in their DNSKEY record sets.</li>
<li>Who is responsible for the Secure Entry Point (SEP), Key Signing Keys (KSK), and Delegation Signer (DS) record.</li>
</ol>
<p>When these configurations are adjusted in a way that (a) all involved providers have each other's public Zone Signing Keys (ZSK), and that (b) Delegation Signer (DS) records reference the necessary Key Signing Keys (KSK), then live-signing of zones by multiple providers is no longer a problem.</p>
<h3 id="model-1">Model 1</h3>
<p>Whereas in both models all providers have each other's Zone Signing Keys (ZSK) added to their DNSKEY record set, in model 1, only one Key Signing Key (KSK) is used to sign such DNSKEY record sets. Management of this KSK and its reference by the DS record (that is, the Secure Entry Point) is the responsibility of the zone owner or only one provider (designated by the zone owner).</p>
<h3 id="model-2">Model 2</h3>
<p>In model 2, on the other hand, each provider uses its own KSK to sign its own DNSKEY record set, and these KSKs are then referenced by the DS record (Secure Entry Point).</p>
<hr />
<h2 id="what-happens-when-multi-signer-dnssec-is-on">What happens when multi-signer DNSSEC is on</h2>
<p>When you turn on multi-signer DNSSEC on Cloudflare, the following changes occur:</p>
<ol>
<li><strong>Internal flag</strong>: Cloudflare sets an internal flag that allows you to add DNSKEY records to your zone.</li>
<li><strong>External ZSKs included</strong>: When you add DNSKEY records from your secondary provider, Cloudflare includes them in the DNSKEY RRset.</li>
<li><strong>Signing with Cloudflare's KSK</strong>: Cloudflare signs the external ZSKs with Cloudflare's KSK, creating a Multi-signer DNSSEC Model 2 RRset.</li>
<li><strong>CDS/CDNSKEY generation</strong>: If you add your other provider's KSK (not required but recommended), Cloudflare produces CDS/CDNSKEY RRsets for compatibility with validation tools.</li>
</ol>
<p>This configuration ensures that resolvers can validate responses from either provider, as all ZSK DNSKEYs are signed by the appropriate KSKs referenced in the DS records.</p>
<hr />
<h2 id="best-practices">Best practices</h2>
<p>When setting up multi-signer DNSSEC, follow the best practices below to help you achieve a smooth deployment.</p>
<h3 id="use-model-2">Use model 2</h3>
<p>Cloudflare recommends model 2 for multi-signer setups. In this model, each provider has their own KSK DNSKEY, resulting in two DS records (one for each provider). This provides better independence and flexibility.</p>
<h3 id="understand-dnskey-flags">Understand DNSKEY flags</h3>
<ul>
<li><strong>ZSKs (Zone Signing Keys)</strong>: flag <code>256</code></li>
<li><strong>KSKs (Key Signing Keys)</strong>: flag <code>257</code></li>
</ul>
<p>When exchanging keys between providers, ensure you are adding the correct key type (typically ZSKs) to the DNSKEY RRset.</p>
<h3 id="adhere-to-ttls">Adhere to TTLs</h3>
<p>Always wait for the TTL duration after making changes to DNSKEYs and DS records before proceeding to the next step. This ensures that cached records expire before new records take effect, preventing validation failures.</p>
<h3 id="verify-provider-compatibility">Verify provider compatibility</h3>
<p>Not all DNS providers support adding external DNSKEYs to their DNSKEY RRset. Before starting a multi-signer migration:</p>
<ul>
<li>Verify that your other provider supports multi-signer DNSSEC.</li>
<li>Confirm they can add Cloudflare's ZSK to their DNSKEY records.</li>
<li>Test the configuration in a non-production environment if possible.</li>
</ul>
<p>Some third-party providers may not support the required functionality.</p>
<h3 id="test-thoroughly">Test thoroughly</h3>
<p>Multi-signer DNSSEC involves coordinating cryptographic keys across multiple providers. Before deploying to production:</p>
<ol>
<li>Verify that both providers have each other's ZSKs in their DNSKEY RRsets.</li>
<li>Confirm that both DS records are present at the registrar.</li>
<li>Use DNSSEC validation tools to test resolution from both providers.</li>
<li>Monitor for validation errors during the transition period.</li>
</ol>
