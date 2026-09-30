---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-10-warp-windows-beta/
  description: New updates and improvements at Cloudflare.
  full_title: WARP client for Windows (version 2026.3.566.1) · Changelog
  head_html: <title>WARP client for Windows (version 2026.3.566.1) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-10-warp-windows-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WARP client for Windows (version 2026.3.566.1) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-10-warp-windows-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-10-warp-windows-beta/#page","headline":"WARP client for Windows (version 2026.3.566.1) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-10-warp-windows-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-10-warp-windows-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2026</time><h2 id="post-title">WARP client for Windows (version 2026.3.566.1)</h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the <a href="https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362">Cloudflare Community forum</a> and let us know.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.</li>
<li>Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.</li>
<li>Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.</li>
<li>Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.</li>
<li>Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.</li>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.</li>
<li>Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>The client may unexpectedly terminate during captive portal login. To work around this issue, use a web browser to authenticate with the captive portal and then re-launch the client.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>The client may become stuck in a <code>Connecting</code> state. To resolve this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface. Alternatively, change the client's operation mode.</li>
<li>The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.</li>
<li>Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.</li>
<li>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 version KB5062553</a> or higher for resolution.</li>
<li>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.
To work around this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface.</li>
</ul>
</li>
</ul>
</div></article></div>
