<p>Periodically, you may need to update your key server when using Cloudflare's Keyless SSL.</p>
<p>To upgrade your key server:</p>
<ol>
<li>Back up the contents of <code>/etc/keyless</code>.</li>
<li>Update your OS’ package listings, for example, <code>apt-get update</code> or <code>yum update</code>.</li>
<li>Upgrade the gokeyless server:</li>
<li>Debian/Ubuntu: <code>apt-get upgrade gokeyless</code></li>
<li>RHEL/CentOS: <code>yum install gokeyless</code></li>
<li>Restart the keyless instance:</li>
<li>systemd: <code>service gokeyless restart</code></li>
<li>upstart/sysvinit: <code>/etc/init.d/gokeyless restart</code></li>
<li>Confirm that HTTPS connections are working as expected.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14002.md")
</aside>
