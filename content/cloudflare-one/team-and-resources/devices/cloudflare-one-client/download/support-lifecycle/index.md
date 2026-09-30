---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/
  description: Reference information for Cloudflare One Client lifecycle and support policy in Zero Trust.
  full_title: Cloudflare One Client lifecycle and support policy · Cloudflare One docs
  head_html: <title>Cloudflare One Client lifecycle and support policy · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Cloudflare One Client lifecycle and support policy in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/index.md"><meta property="og:title" content="Cloudflare One Client lifecycle and support policy · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Cloudflare One Client lifecycle and support policy in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/#page","headline":"Cloudflare One Client lifecycle and support policy \u00b7 Cloudflare One docs","description":"Reference information for Cloudflare One Client lifecycle and support policy in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/
  schema: 1
---
<p>This page details the technical support policies for the Cloudflare One Client (formerly WARP), which operating systems and their versions are supported and for how long, and the process by which Cloudflare One Client features will be deprecated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6108.md")
</aside>
<h2 id="cloudflare-one-client-lifecycle">Cloudflare One Client lifecycle</h2>
<h3 id="desktop-platforms">Desktop platforms</h3>
<p>Cloudflare One Client releases for Windows, macOS, and Linux come in two forms: beta and stable. Occasionally, a stable release will be declared a Long-Term Support release (LTS).</p>
<ul>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">Beta releases</a> allow for early testing of new features before the features ship in the next stable release. Beta releases are not guaranteed to get security fixes and are not recommended for production environments.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Stable releases</a>, including those labeled as LTS releases, are production-ready and will include the latest features as well as functional and security bug fixes. Functional and security bugs found in non-LTS stable releases will be fixed in later stable releases; they are not backported to previous versions. Therefore, Cloudflare recommends regularly deploying the latest stable release.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/">LTS releases</a> receive security bug fixes for a guaranteed minimum of 12 months. When Cloudflare publishes a new LTS release, the previous LTS release continues to receive security fixes for an additional 90 days — giving you a migration window. If the gap between two LTS releases is longer than 12 months, the migration window extends the total support period beyond 12 months. For example, if 15 months pass between two LTS releases, the earlier release receives security fixes for 18 months total (15 months until the next LTS release, plus the 90-day migration window). Cloudflare will announce an upcoming LTS release in advance so you can plan the migration.</p>
<p>To ensure timely security fixes with less frequent <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/#test-before-updates">version testing</a>, customers may choose to deploy only LTS releases and skip the stable releases in between. This approach is recommended for large or risk-averse organizations where stability is more important than rapid adoption of the latest features.</p>
</li>
</ul>
<h3 id="mobile-platforms">Mobile platforms</h3>
<p>Cloudflare One Client releases for iOS, iPadOS, Android, ChromeOS, and ChromeOS Flex are limited to stable releases released via the iOS App Store or Google Play Store. Therefore, security fixes will be shipped via the latest release.</p>
<h3 id="feature-deprecation-policy">Feature deprecation policy</h3>
<p>Major features included in a Cloudflare One Client release will not be removed while that release is still receiving security fixes.</p>
<p>Cloudflare will provide a minimum 90-day notice prior to removing major features in future releases. This allows customers on the stable release track to prepare for feature removal without delaying the adoption of the latest release. Customers on the LTS release track already have a 90-day overlap period between LTS releases.</p>
<h3 id="release-schedule">Release schedule</h3>
<p>Cloudflare does not operate on a fixed release schedule; all releases for the Cloudflare One Client are incremental. When a new Cloudflare One Client version is released, Cloudflare will publish release notes on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Downloads page</a> and in the <a href="/changelog/cloudflare-one-client/">changelog</a>.</p>
<h2 id="supported-operating-systems">Supported operating systems</h2>
<p>The Cloudflare One Client is guaranteed to support operating systems for the primary maintenance timespan provided by the vendors or maintainers. This is to ensure that security fixes in the Cloudflare One Client are always supported by security fixes in the underlying operating system.</p>
<h3 id="windows">Windows</h3>
<p>The Cloudflare One Client support policy for Windows follows <a href="https://learn.microsoft.com/en-us/lifecycle/">Microsoft's Lifecycle Policy</a>.</p>
<ul>
<li><strong>Windows 10 and 11</strong>: The Cloudflare One Client supports <a href="https://learn.microsoft.com/en-us/windows/release-health/supported-versions-windows-client">Windows client versions</a> as long as they remain in active servicing under Microsoft's Modern Lifecycle Policy. Enterprise LTSC editions must remain under Mainstream Support.</li>
<li><strong>Windows Server</strong>: Cloudflare One Client support for Windows Server is pending. Once testing is complete, our policy will be to support <a href="https://learn.microsoft.com/en-us/windows/release-health/windows-server-release-info">Windows Server LTSC releases</a> within their Mainstream Support window. Annual Channel releases of Windows Server will not be supported.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6107.md")
</aside>
<p>As of December 2025, the following versions of Windows are supported:</p>
<table>
<thead>
<tr>
<th>Windows version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>Windows 10 21H2 LTSC</td>
<td>January 2027</td>
</tr>
<tr>
<td>Windows 11 24H2 LTSC</td>
<td>October 2029</td>
</tr>
<tr>
<td>Windows 11 25H2</td>
<td>October 2027</td>
</tr>
<tr>
<td>Windows 11 24H2</td>
<td>October 2026</td>
</tr>
<tr>
<td>Windows Server 2025 LTSC</td>
<td>Pending full testing. Once complete, will be supported until November 2029.</td>
</tr>
<tr>
<td>Windows Server 2022 LTSC</td>
<td>Pending full testing. Once complete, will be supported until October 2026.</td>
</tr>
<tr>
<td>Windows Server 2019 LTSC</td>
<td><a href="#older-versions-of-windows-server">To be determined</a> as it is currently out of mainstream Microsoft support. Usage is highly discouraged.</td>
</tr>
</tbody>
</table>
<h4 id="older-versions-of-windows-server">Older versions of Windows Server</h4>
<p>The Cloudflare One Client will support the most recent Windows Server version that has left Microsoft's Mainstream Support window, as migration of Windows Server has been observed to take significantly longer than most operating systems. Once Windows Server releases have left Mainstream Support, the Cloudflare One Client does not guarantee an amount of time it will continue to be supported, though end of support will be announced 90 days in advance. We strongly recommend migrating as quickly as possible to supported versions of Windows Server to avoid incidents caused by unfixed bugs in the operating system. In all cases, the Cloudflare One Client will not attempt to fix security issues in the underlying operating system.</p>
<h4 id="windows-subsystem-for-linux-wsl">Windows Subsystem for Linux (WSL)</h4>
<p>Windows Subsystem for Linux v2 (WSLv2) is supported by the Cloudflare One Client that is installed on the Windows host (not a Cloudflare One Client running inside WSLv2), so long as the host version of Windows is supported.</p>
<h3 id="macos">macOS</h3>
<p>The Cloudflare One Client supports the current major version of macOS and the two previous major versions. Devices on a previous major version must have the latest minor and patch updates installed (for example, <code>26.6.1</code>) to receive support. This policy aligns with Apple's standard security update cycle, as well as the comparatively rapid release of new macOS versions compared to other desktop operating systems.</p>
<p>As of September 2026, the following major versions of macOS are supported:</p>
<table>
<thead>
<tr>
<th>macOS version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>macOS 27 (Golden Gate)</td>
<td>Release of 2029 major version</td>
</tr>
<tr>
<td>macOS 26 (Tahoe)</td>
<td>Release of 2028 major version</td>
</tr>
<tr>
<td>macOS 15 (Sequoia)</td>
<td>Release of 2027 major version</td>
</tr>
</tbody>
</table>
<h3 id="debian">Debian</h3>
<p>The Cloudflare One Client supports all Debian releases within their <a href="https://www.debian.org/releases/">standard EOL window</a>. Devices must be updated to the latest point release (for example, <code>12.12</code>) to receive support.</p>
<p>As of December 2025, the following versions of Debian are supported:</p>
<table>
<thead>
<tr>
<th>Debian version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>Debian 13 (Trixie)</td>
<td>June 2030</td>
</tr>
<tr>
<td>Debian 12 (Bookworm)</td>
<td>June 2028</td>
</tr>
</tbody>
</table>
<h3 id="ubuntu">Ubuntu</h3>
<p>The Cloudflare One Client supports all Ubuntu releases within their <a href="https://ubuntu.com/about/release-cycle">Standard Security Maintenance window</a>. Devices must be updated to the latest point release (for example, <code>22.04.5</code>) to receive support.</p>
<p>As of December 2025, the following versions of Ubuntu are supported:</p>
<table>
<thead>
<tr>
<th>Ubuntu version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ubuntu 26.04 (Resolute Raccoon)</td>
<td>April 2031</td>
</tr>
<tr>
<td>Ubuntu 25.10 (Questing Quokka)</td>
<td>July 2026</td>
</tr>
<tr>
<td>Ubuntu 25.04 (Plucky Puffin)</td>
<td>January 2026</td>
</tr>
<tr>
<td>Ubuntu 24.04 LTSC (Noble Numbat)</td>
<td>April 2029</td>
</tr>
<tr>
<td>Ubuntu 22.04 LTSC (Jammy Jellyfish)</td>
<td>April 2027</td>
</tr>
</tbody>
</table>
<h3 id="red-hat-enterprise-linux-rhel">Red Hat Enterprise Linux (RHEL)</h3>
<p>Cloudflare One Client support for RHEL is pending. Once testing is complete, our policy will be to support all major versions of RHEL within their <a href="https://access.redhat.com/product-life-cycles">Full Support window</a>. Devices must be updated to the latest minor release (for example, <code>9.4</code>) to receive support.</p>
<p>As of April 2026, only RHEL 8 has completed full compatibility testing, which is now out of the Red Hat Full Support window. Starting with Cloudflare One Client version 2026.6.822.0, RHEL 9 and RHEL 10 are supported for <a href="/mesh/">Cloudflare Mesh</a> functionality only.</p>
<p>This section will be updated as we add RHEL support to match Red Hat's support lifecycle.</p>
<table>
<thead>
<tr>
<th>RHEL version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>RHEL 10</td>
<td>Pending full testing. Supported for Cloudflare Mesh until May 2030.</td>
</tr>
<tr>
<td>RHEL 9</td>
<td>Pending full testing. Supported for Cloudflare Mesh until May 2027.</td>
</tr>
</tbody>
</table>
<h3 id="ios-and-ipados">iOS and iPadOS</h3>
<p>The Cloudflare One Client supports the current major version of iOS and iPadOS as well as the two previous major versions. Devices must have the latest available update installed (for example, <code>17.7.2</code>) to receive support. This policy aligns with Apple's standard security update cycle, as well as the comparatively rapid release of new iOS and iPadOS versions compared to other mobile operating systems.</p>
<p>As of December 2025, the following versions of iOS and iPadOS are supported:</p>
<table>
<thead>
<tr>
<th>iOS or iPadOS version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>iOS and iPadOS 26</td>
<td>Release of 2028 major version</td>
</tr>
<tr>
<td>iOS and iPadOS 18</td>
<td>Release of 2027 major version</td>
</tr>
<tr>
<td>iOS and iPadOS 17</td>
<td>Release of 2026 major version</td>
</tr>
</tbody>
</table>
<h3 id="android">Android</h3>
<p>The Cloudflare One Client supports the current major Android release and the three previous major releases. Devices must have the latest available <a href="https://source.android.com/docs/security/bulletin/asb-overview">Android Security Patch Level</a> installed to receive support.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6106.md")
</aside>
<p>As of December 2025, the following versions of Android are supported:</p>
<table>
<thead>
<tr>
<th>Android version</th>
<th>Supported until</th>
</tr>
</thead>
<tbody>
<tr>
<td>Android 16</td>
<td>Release of 2029 major version</td>
</tr>
<tr>
<td>Android 15</td>
<td>Release of 2028 major version</td>
</tr>
<tr>
<td>Android 14</td>
<td>Release of 2027 major version</td>
</tr>
<tr>
<td>Android 13</td>
<td>Release of 2026 major version</td>
</tr>
<tr>
<td>Android 9-12</td>
<td>Not officially supported, but expected to generally work.</td>
</tr>
</tbody>
</table>
<h3 id="chromeos">ChromeOS</h3>
<p>The Cloudflare One Client supports only the current ChromeOS release on the Stable, LTS, and LTSC channels.</p>
<p>Unlike other operating systems listed in this document, specific ChromeOS version numbers are not tracked here due to the rapid release cadence of the platform (approximately every four weeks to six months). Refer to the official <a href="https://chromiumdash.appspot.com/schedule">ChromeOS Release Schedule</a> to verify the current version for your channel.</p>
