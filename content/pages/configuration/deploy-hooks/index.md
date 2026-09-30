<p>With Deploy Hooks, you can trigger deployments using event sources beyond commits in your source repository. Each event source may obtain its own unique URL, which will receive HTTP POST requests in order to initiate new deployments. This feature allows you to integrate Pages with new or existing workflows. For example, you may:</p>
<ul>
<li>Automatically deploy new builds whenever content in a Headless CMS changes</li>
<li>Implement a fully customized CI/CD pipeline, deploying only under desired conditions</li>
<li>Schedule a CRON trigger to update your website on a fixed timeline</li>
</ul>
<p>To create a Deploy Hook:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Builds** and select **Add deploy hook** to start configuration.
<p><img src="/assets/upstream/images/pages/platform/deploy-hooks-add.png" alt="Add a deploy hook on the Cloudflare dashboard" /></p>
<h2 id="parameters-needed">Parameters needed</h2>
<p>To configure your Deploy Hook, you must enter two key parameters:</p>
<ol>
<li><strong>Deploy hook name:</strong> a unique identifier for your Deploy Hook (for example, <code>contentful-site</code>)</li>
<li><strong>Branch to build:</strong> the repository branch your Deploy Hook should build</li>
</ol>
<p><img src="/assets/upstream/images/pages/platform/deploy-hooks-configure.png" alt="Choosing Deploy Hook name and branch to build on Cloudflare dashboard" /></p>
<h2 id="using-your-deploy-hook">Using your Deploy Hook</h2>
<p>Once your configuration is complete, the Deploy Hook’s unique URL is ready to be used. You will see both the URL as well as the POST request snippet available to copy.</p>
<p><img src="/assets/upstream/images/pages/platform/deploy-hooks-details.png" alt="Reviewing the Deploy Hook's newly generated unique URL" /></p>
<p>Every time a request is sent to your Deploy Hook, a new build will be triggered. Review the <strong>Source</strong> column of your deployment log to see which deployment were triggered by a Deploy Hook.</p>
<p><img src="/assets/upstream/images/pages/platform/deploy-hooks-deployment-logs.png" alt="Reviewing which deployment was triggered by a Deploy Hook" /></p>
<h2 id="security-considerations">Security Considerations</h2>
<p>Deploy Hooks are uniquely linked to your project and do not require additional authentication to be used. While this does allow for complete flexibility, it is important that you protect these URLs in the same way you would safeguard any proprietary information or application secret.</p>
<p>If you suspect unauthorized usage of a Deploy Hook, you should delete the Deploy Hook and generate a new one in its place.</p>
<h2 id="integrating-deploy-hooks-with-common-cms-platforms">Integrating Deploy Hooks with common CMS platforms</h2>
<p>Every CMS provider is different and will offer different pathways in integrating with Pages' Deploy Hooks. The following section contains step-by-step instructions for a select number of popular CMS platforms.</p>
<h3 id="contentful">Contentful</h3>
<p>Contentful supports integration with Cloudflare Pages via its <strong>Webhooks</strong> feature. In your Contentful project settings, go to <strong>Webhooks</strong>, create a new Webhook, and paste in your unique Deploy Hook URL in the <strong>URL</strong> field. Optionally, you can specify events that the Contentful Webhook should forward. By default, Contentful will trigger a Pages deployment on all project activity, which may be a bit too frequent. You can filter for specific events, such as Create, Publish, and many others.</p>
<p><img src="/assets/upstream/images/pages/platform/contentful.png" alt="Configuring Deploy Hooks with Contentful" /></p>
<h3 id="ghost">Ghost</h3>
<p>You can configure your Ghost website to trigger Pages deployments by creating a new <strong>Custom Integration</strong>. In your Ghost website’s settings, create a new Custom Integration in the <strong>Integrations</strong> page.</p>
<p>Each custom integration created can have multiple <strong>webhooks</strong> attached to it. Create a new webhook by selecting <strong>Add webhook</strong> and <strong>Site changed (rebuild)</strong> as the <strong>Event</strong>. Then paste your unique Deploy Hook URL as the <strong>Target URL</strong> value. After creating this webhook, your Cloudflare Pages application will redeploy whenever your Ghost site changes.</p>
<p><img src="/assets/upstream/images/pages/platform/ghost.png" alt="Configuring Deploy Hooks with Ghost" /></p>
<h3 id="sanity">Sanity</h3>
<p>In your Sanity project's Settings page, find the <strong>Webhooks</strong> section, and add the Deploy Hook URL, as seen below. By default, the Webhook will trigger your Pages Deploy Hook for all datasets inside of your Sanity project. You can filter notifications to individual datasets, such as production, using the <strong>Dataset</strong> field:</p>
<p><img src="/assets/upstream/images/pages/platform/sanity.png" alt="Configuring Deploy Hooks with Sanity" /></p>
<h3 id="wordpress">WordPress</h3>
<p>You can configure WordPress to trigger a Pages Deploy Hook by installing the free <strong>WP Webhooks</strong> plugin. The plugin includes a number of triggers, such as <strong>Send Data on New Post, Send Data on Post Update</strong> and <strong>Send Data on Post Deletion</strong>, all of which allow you to trigger new Pages deployments as your WordPress data changes. Select a trigger on the sidebar of the plugin settings and then <a href="https://wordpress.org/plugins/wp-webhooks/"><strong>Add Webhook URL</strong></a>, pasting in your unique Deploy Hook URL.</p>
<p><img src="/assets/upstream/images/pages/platform/wordpress.png" alt="Configuring Deploy Hooks with WordPress" /></p>
<h3 id="strapi">Strapi</h3>
<p>In your Strapi Admin Panel, you can set up and configure webhooks to enhance your experience with Cloudflare Pages. In the Strapi Admin Panel:</p>
<ol>
<li>Navigate to <strong>Settings</strong>.</li>
<li>Select <strong>Webhooks</strong>.</li>
<li>Select <strong>Add New Webhook</strong>.</li>
<li>In the <strong>Name</strong> form field, give your new webhook a unique name.</li>
<li>In the <strong>URL</strong> form field, paste your unique Cloudflare Deploy Hook URL.</li>
</ol>
<p>In the Strapi Admin Panel, you can configure your webhook to be triggered based on events. You can adjust these settings to create a new deployment of your Cloudflare Pages site automatically when a Strapi entry or media asset is created, updated, or deleted.</p>
<p>Be sure to add the webhook configuration to the <a href="https://strapi.io/documentation/developer-docs/latest/setup-deployment-guides/installation.html">production</a> Strapi application that powers your Cloudflare site.</p>
<p><img src="/assets/upstream/images/pages/platform/strapi.png" alt="Configuring Deploy Hooks with Strapi" /></p>
<h3 id="storyblok">Storyblok</h3>
<p>You can set up and configure deploy hooks in Storyblok to trigger events. In your Storyblok space, go to <strong>Settings</strong> and scroll down to <strong>Webhooks</strong>. Paste your deploy hook into the <strong>Story published &amp; unpublished</strong> field and select <strong>Save</strong>.</p>
<p><img src="https://user-images.githubusercontent.com/53130544/161367254-ff475f3b-2821-4ee8-a175-8e96e779aa08.png" alt="Configuring Deploy Hooks with Storyblok" /></p>
