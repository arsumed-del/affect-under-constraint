import unittest,json,tempfile
from pathlib import Path
from study7.src.common import *
from study7.src.runner import run_cell,load
from study7.src.assembly import Assembly
from study7.analysis.analyze import summarize,conjunction
import numpy as np
class Safety(unittest.TestCase):
 def test_output_boundary(self):
  with self.assertRaises(ValueError):output(ROOT.parent/'forbidden.json')
 def test_absent_approval(self):
  self.assertFalse((ROOT/'PREREG_APPROVED').exists())
  with self.assertRaises(FileNotFoundError):require_approval()
 def test_outlet_margins(self):
  x=np.full(80,.1);b=np.full(10000,.1)
  rating=summarize(x,b,.95,1,.15);classifier=summarize(x,b,.95,1,.05)
  self.assertEqual(rating['status'],'small but detectable');self.assertEqual(classifier['status'],'supported')
 def test_primary_exact(self):self.assertEqual(config()['analysis']['primary_ci'],1-.05/3)
if __name__=='__main__':unittest.main()
