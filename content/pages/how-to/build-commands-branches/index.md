<p>This guide will instruct you how to set build commands on specific branches. You will use the <code>CF_PAGES_BRANCH</code> environment variable to run a script on a specified branch as opposed to your Production branch. This guide assumes that you have a Cloudflare account and a Pages project.</p>
<h2 id="set-up">Set up</h2>
<p>Create a <code>.sh</code> file in your project directory. You can choose your file's name, but we recommend you name the file <code>build.sh</code>.</p>
<p>In the following script, you will use the <code>CF_PAGES_BRANCH</code> environment variable to check which branch is currently being built. Populate your <code>.sh</code> file with the following:</p>
<pre><code class="language-bash">&#35; !/bin/bash&#10;&#10;if [ &quot;$CF_PAGES_BRANCH&quot; == &quot;production&quot; ]; then&#10;  &#35; Run the &quot;production&quot; script in `package.json` on the &quot;production&quot; branch&#10;  &#35; &quot;production&quot; should be replaced with the name of your Production branch&#10;&#10;  npm run production&#10;&#10;elif [ &quot;$CF_PAGES_BRANCH&quot; == &quot;staging&quot; ]; then&#10;  &#35; Run the &quot;staging&quot; script in `package.json` on the &quot;staging&quot; branch&#10;  &#35; &quot;staging&quot; should be replaced with the name of your specific branch&#10;&#10;  npm run staging&#10;&#10;else&#10;  &#35; Else run the dev script&#10;  npm run dev&#10;fi&#10;</code></pre>
<h2 id="publish-your-changes">Publish your changes</h2>
<p>To put your changes into effect:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Build & deployments** > **Build configurations** > **Edit configurations**.
4. Update the **Build command** field value to `bash build.sh` and select **Save**.
<p>To test that your build is successful, deploy your project.</p>
