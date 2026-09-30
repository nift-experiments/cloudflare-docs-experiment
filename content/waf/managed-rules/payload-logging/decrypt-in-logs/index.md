<p>You can include the encrypted matched payload in your <a href="/logs/logpush/">Logpush</a> jobs by adding the <strong>General</strong> &gt; <a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/#metadata"><strong>Metadata</strong></a> field from the Firewall Events dataset to your job.</p>
<p>The payload, in its encrypted form, is available in the <a href="#structure-of-encrypted_matched_data-property-in-logpush"><code>encrypted_matched_data</code> property</a> of the <code>Metadata</code> field.</p>
<p>However, you may want to decrypt the matched payload before storing the logs in your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15632.md")
</div> of choice. Cloudflare provides a [sample Worker project](https://github.com/cloudflare/matched-data-worker) on GitHub that does the following:
<ol>
<li>Behaves as an S3-compatible storage to receive logs from Logpush. These logs will contain encrypted matched payload data.</li>
<li>Decrypts matched payload data using your private key.</li>
<li>Sends the logs to the final log storage system with decrypted payload data.</li>
</ol>
<p>You will need to make some changes to the sample project to push the logs containing decrypted payload data to your log storage system.</p>
<p>Refer to the Worker project's <a href="https://github.com/cloudflare/matched-data-worker/blob/main/README.md">README</a> for more information on configuring and deploying this Worker project.</p>
<h2 id="structure-of-encrypted-matched-data-property-in-logpush">Structure of <code>encrypted_matched_data</code> property in Logpush</h2>
<p>Matched payload information includes the specific string that triggered a rule, along with some text that appears immediately before and after the matched string.</p>
<p>Once you decrypt its value, the <code>encrypted_matched_data</code> property of the <code>Metadata</code> field in Logpush has a structure similar to the following:</p>
<pre><code class="language-json">{&#10;	// for fields with only one match (such as URI or user agent fields):&#10;	&quot;&lt;match_location&gt;&quot;: {&#10;		&quot;before&quot;: &quot;&lt;text_before_match&gt;&quot;,&#10;		&quot;content&quot;: &quot;&lt;matched_text&gt;&quot;,&#10;		&quot;after&quot;: &quot;&lt;text_after_match&gt;&quot;&#10;	},&#10;	// for fields with possible multiple matches (such as form, header, or body fields):&#10;	&quot;&lt;match_location&gt;&quot;: [&#10;		{&#10;			&quot;before&quot;: &quot;&lt;text_before_match_1&gt;&quot;,&#10;			&quot;content&quot;: &quot;&lt;matched_text_1&gt;&quot;,&#10;			&quot;after&quot;: &quot;&lt;text_after_match_1&gt;&quot;&#10;		},&#10;		{&#10;			&quot;before&quot;: &quot;&lt;text_before_match_2&gt;&quot;,&#10;			&quot;content&quot;: &quot;&lt;matched_text_2&gt;&quot;,&#10;			&quot;after&quot;: &quot;&lt;text_after_match_2&gt;&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>The <code>before</code> and <code>after</code> properties are optional (there may be no content before/after the matched text) and will contain at most 15 bytes of content appearing before and after the match.</p>
<p>Below are a few examples of payload matches:</p>
<pre><code class="language-json">{&#10;	&quot;http.request.uri&quot;: {&#10;		&quot;before&quot;: &quot;/admin&quot;,&#10;		&quot;content&quot;: &quot;/.git/&quot;,&#10;		&quot;after&quot;: &quot;config&quot;&#10;	}&#10;}&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;http.request.headers.values[3]&quot;: [&#10;		{ &quot;content&quot;: &quot;phar://&quot;, &quot;after&quot;: &quot;example&quot; }&#10;	]&#10;}&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;http.request.body.raw&quot;: {&#10;		&quot;before&quot;: &quot;NY&gt;&quot;,&#10;		&quot;content&quot;: &quot;&lt;!ENTITY xxe SYSTEM \&quot;file:///dev/random\&quot;&gt;] &gt; &quot;,&#10;		&quot;after&quot;: &quot;&lt;foo&gt;&amp;xxe;&lt;/foo&gt;&quot;&#10;	}&#10;}&#10;</code></pre>
