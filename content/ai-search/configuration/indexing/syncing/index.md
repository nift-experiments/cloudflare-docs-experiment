<p>AI Search automatically indexes your content for search. How indexing works depends on your data source.</p>
<h2 id="external-data-sources">External data sources</h2>
<p>For instances connected to a <a href="/ai-search/configuration/data-source/website/">website</a> or <a href="/ai-search/configuration/data-source/r2/">R2 bucket</a>, AI Search creates jobs to sync your data source. Jobs run automatically on a schedule, every 6 hours by default, and process new, modified, or deleted files to keep your search index up to date.</p>
<p>You can view job status and history in the <strong>Jobs</strong> tab in the dashboard or using the <a href="/ai-search/api/instances/rest-api/">Instances API</a>.</p>
<h3 id="sync-interval">Sync interval</h3>
<p>By default, AI Search runs a sync job every 6 hours. To change how often scheduled syncs run, use the <strong>Sync interval</strong> setting in the dashboard, or set the <code>sync_interval</code> field when you <a href="/ai-search/api/instances/workers-binding/#create">create</a> or <a href="/ai-search/api/instances/workers-binding/#update">update</a> an instance through the Workers binding or <a href="/ai-search/api/instances/rest-api/">REST API</a>.</p>
<p>The interval can be 1, 2, 4, 6, 12, or 24 hours. In the API, <code>sync_interval</code> is specified in seconds, so the allowed values are <code>3600</code> (1 hour), <code>7200</code> (2 hours), <code>14400</code> (4 hours), <code>21600</code> (6 hours, the default), <code>43200</code> (12 hours), and <code>86400</code> (24 hours).</p>
<h3 id="trigger-syncs-from-automated-pipelines">Trigger syncs from automated pipelines</h3>
<p>Sync jobs normally run on a schedule, but you can also start one programmatically whenever your source content changes. This is useful for connecting AI Search to a CMS or a content pipeline: when a publish event or a build step completes, have it trigger a sync so the index reflects the change without waiting for the next scheduled run.</p>
<p>Trigger a sync job with the Wrangler CLI, for example from a CI/CD step or deploy hook:</p>
<pre><code class="language-sh">npx wrangler ai-search jobs create &lt;INSTANCE_NAME&gt;&#10;</code></pre>
<p>Or call the <a href="/ai-search/api/instances/rest-api/#jobs">Create job REST API</a> from a CMS webhook or a Worker. Sync jobs can be triggered at most once every 30 seconds.</p>
<h2 id="built-in-storage">Built-in storage</h2>
<p>Files uploaded to <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a> are indexed immediately. There are no sync jobs. Each file is processed individually as it is uploaded.</p>
<h2 id="controls">Controls</h2>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Trigger sync</td>
<td>Manually start a sync job to scan your external data source for changes. Can be triggered every 30 seconds.</td>
</tr>
<tr>
<td>Cancel job</td>
<td>Cancel a running sync job.</td>
</tr>
<tr>
<td>Pause indexing</td>
<td>Temporarily stop all scheduled sync jobs.</td>
</tr>
<tr>
<td>Resume indexing</td>
<td>Resume scheduled sync jobs, including jobs paused automatically after inactivity.</td>
</tr>
<tr>
<td>Sync individual file</td>
<td>Re-index a specific file.</td>
</tr>
</tbody>
</table>
<p>You can perform these actions from the dashboard, the <a href="/ai-search/api/instances/rest-api/">REST API</a>, or the <a href="/ai-search/api/instances/workers-binding/">Workers binding</a>.</p>
<h2 id="performance">Performance</h2>
<p>The total time to index depends on the number and type of files. Factors that affect performance include:</p>
<ul>
<li>Total number of files and their sizes</li>
<li>File formats (for example, images take longer than plain text)</li>
<li>Latency of Workers AI models used for embedding and image processing</li>
</ul>
<h2 id="automatic-pausing-for-inactive-instances">Automatic pausing for inactive instances</h2>
<p>If an instance receives no search request for 31 days, AI Search automatically pauses its scheduled sync jobs. This applies only to <a href="#external-data-sources">external data sources</a> (website or R2), since <a href="#built-in-storage">built-in storage</a> has no sync jobs. This avoids unnecessary requests to your data source to rescan and sync your instance when it is not being used.</p>
<p>A paused instance stays fully searchable, but source changes are not picked up while sync jobs are paused. After the instance receives search or chat traffic again, AI Search automatically resumes scheduled sync jobs during its activity checks. You can also resume manually with the <strong>Resume indexing</strong> control. Refer to <a href="#controls">Controls</a>.</p>
<h2 id="best-practices">Best practices</h2>
<p>To ensure smooth and reliable indexing:</p>
<ul>
<li>Make sure your files are within the <a href="/ai-search/configuration/data-source/#file-limits">size limit</a> and in a <a href="/ai-search/configuration/data-source/#supported-file-types">supported format</a> to avoid being skipped.</li>
<li>For R2-backed instances, keep your <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> valid to prevent indexing failures.</li>
<li>Regularly clean up outdated or unnecessary content to stay within <a href="/ai-search/platform/limits-pricing/">instance limits</a>.</li>
</ul>
