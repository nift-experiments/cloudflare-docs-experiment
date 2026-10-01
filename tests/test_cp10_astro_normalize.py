import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.cp10_astro_normalize import (
    NormalizationError,
    analyze,
    lz_decompress_uri,
    normalize_content,
    normalize_playground_links,
    normalize_svg_dot_pattern_ids,
)


class CP10AstroNormalizeTests(unittest.TestCase):
    def test_cli_refuses_to_overwrite_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = root / "before"
            after = root / "after"
            before.mkdir()
            after.mkdir()
            (before / "index.html").write_text("same")
            (after / "index.html").write_text("same")
            output = root / "report.json"
            output.write_text("preserve")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).parents[1] / "tools/cp10_astro_normalize.py"),
                    "--root",
                    f"before={before}",
                    "--root",
                    f"after={after}",
                    "--output",
                    str(output),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            self.assertEqual(completed.returncode, 2)
            self.assertEqual(output.read_text(), "preserve")

    def test_lz_uri_decoder_and_boundary_normalization(self):
        self.assertEqual(
            lz_decompress_uri(b"BYUwNmD2AEDukCcwBMg"), b"hello world"
        )
        first = (
            b"https://workers.cloudflare.com/playground#"
            b"LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwBWQQE4AHACYAjDNHyAXCxZtgHOFxp8BI8dLkLhAWABQFXHTMrmajVp78hoybPmD5zIA"
        )
        normalized = normalize_playground_links(first)
        self.assertRegex(normalized, rb"playground#cp10-sha256-[0-9a-f]{64}$")
        with self.assertRaises(NormalizationError):
            normalize_playground_links(
                b"https://workers.cloudflare.com/playground#BYUwNmD2AEDukCcwBMg"
            )

    def test_generated_ids_are_bijective_and_lookalikes_are_preserved(self):
        one = b"pm-12345678-1234-4123-8123-123456789abc"
        two = b"pm-abcdefab-cdef-4abc-9abc-abcdefabcdef"
        data = b" ".join((one, one, two, b"pm-not-a-uuid"))
        normalized, categories = normalize_content("page.html", data, {})
        self.assertEqual(normalized.count(b"pm-cp10-000000"), 2)
        self.assertEqual(normalized.count(b"pm-cp10-000001"), 1)
        self.assertIn(b"pm-not-a-uuid", normalized)
        self.assertEqual(categories, ["package-manager-uuid"])

    def test_svg_dot_pattern_ids_normalize_by_definition_order(self):
        def page(first: bytes, second: bytes) -> bytes:
            return b"".join(
                (
                    b'<svg><pattern id="',
                    first,
                    b'"><circle/></pattern><rect fill="url(#',
                    first,
                    b')"/><rect fill="url(#',
                    first,
                    b')"/></svg><svg><pattern id="',
                    second,
                    b'"></pattern><rect fill="url(#',
                    second,
                    b')"/></svg>',
                )
            )

        baseline, categories = normalize_content(
            "index.html", page(b"nb-dots-1nd", b"nb-dots-1ne"), {}
        )
        warmup, _ = normalize_content(
            "index.html", page(b"nb-dots-f", b"nb-dots-g"), {}
        )
        self.assertEqual(baseline, warmup)
        self.assertEqual(categories, ["svg-dot-pattern-id"])
        self.assertIn(b'id="nb-dots-cp10000000"', baseline)
        self.assertEqual(baseline.count(b"url(#nb-dots-cp10000000)"), 2)
        self.assertEqual(normalize_svg_dot_pattern_ids(baseline), baseline)

    def test_svg_dot_pattern_ids_reject_malformed_unpaired_and_colliding(self):
        cases = {
            "malformed": b'<pattern id="nb-dots-UPPER"></pattern>',
            "definition only": b'<pattern id="nb-dots-a"></pattern>',
            "reference only": b'<rect fill="url(#nb-dots-a)"/>',
            "arbitrary id": (
                b'<pattern id="nb-dots-a"></pattern>'
                b'<rect fill="url(#nb-dots-a)"/><div data-id="nb-dots-a"></div>'
            ),
            "duplicate definition": (
                b'<pattern id="nb-dots-a"></pattern>'
                b'<pattern id="nb-dots-a"></pattern><rect fill="url(#nb-dots-a)"/>'
            ),
            "canonical collision": (
                b'<pattern id="nb-dots-a"></pattern>'
                b'<rect fill="url(#nb-dots-a)"/>'
                b'<pattern id="nb-dots-cp10000000"></pattern>'
                b'<rect fill="url(#nb-dots-cp10000000)"/>'
            ),
        }
        for name, value in cases.items():
            with self.subTest(name=name), self.assertRaises(NormalizationError):
                normalize_svg_dot_pattern_ids(value)

    def test_svg_dot_normalizer_does_not_touch_other_ids(self):
        data = b'<svg><pattern id="dots-a"></pattern></svg><div id="nb-card-a"></div>'
        self.assertEqual(normalize_svg_dot_pattern_ids(data), data)

    def test_prompt_normalization_is_route_and_allowlist_limited(self):
        prompt = (
            b"Build a serverless AI inference endpoint on Workers AI with "
            b"streaming responses."
        )
        normalized, categories = normalize_content(
            "agent-setup/codex/index.html", prompt, {}
        )
        self.assertEqual(normalized, b"<CP10-RANDOM-AGENT-PROMPT>")
        self.assertIn("sampled-agent-prompts", categories)
        unchanged, categories = normalize_content("other/index.html", prompt, {})
        self.assertEqual(unchanged, prompt)
        self.assertEqual(categories, [])

    def test_shiki_normalization_rejects_extra_content(self):
        first = b".nb-shiki-b{color:b}.nb-shiki-a{color:a}\n"
        second = b".nb-shiki-a{color:a}.nb-shiki-b{color:b}\n"
        left, categories = normalize_content("_nimbus/shiki.css", first, {})
        right, _ = normalize_content("_nimbus/shiki.css", second, {})
        self.assertEqual(left, right)
        self.assertEqual(categories, ["shiki-rule-order"])
        with self.assertRaises(NormalizationError):
            normalize_content("_nimbus/shiki.css", first + b"body{}", {})

    def test_analyze_classifies_alias_and_rejects_real_difference(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            roots = []
            for label, asset, page in (
                ("r1", "one.ABCdef12.svg", "one.ABCdef12.svg"),
                ("r2", "two.ABCdef12.svg", "two.ABCdef12.svg"),
            ):
                root = base / label
                (root / "_astro").mkdir(parents=True)
                (root / "_astro" / asset).write_text("same-svg")
                (root / "index.html").write_text(page)
                roots.append((label, root))
            report = analyze(roots)
            self.assertTrue(report["normalized_equivalent"])
            self.assertEqual(
                report["category_totals"]["content-identical-svg-alias"]["count"],
                3,
            )
            (roots[1][1] / "real.txt").write_text("real change")
            report = analyze(roots)
            self.assertFalse(report["normalized_equivalent"])
            self.assertIn("real.txt", report["unclassified"])


if __name__ == "__main__":
    unittest.main()
