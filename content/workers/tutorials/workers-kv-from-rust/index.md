<p>This tutorial will teach you how to read and write to KV directly from Rust
using <a href="https://github.com/cloudflare/workers-rs">workers-rs</a>.</p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To complete this tutorial, you will need:</p>
<ul>
<li><a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">Git</a>.</li>
<li><a href="/workers/wrangler/">Wrangler</a> CLI.</li>
<li>The <a href="https://www.rust-lang.org/tools/install">Rust</a> toolchain.</li>
<li>And <code>cargo-generate</code> sub-command by running:</li>
</ul>
<pre><code class="language-sh">cargo install cargo-generate&#10;</code></pre>
<h2 id="1-create-your-worker-project-in-rust"><ol>
<li>Create your Worker project in Rust</li>
</ol></h2>
<p>Open a terminal window, and run the following command to generate a Worker project template in Rust:</p>
<pre><code class="language-sh">cargo generate cloudflare/workers-rs&#10;</code></pre>
<p>Then select <code>template/hello-world-http</code> template, give your project a descriptive name and select enter. A new project should be created in your directory. Open the project in your editor and run <code>npx wrangler dev</code> to compile and run your project.</p>
<p>In this tutorial, you will use Workers KV from Rust to build an app to store and retrieve cities by a given country name.</p>
<h2 id="2-create-a-kv-namespace"><ol start="2">
<li>Create a KV namespace</li>
</ol></h2>
<p>In the terminal, use Wrangler to create a KV namespace for <code>cities</code>. This generates a configuration to be added to the project:</p>
<pre><code class="language-sh">npx wrangler kv namespace create cities&#10;</code></pre>
<p>To add this configuration to your project, open the Wrangler file and create an entry for <code>kv_namespaces</code> above the build command:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16048.md")
</div>
<p>With this configured, you can access the KV namespace with the binding <code>&quot;cities&quot;</code> from Rust.</p>
<h2 id="3-write-data-to-kv"><ol start="3">
<li>Write data to KV</li>
</ol></h2>
<p>For this app, you will create two routes: A <code>POST</code> route to receive and store the city in KV, and a <code>GET</code> route to retrieve the city of a given country. For example, a <code>POST</code> request to <code>/France</code> with a body of <code>{&quot;city&quot;: &quot;Paris&quot;}</code> should create an entry of Paris as a city in France. A <code>GET</code> request to <code>/France</code> should retrieve from KV and respond with Paris.</p>
<p>Install <a href="https://serde.rs/">Serde</a> as a project dependency to handle JSON <code>cargo add serde</code>. Then create an app router and a struct for <code>Country</code> in <code>src/lib.rs</code>:</p>
<pre><code class="language-rust">use serde::{Deserialize, Serialize};&#10;use worker::*;&#10;&#10;&#35;[event(fetch)]&#10;async fn fetch(req: Request, env: Env, _ctx: Context) -&gt; Result&lt;Response&gt; {&#10;    let router = Router::new();&#10;&#10;    &#35;[derive(Serialize, Deserialize, Debug)]&#10;    struct Country {&#10;        city: String,&#10;    }&#10;&#10;    router&#10;        // TODO:&#10;        .post_async(&quot;/:country&quot;, |_, _| async move { Response::empty() })&#10;        // TODO:&#10;        .get_async(&quot;/:country&quot;, |_, _| async move { Response::empty() })&#10;        .run(req, env)&#10;        .await&#10;}&#10;</code></pre>
<p>For the post handler, you will retrieve the country name from the path and the city name from the request body. Then, you will save this in KV with the country as key and the city as value. Finally, the app will respond with the city name:</p>
<pre><code class="language-rust">.post_async(&quot;/:country&quot;, |mut req, ctx| async move {&#10;    let country = ctx.param(&quot;country&quot;).unwrap();&#10;    let city = match req.json::&lt;Country&gt;().await {&#10;        Ok(c) =&gt; c.city,&#10;        Err(_) =&gt; String::from(&quot;&quot;),&#10;    };&#10;    if city.is_empty() {&#10;        return Response::error(&quot;Bad Request&quot;, 400);&#10;    };&#10;    return match ctx.kv(&quot;cities&quot;)?.put(country, &amp;city)?.execute().await {&#10;        Ok(_) =&gt; Response::ok(city),&#10;        Err(_) =&gt; Response::error(&quot;Bad Request&quot;, 400),&#10;    };&#10;})&#10;</code></pre>
<p>Save the file and make a <code>POST</code> request to test this endpoint:</p>
<pre><code class="language-sh">curl --json &#x27;{&quot;city&quot;: &quot;Paris&quot;}&#x27; http://localhost:8787/France&#10;</code></pre>
<h2 id="4-read-data-from-kv"><ol start="4">
<li>Read data from KV</li>
</ol></h2>
<p>To retrieve cities stored in KV, write a <code>GET</code> route that pulls the country name from the path and searches KV. You also need some error handling if the country is not found:</p>
<pre><code class="language-rust">.get_async(&quot;/:country&quot;, |_req, ctx| async move {&#10;    if let Some(country) = ctx.param(&quot;country&quot;) {&#10;        return match ctx.kv(&quot;cities&quot;)?.get(country).text().await? {&#10;            Some(city) =&gt; Response::ok(city),&#10;            None =&gt; Response::error(&quot;Country not found&quot;, 404),&#10;        };&#10;    }&#10;    Response::error(&quot;Bad Request&quot;, 400)&#10;})&#10;</code></pre>
<p>Save and make a curl request to test the endpoint:</p>
<pre><code class="language-sh">curl http://localhost:8787/France&#10;</code></pre>
<h2 id="5-deploy-your-project"><ol start="5">
<li>Deploy your project</li>
</ol></h2>
<p>The source code for the completed app should include the following:</p>
<pre><code class="language-rust">use serde::{Deserialize, Serialize};&#10;use worker::*;&#10;&#10;&#35;[event(fetch)]&#10;async fn fetch(req: Request, env: Env, _ctx: Context) -&gt; Result&lt;Response&gt; {&#10;    let router = Router::new();&#10;&#10;    &#35;[derive(Serialize, Deserialize, Debug)]&#10;    struct Country {&#10;        city: String,&#10;    }&#10;&#10;    router&#10;        .post_async(&quot;/:country&quot;, |mut req, ctx| async move {&#10;            let country = ctx.param(&quot;country&quot;).unwrap();&#10;            let city = match req.json::&lt;Country&gt;().await {&#10;                Ok(c) =&gt; c.city,&#10;                Err(_) =&gt; String::from(&quot;&quot;),&#10;            };&#10;            if city.is_empty() {&#10;                return Response::error(&quot;Bad Request&quot;, 400);&#10;            };&#10;            return match ctx.kv(&quot;cities&quot;)?.put(country, &amp;city)?.execute().await {&#10;                Ok(_) =&gt; Response::ok(city),&#10;                Err(_) =&gt; Response::error(&quot;Bad Request&quot;, 400),&#10;            };&#10;        })&#10;        .get_async(&quot;/:country&quot;, |_req, ctx| async move {&#10;            if let Some(country) = ctx.param(&quot;country&quot;) {&#10;                return match ctx.kv(&quot;cities&quot;)?.get(country).text().await? {&#10;                    Some(city) =&gt; Response::ok(city),&#10;                    None =&gt; Response::error(&quot;Country not found&quot;, 404),&#10;                };&#10;            }&#10;            Response::error(&quot;Bad Request&quot;, 400)&#10;        })&#10;        .run(req, env)&#10;        .await&#10;}&#10;</code></pre>
<p>To deploy your Worker, run the following command:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a>.</li>
<li><a href="/kv/get-started/">Using KV in Workers</a>.</li>
</ul>
