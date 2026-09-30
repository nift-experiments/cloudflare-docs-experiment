<h2 id="exceptions">Exceptions</h2>
<p>An error thrown by an RPC method, or used to reject the method's returned Promise, propagates to the caller as a new error object. With enhanced error serialization, Workers preserves the effective <code>name</code> and <code>message</code> and serializable own properties, including non-enumerable properties such as <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause"><code>cause</code></a>.</p>
<p><a href="/workers/configuration/compatibility-flags/#enhanced-error-serialization">Enhanced error serialization</a> uses the <code>enhanced_error_serialization</code> compatibility flag. It is on by default for compatibility dates on or after <code>2026-04-21</code>. For earlier compatibility dates, add the flag to both the RPC provider and consumer. A Worker can opt out with <code>legacy_error_serialization</code>. Without enhanced error serialization, RPC uses legacy error reconstruction and does not preserve custom own properties.</p>
<p>The provider must be able to serialize the error and its own property values. Keep public error properties small and serializable. If an own property contains a non-serializable value, Workers does not guarantee that the enhanced error details will reach the consumer.</p>
<p>On the consumer, treat the error's serializable fields as the RPC contract. Workers does not preserve or guarantee:</p>
<ul>
<li>The source object's identity, custom prototype, or constructor.</li>
<li>The results of <code>instanceof</code> checks, especially for custom error classes.</li>
<li>Prototype methods or property descriptors.</li>
<li>The provider's original stack trace. The consumer may see a new stack from error reconstruction instead.</li>
<li>Non-serializable property values.</li>
</ul>
<p>For example, an instance of <code>ProviderError extends Error</code> can arrive with <code>name</code> set to <code>&quot;ProviderError&quot;</code> and with serializable own fields such as <code>code</code>, but it is not an instance of a consumer-side <code>ProviderError</code> class. Check documented fields such as <code>name</code> and <code>code</code> instead of relying on class identity.</p>
<h2 id="additional-properties">Additional properties</h2>
<p>For some remote exceptions, the runtime may add properties to the propagated exception, such as retry or Durable Object metadata. These properties are separate from the provider's custom properties. Refer to <a href="/durable-objects/best-practices/error-handling">Durable Object error handling</a> for more details.</p>
