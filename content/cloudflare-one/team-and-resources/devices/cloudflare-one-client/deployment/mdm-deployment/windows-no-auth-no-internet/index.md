<h2 id="availability">Availability <span class="nb-badge">Beta</span></h2>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6333.md")
</div></details>
<p>When <strong>no-auth-no-internet</strong> is enabled, the Cloudflare One Client locks down general internet traffic on the device whenever the device is in an unauthenticated state (i.e., without a valid device registration). During this lockdown, the client allows only the traffic required for the device to remain on the network and for the user to complete IdP authentication. Once the user signs in, normal connectivity resumes and your configured Gateway, Access, RBI, and DLP policies take effect.</p>
<p>When this feature is enabled, the authentication is done via in-app WebView2 browser instead of the default browser on the system.</p>
<p>The lockdown re-engages automatically any time the device transitions back to an unauthenticated state — for example, if the registration is deleted/revoked, another OS user that has never authenticated with the Cloudflare One Client logs in while in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a>, or the user switches into a new organization.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>The Cloudflare One Client must be <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#windows">deployed via MDM</a>.</li>
<li>The device must have <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#authenticate-in-embedded-browser">WebView2</a> available. By default, the WebView2 runtime should be present on all Windows versions that Cloudflare One Client supports.</li>
</ul>
<h2 id="enable-no-auth-no-internet">Enable no-auth-no-internet</h2>
<p>To enable the feature, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#windows">deploy an MDM file</a> with the <code>no_auth_no_internet</code> top-level key set to <code>true</code>:</p>
<pre><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;no_auth_no_internet&lt;/key&gt;&#10;  &lt;true/&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;your-team-name&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Default&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>When the Cloudflare One Client reads this configuration and detects that no user is authenticated, it applies the firewall lockdown and prompts the user to authenticate. After successful authentication, the lockdown is completely lifted.</p>
<h2 id="block-access-to-rfc-1918-ranges-in-lockdown-state">Block access to RFC 1918 ranges in lockdown state</h2>
<p>By default, the Cloudflare One Client permits traffic to <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> private address ranges (<code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, and <code>192.168.0.0/16</code>) while the device is locked down. This allows the device to reach on-premise resources such as a domain controller, an MDM server, or a local printer before the user authenticates.</p>
<p>To block RFC 1918 traffic during lockdown, set <code>no_auth_no_internet_block_rfc_1918</code> to <code>true</code>:</p>
<pre><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;no_auth_no_internet&lt;/key&gt;&#10;  &lt;true/&gt;&#10;  &lt;key&gt;no_auth_no_internet_block_rfc_1918&lt;/key&gt;&#10;  &lt;true/&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;your-team-name&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Default&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li>The lockdown is enforced only when there is an active interactive user session (for example, a user is logged in and the device is not locked).</li>
<li>Since authentication now occurs in an embedded WebView2 window, IdP flows that depend on the user's default browser (for example, browser-specific extensions or password managers) may not work.</li>
<li>Some Windows applications, including Copilot and Teams (personal), may retain internet access while the Cloudflare One Client authentication window is open.</li>
</ul>
