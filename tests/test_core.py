import unittest
from timezone_fold_witness import run
class Tests(unittest.TestCase):
 def test_paris_fold_has_two_real_instants(self):
  r=run({'zone':'Europe/Paris','start_local':'2026-10-25T02:30','end_local':'2026-10-25T03:30'});self.assertEqual(r['start']['status'],'ambiguous');self.assertEqual({x['elapsed_seconds']for x in r['possible_intervals']},{3600,7200})
 def test_spring_gap_is_not_shifted_forward(self):
  r=run({'zone':'Europe/Paris','start_local':'2026-03-29T02:30','end_local':'2026-03-29T03:30'});self.assertEqual(r['start']['status'],'gap');self.assertEqual(r['possible_intervals'],[])
 def test_explicit_fold_selects_requested_instant(self):
  r=run({'zone':'Europe/Paris','start_local':'2026-10-25T02:30','end_local':'2026-10-25T03:30','start_fold':1});self.assertEqual(len(r['possible_intervals']),1);self.assertEqual(r['possible_intervals'][0]['elapsed_seconds'],3600)
 def test_normal_utc_time_not_duplicated(self):
  r=run({'zone':'UTC','start_local':'2026-01-01T00:00','end_local':'2026-01-01T01:00'});self.assertEqual(len(r['possible_intervals']),1)
