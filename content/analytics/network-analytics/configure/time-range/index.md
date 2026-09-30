<h2 id="using-the-timeframe-drop-down-list">Using the timeframe drop-down list</h2>
<p>Use the timeframe drop-down list to change the time range over which Network Analytics displays data. When you select a timeframe, the entire view is updated to reflect your choice.</p>
<p>In the Network Analytics dashboard, the range of historical data you can query is 112 days.</p>
<p>When you select <em>Previous 30 minutes</em>, the <strong>Network Analytics</strong> card will show the data from the last 30 minutes, refreshing every 20 seconds. A <em>Live</em> notification appears next to the statistic drop-down list to let you know that the view keeps updating automatically:</p>
<p><img src="/assets/upstream/images/analytics/network-analytics/timeframe-selector.png" alt="Timeframe drop-down with Previous 30 minutes selected." /></p>
<h2 id="zooming-in-the-chart">Zooming in the chart</h2>
<p>To zoom in a specific period, select and drag to define a region in the <strong>Packets summary</strong> (or <strong>Bits summary</strong>) chart. To zoom out, select <strong>X</strong> in the time range selector.</p>
<p><img src="/images/analytics/network-analytics/chart-zoom-in.gif" alt="User zooming in a given period in the Network Analytics traffic chart." /></p>
<p>The effective resolution goes up when you zoom in and goes down when you zoom out, due to the <a href="/analytics/network-analytics/understand/concepts/#adaptive-bit-rate-sampling">Adaptive Bit Rate</a>. This means that a big packet burst that lasted a few seconds may look less impactful when analyzing a chart displaying data for 24 hours or more.</p>
