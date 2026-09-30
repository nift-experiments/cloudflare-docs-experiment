<p>In this tutorial, you will build a project that leverages <a href="https://platform.openai.com/docs/guides/function-calling">OpenAI's function calling</a> feature, available in OpenAI's latest Chat Completions API models.</p>
<p>The function calling feature allows the AI model to intelligently decide when to call a function based on the input, and respond in JSON format to match the function's signature. You will use the function calling feature to request for the model to determine a website URL which contains information relevant to a message from the user, retrieve the text content of the site, and, finally, return a final response from the model informed by real-time web data.</p>
<h2 id="what-you-will-learn">What you will learn</h2>
<ul>
<li>How to use OpenAI's function calling feature.</li>
<li>Integrating OpenAI's API in a Cloudflare Worker.</li>
<li>Fetching and processing website content using Cheerio.</li>
<li>Handling API responses and function calls in JavaScript.</li>
<li>Storing API keys as secrets with Wrangler.</li>
</ul>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<p>Create a Worker project in the command line:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- openai-function-calling-workers</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- openai-function-calling-workers" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare openai-function-calling-workers</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare openai-function-calling-workers" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest openai-function-calling-workers</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest openai-function-calling-workers" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your new <code>openai-function-calling-workers</code> Worker project:</p>
<pre><code class="language-sh">cd openai-function-calling-workers&#10;</code></pre>
<p>Inside of your new <code>openai-function-calling-workers</code> directory, find the <code>src/index.js</code> file. You will configure this file for most of the tutorial.</p>
<p>You will also need an OpenAI account and API key for this tutorial. If you do not have one, <a href="https://platform.openai.com/signup">create a new OpenAI account</a> and <a href="https://platform.openai.com/account/api-keys">create an API key</a> to continue with this tutorial. Make sure to store you API key somewhere safe so you can use it later.</p>
<h2 id="2-make-a-request-to-openai"><ol start="2">
<li>Make a request to OpenAI</li>
</ol></h2>
<p>With your Worker project created, make your first request to OpenAI. You will use the OpenAI node library to interact with the OpenAI API. In this project, you will also use the Cheerio library to handle processing the HTML content of websites</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i openai cheerio</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i openai cheerio" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add openai cheerio</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add openai cheerio" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add openai cheerio</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add openai cheerio" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add openai cheerio</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add openai cheerio" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Now, define the structure of your Worker in <code>index.js</code>:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Initialize OpenAI API&#10;		// Handle incoming requests&#10;		return new Response(&quot;Hello World!&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>Above <code>export default</code>, add the imports for <code>openai</code> and <code>cheerio</code>:</p>
<pre><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;import * as cheerio from &quot;cheerio&quot;;&#10;</code></pre>
<p>Within your <code>fetch</code> function, instantiate your <code>OpenAI</code> client:</p>
<pre><code class="language-js">async fetch(request, env, ctx) {&#10;  const openai = new OpenAI({&#10;    apiKey: env.OPENAI_API_KEY,&#10;  });&#10;&#10;  // Handle incoming requests&#10;  return new Response(&#x27;Hello World!&#x27;);&#10;},&#10;</code></pre>
<p>Use <a href="/workers/wrangler/commands/general/#secret-put"><code>wrangler secret put</code></a> to set <code>OPENAI_API_KEY</code>. This <a href="/workers/configuration/secrets/">secret's</a> value is the API key you created earlier in the OpenAI dashboard:</p>
<pre><code class="language-sh">npx wrangler secret put &lt;OPENAI_API_KEY&gt;&#10;</code></pre>
<p>For local development, create a new file <code>.dev.vars</code> in your Worker project and add this line. Make sure to replace <code>OPENAI_API_KEY</code> with your own OpenAI API key:</p>
<pre><code class="language-txt">OPENAI_API_KEY = &quot;&lt;YOUR_OPENAI_API_KEY&gt;&quot;&#10;</code></pre>
<p>Now, make a request to the OpenAI <a href="https://platform.openai.com/docs/guides/gpt/chat-completions-api">Chat Completions API</a>:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const openai = new OpenAI({&#10;			apiKey: env.OPENAI_API_KEY,&#10;		});&#10;&#10;		const url = new URL(request.url);&#10;		const message = url.searchParams.get(&quot;message&quot;);&#10;&#10;		const messages = [&#10;			{&#10;				role: &quot;user&quot;,&#10;				content: message ? message : &quot;What&#x27;s in the news today?&quot;,&#10;			},&#10;		];&#10;&#10;		const tools = [&#10;			{&#10;				type: &quot;function&quot;,&#10;				function: {&#10;					name: &quot;read_website_content&quot;,&#10;					description: &quot;Read the content on a given website&quot;,&#10;					parameters: {&#10;						type: &quot;object&quot;,&#10;						properties: {&#10;							url: {&#10;								type: &quot;string&quot;,&#10;								description: &quot;The URL to the website to read&quot;,&#10;							},&#10;						},&#10;						required: [&quot;url&quot;],&#10;					},&#10;				},&#10;			},&#10;		];&#10;&#10;		const chatCompletion = await openai.chat.completions.create({&#10;			model: &quot;gpt-4o-mini&quot;,&#10;			messages: messages,&#10;			tools: tools,&#10;			tool_choice: &quot;auto&quot;,&#10;		});&#10;&#10;		const assistantMessage = chatCompletion.choices[0].message;&#10;		console.log(assistantMessage);&#10;&#10;		//Later you will continue handling the assistant&#x27;s response here&#10;		return new Response(assistantMessage.content);&#10;	},&#10;};&#10;</code></pre>
<p>Review the arguments you are passing to OpenAI:</p>
<ul>
<li><strong>model</strong>: This is the model you want OpenAI to use for your request. In this case, you are using <code>gpt-4o-mini</code>.</li>
<li><strong>messages</strong>: This is an array containing all messages that are part of the conversation. Initially you provide a message from the user, and we later add the response from the model. The content of the user message is either the <code>message</code> query parameter from the request URL or the default &quot;What's in the news today?&quot;.</li>
<li><strong>tools</strong>: An array containing the actions available to the AI model. In this example you only have one tool, <code>read_website_content</code>, which reads the content on a given website.
<ul>
<li><strong>name</strong>: The name of your function. In this case, it is <code>read_website_content</code>.</li>
<li><strong>description</strong>: A short description that lets the model know the purpose of the function. This is optional but helps the model know when to select the tool.</li>
<li><strong>parameters</strong>: A JSON Schema object which describes the function. In this case we request a response containing an object with the required property <code>url</code>.</li>
</ul>
</li>
<li><strong>tool_choice</strong>: This argument is technically optional as <code>auto</code> is the default. This argument indicates that either a function call or a normal message response can be returned by OpenAI.</li>
</ul>
<h2 id="3-building-your-read-website-content-function"><ol start="3">
<li>Building your <code>read_website_content()</code> function</li>
</ol></h2>
<p>You will now need to define the <code>read_website_content</code> function, which is referenced in the <code>tools</code> array. The <code>read_website_content</code> function fetches the content of a given URL and extracts the text from <code>&lt;p&gt;</code> tags using the <code>cheerio</code> library:</p>
<p>Add this code above the <code>export default</code> block in your <code>index.js</code> file:</p>
<pre><code class="language-js">async function read_website_content(url) {&#10;	console.log(&quot;reading website content&quot;);&#10;&#10;	const response = await fetch(url);&#10;	const body = await response.text();&#10;	let cheerioBody = cheerio.load(body);&#10;	const resp = {&#10;		website_body: cheerioBody(&quot;p&quot;).text(),&#10;		url: url,&#10;	};&#10;	return JSON.stringify(resp);&#10;}&#10;</code></pre>
<p>In this function, you take the URL that you received from OpenAI and use JavaScript's <a href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch"><code>Fetch API</code></a> to pull the content of the website and extract the paragraph text. Now we need to determine when to call this function.</p>
<h2 id="4-process-the-assistant-s-messages"><ol start="4">
<li>Process the Assistant's Messages</li>
</ol></h2>
<p>Next, we need to process the response from the OpenAI API to check if it includes any function calls. If a function call is present, you should execute the corresponding function in your Worker. Note that the assistant may request multiple function calls.</p>
<p>Modify the fetch method within the <code>export default</code> block as follows:</p>
<pre><code class="language-js">// ... your previous code ...&#10;&#10;if (assistantMessage.tool_calls) {&#10;	for (const toolCall of assistantMessage.tool_calls) {&#10;		if (toolCall.function.name === &quot;read_website_content&quot;) {&#10;			const url = JSON.parse(toolCall.function.arguments).url;&#10;			const websiteContent = await read_website_content(url);&#10;			messages.push({&#10;				role: &quot;tool&quot;,&#10;				tool_call_id: toolCall.id,&#10;				name: toolCall.function.name,&#10;				content: websiteContent,&#10;			});&#10;		}&#10;	}&#10;&#10;	const secondChatCompletion = await openai.chat.completions.create({&#10;		model: &quot;gpt-4o-mini&quot;,&#10;		messages: messages,&#10;	});&#10;&#10;	return new Response(secondChatCompletion.choices[0].message.content);&#10;} else {&#10;	// this is your existing return statement&#10;	return new Response(assistantMessage.content);&#10;}&#10;</code></pre>
<p>Check if the assistant message contains any function calls by checking for the <code>tool_calls</code> property. Because the AI model can call multiple functions by default, you need to loop through any potential function calls and add them to the <code>messages</code> array. Each <code>read_website_content</code> call will invoke the <code>read_website_content</code> function you defined earlier and pass the URL generated by OpenAI as an argument. `</p>
<p>The <code>secondChatCompletion</code> is needed to provide a response informed by the data you retrieved from each function call. Now, the last step is to deploy your Worker.</p>
<p>Test your code by running <code>npx wrangler dev</code> and open the provided url in your browser. This will now show you OpenAI’s response using real-time information from the retrieved web data.</p>
<h2 id="5-deploy-your-worker-application"><ol start="5">
<li>Deploy your Worker application</li>
</ol></h2>
<p>To deploy your application, run the <code>npx wrangler deploy</code> command to deploy your Worker application:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>You can now preview your Worker at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>. Going to this URL will display the response from OpenAI. Optionally, add the <code>message</code> URL parameter to write a custom message: for example, <code>https://&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/?message=What is the weather in NYC today?</code>.</p>
<h2 id="6-next-steps"><ol start="6">
<li>Next steps</li>
</ol></h2>
<p>Reference the <a href="https://github.com/LoganGrasby/Cloudflare-OpenAI-Functions-Demo/blob/main/src/worker.js">finished code for this tutorial on GitHub</a>.</p>
<p>To continue working with Workers and AI, refer to <a href="https://blog.cloudflare.com/langchain-and-cloudflare/">the guide on using LangChain and Cloudflare Workers together</a> or <a href="https://blog.cloudflare.com/magic-in-minutes-how-to-build-a-chatgpt-plugin-with-cloudflare-workers/">how to build a ChatGPT plugin with Cloudflare Workers</a>.</p>
<p>If you have any questions, need assistance, or would like to share your project, join the Cloudflare Developer community on <a href="https://discord.cloudflare.com">Discord</a> to connect with fellow developers and the Cloudflare team.</p>
