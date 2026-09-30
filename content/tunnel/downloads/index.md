---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/downloads/
  description: Download the cloudflared daemon for your operating system.
  full_title: Downloads · Cloudflare Docs
  head_html: <title>Downloads · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Download the cloudflared daemon for your operating system."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/downloads/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/downloads/index.md"><meta property="og:title" content="Downloads · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Download the cloudflared daemon for your operating system."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/downloads/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/downloads/#page","headline":"Downloads \u00b7 Cloudflare Docs","description":"Download the cloudflared daemon for your operating system.","url":"https://developers.cloudflare.com/tunnel/downloads/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /tunnel/downloads/
  schema: 1
---
<p>Cloudflare Tunnel requires the installation of a lightweight daemon, <code>cloudflared</code>, to connect your infrastructure to Cloudflare. If you are <a href="/tunnel/get-started/">creating a tunnel through the dashboard</a>, you can simply copy-paste the installation command shown in the dashboard.</p>
<p>To download and install <code>cloudflared</code> manually, use one of the following links.</p>
<h2 id="github-repository">GitHub repository</h2>
<p><code>cloudflared</code> is an <a href="https://github.com/cloudflare/cloudflared">open source project</a> maintained by Cloudflare.</p>
<ul>
<li>
<p><a href="https://github.com/cloudflare/cloudflared/releases">All releases</a></p>
</li>
<li>
<p><a href="https://github.com/cloudflare/cloudflared/blob/master/RELEASE_NOTES">Release notes</a></p>
</li>
</ul>
<h2 id="latest-release">Latest release</h2>
<h3 id="linux">Linux</h3>
<p>You can download and install <code>cloudflared</code> via the <a href="https://pkg.cloudflare.com/">Cloudflare Package Repository</a>.</p>
<p>Alternatively, download the latest release directly:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>amd64 / x86-64</th>
<th>x86 (32-bit)</th>
<th>ARM</th>
<th>ARM64</th>
</tr>
</thead>
<tbody>
<tr>
<td>Binary</td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64">Download</a></td>
</tr>
<tr>
<td>.deb</td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386.deb">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm.deb">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64.deb">Download</a></td>
</tr>
<tr>
<td>.rpm</td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-x86_64.rpm">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386.rpm">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm.rpm">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-aarch64.rpm">Download</a></td>
</tr>
</tbody>
</table>
<h3 id="macos">macOS</h3>
<p>Download and install <code>cloudflared</code> via Homebrew:</p>
<pre tabindex="0"><code class="language-sh">brew install cloudflared&#10;</code></pre>
<p>Alternatively, download the <a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-arm64.tgz">latest Darwin arm64 release</a> or <a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz">latest Darwin amd64 release</a> directly.</p>
<h3 id="windows">Windows</h3>
<p>Download the latest release from <a href="https://github.com/cloudflare/cloudflared/releases/latest">GitHub</a>:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>32-bit</th>
<th>64-bit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Executable</td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.exe">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe">Download</a></td>
</tr>
<tr>
<td>MSI</td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.msi">Download</a></td>
<td><a href="https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.msi">Download</a></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14952.md")
</aside>
<h3 id="docker">Docker</h3>
<p>A Docker image of <code>cloudflared</code> is <a href="https://hub.docker.com/r/cloudflare/cloudflared">available on DockerHub</a>.</p>
<h2 id="deprecated-releases">Deprecated releases</h2>
<p>Cloudflare supports versions of <code>cloudflared</code> that are within one year of the most recent release. Breaking changes unrelated to feature availability may be introduced that will impact versions released more than one year ago. For example, as of January 2023 Cloudflare will support <code>cloudflared</code> version 2023.1.1 to cloudflared 2022.1.1.</p>
<p>To update <code>cloudflared</code>, refer to <a href="/tunnel/guides/update-cloudflared/">Update cloudflared</a>.</p>
