<p>Cloudflare Logpush supports pushing logs to a limited set of services providers. However, you can configure Logpush via API.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<p>Refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a> for the list of services you can configure to use with Logpush through the Cloudflare dashboard. Interested in a different service? Take this <a href="https://docs.google.com/forms/d/e/1FAIpQLScwOSabROywVajpMX2ZYCVl3saYs11cP4NIC8QR-wmOAnxOtA/viewform">survey</a>.</p>
<h2 id="manage-via-api">Manage via API</h2>
<p>The Cloudflare Logpush API allows you to configure and manage jobs via create, retrieve, update, and delete operations (CRUD).</p>
<p>With Logpush, you can create a job to upload logs of the metadata Cloudflare collects in batches as soon as possible to your cloud service provider. The default number of jobs that you can setup per dataset per domain is four, but you can setup more jobs depending on your plan and subscriptions.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To get started:</p>
<ol>
<li>
<p>Set up a storage provider and grant Cloudflare access. Your storage provider may request your Cloudflare API credentials and other information including:</p>
<ul>
<li>Email address</li>
<li>Cloudflare API key</li>
<li>Zone ID</li>
<li>Destination access details for your cloud service provider</li>
</ul>
</li>
<li>
<p>Configure your Logpush job. For more information on how to configure a Logpush job, refer to <a href="/logs/logpush/logpush-job/api-configuration/">API configuration</a>.</p>
</li>
</ol>
