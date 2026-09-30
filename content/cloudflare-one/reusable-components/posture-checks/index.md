<p>With Cloudflare Zero Trust, you can configure Zero Trust policies that rely on additional signals from the Cloudflare One Client or from third-party endpoint security providers. When device posture checks are configured, users can only connect to a protected application or network resource if they have a managed or healthy device.</p>
<h2 id="1-enable-device-posture-checks"><ol>
<li>Enable device posture checks</li>
</ol></h2>
<p>Setup instructions and requirements vary depending on the device posture attribute. Refer to the links below to view the setup guide for your provider.</p>
<ul>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client checks</a> are performed by the Cloudflare One Client.</li>
<li><a href="/cloudflare-one/integrations/service-providers/">Service-to-service checks</a> are performed by third-party device posture providers.</li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/access-integrations/">Access integration checks</a> are only configurable for Access applications. These attributes cannot be used in Gateway policies.</li>
</ul>
<h2 id="2-verify-device-posture-checks"><ol start="2">
<li>Verify device posture checks</li>
</ol></h2>
<p>Before integrating a device posture check in a Gateway or Access policy, verify that the Pass/Fail results match your expectations. To view the latest test results for a specific device:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
<li>Select the device.</li>
<li>Select <strong>View details</strong>.</li>
<li>Select the <strong>Posture checks</strong> tab.</li>
</ol>
<h2 id="3-build-a-device-posture-policy"><ol start="3">
<li>Build a device posture policy</li>
</ol></h2>
<p>You can now use your device posture check in an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> or a Gateway <a href="/cloudflare-one/traffic-policies/network-policies/common-policies/#enforce-device-posture">network</a> or <a href="/cloudflare-one/traffic-policies/http-policies/common-policies/#check-device-posture">HTTP</a> policy. In Access, the enabled device posture attributes will appear in the list of available <a href="/cloudflare-one/access-controls/policies/#selectors">selectors</a>. In Gateway, the attributes will appear when you choose the <a href="/cloudflare-one/traffic-policies/network-policies/#device-posture">Passed Device Posture Check</a> selector.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="gateway-policy-limitation">Gateway policy limitation</h3>
@markup("md", "content/.markup/bodies/5894.md")
</aside>
<h2 id="4-ensure-traffic-is-going-through-the-cloudflare-one-client"><ol start="4">
<li>Ensure traffic is going through the Cloudflare One Client</li>
</ol></h2>
<p><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client</a> and <a href="/cloudflare-one/integrations/service-providers/">service-to-service</a> posture checks rely on traffic going through the Cloudflare One Client to detect posture information for a device. In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel configuration</a>, ensure that the following domains are included in the Cloudflare One Client:</p>
<ul>
<li>The IdP used to authenticate to Cloudflare Zero Trust if posture check is part of an Access policy.</li>
<li><code>&lt;your-team-name&gt;.cloudflareaccess.com</code> if posture check is part of an Access policy.</li>
<li>The application protected by the Access or Gateway policy.</li>
</ul>
<h2 id="policy-enforcement-rate">Policy enforcement rate</h2>
<p>Access detects changes in device posture at the same rate as the <a href="#polling-frequency">polling frequency</a> configured for the posture check.</p>
<p>Because Gateway evaluates network and HTTP policies on every request, it maintains a local cache of posture results that is only updated every five minutes. Therefore, Gateway policies are subject to an additional five-minute delay. For example, if you set your polling frequency to 10 minutes, it may take up to 15 minutes for Gateway to detect posture changes on a device.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Device posture policy enforcement&#10;A[Device] --schedule--&gt; B[Cloudflare One Client]--&gt; C((Cloudflare)) --&gt; D[Access policy]&#10;C --5 min--&gt; E[Cache] --&gt; F[Gateway policy]&#10;A --&gt; G[Service provider] --interval--&gt; C&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5893.md")
</aside>
<h3 id="expiration">Expiration</h3>
<p>By default, the posture result on Cloudflare remains valid until it is overwritten by new data. You can specify an <code>expiration</code> time using our <a href="/api/resources/zero_trust/subresources/devices/subresources/posture/methods/update/">API</a>. Cloudflare recommends setting the expiration to be at least double the <a href="#polling-frequency">polling frequency</a>. For example, if the posture check polling frequency is set to one hour, its expiration time should be set to two hours or greater.</p>
<h3 id="polling-frequency">Polling frequency</h3>
<h4 id="cloudflare-one-client-checks">Cloudflare One Client checks</h4>
<p>By default, the Cloudflare One Client polls the device for status changes every five minutes. To modify the polling frequency, use the API to update the <a href="/api/resources/zero_trust/subresources/devices/subresources/posture/methods/update/"><code>schedule</code></a> parameter.</p>
<h4 id="service-provider-checks">Service provider checks</h4>
<p>When setting up a <a href="/cloudflare-one/integrations/service-providers/">service-to-service integration</a>, you will choose a polling frequency to determine how often Cloudflare will query the third-party API. To set the polling frequency via the API, use the <a href="/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/edit/"><code>interval</code></a> parameter.</p>
