<p>Data classes are reusable classification rules built from detection entries, other data classes, sensitivity levels, and data tags.</p>
<p>Use a data class when you want to combine multiple signals into a single reusable classification rule that can then be added to custom DLP profiles.</p>
<h2 id="what-a-data-class-does">What a data class does</h2>
<p>A data class lets you define classification logic separately from a DLP profile.</p>
<p>Instead of rebuilding the same logic in multiple profiles, you can create one reusable data class and apply it wherever you need it.</p>
<p>Data classes can also assign labels to matched content. This lets you connect raw detections to a broader classification model instead of relying only on direct entry matching in a profile.</p>
<h2 id="create-a-data-class">Create a data class</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Data classes</strong>.</li>
<li>Select <strong>Create data class</strong>.</li>
<li>Enter a name and optional description.</li>
<li>Build the detection rules for the data class.</li>
<li>Assign the labels you want matching content to receive.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="build-detection-rules">Build detection rules</h2>
<p>Data classes use a rule builder to combine multiple signals into one classification rule.</p>
<p>You can build rules from:</p>
<ul>
<li><a href="/cloudflare-one/data-loss-prevention/detection-entries/">detection entries</a></li>
<li>other existing data classes</li>
</ul>
<p>Use logical operators such as <code>AND</code> and <code>OR</code> to control how those conditions are evaluated.</p>
<p>Because data classes can reference other data classes, you can build reusable classification layers instead of recreating the same logic in multiple places. Cloudflare excludes the current data class from the selector to prevent recursive references.</p>
<h2 id="assign-labels">Assign labels</h2>
<p>After you define the rule logic, choose the labels you want matching content to receive.</p>
<p>You can assign:</p>
<ul>
<li>a sensitivity schema and sensitivity level</li>
<li>a data tag group and one or more data tags</li>
</ul>
<p>When content matches the data class, Cloudflare applies those labels to the match.</p>
<h2 id="use-a-data-class-in-a-dlp-profile">Use a data class in a DLP profile</h2>
<p>After you create a data class, you can add it to a custom DLP profile.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Create or edit a custom DLP profile.</li>
<li>In <strong>Data classes</strong>, select <strong>Add data classes</strong>.</li>
<li>Choose the data classes you want to include, then select <strong>Confirm</strong>.</li>
<li>(Optional) Add direct detection entries or labels to the profile.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<p>Custom DLP profiles can combine direct detection entries, data classes, and labels in the same profile.</p>
