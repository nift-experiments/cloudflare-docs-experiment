<p>Zaraz allows you to test your configurations before publishing them. This is helpful to avoid unintended consequences when deploying a new tool or trigger.</p>
<p>After enabling Preview &amp; Publish you will also have access to <a href="/zaraz/history/versions/">Zaraz History</a>.</p>
<h2 id="enable-preview-publish-mode">Enable Preview &amp; Publish mode</h2>
<p>By default, Zaraz is configured to commit changes in real time. To enable preview mode and test new features you are adding to Zaraz:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>History</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enable <strong>Preview &amp; Publish Workflow</strong>.</li>
</ol>
<p>You are now working in preview mode. To commit changes and make them live, you will have to select <strong>Publish</strong> on your account.</p>
<h3 id="test-changes-before-publishing-them">Test changes before publishing them</h3>
<p>Now that you have Zaraz working in preview mode, you can open your website and test your settings:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Navigate to the website where you want to test your new settings.</li>
<li>Access the browser’s developer tools. For example, to access developer tools in Google Chrome, select <strong>View</strong> &gt; <strong>Developer</strong> &gt; <strong>Developer Tools</strong>.</li>
<li>Select the <strong>Console</strong> pane and enter the following command to start Zaraz’s preview mode:</li>
</ol>
<pre><code class="language-js">zaraz.preview(&quot;&lt;YOUR_DEBUG_KEY&gt;&quot;);&#10;</code></pre>
<ol start="5">
<li>Your website will reload along with Zaraz debugger, and Zaraz will use the most recent changes in preview mode.</li>
<li>If you are satisfied with your changes, go back to the dashboard and select <strong>Publish</strong> to apply them to all users. If not, use the dashboard to continue adjusting your configuration.</li>
</ol>
<p>To exit preview mode, close Zaraz debugger.</p>
<h2 id="disable-preview-publish-mode">Disable Preview &amp; Publish mode</h2>
<p>Disable Preview &amp; Publish mode to work in real time. When you work in real time, any changes made on the dashboard are applied instantly to the domain you are working on.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>History</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Disable <strong>Preview &amp; Publish Workflow</strong>.</li>
<li>In the modal, decide if you want to delete all unpublished changes, or if you want to publish any change made in the meantime.</li>
</ol>
<p>Zaraz is now working in real time. Any change you make will be immediately applied the domain you are working on.</p>
