<p>Kentik is a network observability company that helps detect attacks on your network and triggers Cloudflare's Magic Transit to begin advertisement. Together, Kentik and Magic Transit On Demand work to create a fully Software-as-a-Service (SaaS)-based, Distributed Denial of Service (<a href="/ddos-protection/">DDoS</a>) protection solution to help you mitigate attacks and protect your network automatically.</p>
<p>In this tutorial, the example scenario includes two mitigations, one which pulls the advertisement from the router and a second mitigation that makes an API call to Cloudflare to begin advertising the prefixes from Cloudflare's global network.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You will need the email address associated with your Cloudflare account, Cloudflare Account ID, and Cloudflare API token to configure the connection for Magic Transit in Kentik.</p>
<h2 id="configure-the-kentik-portal">Configure the Kentik portal</h2>
<ol>
<li>
<p>Log in to your Kentik account.</p>
</li>
<li>
<p>Select <strong>Menu</strong> &gt; <strong>Settings</strong>.</p>
</li>
<li>
<p>From the <strong>Settings</strong> page under <strong>Customizations</strong>, select <strong>Mitigations</strong>.</p>
</li>
<li>
<p>On the <strong>Configure Mitigations</strong> page, locate the <strong>Cloudflare</strong> section.</p>
</li>
<li>
<p>Select <strong>Edit</strong> next to the Cloudflare branded mitigation to edit and review the information.</p>
<p>In the following example, section 2 uses the Cloudflare email address, Account ID, and API token to send the API call to Cloudflare to begin advertising routes and turn on Magic Transit for the customer's network.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/magic-transit/kentik-setup.png" alt="Kentik mitigation setup" /></p>
<ol start="6">
<li>
<p>After reviewing the information, select <strong>Update Mitigation Platform</strong>.</p>
</li>
<li>
<p>Select <strong>Menu</strong> &gt; <strong>Library</strong>.</p>
</li>
<li>
<p>On the <strong>Library</strong> page, in the search field, enter <strong>Cloudflare</strong>.</p>
</li>
<li>
<p>Under <strong>Uncategorized Views</strong>, select <strong>Cloudflare Saved View</strong>. This displays the data explorer.</p>
</li>
<li>
<p>From <strong>Options</strong> &gt; <strong>Time</strong>, you can edit the <strong>Lookback</strong> information to review traffic source information for a specific time period.</p>
</li>
</ol>
<p>For additional information about Kentik and Magic Transit, refer to <a href="https://kb.kentik.com/v1/docs/mitigation-overview#cloudflare-mt-setup">Kentik's Magic Transit setup</a>.</p>
<h2 id="access-cloudflare-account">Access Cloudflare account</h2>
<ol>
<li>Go to the <strong>Address space</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>BYOIP addresses</strong> tab.</p>
</li>
<li>
<p>In this example scenario, the prefix Cloudflare protects displays a <strong>Withdrawn</strong> status.</p>
<p>After a DDoS attack occurs, the status changes to <strong>Advertised</strong>, which indicates Cloudflare protects the network.</p>
</li>
</ol>
<h2 id="analytics">Analytics</h2>
<p>For a detailed view of actions taken and attack types, use the <strong>Network Analytics</strong> dashboard. For more information about Network Analytics, refer to <a href="/analytics/network-analytics/">Network Analytics</a>.</p>
<p>Go to the <strong>Network Analytics</strong> page.</p>
<div class="nb-dash-button"></div>
