<h2 id="windows">Windows</h2>
<ol>
<li>Create a script file with <code>.bat</code>, <code>.cmd</code>, and <code>.ps1</code> file formats to download, install and configure the Cloudflare One Client (formerly WARP) Windows application on the device. Listed below is a sample script with all of the configurable parameters:</li>
</ol>
<pre><code class="language-python">&lt;# Choose file name for downloading application #&gt;&#10;$filename = filename.msi&#x27;&#10;&#10;&lt;# Download URL of the installer. #&gt;&#10;$url = &#x27;https://downloads.cloudflareclient.com/v1/download/windows/ga&#x27;&#10;Write-Host &#x27;Downloading App from&#x27; $url&#10;Invoke-WebRequest -Uri $url -OutFile $filename&#10;&#10;&lt;# Run the installer and wait for the installation to finish #&gt;&#10;$arguments = &quot;ORGANIZATION=&quot;exampleorg&quot; SERVICE_MODE=&quot;warp&quot; GATEWAY_UNIQUE_ID=&quot;fmxk762nrj&quot; SUPPORT_URL=&quot;http://support.example.com&quot;&quot;&#10;&#10;$installProcess = (Start-Process $filename -ArgumentList $arguments -PassThru -Wait)&#10;&#10;&lt;# Check if installation was successful #&gt;&#10;if ($installProcess.ExitCode -ne 0) {&#10;    Write-Host &quot;Installation failed!&quot;&#10;    exit $installProcess.ExitCode&#10;}&#10;else {&#10;    Write-Host &quot;Installation completed successfully!&quot;&#10;}&#10;</code></pre>
<ol start="2">
<li>
<p>Push the script file to the devices using Hexnode.</p>
</li>
<li>
<p>On your Hexnode console, go to <strong>Manage</strong> &gt; <strong>Devices</strong>.</p>
</li>
<li>
<p>Select your device name. This will take you to the <strong>Device Summary</strong>.</p>
</li>
<li>
<p>Select <strong>Actions</strong> &gt; <strong>Execute Custom Script</strong>.</p>
</li>
<li>
<p>Choose the script file source as <em>Upload file</em>, then upload the script file.</p>
</li>
<li>
<p>Select <strong>Execute</strong>.</p>
</li>
</ol>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h2 id="macos">macOS</h2>
<ol>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos">Download</a> the Cloudflare One Client for macOS.</p>
</li>
<li>
<p>On your Hexnode console, go to <strong>Apps</strong> &gt; <strong>Add Apps</strong> &gt; <strong>Enterprise App</strong>.</p>
</li>
<li>
<p>Select <em>macOS</em> as the app platform.</p>
</li>
<li>
<p>Add an app name, category and description.</p>
</li>
<li>
<p>Upload the <code>Cloudflare_WARP_&lt;VERSION&gt;.pkg</code> file and select <strong>Add</strong>.</p>
</li>
<li>
<p>Set up an XML file with the supported app configurations for the app.
Here is a sample XML file with the accepted parameters.</p>
</li>
</ol>
<pre><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;!DOCTYPE plist PUBLIC &quot;-//Apple//DTD PLIST 1.0//EN&quot; &quot;http://www.apple.com/DTDs/PropertyList-1.0.dtd&quot;&gt;&#10;&lt;plist version=&quot;1.0&quot;&gt;&#10;&lt;dict&gt;&#10;&lt;key&gt;organization&lt;/key&gt;&#10;&lt;string&gt;organizationname&lt;/string&gt;&#10;&lt;key&gt;auto_connect&lt;/key&gt;&#10;&lt;integer&gt;1&lt;/integer&gt;&#10;&lt;key&gt;switch_locked&lt;/key&gt;&#10;&lt;false /&gt;&#10;&lt;key&gt;service_mode&lt;/key&gt;&#10;&lt;string&gt;warp&lt;/string&gt;&#10;&lt;key&gt;support_url&lt;/key&gt;&#10;&lt;string&gt;https://support.example.com&lt;/string&gt;&#10;&lt;/dict&gt;&#10;&lt;/plist&gt;&#10;</code></pre>
<ol start="7">
<li>
<p>On your Hexnode console, go to <strong>Policies</strong>.</p>
</li>
<li>
<p>Create a new policy and provide a policy name.</p>
</li>
<li>
<p>Go to <strong>macOS</strong> &gt; <strong>App Management</strong> &gt; <strong>Mandatory Apps</strong> and start setting up the policy.</p>
</li>
<li>
<p>Select <strong>Add</strong> and select the previously uploaded Cloudflare One Client app.</p>
</li>
<li>
<p>Go to <strong>App Configurations</strong> &gt; <strong>Add new configuration</strong>.</p>
</li>
<li>
<p>Select the <em>Cloudflare One Client</em> app and upload the XML file from Step 6.</p>
</li>
<li>
<p>Now go to <strong>Policy Targets</strong> and associate the policy with the target entities.</p>
</li>
</ol>
<p>This will push the app along with the configurations to the selected devices.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h2 id="ios">iOS</h2>
<ol>
<li>
<p>On your Hexnode console, go to <strong>Apps</strong> &gt; <strong>Add Apps</strong> &gt; <strong>Store App</strong>.</p>
</li>
<li>
<p>Select <em>iOS</em> as the app platform.</p>
</li>
<li>
<p>Search for <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492"><strong>Cloudflare One Agent</strong></a> and <strong>Add</strong> the app.</p>
</li>
<li>
<p>Set up an XML file with the supported app configurations for the app. Refer this sample XML code to identify the supported arguments:</p>
</li>
</ol>
<pre><code class="language-xml">&lt;dict&gt;&#10;&lt;key&gt;organization&lt;/key&gt;&#10;&lt;string&gt;yourorganization&lt;/string&gt;&#10;&lt;key&gt;auto_connect&lt;/key&gt;&#10;&lt;integer&gt;1&lt;/integer&gt;&#10;&lt;key&gt;switch_locked&lt;/key&gt;&#10;&lt;false /&gt;&#10;&lt;key&gt;service_mode&lt;/key&gt;&#10;&lt;string&gt;warp&lt;/string&gt;&#10;&lt;key&gt;support_url&lt;/key&#10;&lt;string&gt;https://support.example.com&lt;/string&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<ol start="5">
<li>
<p>Upload the app configurations in Hexnode:</p>
<ol>
<li>On your Hexnode console, go to the <strong>Apps</strong> tab.</li>
<li>Find the Cloudflare One Agent app and select its name.</li>
<li>Select the settings icon and choose <strong>App Configuration</strong>.</li>
<li>Upload the XML file in the corresponding field.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
</li>
<li>
<p>Push the app to the target devices using Hexnode.</p>
<ol>
<li>On your Hexnode console, go to <strong>Policies</strong> and create a new policy.</li>
<li>Provide a name for the policy and go to <strong>iOS</strong>.</li>
<li>Go to <strong>Mandatory Apps</strong> &gt; <strong>Configure</strong>.</li>
<li>Select <strong>Add</strong> &gt; <strong>Add app</strong>, check the required app, and select <strong>Done</strong>.</li>
<li>Go to <strong>Policy Targets</strong> and associate the policy with the required target devices.</li>
</ol>
</li>
</ol>
<p>This will push the app along with the configurations to the selected devices.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h2 id="android">Android</h2>
<ol>
<li>On your Hexnode console, go to <strong>Apps</strong> &gt; <strong>Add Apps</strong> &gt; <strong>Managed Google Apps</strong>.</li>
<li>Search for the app <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent"><strong>Cloudflare One Agent</strong></a>.</li>
<li>Approve the app as a Managed Google Play app.</li>
<li>Go to <strong>Policies</strong> and create a new policy.</li>
<li>Go to <strong>Android</strong> &gt; <strong>App Configurations</strong> &gt; <strong>Add new configuration</strong>.</li>
<li>Find the <strong>Cloudflare One Agent</strong> app and set up your custom configurations.</li>
<li>Go to <strong>Policy Targets</strong> and associate the policy with the required target devices.</li>
<li>Save the policy.</li>
</ol>
<p>This will push the app along with the configurations to the selected devices.</p>
<p>After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
