<p>The Zaraz Context Enricher is a tool to modify or enrich <a href="/zaraz/reference/context/">the context</a> that is being used across Zaraz using a Cloudflare Worker. The Context Enricher allows you access to the client and system variables.</p>
<h2 id="creating-a-worker">Creating a Worker</h2>
<p>To use a Context Enricher, you first need to create a new Cloudflare Worker. You can do this through the Cloudflare dashboard or by using <a href="/workers/get-started/guide/">Wrangler</a>.</p>
<p>To create a new Worker in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Give a name to your Worker and select **Deploy**.
4. Select **Edit code**.
<p>You have now created a basic Worker that responds with &quot;Hello world.&quot; To make this Worker functional when using it as a Context Enricher, you need to change the code to return the context back:</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    const { system, client } = await request.json();&#10;&#10;    // Here goes your modification to the system or client objects.&#10;    /*&#10;      For example, to change the country to a fictitious &quot;Pirate&#x27;s Island&quot; (&quot;PI&quot;), use:&#10;      system.device.location.country = &#x27;PI&#x27;;&#10;    &#42;/&#10;&#10;    return new Response(JSON.stringify({ system, client }));&#10;  },&#10;};&#10;</code></pre>
<p>Keep reading for more complete examples of different use cases or refer to <a href="/zaraz/reference/context/">Zaraz Context</a>.</p>
<h2 id="configuring-your-context-enricher">Configuring your Context Enricher</h2>
<p>Now that your Worker is published, you can select it in your Zaraz settings:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Context Enricher Worker.
3. Save your settings.
<p>Your Context Enricher will now run on all Zaraz requests in that given zone.</p>
<h2 id="example-context-enricher">Example Context Enricher</h2>
<h3 id="adding-arbitrary-information-using-an-api">Adding arbitrary information using an API</h3>
<p>You can use the Context Enricher to add information to your context. For example, you could use an API to get the current weather for the user's location and add it to the context.</p>
<pre><code class="language-js">function getWeatherForLocation({ client, system }) {&#10;  // Get the location from the context.&#10;  const { city } = system.device.location;&#10;&#10;  // Get the weather from an API.&#10;  const response = await fetch(&#10;    `https://wttr.in/${encodeURIComponents(city)}?format=j1`&#10;  ).then((response) =&gt; response.json());&#10;&#10;  // Add the weather to the context.&#10;  client.weather = weather;&#10;&#10;  return { client, system };&#10;}&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    const { system, client } = await request.json();&#10;&#10;    // Add the weather to the context.&#10;    const newContext = getWeatherForLocation({ system, client });&#10;&#10;    // Return as JSON&#10;    return new Response(JSON.stringify(newContext));&#10;  },&#10;};&#10;</code></pre>
<p>Now, you can use the weather property anywhere in Zaraz by choosing the <code>Track Property</code> from the attributes input and entering <code>weather</code>.</p>
<h3 id="masking-sensitive-information-such-as-emails">Masking sensitive information, such as emails</h3>
<p>Let's assume we want to redact sensitive information, such as emails. For this, we're going to replace all occurrences of email addresses throughout the context. Please keep in mind that this is only an example and might not fit all edge or use cases.</p>
<p>For the sake of simplicity of this example, we're going to replace all strings that contain an <code>@</code> symbol:</p>
<pre><code class="language-js">function redactEmailAddressesFromObject(context) {&#10;  // Loop through all keys of the object.&#10;  for (const key in context) {&#10;    // Check if the value is a string.&#10;    if (typeof context[key] === &quot;string&quot;) {&#10;      // Check if the string contains an @ symbol.&#10;      if (context[key].includes(&quot;@&quot;)) {&#10;        // Replace the string with a redacted version.&#10;        context[key] = &quot;REDACTED@example.com&quot;;&#10;      }&#10;    } else if (typeof context[key] === &quot;object&quot;) {&#10;      // Recursively call this function to redact the object.&#10;      context[key] = redactEmailAddressesFromObject(context[key]);&#10;    }&#10;  }&#10;&#10;  return context;&#10;}&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    const { system, client } = await request.json();&#10;&#10;    // Redact email addresses from the context.&#10;    const newContext = redactEmailAddressesFromObject({ system, client });&#10;&#10;    // Return as JSON&#10;    return new Response(JSON.stringify(newContext));&#10;  },&#10;};&#10;</code></pre>
