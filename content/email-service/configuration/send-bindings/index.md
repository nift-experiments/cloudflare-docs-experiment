<p>When you add a <code>send_email</code> binding to a Worker, you can restrict which addresses it may send from and to. Configure these restrictions in your Wrangler configuration file. For the binding API itself, refer to the <a href="/email-service/api/send-emails/workers-api/">Workers API</a>.</p>
<h2 id="binding-types">Binding types</h2>
<p>Each entry in <code>send_email</code> can be configured to restrict what the binding can do. The sender address must always belong to a domain you have onboarded to Email Service.</p>
<ul>
<li><strong>No restriction attribute</strong>: The binding can send to any verified destination address in your account.</li>
<li><strong><code>destination_address</code></strong>: The binding can only send to the single destination address configured here. If you call <code>send()</code> with <code>to</code> set to <code>null</code> or <code>undefined</code>, the configured address is used.</li>
<li><strong><code>allowed_destination_addresses</code></strong>: The binding can only send to addresses listed in this allowlist.</li>
<li><strong><code>allowed_sender_addresses</code></strong>: The binding can only send from the addresses listed in this allowlist.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8615.md")
</div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/api/send-emails/workers-api/">Workers API</a> — send emails from a Worker using the binding.</li>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — onboard the domains you send from.</li>
</ul>
