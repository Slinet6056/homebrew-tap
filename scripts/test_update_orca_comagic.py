import unittest

from update_orca_comagic import render_cask


class ComagicManifestTest(unittest.TestCase):
    def test_rejects_release_metadata_that_could_change_the_cask_source(self):
        manifest = {
            "version": "1.4.259-comagic.17",
            "commit": "a" * 40,
            "tag": "comagic-" + "a" * 40,
            "sha256": {"arm64": "b" * 64, "x64": "c" * 64},
        }
        self.assertIn('version "1.4.259-comagic.17"', render_cask(manifest))
        for field, value in (
            ("version", '1.4.259"\n  system "unwanted"'),
            ("tag", "comagic-" + "d" * 40),
            ("commit", "../../other-release"),
            ("sha256", {"arm64": "not-a-checksum", "x64": "c" * 64}),
        ):
            with self.subTest(field=field), self.assertRaises(ValueError):
                render_cask({**manifest, field: value})


if __name__ == "__main__":
    unittest.main()
