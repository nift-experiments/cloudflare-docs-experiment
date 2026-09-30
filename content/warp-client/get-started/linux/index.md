<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-zero-trust">Looking for Zero Trust?</h3>
@markup("md", "content/.markup/bodies/15772.md")
</aside>
<p>You have two ways of installing WARP on Linux, depending on the distro you are using:</p>
<ul>
<li>Find the latest WARP client in the <a href="https://pkg.cloudflareclient.com/">package repository</a>.</li>
<li>Install the <code>cloudflare-warp</code> package that suits your distro:
<ul>
<li><strong>apt-based OS</strong> (like Ubuntu): <code>sudo apt install cloudflare-warp</code>.</li>
<li><strong>yum-based OS</strong> (like CentOS or RHEL): <code>sudo yum install cloudflare-warp</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15771.md")
</aside>
<h2 id="using-warp">Using WARP</h2>
<p>The command line interface is the primary way to use WARP.</p>
<h3 id="initial-connection">Initial connection</h3>
<p>To connect for the very first time:</p>
<ol>
<li>Register the client <code>warp-cli registration new</code>.</li>
<li>Connect <code>warp-cli connect</code>.</li>
<li>Run <code>curl https://www.cloudflare.com/cdn-cgi/trace</code> and verify that <code>warp=on</code>.</li>
</ol>
<h3 id="switch-modes">Switch modes</h3>
<p>You can use <code>warp-cli mode --help</code> to get a list of modes to switch between. For example:</p>
<ul>
<li><strong>DNS only mode via DoH:</strong> <code>warp-cli mode doh</code></li>
<li><strong>WARP with DoH:</strong> <code>warp-cli mode warp+doh</code></li>
</ul>
<h3 id="switch-tunnel-protocol">Switch tunnel protocol</h3>
<p>You can switch the protocol that WARP uses to route traffic from the device to Cloudflare.</p>
<ul>
<li><strong>WireGuard:</strong> <code>warp-cli tunnel protocol set WireGuard</code></li>
<li><strong>MASQUE:</strong> (default) <code>warp-cli tunnel protocol set MASQUE</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15770.md")
</aside>
<p>For information on WireGuard versus MASQUE, refer to our <a href="https://blog.cloudflare.com/zero-trust-warp-with-a-masque">blog post</a>.</p>
<h3 id="using-1-1-1-1-for-families">Using 1.1.1.1 for Families</h3>
<p>The Linux client supports all 1.1.1.1 for Families modes, in either WARP on DNS-only mode:</p>
<ul>
<li><strong>Families mode off:</strong> <code>warp-cli dns families off</code></li>
<li><strong>Malware protection:</strong> <code>warp-cli dns families malware</code></li>
<li><strong>Malware and adult content:</strong> <code>warp-cli dns families full</code></li>
</ul>
<h3 id="enable-warp-unlimited">Enable WARP+ Unlimited</h3>
<p>To enable <a href="/warp-client/warp-modes/#warp-unlimited">WARP+ Unlimited</a> on Linux, you will need an iOS or Android device that has an existing WARP+ Unlimited subscription.</p>
<ol>
<li>On your iOS or Android device, launch the <strong>1.1.1.1 Faster Internet</strong> app.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Account</strong> and copy the <strong>Key</strong> value.</li>
<li>On your Linux device, run the following command:</li>
</ol>
<pre><code class="language-sh">warp-cli registration license &lt;KEY&gt;&#10;</code></pre>
<ol start="4">
<li>Verify the new registration:</li>
</ol>
<pre><code class="language-sh">warp-cli registration show&#10;</code></pre>
<pre><code class="language-sh">Account type: Unlimited&#10;...&#10;</code></pre>
<p>Your WARP+ Unlimited subscription is now active on this device.</p>
<h3 id="additional-commands">Additional commands</h3>
<p>A complete list of all supported commands can be found by running:</p>
<pre><code class="language-sh">warp-cli --help&#10;</code></pre>
<h2 id="feedback">Feedback</h2>
<p>You can find logs required to debug WARP issues by running <code>sudo warp-diag</code>. This will place a <code>warp-debugging-info.zip</code> file in the path from which you ran the command.</p>
<p>To report bugs or provide feedback to the team use the command <code>sudo warp-diag feedback</code>. This will submit a support ticket.</p>
