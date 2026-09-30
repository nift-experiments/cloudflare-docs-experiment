#!/usr/bin/env python3
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('nav', ROOT / 'tools/generate_navigation.py')
nav = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nav)


class TestNavigation(unittest.TestCase):
    def write(self, root, relative, frontmatter, body='Body.'):
        path = root / 'src/content/docs' / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'---\n{frontmatter}\n---\n\n{body}\n')

    def test_tree_context_order_badges_and_hidden_pages(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            directory = root / 'src/content/directory'
            directory.mkdir(parents=True)
            (directory / 'widget.yaml').write_text(
                'name: Widget\nentry:\n  title: Widget Platform\n  url: /widget/\n  group: Developer platform\n'
            )
            self.write(root, pathlib.Path('widget/index.mdx'), 'title: Widget\nsidebar:\n  order: 1')
            self.write(root, pathlib.Path('widget/start/index.mdx'), 'title: Start here\nsidebar:\n  group:\n    label: Getting started\n    badge: Beta\n  order: 2')
            self.write(root, pathlib.Path('widget/start/install.mdx'), 'title: Install\nsidebar:\n  order: 1')
            self.write(root, pathlib.Path('widget/start/hidden.mdx'), 'title: Hidden\nsidebar:\n  hidden: true')
            self.write(root, pathlib.Path('widget/start/disabled.mdx'), 'title: Disabled\nsidebar: false')
            self.write(root, pathlib.Path('widget/reference/index.mdx'), 'title: Reference\nsidebar:\n  group:\n    hideIndex: true\n  order: 3')
            self.write(root, pathlib.Path('widget/reference/api.mdx'), 'title: API')
            destination = root / 'out/navigation.json'

            first = nav.generate(root, destination, 'frozen')
            initial_bytes = destination.read_bytes()
            second = nav.generate(root, destination, 'frozen')

            self.assertEqual(first, second)
            self.assertEqual(initial_bytes, destination.read_bytes())
            manifest = json.loads(destination.read_text())
            self.assertNotIn('children', manifest['products']['widget'])
            payload = json.loads((destination.parent / 'navigation/widget.json').read_text())
            self.assertEqual(payload['product']['children'], first['products']['widget']['children'])
            self.assertEqual(payload['routes'], first['routes'])
            self.assertEqual(first['products']['widget']['label'], 'Widget Platform')
            tree = first['products']['widget']['children']
            getting_started = next(node for node in tree if node['label'] == 'Getting started')
            self.assertEqual(getting_started['badge'], {'text': 'Beta', 'variant': 'caution'})
            self.assertEqual(getting_started['href'], '/widget/start/')
            self.assertEqual([node['label'] for node in getting_started['children']], ['Install', 'Overview'])
            self.assertNotIn('Hidden', json.dumps(tree))
            self.assertNotIn('Disabled', json.dumps(tree))
            reference = next(node for node in tree if node['label'] == 'Reference')
            self.assertEqual([node['label'] for node in reference['children']], ['API'])
            context = first['routes']['/widget/start/install/']
            self.assertEqual(context['activeAncestorIds'], ['group:widget:start'])
            self.assertEqual(context['previous']['href'], '/widget/')
            self.assertEqual(context['next']['href'], '/widget/start/')

    def test_hide_children_collapses_group_to_index_link(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            (root / 'src/content/directory').mkdir(parents=True)
            self.write(root, pathlib.Path('thing/index.mdx'), 'title: Thing')
            self.write(root, pathlib.Path('thing/archive/index.mdx'), 'title: Archive\nhideChildren: true')
            self.write(root, pathlib.Path('thing/archive/old.mdx'), 'title: Old')
            result = nav.generate(root, root / 'navigation.json')
            rendered = json.dumps(result['products']['thing']['children'])
            self.assertIn('/thing/archive/', rendered)
            self.assertNotIn('/thing/archive/old/', rendered)

    def test_route_normalization_matches_imported_routes(self):
        self.assertEqual(
            '/realtime/realtimekit/broadcast-apis/',
            nav.route_for(pathlib.Path('realtime/realtimekit/collaborative-stores/broadcast.mdx'),
                          {'slug': 'realtime/realtimekit/broadcast-apis'}),
        )
        self.assertEqual(
            '/rules/reference/geographic-locations/',
            nav.route_for(pathlib.Path('rules/reference/geographic locations.mdx')),
        )
        self.assertEqual(
            '/waf/tools/wordpresscom-and-cloudflare/',
            nav.route_for(pathlib.Path('waf/tools/wordpress.com-and-cloudflare.mdx')),
        )


if __name__ == '__main__':
    unittest.main()
