<p>Zaraz supports loading custom third-party tools using <a href="https://managedcomponents.dev/">Managed Components</a>. These can be Managed Components that you have developed yourself or that were developed by others. Using Custom Managed Components with Zaraz is done by converting them into a Cloudflare Worker running in your account.</p>
<p>If you are new to Managed Components, we recommend you get started with <a href="https://managedcomponents.dev/getting-started/quickstart">creating your own Managed Component</a> or check out <a href="https://github.com/managed-components/demo">our demo Managed Component</a>.</p>
<h2 id="prepare-a-managed-component">Prepare a Managed Component</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17609.md")
</aside>
<p>To get started, you need have a JavaScript file ready for deployment, that exports the default Managed Component function for your Managed Component.</p>
<p>In this guide, we will use a simple example of a Custom Managed Component that counts user visits and logs this data in the console:</p>
<pre><code class="language-javascript">// File: index.js&#10;export default async function (manager) {&#10;	// Add a pageview event&#10;	manager.addEventListener(&quot;pageview&quot;, event, () =&gt; {&#10;		const { client } = event;&#10;&#10;		// Get the variable &quot;counter&quot; from the client&#x27;s cookies and increase by 1&#10;		let counter = parseInt(client.get(&quot;counter&quot;)) || 0;&#10;		counter += 1;&#10;&#10;		// Log the increased number&#10;		client.execute(`console.log(&#x27;Views: ${counter}&#x27;)`);&#10;&#10;		// Store the increased number for the next visit&#10;		client.set(&quot;counter&quot;, counter);&#10;	});&#10;}&#10;</code></pre>
<h2 id="deploy-a-managed-component-to-cloudflare">Deploy a Managed Component to Cloudflare</h2>
<ol>
<li>Open a terminal in your Managed Component’s root directory.</li>
<li>From there, run <code>npx managed-component-to-cloudflare-worker ./index.js my-new-counter-mc</code>, which will deploy the Managed Component to a specialized Cloudflare Worker. Change the path to your <code>index.js</code>. You can also rename the Component.</li>
<li>Your Managed Component should now be <a href="https://dash.cloudflare.com/redirect?account=/workers-and-pages">visible on your account</a> as a Cloudflare Worker prefixed with <code>custom-mc-</code>.</li>
</ol>
<h2 id="configure-a-managed-component-in-cloudflare">Configure a Managed Component in Cloudflare</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17608.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Tools Configuration** > [**Third-party tools**](https://dash.cloudflare.com/?to=/:account/:zone/zaraz/tools-config/tools/catalog).
3. Select **Add new tool** and choose **Custom Managed Component** from the tools library page. Select **Continue** to confirm your selection.
4. In **Select Custom MC**, choose a Custom Managed Component that you have deployed to your account, such as `custom-mc-my-new-counter-mc`. Select **Continue**.
5. In **Permissions**, select the permissions you want to grant the Custom Managed Component. If you run an untrusted Managed Component, pay close attention to what permissions you are granting. Select **Continue**.
6. In **Set up**, configure the settings for your new tool. The information you need to enter will depend on the code of the Managed Component. You can add settings and default fields, as well as use [variables you have previously set up](/zaraz/variables/create-variables/).
7. Select **Save**.
<p>While your tool is now configured, it does not have any actions associated with it yet. Adding new actions will tell Zaraz when to contact your Managed Component, and what information to send to it. When adding actions, make sure to verify the Action Type you are using. The types <code>pageview</code> and <code>event</code> are most commonly used, but you can add any action type to match the event listeners your Managed Component is using. Learn how to <a href="/zaraz/custom-actions/">create additional actions</a>.</p>
<p>If your Managed Component listens to <code>ecommerce</code> events, toggle <strong>E-commerce tracking</strong> in the Managed Component Settings page.</p>
<h2 id="unsupported-features">Unsupported Features</h2>
<p>As of now, Custom Managed Components do not support the use of the following methods yet:</p>
<ul>
<li><code>manager.registerEmbed</code></li>
<li><code>manager.registerWidget</code></li>
<li><code>manager.proxy</code></li>
<li><code>manager.serve</code></li>
</ul>
