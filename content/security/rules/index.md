<p>Security rules perform security-related actions on incoming requests that match specified filters. Rules are evaluated and executed in order, from first to last.</p>
<p>You can create Security Rules from reviewed <a href="/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/">Attack Signature Detection</a> confidence, category, and Ref metadata.</p>
<p>To access security rules in the new security dashboard, go to the <strong>Security rules</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="security-rules">Security rules</h2>
<p>The <strong>Security rules</strong> tab includes a list of different types of rules configured in your domain/zone to protect your applications and resources.</p>
<p>To create a security rule:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>(Optional) Select <strong>Templates</strong>, and then select a template from the list. You can customize the default configuration of the template before deploying the new rule. Refer to the resources listed in the next step.</p>
</li>
<li>
<p>Select <strong>Create rule</strong> &gt; select the type of rule you want to create. Refer to the following resources about each rule type:</p>
<ul>
<li><a href="/waf/custom-rules/create-dashboard/#rule-form">Custom rules</a></li>
<li><a href="/waf/rate-limiting-rules/create-zone-dashboard/#rule-form">Rate limiting rules</a></li>
<li><a href="/api-shield/security/sequence-mitigation/#rule-form">API sequence rules</a></li>
<li><a href="/api-shield/security/jwt-validation/#rule-form">API JWT validation rules</a> (requires a <a href="/security/settings/#all-settings">token configuration</a>)</li>
<li><a href="/waf/managed-rules/waf-exceptions/define-dashboard/#2-define-basic-exception-parameters">Managed rules exceptions</a></li>
<li><a href="/client-side-security/rules/create-dashboard/#rule-form">Content security rules</a> (previously known as policies)</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/359.md")
</aside>
<h2 id="ddos-protection">DDoS protection</h2>
<p>The <strong>DDoS protection</strong> tab shows the multiple DDoS mitigation services provided by Cloudflare. You can create rules to override these mitigation tools. DDoS attack protection overrides are only available to Enterprise customers with the Advanced DDoS Protection subscription.</p>
<p>To learn more about DDoS protection overrides, refer to the following resources:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/">HTTP DDoS attack protection overrides</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/">Network-layer DDoS attack protection overrides</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/358.md")
</aside>
<h2 id="interaction-between-different-app-security-features">Interaction between different app security features</h2>
<p>If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
