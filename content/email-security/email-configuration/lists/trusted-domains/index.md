<p><strong>Trusted domains</strong> allows you to identify domains that should be exempted from Email security (formerly Area 1) detections.</p>
<h2 id="default-behavior">Default behavior</h2>
<p>When messages come to your recipients from certain domains, Email security triggers certain <a href="/email-security/reference/dispositions-and-attributes/">detections</a> by default:</p>
<ul>
<li><strong>Proximity Domains</strong>: Domains with similar spelling to your existing domain. Will trigger a <code>SPOOF</code> detection.</li>
<li><strong>Recent Domains</strong>: Domains created recently (exact definition set in <a href="/email-security/email-configuration/enhanced-detections/added-detections/">Added Detections</a>). Will trigger a <code>MALICIOUS</code> or <code>SUSPICIOUS</code> detection.</li>
</ul>
<p>However, sometimes those domains are legitimate. For example, your company may have registered several lookalike domains to combat domain squatters.</p>
<p>To exempt specific domains from these detections, you can add trusted domains.</p>
<h2 id="add-a-trusted-domain">Add a trusted domain</h2>
<p>To add a trusted domain:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Allow List</strong> &gt; <strong>Trusted Domains</strong>.</p>
</li>
<li>
<p>Select <strong>+ Add Domain</strong>.</p>
</li>
<li>
<p>The exact flow varies based on what you select for your <strong>Pattern Type</strong>:</p>
<ul>
<li><strong>Domain</strong>: Allows you to specify a particular domain and then adjust triggers for <em>Proximity Domain</em> and <em>Recent Domain</em>.</li>
<li><strong>Create Regex</strong>: Allows you to create Regex rules for the domain name, top-level domain (TLDs), and subdomains and then adjust triggers for <em>Proximity Domain</em> and <em>Recent Domain</em>.</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can also upload a CSV file of multiple allowed patterns, so long as the file is smaller than 150 KB, starts with a header row of all required values, and contains no additional fields.</p>
<p>An example file would look like this:</p>
<pre><code class="language-txt">Domain, Notes, Proximity, Recent&#10;mydomain.com, First Person, true, true&#10;testdomain.com, New Hire, false, true&#10;</code></pre>
