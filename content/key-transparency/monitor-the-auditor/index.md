---
cp9:
  canonical: https://developers.cloudflare.com/key-transparency/monitor-the-auditor/
  description: Verify Key Transparency audit proofs locally using the Plexi CLI tool.
  full_title: Monitor the Auditor · Cloudflare Key Transparency Auditor docs
  head_html: <title>Monitor the Auditor · Cloudflare Key Transparency Auditor docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify Key Transparency audit proofs locally using the Plexi CLI tool."><link rel="canonical" href="https://developers.cloudflare.com/key-transparency/monitor-the-auditor/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/key-transparency/monitor-the-auditor/index.md"><meta property="og:title" content="Monitor the Auditor · Cloudflare Key Transparency Auditor docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify Key Transparency audit proofs locally using the Plexi CLI tool."><meta property="og:url" content="https://developers.cloudflare.com/key-transparency/monitor-the-auditor/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Key Transparency Auditor"><meta name="algolia_product_filter" content="Key Transparency Auditor"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Key Transparency Auditor"><meta name="pcx_tags" content="CLI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/key-transparency/monitor-the-auditor/#page","headline":"Monitor the Auditor \u00b7 Cloudflare Key Transparency Auditor docs","description":"Verify Key Transparency audit proofs locally using the Plexi CLI tool.","url":"https://developers.cloudflare.com/key-transparency/monitor-the-auditor/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CLI"]}</script>
  markdown: true
  noindex: false
  route: /key-transparency/monitor-the-auditor/
  schema: 1
---
<p>Cloudflare's Key Transparency Auditor validates Log audit proofs and provides a signature for them. The Log can then distribute these signatures to its end-users, and provides users with confidence that keys have not been tampered with.</p>
<p>In order to verify our work, you can use <a href="https://github.com/cloudflare/plexi">Plexi</a>, a CLI tool that allows anyone to perform proof verification locally via a public <a href="/key-transparency/api/">API</a>.</p>
<h2 id="features">Features</h2>
<ul>
<li>Verify authenticity of a signature, to confirm it has been signed by a given public key</li>
<li>Verify the validity of <a href="https://github.com/facebook/akd">facebook/akd</a> proofs</li>
<li>List Logs an Auditor monitors</li>
</ul>
<h2 id="installation">Installation</h2>
<table>
<thead>
<tr>
<th align="left">Environment</th>
<th align="left">CLI Command</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://www.rust-lang.org/tools/install">Cargo</a> (Rust 1.81+)</td>
<td align="left"><code>cargo install plexi</code></td>
</tr>
</tbody>
</table>
<h2 id="usage">Usage</h2>
<p>Use the <code>--help</code> option for more details about the commands and their options.</p>
<pre tabindex="0"><code class="language-bash">plexi [OPTIONS] &lt;COMMAND&gt;&#10;</code></pre>
<h3 id="configure-your-auditor-remote">Configure your auditor remote</h3>
<p><code>plexi</code> does not come with a default remote auditor, and you will need to choose your own.</p>
<p>You can do so either by passing <code>--remote-url=&lt;REMOTE&gt;</code> or setting the <code>PLEXI_REMOTE_URL</code> environment variable.</p>
<p>A common remote is provided below:</p>
<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="left">Remote</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Cloudflare</td>
<td align="left"><code>https://plexi.key-transparency.cloudflare.com</code></td>
</tr>
</tbody>
</table>
<p>If you have deployed your own auditor, you can add a remote by filing a <a href="https://github.com/cloudflare/plexi/issues">GitHub issue</a>.</p>
<h3 id="list-monitored-logs">List monitored Logs</h3>
<p>An auditor monitors multiple Logs at once. To discover which Logs an auditor is monitoring, run the following:</p>
<pre tabindex="0"><code class="language-shell">plexi ls --remote-url &#x27;https://plexi.key-transparency.cloudflare.com&#x27;&#10;whatsapp.key-transparency.v1&#10;</code></pre>
<h3 id="audit-a-signature">Audit a signature</h3>
<p>The Key Transparency Auditor vouches for Log validity by ensuring epoch uniqueness and verifying the associated proof.</p>
<p><code>plexi audit</code> provides information about a given epoch and its validity. It can perform a local audit to confirm the auditor behaviour.</p>
<p>For instance, to verify WhatsApp Log auditted by Cloudflare Auditor, run the following:</p>
<pre tabindex="0"><code class="language-shell">&gt; plexi audit --remote-url &#x27;https://plexi.key-transparency.cloudflare.com&#x27; --namespace &#x27;whatsapp.key-transparency.v1&#x27; --long&#10;Namespace&#10;  Name               : whatsapp.key-transparency.v1&#10;  Ciphersuite        : ed25519(protobuf)&#10;&#10;Signature (2024-09-23T16:53:45Z)&#10;  Epoch height      	: 489193&#10;  Epoch digest      	: cbe5097ae832a3ae51ad866104ffd4aa1f7479e873fd18df9cb96a02fc91ebfe&#10;  Signature         	: fe94973e19da826487b637c019d3ce52f0c08093ada00b4fe6563e2f8117b4345121342bc33aae249be47979dfe704478e2c18aed86e674df9f934b718949c08&#10;  Signature verification: success&#10;  Proof verification	: success&#10;</code></pre>
