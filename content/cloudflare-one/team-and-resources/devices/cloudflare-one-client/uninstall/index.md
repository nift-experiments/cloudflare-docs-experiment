<p>The following procedures will uninstall the Cloudflare One Client (formerly WARP) from your device. If you used the Cloudflare One Client to deploy a root certificate, the certificate will also be removed.</p>
<h2 id="windows">Windows</h2>
<ol>
<li>Go to Windows Settings (Windows Key + I).</li>
<li>Select <strong>Apps</strong>.</li>
<li>Select <strong>Installed Apps</strong>.</li>
<li>Scroll to find the Cloudflare One Client application, click the three dots (...), and select <strong>Uninstall</strong>.</li>
</ol>
<h2 id="macos">macOS</h2>
<p>We include an uninstall script as part of the macOS package that you originally used.</p>
<ol>
<li>To find and run the uninstall script, run the following commands:</li>
</ol>
<pre><code class="language-sh">cd /Applications/Cloudflare\ WARP.app/Contents/Resources&#10;./uninstall.sh&#10;</code></pre>
<ol start="2">
<li>If prompted, enter your admin credentials to proceed with the uninstall.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6051.md")
</aside>
<h2 id="linux">Linux</h2>
<p>On CentOS 8, RHEL 8:</p>
<pre><code class="language-sh">sudo yum remove cloudflare-warp&#10;</code></pre>
<p>On Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04, Debian 9, Debian 10, Debian 11:</p>
<pre><code class="language-sh">sudo apt remove cloudflare-warp&#10;</code></pre>
<h2 id="ios-and-android">iOS and Android</h2>
<ol>
<li>Find the Cloudflare One Agent application (or the legacy 1.1.1.1 application) on the home screen.</li>
<li>Select and hold the application tile, and then select <strong>Remove App</strong>.</li>
<li>Select <strong>Delete App</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6050.md")
</aside>
