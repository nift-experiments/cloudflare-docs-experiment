<p>When Email security detects a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8573.md")
</div> email, the metadata of the detection can be sent directly to Falcon LogScale. For this tutorial, you will need a working Falcon LogScale account. You will also need to create a new Ingest Token in your LogScale account. Ingest Tokens identify repositories and are used to configure data ingestion to your repository. Refer to [Falcon LogScale documentation](https://library.humio.com/falcon-logscale-cloud/ingesting-data-tokens.html) for more information.
<p>After creating your Ingest Token:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Alert Webhooks</strong>.</li>
<li>Select <strong>New Webhook</strong>.</li>
<li>In <strong>App Type</strong>, select <strong>SIEM</strong>.</li>
<li>Choose <em>Crowdstrike</em> from the dropdown, and paste your Ingest Token into the <strong>Auth Code</strong> section.</li>
<li>In <strong>Target</strong>, paste the URL <code>https://cloud.community.humio.com/api/v1/ingest/hec/raw</code>.</li>
<li>Select <strong>Publish Webhook</strong>.</li>
</ol>
