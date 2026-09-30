<p>Customers with a Bot Management and a <a href="/workers/">Workers</a> subscription can use the template below to introduce a delay to requests that are likely from bots.</p>
<p>The template sets a minimum and maximum delay, and delays requests where the bot score is less than 30 and the URI path starts with <code>/exampleURI</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3462.md")
</div>
