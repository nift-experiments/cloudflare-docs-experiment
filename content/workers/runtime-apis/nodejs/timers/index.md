<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17133.md")
</aside>
<p>Use <a href="https://nodejs.org/api/timers.html"><code>node:timers</code></a> APIs to schedule functions to be executed later.</p>
<p>This includes <a href="https://nodejs.org/api/timers.html#settimeoutcallback-delay-args"><code>setTimeout</code></a> for calling a function after a delay,
<a href="https://nodejs.org/api/timers.html#clearintervaltimeout"><code>setInterval</code></a> for calling a function repeatedly,
and <a href="https://nodejs.org/api/timers.html#setimmediatecallback-args"><code>setImmediate</code></a> for calling a function in the next iteration of the event loop.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17134.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17132.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17131.md")
</aside>
<p>The full <code>node:timers</code> API is documented in the <a href="https://nodejs.org/api/timers.html">Node.js documentation for <code>node:timers</code></a>.</p>
