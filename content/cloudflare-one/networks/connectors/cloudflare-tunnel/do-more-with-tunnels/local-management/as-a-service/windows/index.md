---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/
  description: Windows in Zero Trust networking.
  full_title: Run as a service on Windows · Cloudflare One docs
  head_html: <title>Run as a service on Windows · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Windows in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/index.md"><meta property="og:title" content="Run as a service on Windows · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Windows in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Windows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/#page","headline":"Run as a service on Windows \u00b7 Cloudflare One docs","description":"Windows in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Windows"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/windows/
  schema: 1
---
<p>You can install <code>cloudflared</code> as a system service on Windows.</p>
<h2 id="configure-cloudflared-as-a-service">Configure <code>cloudflared</code> as a service</h2>
<p>By default, Cloudflare Tunnel expects all of the configuration to exist in the <code>%USERPROFILE%\.cloudflared\config.yml</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/">configuration file</a>. At a minimum you must specify the following arguments to run as a service:</p>
<table>
<thead>
<tr>
<th>Argument</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tunnel</code></td>
<td>The UUID of your tunnel</td>
</tr>
<tr>
<td><code>credentials-file</code></td>
<td>The location of the credentials file for your tunnel</td>
</tr>
</tbody>
</table>
<h2 id="run-cloudflared-as-a-service">Run <code>cloudflared</code> as a service</h2>
<ol>
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Download</a> the latest <code>cloudflared</code> version.</p>
</li>
<li>
<p>Create a new directory:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">C:\Cloudflared\bin&#10;</code></pre>
<ol start="3">
<li>
<p>Copy the <code>.exe</code> file you downloaded in step 1 to the new directory and rename it to <code>cloudflared.exe</code>.</p>
</li>
<li>
<p>Open CMD as an administrator and go to <code>C:\Cloudflared\bin</code>.</p>
</li>
<li>
<p>Run this command to install <code>cloudflared</code>:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">cloudflared.exe service install&#10;</code></pre>
<ol start="6">
<li>Next, run this command to create another directory:</li>
</ol>
<pre tabindex="0"><code class="language-bash">mkdir C:\Windows\System32\config\systemprofile\.cloudflared&#10;</code></pre>
<ol start="7">
<li>Log in and authenticate <code>cloudflared</code>:</li>
</ol>
<pre tabindex="0"><code class="language-bash">cloudflared.exe login&#10;</code></pre>
<ol start="8">
<li>The login command will generate a <code>cert.pem</code> file and save it to your user profile by default. Copy the file to the <code>.cloudflared</code> folder created in step 5 using this command:</li>
</ol>
<pre tabindex="0"><code class="language-bash">copy C:\Users\%USERNAME%\.cloudflared\cert.pem C:\Windows\System32\config\systemprofile\.cloudflared\cert.pem&#10;</code></pre>
<ol start="9">
<li>Next, create a tunnel:</li>
</ol>
<pre tabindex="0"><code class="language-bash">cloudflared.exe tunnel create &lt;Tunnel Name&gt;&#10;</code></pre>
<p>This will generate a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/local-tunnel-terms/#credentials-file">credentials file</a> in <code>.json</code> format.</p>
<ol start="10">
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#4-create-a-configuration-file">Create a configuration file</a> with the
following content:</li>
</ol>
<pre tabindex="0"><code class="language-txt">tunnel: &lt;Tunnel ID&gt;&#10;credentials-file: C:\Windows\System32\config\systemprofile\.cloudflared\&lt;Tunnel-ID&gt;.json&#10;&#35; Uncomment the following two lines if you are using self-signed certificates in your origin server&#10;&#35; originRequest:&#10;&#35;   noTLSVerify: true&#10;&#10;ingress:&#10;  &#45; hostname: app.mydomain.com&#10;    service: https://internal.mydomain.com&#10;  &#45; service: http_status:404&#10;logfile:  C:\Cloudflared\cloudflared.log&#10;</code></pre>
<ol start="11">
<li>Copy the credentials file to the folder created in step 6:</li>
</ol>
<pre tabindex="0"><code class="language-bash">copy C:\Users\%USERNAME%\.cloudflared\&lt;Tunnel-ID&gt;.json C:\Windows\System32\config\systemprofile\.cloudflared\&lt;Tunnel-ID&gt;.json&#10;</code></pre>
<ol start="12">
<li>Validate the ingress rule entries in your configuration file using the command:</li>
</ol>
<pre tabindex="0"><code class="language-bash">cloudflared.exe tunnel ingress validate&#10;</code></pre>
<ol start="13">
<li>
<p>In the Registry Editor, go to <code>Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Cloudflared</code>.</p>
</li>
<li>
<p>In the Cloudflared registry entry, modify <code>ImagePath</code> to point to the <code>cloudflared.exe</code> and <code>config.yml</code> files. Make sure that there are no extra spaces or characters while you modify the registry entry, as this could cause problems with starting the service.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">C:\Cloudflared\bin\cloudflared.exe --config=C:\Windows\System32\config\systemprofile\.cloudflared\config.yml tunnel run&#10;</code></pre>
<ol start="15">
<li>If the service does not start, run the following command from <code>C:\Cloudflared\bin</code>:</li>
</ol>
<pre tabindex="0"><code class="language-bash">sc start cloudflared&#10;</code></pre>
<pre tabindex="0"><code>You will see the output below:&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">SERVICE_NAME: cloudflared&#10;        TYPE               : 10  WIN32_OWN_PROCESS&#10;        STATE              : 2  START_PENDING&#10;                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)&#10;        WIN32_EXIT_CODE    : 0  (0x0)&#10;        SERVICE_EXIT_CODE  : 0  (0x0)&#10;        CHECKPOINT         : 0x0&#10;        WAIT_HINT          : 0x7d0&#10;        PID                : 3548&#10;        FLAGS              :&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>You can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#5-start-routing-traffic">route traffic through your tunnel</a>. If you add IP routes or otherwise change the configuration, restart the service to load the new configuration:</p>
<pre tabindex="0"><code class="language-bash">sc stop cloudflared&#10;sc start cloudflared&#10;</code></pre>
