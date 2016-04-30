import os.path
import random

class Card:
  """Representation of a Playing Card"""
  def __init__(self,index,facedown=False):
    self.cardnames=["Back","Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    self.imgdir=os.path.join(os.getcwd(),"img")
    self.imgfile=""
    self.backimg=""
    self.facedown=facedown
    self.index=index
    if self.index<14:
      self.suitname="Spades"
      self.value=index
    elif self.index<27:
      self.suitname="Diamonds"
      self.value=index-13
    elif self.index<40:
      self.suitname="Hearts"
      self.value=index-26
    else:
      self.suitname="Clubs"
      self.value=index-39
    self.cardname=self.cardnames[self.value]
    self.imgfn="%d.png" % index
    if os.path.isdir(self.imgdir):
      imgpath=os.path.join(self.imgdir,self.imgfn)
      self.backimg=os.path.join(self.imgdir,"back.png")
      if os.path.exists(imgpath):
        self.imgfile=imgpath

  def name(self):
    if self.facedown:
      return "Facedown"
    return "%s of %s" % (self.cardname,self.suitname)

  def suit(self):
    return self.suitname

  def indexname(self):
    return self.cardname

  def image(self):
    if self.facedown:
      return self.backimg
    return self.imgfile

  def flip(self):
    self.facedown=False if self.facedown else True
    return self.image()

  def isdown(self):
    return self.facedown

class Stack:
  """Representation of a stack of playing cards"""
  def __init__(self,numberofdecks=0,noaces=0):
    self.cards=[]
    if numberofdecks>0:
      self.initfull(numberofdecks)
    if noaces>0:
      self.initnoaces()
    random.seed()

  def addnewcard(self,index):
    self.cards.append(Card(index))

  def addcard(self,card):
    self.cards.append(card)

  def addtopcard(self,card):
    self.cards.insert(0,card)

  def initfull(self,numberofdecks=1):
    for y in range(numberofdecks):
      for x in range(1,53):
        self.addnewcard(x)

  def initnoaces(self):
    self.initfull(1)
    t=[]
    t=self.getcard(39)
    t=self.getcard(26)
    t=self.getcard(13)
    t=self.getcard(0)
    t=None

  def length(self):
    return len(self.cards)

  def shuffle(self):
    random.shuffle(self.cards)

  def topcard(self):
    if len(self.cards):
      return self.cards[0]
    return None

  def bottomcard(self):
    if len(self.cards):
      return self.cards[len(self.cards)-1]
    return None

  def getbottomcard(self):
    if len(self.cards):
      return self.cards.pop()
    return None

  def gettopcard(self):
    l=len(self.cards)
    if l:
      c=self.topcard()
      self.cards=self.cards[1:]
      return c
    return None

  def getcard(self,index):
    l=len(self.cards)
    if l>index:
      c=self.cards[index]
      if index > 0:
        t=self.cards[:index]
        t.extend(self.cards[index+1:])
        self.cards=t
      else:
        self.cards=self.cards[1:]
      return c
    return None

  def getncards(self,n):
    l=len(self.cards)
    if l>n:
      t=self.cards[:n]
      self.cards=self.cards[n:]
    else:
      t=self.cards
      self.cards=[]
    return t

  def addncards(self,ncards):
    if len(ncards) > 0:
      for card in ncards:
        self.addcard(card)

  def status(self):
    c=self.topcard()
    if c!=None:
      s=c.name()
    else:
      s=""
    return "%d cards: %s" % (self.length(),s)
