<h2 id="enable-auto-updates-to-the-machine-learning-models">Enable auto-updates to the Machine Learning models</h2>
<p>Cloudflare encourages Enterprise customers to enable auto-updates to its Machine Learning models to get the newest bot detection models as they are released.</p>
<p>To enable auto-updates:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3467.md")
</div>
<h3 id="what-will-change">What will change</h3>
<p>If you are on an older Machine Learning model, you will see a score change to requests scored by the <strong>Machine Learning</strong> source instantly. If you are already on the latest model, you will see changes only after a new Machine Learning model becomes the global default.</p>
<p>Customers will be notified via email and dashboard prior to a new Machine Learning model becoming the global default.</p>
<h3 id="risks-of-not-updating">Risks of not updating</h3>
<p>By not updating to the latest version, you will be using a Machine Learning model no longer maintained or monitored by our engineering team. As Internet traffic changes and new trends evolve, scoring accuracy by older versions may degrade.</p>
<h3 id="model-versions-and-release-notes">Model versions and release notes</h3>
<table>
<thead>
<tr>
<th>Version</th>
<th>Release Notes</th>
<th>Launch Date</th>
</tr>
</thead>
<tbody>
<tr>
<td>v1</td>
<td>First Machine Learning Model released.</td>
<td>Q1 2019</td>
</tr>
<tr>
<td>v2</td>
<td>Introduced dynamic inter-request features to leverage the Cloudflare network to detect new bots more accurately. <br/><br/>Feedback other Bot Management detection mechanisms to the machine learning model to more accurately detect bots.</td>
<td>Q1 2020</td>
</tr>
<tr>
<td>v3</td>
<td>Fixed accuracy issues under some conditions in the previous version.</td>
<td>Q2 2020</td>
</tr>
<tr>
<td>v4</td>
<td>Improved scoring for iOS devices. <br/><br/>Fixed scoring inaccuracy in Firefox builds.</td>
<td>Q1 2021</td>
</tr>
<tr>
<td>v5</td>
<td>Recalibrated model for the <a href="https://blog.cloudflare.com/deprecating-cfduid-cookie/">removal of <code>_cfduid</code> cookie</a>. <br/><br/> Introduced new signals to reduce false negatives.</td>
<td>Q2 2021</td>
</tr>
<tr>
<td>v6</td>
<td>Significantly improved scoring for native Android application traffic. <br/><br/>Improved scoring on the newest versions of Chromium browsers.</td>
<td>Q1 2022</td>
</tr>
<tr>
<td>v7</td>
<td>Increased recognition of distributed botnets. <br/><br/>Improved HTTP/3 scoring.</td>
<td>Q1 2024</td>
</tr>
<tr>
<td>v8</td>
<td>Improved detection of residential proxies. <br/><br/>Increased weight on network level traffic characteristics.</td>
<td>Q2 2024</td>
</tr>
<tr>
<td>v9</td>
<td>Improved model consistency and model efficacy against randomization attack techniques</td>
<td>Q2 2025</td>
</tr>
</tbody>
</table>
