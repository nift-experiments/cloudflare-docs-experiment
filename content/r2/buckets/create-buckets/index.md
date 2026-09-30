<p>You can create a bucket from the Cloudflare dashboard or using Wrangler.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11495.md")
</aside>
<h2 id="bucket-level-operations">Bucket-Level Operations</h2>
<p>Create a bucket with the <a href="/workers/wrangler/commands/r2/#r2-bucket-create"><code>r2 bucket create</code></a> command:</p>
<pre><code class="language-sh">wrangler r2 bucket create your-bucket-name&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11494.md")
</aside>
<p>List buckets in the current account with the <a href="/workers/wrangler/commands/r2/#r2-bucket-list"><code>r2 bucket list</code></a> command:</p>
<pre><code class="language-sh">wrangler r2 bucket list&#10;</code></pre>
<p>To delete a bucket, you must first empty it and then delete it. For detailed instructions, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a>.</p>
<h2 id="notes">Notes</h2>
<ul>
<li>Bucket names and buckets are not public by default. To allow public access to a bucket, refer to <a href="/r2/buckets/public-buckets/">Public buckets</a>.</li>
<li>For information on controlling access to your R2 bucket with Cloudflare Access, refer to <a href="/r2/tutorials/cloudflare-access/">Protect an R2 Bucket with Cloudflare Access</a>.</li>
<li>Invalid (unauthorized) access attempts to private buckets do not incur R2 operations charges against that bucket. Refer to the <a href="/r2/pricing/#frequently-asked-questions">R2 pricing FAQ</a> to understand what operations are billed vs. not billed.</li>
</ul>
