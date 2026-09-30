---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/
  description: OS version in Zero Trust.
  full_title: OS version · Cloudflare One docs
  head_html: <title>OS version · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="OS version in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/index.md"><meta property="og:title" content="OS version · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="OS version in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/#page","headline":"OS version \u00b7 Cloudflare One docs","description":"OS version in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/os-version/
  schema: 1
---
<p>The OS Version device posture attribute checks whether the version of a device's operating system matches, is greater than or lesser than the configured value.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-os-version-check">Enable the OS version check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>OS version</strong>.</li>
<li>Configure the <strong>Operating system</strong>, <strong>Operator</strong>, and <strong>Version</strong> fields to specify the <a href="#determine-the-os-version">OS version</a> you want devices to match.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5911.md")
</aside>
<ol start="5">
<li>(Optional) Configure additional OS-specific fields:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5916.md")
</div></div>
<ol start="6">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the OS version check is returning the expected results.</p>
<h2 id="determine-the-os-version">Determine the OS version</h2>
<p>Operating systems display version numbers in different ways. This section covers how to retrieve the version number in each OS, in a format matching what the OS version posture check expects.</p>
<h3 id="macos">macOS</h3>
<ol>
<li>Open a terminal window.</li>
<li>Use the <code>defaults</code> command to check for the value of <code>SystemVersionStampAsString</code>.</li>
</ol>
<pre tabindex="0"><code class="language-sh">defaults read loginwindow SystemVersionStampAsString&#10;</code></pre>
<h3 id="windows">Windows</h3>
<p>Windows version numbers consist of four parts: <code>Major.Minor.Build.UBR</code>. For example, <code>10.0.19045.3803</code> where:</p>
<ul>
<li><code>10.0</code> is the <strong>Version</strong> (Major.Minor)</li>
<li><code>19045</code> is the <strong>Build</strong> number</li>
<li><code>3803</code> is the <strong>UBR</strong> (Update Build Revision)</li>
</ul>
<p>To determine the Windows version on your device:</p>
<ol>
<li>Open a PowerShell window.</li>
<li>Get the <strong>Version</strong> (Major.Minor.Build):</li>
</ol>
<pre tabindex="0"><code class="language-bash">(Get-CimInstance Win32_OperatingSystem).version&#10;</code></pre>
<p>This returns the version in the format <code>Major.Minor.Build</code> (for example, <code>10.0.19045</code>).</p>
<ol start="3">
<li>Get the <strong>UBR</strong> (Update Build Revision):</li>
</ol>
<pre tabindex="0"><code class="language-bash">(Get-ItemProperty -Path &quot;HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion&quot; -Name UBR).UBR&#10;</code></pre>
<p>This returns the UBR value (for example, <code>3803</code>).</p>
<h3 id="linux">Linux</h3>
<h4 id="os-version">OS version</h4>
<p>The Linux OS version check reads the system kernel version.</p>
<ol>
<li>
<p>Open a Terminal window.</p>
</li>
<li>
<p>Run the <code>uname -r</code> command to get the complete kernel version. For example,</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">$ uname -r&#10;5.14.0-25.el9.x86_64&#10;</code></pre>
<ol start="3">
<li>
<p><strong>Version</strong> is the first three numbers of the output in SemVer format (<code>5.14.0</code>).</p>
</li>
<li>
<p><strong>Patch Version</strong> is the first number after the SemVer (<code>25</code>).</p>
</li>
</ol>
<h4 id="distro-version">Distro version</h4>
<p>The Cloudflare One Client reads <strong>Distro name</strong> and <strong>Distro revision</strong> from the <code>/etc/os-release</code> file. The name comes from the <strong>ID</strong> field, and the revision comes from the <strong>VERSION_ID</strong> field.</p>
<p>To determine the Linux distro version on your device:</p>
<ol>
<li>
<p>Open a Terminal window.</p>
</li>
<li>
<p>Get the OS identification fields that contain <code>ID</code>:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">cat /etc/os-release | grep &quot;ID&quot;&#10;</code></pre>
<ol start="3">
<li>If the output of the above command contained <code>ID=ubuntu</code> and <code>VERSION_ID=22.04</code>, <strong>Distro name</strong> would be <code>ubuntu</code> and <strong>Distro revision</strong> would be <code>22.04</code>. The Cloudflare One Client will check these strings for an exact match.</li>
</ol>
<h3 id="chromeos">ChromeOS</h3>
<p>ChromeOS version numbers consist of <a href="https://www.chromium.org/developers/version-numbers/">four parts</a>: <code>MAJOR.MINOR.BUILD.PATCH</code>. The OS version posture check returns <code>MAJOR.MINOR.BUILD</code>.</p>
<p>To determine the ChromeOS version on your device:</p>
<ol>
<li>Open Chrome browser and go to <code>chrome://system</code>.</li>
<li>Find the following values:</li>
</ol>
<table>
<thead>
<tr>
<th>Property</th>
<th>OS version component</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CHROMEOS_RELEASE_CHROME_MILESTONE</code></td>
<td><code>MAJOR</code></td>
</tr>
<tr>
<td><code>CHROMEOS_RELEASE_BUILD_NUMBER</code></td>
<td><code>MINOR</code></td>
</tr>
<tr>
<td><code>CHROMEOS_RELEASE_BRANCH_NUMBER</code></td>
<td><code>BUILD</code></td>
</tr>
</tbody>
</table>
3. The OS version in Semver format is `MAJOR.MINOR.BUILD` (for example, `103.14816.131`).
