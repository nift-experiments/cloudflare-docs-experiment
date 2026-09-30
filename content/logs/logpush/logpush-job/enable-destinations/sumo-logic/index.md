<p>Cloudflare Logpush supports pushing logs directly to Sumo Logic via the Cloudflare dashboard or via API.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<ol>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page at the account or or domain (also known as zone) level.</p>
<p>For account: <div class="nb-dash-button"></div></p>
<p>For domain (also known as zone): <div class="nb-dash-button"></div></p>
</li>
<li>
<p>Depending on your choice, you have access to <a href="/logs/logpush/logpush-job/datasets/account/">account-scoped datasets</a> and <a href="/logs/logpush/logpush-job/datasets/zone/">zone-scoped datasets</a>, respectively.</p>
</li>
<li>
<p>Select <strong>Create a Logpush job</strong>.</p>
</li>
<li>
<p>In <strong>Select a destination</strong>, choose <strong>Sumo Logic</strong>.</p>
</li>
<li>
<p>Enter the <strong>HTTP Source Address</strong>. To get the HTTP Source Address (URL) configure a <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/">Sumo Logic Hosted Collector</a> with an <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/logs-metrics/">HTTP Logs &amp; Metrics Source</a>. Note that the same collector can be used for multiple Logpush jobs, but each job must have a dedicated source. When you are done entering the destination details, select <strong>Continue</strong>.</p>
</li>
<li>
<p>Select the dataset to push to the storage service.</p>
</li>
<li>
<p>In the next step, you need to configure your logpush job:</p>
<ul>
<li>Enter the <strong>Job name</strong>.</li>
<li>Under <strong>If logs match</strong>, you can select the events to include and/or remove from your logs. Refer to <a href="/logs/logpush/logpush-job/filters/">Filters</a> for more information. Not all datasets have this option available.</li>
<li>In <strong>Send the following fields</strong>, you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.</li>
</ul>
</li>
<li>
<p>In <strong>Advanced Options</strong>, you can:</p>
<ul>
<li>Choose the format of timestamp fields in your logs (<code>RFC3339</code> (default), <code>Unix</code>, or <code>UnixNano</code>).</li>
<li>Select a <a href="/logs/logpush/logpush-job/api-configuration/#sampling-rate">sampling rate</a> for your logs or push a randomly-sampled percentage of logs.</li>
<li>Enable redaction for <code>CVE-2021-44228</code>. This option will replace every occurrence of <code>${</code> with <code>x{</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit</strong> once you are done configuring your logpush job.</p>
</li>
</ol>
<h2 id="configure-a-hosted-collector">Configure a Hosted Collector</h2>
<p>Cloudflare can send logs to a Hosted Collector with <strong>HTTP Logs &amp; Metrics</strong> as the source. Once you have set up a collector, you simply provide the HTTP Source Address (a unique URL) to which logs can be posted.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To enable Logpush to Sumo Logic:</p>
<ol>
<li>
<p>Configure a Hosted Collector. Refer to <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/configure-hosted-collector/">instructions from Sumo Logic</a>.</p>
</li>
<li>
<p>Configure an HTTP Logs &amp; Metrics Source. Refer to <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/">instructions from Sumo Logic</a>. The last step indicates how to get the HTTP Source Address (URL).</p>
</li>
<li>
<p>Provide the HTTP Source Address (URL) when prompted by the Logpush API or UI.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/10538.md")
</aside>
