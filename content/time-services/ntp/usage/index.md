---
cp9:
  canonical: https://developers.cloudflare.com/time-services/ntp/usage/
  description: Guide for consuming randomness from drand.
  full_title: Using Cloudflare's Time Service · Cloudflare Time Services docs
  head_html: <title>Using Cloudflare&#x27;s Time Service · Cloudflare Time Services docs</title><meta name="generator" content="Nift"><meta name="description" content="Guide for consuming randomness from drand."><link rel="canonical" href="https://developers.cloudflare.com/time-services/ntp/usage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/time-services/ntp/usage/index.md"><meta property="og:title" content="Using Cloudflare&#x27;s Time Service · Cloudflare Time Services docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Guide for consuming randomness from drand."><meta property="og:url" content="https://developers.cloudflare.com/time-services/ntp/usage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Time Services"><meta name="algolia_product_filter" content="Time Services"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Time Services"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/time-services/ntp/usage/#page","headline":"Using Cloudflare's Time Service \u00b7 Cloudflare Time Services docs","description":"Guide for consuming randomness from drand.","url":"https://developers.cloudflare.com/time-services/ntp/usage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /time-services/ntp/usage/
  schema: 1
---
<p><a href="https://tools.ietf.org/html/rfc1305">Network Time Protocol</a> (NTP) is an Internet protocol designed to synchronize time between computer systems communicating over unreliable and variable-latency network paths. Cloudflare offers its version of NTP for free so you can use our <a href="https://www.cloudflare.com/network/">global anycast network</a> to synchronize time from our closest server.</p>
<p>To use our NTP server, change the time configuration in your device to point to <code>time.cloudflare.com</code>.</p>
<h2 id="macos">macOS</h2>
<p>To have your Mac to synchronize time from <code>time.cloudflare.com</code>:</p>
<ol>
<li>Go to <strong>System Settings</strong>.</li>
<li>Go to <strong>General</strong> &gt; <strong>Date &amp; Time</strong>.</li>
<li>Enable <strong>Set date and time automatically</strong>.</li>
<li>For <strong>Source</strong>, select <strong>Set...</strong> and enter <code>time.cloudflare.com</code> in the text field that appears.</li>
</ol>
<p><img src="/assets/upstream/images/time-services/mactime.png" alt="Screenshot of updating the Date &amp; Time settings on machine running macOS" /></p>
<h2 id="windows">Windows</h2>
<p>To have your Windows machine synchronize time from <code>time.cloudflare.com</code>:</p>
<ol>
<li>Go to <strong>Control Panel</strong>.</li>
<li>Go to <strong>Clock and Region</strong>.</li>
<li>Click <strong>Date and Time</strong>.</li>
<li>Go to the <strong>Internet Time</strong> tab.</li>
<li>Click <strong>Change settings..</strong></li>
<li>For <strong>Server:</strong>, type <code>time.cloudflare.com</code> and click <strong>Update now</strong>.</li>
<li>Click <strong>OK</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/time-services/window.png" alt="Screenshot of updating the Date and Time settings on machine running Windows" /></p>
<h2 id="linux">Linux</h2>
<p>Cloudflare's time servers are included in <a href="https://www.ntppool.org/en/">pool.ntp.org</a> which is the default time service for many Linux distributions and network appliances. If your NTP client is synchronizing from one of the below servers, you are already using Cloudflare's time services.</p>
<ul>
<li><a href="https://www.ntppool.org/scores/162.159.200.1">162.159.200.1</a></li>
<li><a href="https://www.ntppool.org/scores/162.159.200.123">162.159.200.123</a></li>
<li><a href="https://www.ntppool.org/scores/2606:4700:f1::1">2606:4700:f1::1</a></li>
<li><a href="https://www.ntppool.org/scores/2606:4700:f1::123">2606:4700:f1::123</a></li>
</ul>
<p>To manually configure your NTP client to use our time service, please first refer to the documentation for your Linux distribution to determine which NTP client you are using and where the configuration files are stored.</p>
<p>For example:</p>
<ul>
<li><a href="https://ubuntu.com/server/docs/about-time-synchronisation">Ubuntu</a></li>
<li><a href="https://wiki.debian.org/NTP">Debian</a></li>
<li><a href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-configuring_ntp_using_the_chrony_suite">RHEL</a></li>
</ul>
<p>Exact configuration will vary by Linux distribution, but below are some example configurations for popular clients:</p>
<h3 id="chrony-https-chrony-project-org"><a href="https://chrony-project.org">chrony</a></h3>
<ol>
<li>Add <code>time.cloudflare.com</code> as a server in the configuration file on your system (e.g., <code>/etc/chrony/chrony.conf</code>)</li>
</ol>
<pre tabindex="0"><code>server time.cloudflare.com iburst&#10;</code></pre>
<ol start="2">
<li>Restart the chronyd service.</li>
</ol>
<pre tabindex="0"><code>systemctl restart chronyd&#10;</code></pre>
<h3 id="systemd-timesyncd-https-man7-org-linux-man-pages-man5-timesyncd-conf-5-html"><a href="https://man7.org/linux/man-pages/man5/timesyncd.conf.5.html">systemd-timesyncd</a></h3>
<ol>
<li>Add <code>time.cloudflare.com</code> to the <code>[Time]</code> section of the configuration file on your system (e.g., <code>/etc/systemd/timesyncd.conf</code>)</li>
</ol>
<pre tabindex="0"><code>[Time]&#10;NTP=time.cloudflare.com&#10;</code></pre>
<ol start="2">
<li>Restart the systemd-timesyncd service.</li>
</ol>
<pre tabindex="0"><code>systemctl restart systemd-timesyncd&#10;</code></pre>
<h3 id="ntpd-https-linux-die-net-man-5-ntp-conf"><a href="https://linux.die.net/man/5/ntp.conf">ntpd</a></h3>
<ol>
<li>Add <code>time.cloudflare.com</code> as a server in the configuration file on your system (e.g., <code>/etc/ntp.conf</code>)</li>
</ol>
<pre tabindex="0"><code>server time.cloudflare.com iburst&#10;</code></pre>
<ol start="2">
<li>Restart the ntpd service.</li>
</ol>
<pre tabindex="0"><code>systemctl restart ntpd&#10;</code></pre>
