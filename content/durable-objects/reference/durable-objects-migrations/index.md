<p>The <code>exports</code> field in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> is the declarative way to manage <a href="/durable-objects/">Durable Object class</a> lifecycle. You declare each Durable Object class your Worker exports — along with whether it is live, deleted, renamed, or transferred — and Cloudflare reconciles your declaration against the namespaces that have already been provisioned for your Worker.</p>
<p>This page covers how to:</p>
<ul>
<li><a href="#define-a-durable-object-class">Create</a> a new Durable Object class.</li>
<li><a href="#delete-a-durable-object-class">Delete</a> a Durable Object class and its data.</li>
<li><a href="#rename-a-durable-object-class">Rename</a> a Durable Object class.</li>
<li><a href="#transfer-a-durable-object-class-between-workers">Transfer</a> a Durable Object class between Workers.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-the-legacy-migrations-array">Looking for the legacy `migrations` array?</h3>
@markup("md", "content/.markup/bodies/8108.md")
</aside>
<h2 id="how-exports-works">How <code>exports</code> works</h2>
<p>When you deploy a Worker that declares <code>exports</code>, Cloudflare compares three sources of truth:</p>
<ol>
<li><strong>Your code</strong> — the set of Durable Object classes the Worker actually exports.</li>
<li><strong>Your <code>exports</code> configuration</strong> — what you have declared about each class.</li>
<li><strong>Provisioned state</strong> — the Durable Object namespaces that already exist for this Worker.</li>
</ol>
<p>A class that appears only in your code is ignored until you declare it in <code>exports</code>; Cloudflare does not provision a namespace implicitly. Other disagreements, such as a live entry whose class is missing from code or a provisioned namespace with no matching entry, are surfaced as structured errors or, where the intent is unambiguous, actions that Cloudflare applies for you.</p>
<p>A minimal <code>exports</code> block declares each Durable Object class as a live entry:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8109.md")
</div>
<p>To declare a destructive operation — deleting, renaming, or transferring a class — you change the entry's <code>state</code> to a tombstone variant. The class name remains the same; the value tells Cloudflare what to do with the existing namespace.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th><code>state</code></th>
<th>Required fields</th>
</tr>
</thead>
<tbody>
<tr>
<td>Define a new class (default)</td>
<td><code>&quot;created&quot;</code> (or omitted)</td>
<td><code>storage</code></td>
</tr>
<tr>
<td>Delete a class</td>
<td><code>&quot;deleted&quot;</code></td>
<td><em>(none)</em></td>
</tr>
<tr>
<td>Rename a class</td>
<td><code>&quot;renamed&quot;</code></td>
<td><code>renamed_to</code></td>
</tr>
<tr>
<td>Transfer a class to another Worker</td>
<td><code>&quot;transferred&quot;</code></td>
<td><code>transferred_to</code></td>
</tr>
<tr>
<td>Receive a transfer from another Worker</td>
<td><code>&quot;expecting-transfer&quot;</code></td>
<td><code>storage</code>, <code>transfer_from</code></td>
</tr>
</tbody>
</table>
<p>The rest of this page describes each operation in detail and links to the <a href="#exports-configuration-reference"><code>exports</code> configuration reference</a> for the full schema.</p>
<h2 id="define-a-durable-object-class">Define a Durable Object class</h2>
<p>To define a new Durable Object class, add an entry to <code>exports</code> keyed by the class name and set <code>storage</code> to <code>&quot;sqlite&quot;</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommended-sqlite-backed-durable-objects">Recommended SQLite-backed Durable Objects</h3>
@markup("md", "content/.markup/bodies/8107.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8111.md")
</div>
<p>Cloudflare provisions a namespace for the class the first time you deploy. On subsequent deploys with the same entry, no namespace changes are made — the entry simply confirms that the class is still live.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8106.md")
</aside>
<h2 id="delete-a-durable-object-class">Delete a Durable Object class</h2>
<p>Replace the live entry with a <code>deleted</code> tombstone to retire a Durable Object class. Deleting a class removes its namespace and <strong>all of its stored data permanently</strong> — this is not a soft delete.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8113.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deleting-a-class-destroys-its-data">Deleting a class destroys its data</h3>
@markup("md", "content/.markup/bodies/8105.md")
</aside>
<p>A <code>deleted</code> tombstone has two preconditions enforced at deploy time:</p>
<ul>
<li>The class must not be present in your Worker code. Cloudflare will not delete a namespace whose class is still being shipped, because runtime bindings would resolve to a deleted namespace.</li>
<li>No other Worker in your account may bind to the namespace. If another Worker still binds to the class, the deploy is rejected with <code>tombstone_delete_blocked_by_external_bindings</code> and the list of referencing scripts is returned. Redeploy those Workers without the binding first, then re-run your deploy.</li>
</ul>
<p>Once the namespace has been deleted, the tombstone becomes stale. Cloudflare reports this in the <a href="#reading-the-reconciliation-output">reconciliation output</a> and lists the entry in <code>removable_entries</code> so you can safely remove it from <code>exports</code>.</p>
<h2 id="rename-a-durable-object-class">Rename a Durable Object class</h2>
<p>Renaming a Durable Object class moves stored data from one class to another within the same Worker. Renaming requires:</p>
<ul>
<li>A <code>renamed</code> tombstone keyed by the old class name, with <code>renamed_to</code> pointing at the new class name.</li>
<li>A live entry for the new class name in the same <code>exports</code> map (so the data has somewhere to land).</li>
</ul>
<p>For a brand-new deploy where the old class is no longer in your code, a single deploy is enough:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8114.md")
</div>
<p>After the rename applies, the namespace's class name is updated to <code>NewName</code> and runtime bindings that reference the new class name resolve to the same data.</p>
<h3 id="avoid-downtime-during-a-rename">Avoid downtime during a rename</h3>
<p>A Durable Object class rename involves two updates that are not perfectly atomic at the runtime layer: the namespace's class pointer and the Worker code that exports the class. During a deploy rollout, one update may be visible before the other for a few seconds. To avoid runtime errors during this window, use a <strong>three-deploy rename</strong>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8116.md")
</div>
<p>The <code>renamed_to</code> target must:</p>
<ul>
<li>Be a valid JavaScript identifier and differ from the source class name.</li>
<li>Appear as a live entry (<code>state: &quot;created&quot;</code> or omitted) in the same <code>exports</code> map. Cloudflare rejects a <code>renamed_to</code> value that names another tombstone or is missing entirely.</li>
<li>Not collide with an existing namespace under the same name on this Worker. If a namespace already exists under the target name, delete it via its own <code>deleted</code> tombstone in a prior deploy first.</li>
</ul>
<h2 id="transfer-a-durable-object-class-between-workers">Transfer a Durable Object class between Workers</h2>
<p>Transferring moves an existing Durable Object namespace from one Worker (the <strong>source</strong>) to another Worker (the <strong>target</strong>) in the same account. Because two Workers must coordinate, transfer is a multi-deploy flow.</p>
<p>The target Worker declares an <code>expecting-transfer</code> entry that names the source Worker. The source Worker declares a <code>transferred</code> tombstone that names the target Worker. The actual handoff commits when the source Worker's deploy lands.</p>
<p>The recommended sequence is four deploys:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8122.md")
</div>
<p>After the handoff has rolled out everywhere, you can remove <code>MyDO</code> from the source Worker's code and delete the <code>transferred</code> tombstone from the source's <code>exports</code> map. While other Workers in the account still bind to <code>MyDO</code> on the source, the reconciliation output lists them in <code>referencing_scripts</code>; redeploy each of them with bindings re-pointed at the target before removing the source tombstone.</p>
<h3 id="cancel-a-pending-transfer">Cancel a pending transfer</h3>
<p>A pending transfer persists until the source Worker commits with a <code>transferred</code> tombstone, or the target Worker cancels by removing the <code>expecting-transfer</code> entry. To cancel, redeploy the target without the entry (or replace it with a normal live entry). Cloudflare deletes the pending record and the source Worker keeps its namespace.</p>
<h3 id="transfer-constraints">Transfer constraints</h3>
<ul>
<li>Both Workers must live in the same Cloudflare account.</li>
<li>Cross-<a href="/cloudflare-for-platforms/workers-for-platforms/">dispatch-namespace</a> transfers are not supported. The source and target Workers must both be in the same dispatch-namespace context (or both be outside any dispatch namespace).</li>
<li>A target Worker can hold only one pending phase-1 hint per class at a time. To redirect a pending transfer to a different source, cancel the current pending transfer first.</li>
</ul>
<h2 id="storage-backends">Storage backends</h2>
<p>Live entries (<code>state: &quot;created&quot;</code> and <code>state: &quot;expecting-transfer&quot;</code>) must declare a <code>storage</code> value:</p>
<ul>
<li><code>&quot;sqlite&quot;</code> selects the SQLite storage backend. This is the recommended and only path for new namespaces. SQLite-backed namespaces support <a href="/durable-objects/api/sqlite-storage-api/">SQL</a>, <a href="/durable-objects/api/sqlite-storage-api/#point-in-time-recovery-api">Point-in-Time Recovery</a>, and a higher per-object storage limit.</li>
<li><code>&quot;legacy-kv&quot;</code> selects the key-value storage backend. Cloudflare only accepts this value for namespaces that were already provisioned with key-value storage (typically Workers that started on the <a href="/durable-objects/reference/durable-object-class-migrations-legacy/">legacy <code>migrations</code> array</a> before SQLite was the default). You cannot create a <strong>new</strong> key-value-backed namespace through <code>exports</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8104.md")
</aside>
<p>Storage type is immutable once a namespace exists. Cloudflare rejects an <code>exports</code> change that switches a provisioned namespace from <code>sqlite</code> to <code>legacy-kv</code> or vice versa with the error <code>storage_type_mismatch</code>. To genuinely change storage backends, delete the namespace via a <code>deleted</code> tombstone and re-provision it under the new backend (with full data loss in between).</p>
<h2 id="reading-the-reconciliation-output">Reading the reconciliation output</h2>
<p>When a deployment applies a Durable Object class lifecycle change, <code>wrangler deploy</code> prints a <code>Durable Object exports reconciliation</code> block. The block also appears when reconciliation produces warnings, info notices, or removable entries. Wrangler omits the block when nothing changed and there are no notices.</p>
<p>A typical output looks like:</p>
<pre><code class="language-txt">Durable Object exports reconciliation:&#10;  Created: ChatRoom&#10;  Renamed: OldRoom → ChatRoom&#10;  Transferred (committed): Widget → target-worker&#10;  Transfer pending: Incoming ← source-worker&#10;&#10;  Info:&#10;    [tombstone_class_still_in_code] OldRoom: Tombstone of type &#x27;renamed&#x27; applied. Class &#x27;OldRoom&#x27; is still exported in code; this is the supported pattern for zero-downtime rename rollouts.&#10;    [stale_tombstone] OldGone: Tombstone of type &#x27;deleted&#x27; for class &#x27;OldGone&#x27; has no effect (no namespace exists with this class name). Safe to remove from `exports`.&#10;&#10;  Safe to remove from `exports`: OldGone&#10;</code></pre>
<p>The block has four sections:</p>
<ul>
<li><strong>Action lines</strong> (<code>Created</code>, <code>Updated</code>, <code>Deleted</code>, <code>Renamed</code>, <code>Transferred</code>, <code>Transfer pending</code>) report the changes Cloudflare applied during this deploy.</li>
<li><strong>Warnings</strong> (yellow) flag conditions that should be investigated but do not block the deploy. The set of warning scenarios is reserved for future use; current Cloudflare deploys do not emit them.</li>
<li><strong>Info</strong> (dimmed) reports non-blocking notices: stale tombstones that no longer apply, and tombstones applied while the source class is still in code (the supported pattern for zero-downtime rollouts).</li>
<li><strong>Safe to remove from <code>exports</code></strong> lists tombstone entries that are stale and have no other Workers in the account binding to the source class. You can delete these entries from your <code>exports</code> map on your next config edit.</li>
</ul>
<p>Info entries can include a <code>referencing_scripts</code> list — other Workers in the account whose bindings still resolve to the affected namespace. Redeploy those Workers with bindings re-pointed at the new class name before removing the tombstone, or you will orphan their bindings.</p>
<p>If the deploy fails, the output shows a structured error per class:</p>
<pre><code class="language-txt">✘ [orphaned_provisioned_namespace] class &#x27;Bar&#x27;: A namespace exists for &#x27;Bar&#x27; but no `exports` entry declares it.&#10;    Suggestion: add an `exports` entry for &#x27;Bar&#x27;, or add a `deleted` tombstone to remove the namespace.&#10;    Referencing scripts: worker-foo, worker-bar&#10;</code></pre>
<p>All class-level errors from a single deploy are reported together so you can fix them in one round trip. Refer to the <a href="#error-reference">error reference</a> for the full list of error scenarios.</p>
<h2 id="stale-tombstones-and-cleanup">Stale tombstones and cleanup</h2>
<p>A tombstone becomes <strong>stale</strong> when applying it produces no state change — for example, a <code>deleted</code> tombstone for a class whose namespace has already been removed, or a <code>renamed</code> tombstone after the rename has already landed.</p>
<p>Cloudflare emits a <code>stale_tombstone</code> info notice on every deploy where a tombstone is stale, until you remove the entry from <code>exports</code>. The notice is intentionally repeated so you do not forget to clean up.</p>
<p>For renamed and transferred tombstones, Cloudflare also enumerates other Workers in your account whose <code>durable_objects.bindings</code> entries still reference the source class name. These appear as <code>referencing_scripts</code> on the info notice. While <code>referencing_scripts</code> is non-empty, removing the tombstone could orphan those bindings — redeploy the referencing Workers with bindings re-pointed at the new class first.</p>
<p>The top-level &quot;Safe to remove from <code>exports</code>&quot; line in the reconciliation output names every stale tombstone whose <code>referencing_scripts</code> is empty. Use that list as the authoritative &quot;you can delete these now&quot; hint.</p>
<h2 id="environments-dispatch-namespaces-and-previews">Environments, dispatch namespaces, and previews</h2>
<p><code>exports</code> can be specified at the top level of your Wrangler configuration file and overridden per <a href="/durable-objects/reference/environments/">environment</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8123.md")
</div>
<p>If <code>exports</code> is only declared at the top level, named environments inherit the same value. Each environment maintains its own provisioned namespaces, so tombstones apply only within the environment they are declared in.</p>
<p><a href="/workers/versions-and-deployments/preview-urls/">Preview deployments</a> and <a href="/cloudflare-for-platforms/workers-for-platforms/">dispatch namespaces</a> follow the same rules. Cross-dispatch-namespace transfers are not supported — the source and target Workers in a <code>transferred</code> / <code>expecting-transfer</code> pair must both live in the same dispatch-namespace context (or both be outside any dispatch namespace).</p>
<h2 id="exports-configuration-reference"><code>exports</code> configuration reference</h2>
<p>The <code>exports</code> field is a map keyed by Durable Object class name. Each value is an object whose fields depend on <code>state</code>:</p>
<ul>
<li>
<p><code>type</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>For Durable Object class entries, set this to <code>&quot;durable-object&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>state</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The lifecycle state. One of <code>&quot;created&quot;</code> (the default, omit to use), <code>&quot;deleted&quot;</code>, <code>&quot;renamed&quot;</code>, <code>&quot;transferred&quot;</code>, or <code>&quot;expecting-transfer&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>storage</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span></p>
<ul>
<li>Required when <code>state</code> is <code>&quot;created&quot;</code> or <code>&quot;expecting-transfer&quot;</code>. One of <code>&quot;sqlite&quot;</code> (recommended, the only valid value for new namespaces) or <code>&quot;legacy-kv&quot;</code> (only for existing key-value-backed namespaces). Forbidden on tombstone states.</li>
</ul>
</li>
<li>
<p><code>renamed_to</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span></p>
<ul>
<li>Required when <code>state</code> is <code>&quot;renamed&quot;</code>. The destination class name. Must be a valid JavaScript identifier, differ from the source class name, and appear as a live entry in the same <code>exports</code> map.</li>
</ul>
</li>
<li>
<p><code>transferred_to</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span></p>
<ul>
<li>Required when <code>state</code> is <code>&quot;transferred&quot;</code>. The name of the target Worker that will receive the namespace.</li>
</ul>
</li>
<li>
<p><code>transfer_from</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span></p>
<ul>
<li>Required when <code>state</code> is <code>&quot;expecting-transfer&quot;</code>. The name of the source Worker the namespace is being transferred from.</li>
</ul>
</li>
</ul>
<p>The following table lists the allowed and forbidden fields for each <code>state</code>:</p>
<table>
<thead>
<tr>
<th><code>state</code></th>
<th>Required</th>
<th>Forbidden</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;created&quot;</code> (default)</td>
<td><code>storage</code></td>
<td><code>renamed_to</code>, <code>transferred_to</code>, <code>transfer_from</code></td>
</tr>
<tr>
<td><code>&quot;deleted&quot;</code></td>
<td><em>(none)</em></td>
<td><code>storage</code>, <code>renamed_to</code>, <code>transferred_to</code>, <code>transfer_from</code></td>
</tr>
<tr>
<td><code>&quot;renamed&quot;</code></td>
<td><code>renamed_to</code></td>
<td><code>storage</code>, <code>transferred_to</code>, <code>transfer_from</code></td>
</tr>
<tr>
<td><code>&quot;transferred&quot;</code></td>
<td><code>transferred_to</code></td>
<td><code>storage</code>, <code>renamed_to</code>, <code>transfer_from</code></td>
</tr>
<tr>
<td><code>&quot;expecting-transfer&quot;</code></td>
<td><code>storage</code>, <code>transfer_from</code></td>
<td><code>renamed_to</code>, <code>transferred_to</code></td>
</tr>
</tbody>
</table>
<h2 id="error-reference">Error reference</h2>
<p>When a deploy fails reconciliation, Cloudflare returns one error per class along with a structured <code>scenario</code> tag, a human-readable message, and where applicable a <code>suggestion</code> and <code>referencing_scripts</code> list:</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Meaning</th>
<th>How to fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>provisioned_class_missing_from_config</code></td>
<td>A namespace exists for a class that the Worker code still exports, but <code>exports</code> has no entry for it.</td>
<td>Add a live entry (<code>state: &quot;created&quot;</code>) to keep the namespace, or add a tombstone (<code>deleted</code>, <code>renamed</code>, or <code>transferred</code>) to retire it.</td>
</tr>
<tr>
<td><code>config_export_not_in_code</code></td>
<td>A live entry declares a class that the Worker code does not export.</td>
<td>Add the class to your code, or replace the entry with a tombstone.</td>
</tr>
<tr>
<td><code>config_references_nonexistent_class</code></td>
<td>A live entry declares a class that is neither in code nor provisioned.</td>
<td>Remove the entry, or add the class to your Worker code.</td>
</tr>
<tr>
<td><code>orphaned_provisioned_namespace</code></td>
<td>A namespace exists for a class that is neither in code nor declared.</td>
<td>Add a tombstone for the class, or add the class back to code and <code>exports</code>.</td>
</tr>
<tr>
<td><code>invalid_export</code></td>
<td>An <code>exports</code> entry is structurally invalid — for example, requesting <code>legacy-kv</code> for a new namespace, or a class that maps to more than one provisioned namespace.</td>
<td>Correct the entry: use <code>&quot;storage&quot;: &quot;sqlite&quot;</code> for new namespaces, or resolve the duplicate with a <code>deleted</code> or <code>renamed</code> tombstone.</td>
</tr>
<tr>
<td><code>tombstone_delete_class_still_in_code</code></td>
<td>A <code>deleted</code> tombstone names a class that is still exported in code.</td>
<td>Remove the class from your code first, then deploy the tombstone.</td>
</tr>
<tr>
<td><code>tombstone_delete_blocked_by_external_bindings</code></td>
<td>Another Worker in the account binds to the namespace being deleted.</td>
<td>Redeploy the referencing Workers without the binding, then re-run your deploy.</td>
</tr>
<tr>
<td><code>tombstone_renamed_to_occupied</code></td>
<td>A <code>renamed_to</code> target collides with an existing namespace under that name.</td>
<td>Delete the colliding namespace via its own <code>deleted</code> tombstone in a prior deploy.</td>
</tr>
<tr>
<td><code>transferred_pending_not_found</code></td>
<td>A <code>transferred</code> tombstone has no matching <code>expecting-transfer</code> entry on the target.</td>
<td>Deploy the target Worker first with an <code>expecting-transfer</code> entry naming this Worker.</td>
</tr>
<tr>
<td><code>transferred_target_missing</code></td>
<td>The target Worker named by <code>transferred_to</code> no longer exists.</td>
<td>Update <code>transferred_to</code> to a valid target, or remove the tombstone.</td>
</tr>
<tr>
<td><code>transferred_target_mismatch</code></td>
<td>The <code>transferred_to</code> value does not match the target recorded by the pending transfer.</td>
<td>Set <code>transferred_to</code> to the pending transfer's target, or have the target cancel its <code>expecting-transfer</code> entry before redirecting.</td>
</tr>
<tr>
<td><code>transferred_source_in_dispatch_namespace</code></td>
<td>The source Worker declaring the <code>transferred</code> tombstone is in a dispatch namespace; cross-dispatch transfer is not supported.</td>
<td>Perform the transfer within a single dispatch-namespace context.</td>
</tr>
<tr>
<td><code>transferred_target_in_dispatch_namespace</code></td>
<td>The target of a <code>transferred</code> tombstone is in a dispatch namespace; cross-dispatch transfer is not supported.</td>
<td>Cancel the pending transfer by having the target redeploy without <code>expecting-transfer</code>, or keep both Workers in the same context.</td>
</tr>
<tr>
<td><code>phase_one_transfer_after_commit_mismatch</code></td>
<td>The target's namespace was transferred from a different source than the one declared.</td>
<td>Remove the <code>expecting-transfer</code> entry — the transfer cannot be redirected after commit.</td>
</tr>
<tr>
<td><code>phase_one_transfer_target_class_provisioned</code></td>
<td>The target Worker already owns a namespace for the class.</td>
<td>Replace the <code>expecting-transfer</code> entry with a normal live entry, or delete the existing namespace first.</td>
</tr>
<tr>
<td><code>phase_one_transfer_duplicate</code></td>
<td>Another <code>expecting-transfer</code> hint is already in flight for the same class.</td>
<td>Cancel the existing pending transfer first by removing or replacing its entry.</td>
</tr>
<tr>
<td><code>phase_one_transfer_source_missing</code></td>
<td>The source Worker named by <code>transfer_from</code> does not exist in the account.</td>
<td>Correct the source Worker name.</td>
</tr>
<tr>
<td><code>phase_one_transfer_source_namespace_missing</code></td>
<td>The source Worker has no namespace for the class.</td>
<td>Make sure the source Worker has the class deployed before the target declares <code>expecting-transfer</code>.</td>
</tr>
<tr>
<td><code>phase_one_transfer_source_in_dispatch_namespace</code></td>
<td>The source Worker is in a dispatch namespace; cross-dispatch transfer is not supported.</td>
<td>Move the transfer within a single dispatch-namespace context.</td>
</tr>
<tr>
<td><code>phase_one_transfer_target_in_dispatch_namespace</code></td>
<td>The target Worker is in a dispatch namespace; cross-dispatch transfer is not supported.</td>
<td>Move the transfer within a single dispatch-namespace context.</td>
</tr>
<tr>
<td><code>storage_type_mismatch</code></td>
<td>The declared <code>storage</code> value does not match the provisioned namespace's storage backend.</td>
<td>Storage backends cannot be changed in place. Delete the namespace and re-provision it under the new backend if you genuinely need to switch.</td>
</tr>
<tr>
<td><code>free_tier_requires_sqlite</code></td>
<td>The account's plan only supports SQLite-backed namespaces, but the entry requests <code>legacy-kv</code>.</td>
<td>Use <code>&quot;storage&quot;: &quot;sqlite&quot;</code>.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8103.md")
</aside>
<h2 id="constraints-and-limitations">Constraints and limitations</h2>
<ul>
<li><strong><code>exports</code> and <code>migrations</code> are mutually exclusive.</strong> A Worker configuration that contains both fields is rejected at validation. Once a Worker has been deployed with <code>exports</code>, subsequent deploys must continue to use <code>exports</code> (or neither, which reconciles against an empty config and is usually a mistake).</li>
<li><strong><code>wrangler versions upload</code> does not apply lifecycle changes.</strong> Just like the legacy <code>migrations</code> array, Durable Object lifecycle changes can only be applied via <code>wrangler deploy</code>. If your Wrangler configuration contains <code>exports</code> entries, <code>wrangler versions upload</code> fails fast with an actionable error. Refer to <a href="/workers/versions-and-deployments/deployment-management/#durable-object-migrations">Deployment management - Durable Object migrations</a>.</li>
<li><strong>Gradual deployments are not supported with <code>exports</code>.</strong> Lifecycle changes are atomic at the Cloudflare control plane and cannot be rolled out gradually. Refer to <a href="/workers/versions-and-deployments/gradual-deployments/with-durable-objects/#durable-object-class-lifecycle-changes">Gradual deployments with Durable Objects - Durable Object class lifecycle changes</a>.</li>
<li><strong>Rollbacks cannot cross a lifecycle change.</strong> You cannot roll back to a version deployed before an <code>exports</code>-driven lifecycle change. Refer to <a href="/workers/versions-and-deployments/rollbacks/#bindings">Rollbacks - Bindings</a>.</li>
<li><strong>Storage backends are immutable once provisioned.</strong> You cannot change a namespace's <code>storage</code> value in place; delete and re-provision instead.</li>
</ul>
<h2 id="migrate-from-the-legacy-migrations-flow">Migrate from the legacy <code>migrations</code> flow</h2>
<p>Existing Workers using the <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code> array</a> can move to <code>exports</code> without any data migration. The provisioned namespaces remain in place; only the configuration shape changes.</p>
<p>To determine a class's existing storage backend, trace it to the migration that originally created it. Classes introduced through <code>new_sqlite_classes</code> use <code>sqlite</code>, while classes introduced through <code>new_classes</code> use <code>legacy-kv</code>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8124.md")
</div>
<p>Side-by-side, the equivalent of a typical <code>migrations</code> history is:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8125.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8126.md")
</div>
<p>Future lifecycle changes (deletes, renames, transfers) happen entirely through <code>exports</code> — there is no equivalent of the <code>tag</code> field and no need to keep historical entries. The current state of your <code>exports</code> map is the source of truth.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8102.md")
</aside>
