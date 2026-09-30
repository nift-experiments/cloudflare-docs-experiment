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
<pre><code>server time.cloudflare.com iburst&#10;</code></pre>
<ol start="2">
<li>Restart the chronyd service.</li>
</ol>
<pre><code>systemctl restart chronyd&#10;</code></pre>
<h3 id="systemd-timesyncd-https-man7-org-linux-man-pages-man5-timesyncd-conf-5-html"><a href="https://man7.org/linux/man-pages/man5/timesyncd.conf.5.html">systemd-timesyncd</a></h3>
<ol>
<li>Add <code>time.cloudflare.com</code> to the <code>[Time]</code> section of the configuration file on your system (e.g., <code>/etc/systemd/timesyncd.conf</code>)</li>
</ol>
<pre><code>[Time]&#10;NTP=time.cloudflare.com&#10;</code></pre>
<ol start="2">
<li>Restart the systemd-timesyncd service.</li>
</ol>
<pre><code>systemctl restart systemd-timesyncd&#10;</code></pre>
<h3 id="ntpd-https-linux-die-net-man-5-ntp-conf"><a href="https://linux.die.net/man/5/ntp.conf">ntpd</a></h3>
<ol>
<li>Add <code>time.cloudflare.com</code> as a server in the configuration file on your system (e.g., <code>/etc/ntp.conf</code>)</li>
</ol>
<pre><code>server time.cloudflare.com iburst&#10;</code></pre>
<ol start="2">
<li>Restart the ntpd service.</li>
</ol>
<pre><code>systemctl restart ntpd&#10;</code></pre>
