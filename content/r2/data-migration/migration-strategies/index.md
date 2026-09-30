<p>You can use a combination of Super Slurper and Sippy to effectively migrate all objects with minimal downtime.</p>
<h3 id="when-the-source-bucket-is-actively-being-read-from-written-to">When the source bucket is actively being read from / written to</h3>
<ol>
<li>Enable Sippy and start using the R2 bucket in your application.
<ul>
<li>This copies objects from your previous bucket into the R2 bucket on demand when they are requested by the application.</li>
<li>New uploads will go to the R2 bucket.</li>
</ul>
</li>
<li>Use Super Slurper to trigger a one-off migration to copy the remaining objects into the R2 bucket.
<ul>
<li>In the <strong>Destination R2 bucket</strong> &gt; <strong>Overwrite files?</strong>, select &quot;Skip existing&quot;.</li>
</ul>
</li>
</ol>
<h3 id="when-the-source-bucket-is-not-being-read-often">When the source bucket is not being read often</h3>
<ol>
<li>Use Super Slurper to copy all objects to the R2 bucket.
<ul>
<li>Note that Super Slurper may skip some objects if they are uploaded after it lists the objects to be copied.</li>
</ul>
</li>
<li>Enable Sippy on your R2 bucket, then start using the R2 bucket in your application.
<ul>
<li>New uploads will go to the R2 bucket.</li>
<li>Objects which were uploaded while Super Slurper was copying the objects will be copied on-demand (by Sippy) when they are requested by the application.</li>
</ul>
</li>
</ol>
<h3 id="optimizing-your-slurper-data-migration-performance">Optimizing your Slurper data migration performance</h3>
<p>For an account, you can run three concurrent Slurper migration jobs at any given time, and each Slurper migration job can process a set amount of requests per second.</p>
<p>To increase overall throughput and reliability, we recommend splitting your migration into smaller, concurrent jobs using the prefix (or bucket subpath) option.</p>
<p>When creating a migration job:</p>
<ol>
<li>Go to the <strong>Source bucket</strong> step.</li>
<li>Under <strong>Define rules</strong>, in <strong>Bucket subpath</strong>, specify subpaths to divide your data by prefix.</li>
<li>Complete the data migration set up.</li>
</ol>
<p>For example, suppose your source bucket contains:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/11475.md")&#10;&#10;&#10;</pre>
<p>You can create separate jobs with prefixes such as:</p>
<ul>
<li><code>/photos/2024</code> to migrate all 2024 files</li>
<li><code>/photos/202</code> to migrate all files from 2023 and 2024</li>
</ul>
<p>Each prefix runs as an independent migration job, allowing Slurper to transfer data in parallel. This improves total transfer speed and ensures that a failure in one job does not interrupt the others.</p>
