---
cp9:
  canonical: https://developers.cloudflare.com/spectrum/about/ftp/
  description: Enable Spectrum for FTP services and understand protocol limitations.
  full_title: FTP · Cloudflare Spectrum docs
  head_html: <title>FTP · Cloudflare Spectrum docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable Spectrum for FTP services and understand protocol limitations."><link rel="canonical" href="https://developers.cloudflare.com/spectrum/about/ftp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/spectrum/about/ftp/index.md"><meta property="og:title" content="FTP · Cloudflare Spectrum docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable Spectrum for FTP services and understand protocol limitations."><meta property="og:url" content="https://developers.cloudflare.com/spectrum/about/ftp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Spectrum"><meta name="algolia_product_filter" content="Spectrum"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Spectrum"><meta name="pcx_tags" content="FTP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/spectrum/about/ftp/#page","headline":"FTP \u00b7 Cloudflare Spectrum docs","description":"Enable Spectrum for FTP services and understand protocol limitations.","url":"https://developers.cloudflare.com/spectrum/about/ftp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["FTP"]}</script>
  markdown: true
  noindex: false
  route: /spectrum/about/ftp/
  schema: 1
---
<p>Enabling Spectrum for FTP is not straightforward due to the implementation of the protocol. This guide gives an overview of the intricacies of FTP and under which circumstances you can enable Spectrum for your FTP service.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13878.md")
</aside>
<h2 id="how-ftp-operates">How FTP Operates</h2>
<p>FTP leverages two different sockets, one for issuing commands and the other for actual data transfer. The control socket takes care of users logging in and sending commands, and the data socket is where directory listings and files actually get transferred.</p>
<p>There are two ways in which client and server can establish a data socket: active and passive. In active mode, the server connects <em>back</em> to the client on a port that they have specified, which can create issues where clients are behind an NAT. The alternative is passive mode, where the server opens an extra port that the client then connects to. For an overview of active versus passive FTP, refer to <a href="http://slacksite.com/other/ftp.html">Active FTP vs. Passive FTP, a Definitive Explanation</a>.</p>
<p>In passive mode, the FTP server communicates a port that the client should connect to, which is done on the control socket via a PASV command. By default, the FTP server responds with the IP address that it is listening on. This scenario is fine for servers running directly on a public-facing IP but creates issues when a server is behind an NAT, firewall, or Cloudflare Spectrum.</p>
<p>Alternatively, more modern FTP server software supports <a href="https://tools.ietf.org/html/rfc2428">FTP extensions</a>, which introduces the EPSV command that omits the IP address that the client should connect on. Instead, the client connects to the same IP that it connected to for the control pane.</p>
<h2 id="what-does-and-does-not-work">What Does and Does Not Work</h2>
<p>Spectrum is able to protect servers serving FTP traffic in <em>passive mode only</em>. Active mode is not supported due to the fact that the origin server sees the Spectrum IP as being the client instead of the actual client IP. When the client issues a PORT command with their own IP, the FTP server rejects because the two addresses do not match.</p>
<p>Passive mode in combination with EPSV works out of the box with no origin-side configuration required. Note that the client must also support EPSV for this to work. Traditional passive mode with PASV is possible with minimal origin-side configuration (see below, Protecting an FTP server with Spectrum)</p>
<h2 id="protect-an-ftp-server-with-spectrum">Protect an FTP Server with Spectrum</h2>
<p>Configuring Spectrum to protect your FTP server requires creating a set of Spectrum applications that point to your origin and some configuration on the FTP server.</p>
<h3 id="protect-the-control-port">Protect the Control Port</h3>
<p>The control plane runs on port 21 by default, and there is nothing special that needs to be to protect this part of the FTP server. In the example below, replace 198.51.100.1 with the IP of the origin server.</p>
<p><img src="/assets/upstream/images/spectrum/ftp-control-plane-app.png" alt="Add an application dialog with IP address and port set to 21" /></p>
<p>This configuration proxies incoming connections to the origin. However, if clients issue a PASV command, they will still receive the IP of the actual origin for the data connection. This is not preferred, as this exposes the origin's IP to the client instead of being masked behind Spectrum. Steps to prevent this are documented in sections below.</p>
<h3 id="protect-data-ports">Protect Data Ports</h3>
<p>Most FTP servers allow configuration of the port range that the server will use to open data connections. It is recommended to specify a port range to prevent accidentally exposing other ports on the server. For each port in the range, create a corresponding Spectrum application that maps to that port.</p>
<p>Additionally, the FTP server needs to be configured to expose the correct IP when the client issues a PASV command. This IP should match the IP of the Spectrum app.</p>
<p>Some FTP servers also allow dynamic resolving of hostnames. In this case, it is recommended to use the Spectrum app URL instead of the IP.</p>
<p>Example configuration for <a href="https://security.appspot.com/vsftpd.html">vsftpd</a>:</p>
<blockquote>
<pre tabindex="0"><code class="language-bash">pasv_min_port=20000&#10;pasv_max_port=20020&#10;&#10;pasv_enable=YES&#10;pasv_address=ftp.example.com&#10;pasv_addr_resolve=YES&#10;pasv_promiscuous=YES&#10;</code></pre>
</blockquote>
<h3 id="spectrum-ftps-proftpd-instructions">Spectrum FTPS (ProFTPD) instructions</h3>
<p>To use Spectrum TCP to proxy and protect FTPS, specifically ProFTPD, the following example configuration is recommended:</p>
<ul>
<li><strong>Control Port</strong>: Port 21</li>
<li><strong>Data Ports</strong>: Port ranges 50000-50500</li>
</ul>
<p>On the ProFTPD server side use the following example configuration:</p>
<ul>
<li><code>MasqueradeAddress</code>: <code>www.example.com</code></li>
<li><code>AllowForeignAddress</code>: You can use the option <code>on</code> to allow all IPs, but it is recommended to only allow <a href="/fundamentals/concepts/cloudflare-ip-addresses/#allow-cloudflare-ip-addresses">Cloudflare IP</a>.</li>
<li><code>PassivePorts</code>: <code>50000-50500</code></li>
</ul>
<p>For more details, refer to the <a href="http://www.proftpd.org/docs/modules/mod_core.html">ProFTPD documentation</a>.</p>
<h2 id="sftp">SFTP</h2>
<p>Unlike FTP or FTPS, enabling Spectrum for SFTP does not require extra configuration. When setting up a Spectrum application for SSH, select port 22 and TCP.</p>
<h2 id="microsoft-windows-iis-ftp">Microsoft Windows IIS FTP</h2>
<p>Refer to the <a href="https://docs.microsoft.com/en-us/iis/publish/using-the-ftp-service/configuring-ftp-firewall-settings-in-iis-7#step-1-configure-the-passive-port-range-for-the-ftp-service">Microsoft Windows IIS documentation</a> to configure a static data port range and external IP matching your Spectrum application.</p>
<p>Additionally, IIS requires that the source IP for both, FTP control and data connections are the same. However, when using Spectrum, this requirement may not be met, as both connections often terminate on different servers with their own unique egress IPs. To ensure proper functionality, also set <code>dataChannelSecurity/matchClientAddressForPasv = false</code>. Refer to <a href="https://learn.microsoft.com/en-us/iis/configuration/system.applicationhost/sites/site/ftpserver/security/datachannelsecurity">Microsoft Windows IIS FTP Official Guide</a> for further details.</p>
