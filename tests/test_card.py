import os
import os.path
import sys

modpath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,modpath)

from cards import Card
from cards import Stack

def test_correct_card():
  c=Card(7,False)
  assert c.name() == "Seven of Spades"

def test_correct_index():
  c=Card(7,False)
  assert c.index == 7

def test_correct_suit():
  c=Card(15,False)
  assert c.suit() == "Diamonds"

def test_facedown():
  c=Card(7,True)
  assert c.name() == "Facedown"

def test_isdown():
  c=Card(7,True)
  assert c.isdown() == True

def test_imgfile():
  c=Card(7,False)
  ipath=os.path.abspath(os.path.join(modpath,"img"))
  ifn=os.path.join(ipath,"7.png")
  bfn=os.path.join(ipath,"back.png")
  imgfn=c.image()
  if imgfn == ifn:
    c.flip()
    imgfn=c.image()
    assert imgfn == bfn
  else:
    assert imgfn == ifn

def test_stacklength():
  s=Stack(1)
  assert s.length() == 52

def test_stack():
  s=Stack(1)
  assert s.topcard().name() == "Ace of Spades"

def test_noaces():
  s=Stack(noaces=1)
  assert s.topcard().name() == "Two of Spades"

def test_get_bottom_card():
  s=Stack(1)
  c=s.getbottomcard()
  l=s.length()
  if l < 52:
    assert c.name() == "King of Clubs"
  else:
    assert l == 51

def test_getncards():
  s=Stack(1)
  cs=s.getncards(5)
  l=s.length()
  if l < 48:
    assert len(cs) == 5
  else:
    assert l == 47

def test_addncards():
  s=Stack(1)
  cs=s.getncards(5)
  l=s.length()
  if l < 48:
    s.addncards(cs)
    assert s.length() == 52
  else:
    assert l == 47
