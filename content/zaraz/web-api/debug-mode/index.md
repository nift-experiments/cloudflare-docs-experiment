<p>Zaraz offers a debug mode to troubleshoot the events and triggers systems. To activate debug mode you need to create a special debug cookie (<code>zarazDebug</code>) containing your debug key.
You can set this cookie manually or via the <code>zaraz.debug</code> helper function available in your console.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Copy your **Debug Key**.
3. Open a web browser and access its Developer Tools. For example, to access Developer Tools in Google Chrome, select **View** > **Developer** > **Developer Tools**.
4. Select the **Console** pane and enter the following command to create a debug cookie:
<pre><code class="language-js">zaraz.debug(&quot;YOUR_DEBUG_KEY&quot;)&#10;</code></pre>
<p>Zaraz’s debug mode is now enabled. A pop-up window will show up with the debugger information. To exit debug mode, remove the cookie by typing <code>zaraz.debug()</code> in the console pane of the browser.</p>
