<p>When users connect to an Access application through <code>cloudflared</code>, the browser prompts them to allow access by displaying this page:</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/non-http/access-screen.png" alt="Access request prompt page displayed after logging in with cloudflared." /></p>
<p>Automatic <code>cloudflared</code> authentication allows users to skip this login page if they already have an active IdP session.</p>
<p>To enable automatic <code>cloudflared</code> authentication:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate your application and select <strong>Configure</strong>.</li>
<li>Go to <strong>Authentication</strong>.</li>
<li>Turn on <strong>Allow automatic Cloudflared authentication</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>This option will still prompt a browser window in the background, but authentication will now happen automatically.</p>
