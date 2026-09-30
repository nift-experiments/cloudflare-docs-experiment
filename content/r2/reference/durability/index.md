<p>R2 is designed to provide 99.999999999% (eleven 9s) of annual durability.  This means that if you store 10,000,000 objects on R2, you can expect to lose an object once every 10,000 years on average.</p>
<h2 id="how-r2-achieves-eleven-nines-durability">How R2 achieves eleven-nines durability</h2>
<p>R2's durability is built on multiple layers of redundancy and data protection:</p>
<ul>
<li>
<p><strong>Replication</strong>: When you upload an object, R2 stores multiple &quot;copies&quot; of that object through either full replication and/or erasure coding. This ensures that the full or partial failure of any individual disk does not result in data loss. Erasure coding distributes parts of the object across multiple disks, ensuring that even if some disks fail, the object can still be reconstructed from a subset of the available parts, preventing hardware failure or physical impacts to data centers (such as fire or floods) from causing data loss.</p>
</li>
<li>
<p><strong>Hardware redundancy</strong>: Storage clusters are comprised of hardware distributed across several data centers within a geographic region. This physical distribution ensures that localized failures—such as power outages, network disruptions, or hardware malfunctions at a single facility—do not result in data loss.</p>
</li>
<li>
<p><strong>Synchronous writes</strong>: R2 returns an <code>HTTP 200 (OK)</code> for a write via API or otherwise indicates success only when data has been persisted to disk. We do not rely on asynchronous replication to support underlying durability guarantees. This is critical to R2’s consistency guarantees and mitigates the chance of a client receiving a successful API response without the underlying metadata and storage infrastructure having persisted the change.</p>
</li>
</ul>
<h3 id="considerations">Considerations</h3>
<ul>
<li>Durability is not a guarantee of data availability. It is a measure of the likelihood of data loss.</li>
<li>R2 provides an availability <a href="https://www.cloudflare.com/r2-service-level-agreement/">SLA of 99.9%</a></li>
<li>Durability does not prevent intentional or accidental deletion of data. Use <a href="/r2/buckets/bucket-locks/">bucket locks</a> and/or bucket-scoped <a href="/r2/api/tokens/">API tokens</a> to limit access to data.</li>
<li>Durability is also distinct from <a href="/r2/reference/consistency/">consistency</a>, which describes how reads and writes are reflected in the system's state (e.g. eventual consistency vs. strong consistency).</li>
</ul>
