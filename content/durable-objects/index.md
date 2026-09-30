<div class="nb-description">
@markup("md", "content/.markup/bodies/1081.md")
</div>
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<p>Durable Objects provide a building block for stateful applications and distributed systems.</p>
<p>Use Durable Objects to build applications that need coordination among multiple clients, like collaborative editing tools, interactive chat, multiplayer games, live notifications, and deep distributed systems, without requiring you to build serialization and coordination primitives on your own.</p>
<p><a class="nb-link-button" href="/durable-objects/get-started/">Get started</a></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1080.md")
</aside>
<h3 id="what-are-durable-objects">What are Durable Objects?</h3>
<p>A Durable Object is a special kind of <a href="/workers/">Cloudflare Worker</a> which uniquely combines compute with storage. Like a Worker, a Durable Object is automatically provisioned geographically close to where it is first requested, starts up quickly when needed, and shuts down when idle. You can have millions of them around the world. However, unlike regular Workers:</p>
<ul>
<li>Each Durable Object has a <strong>globally-unique name</strong>, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together.</li>
<li>Each Durable Object has some <strong>durable storage</strong> attached. Since this storage lives together with the object, it is strongly consistent yet fast to access.</li>
</ul>
<p>Therefore, Durable Objects enable <strong>stateful</strong> serverless applications.</p>
<p>For more information, refer to the full <a href="/durable-objects/concepts/what-are-durable-objects/">What are Durable Objects?</a> page.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1083.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1084.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1085.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1086.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1087.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1088.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1089.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/1095.md")
</div>
