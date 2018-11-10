#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	Sanseido Definitions plugin for Anki
	pulls definitions from sanseido.net's デイリーコンサイス国語辞典
	
	Definition fetching adapted from rikaichan.js
	Field updating modified from Sentence_Gloss.py
	
	@author 	= kqueryful
	@date 		= 1/18/2015
	@version 	= 1.0
"""
from bs4.BeautifulSoup import BeautifulSoup
import urllib
import re
from aqt.utils import showInfo
import random

from nhk_pronunciation import multi_lookup

# Edit these field names if necessary ==========================================
expressionField = 'Expression'
definitionField = 'Sanseido'
# ==============================================================================

# Fetch definition from Sanseido ===============================================
def fetchDef(term):
    searched = re.search(r'^[^\[]+',term)
    if searched:
        term = searched.group(0)
	defText = ""
	pageUrl = "http://www.sanseido.biz/User/Dic/Index.aspx?TWords=" + urllib.quote(term.encode('utf-8')) + "&st=0&DailyJJ=checkbox"
	response = urllib.urlopen(pageUrl)
	soup = BeautifulSoup(response)
	NetDicBody = soup.find('div', class_ = "NetDicBody")
	if NetDicBody != None:
		defFinished = False
		
		for line in NetDicBody.children:
			if line.name == "b":
				if len(line) != 1:
					for child in line.children:
						if child.name == "span":
							defFinished = True
			if defFinished:
				break
			
			if line.string != None and line.string != u"\n":
				defText += line.string
				
	defText = re.sub(ur"［(?P<no>[２-９]+)］", ur"<br/><br/>［\1］", defText)
	if defText: defText = u"　・　<b>" + term + "</b>: " + defText
	return re.sub(ur"（(?P<num>[２-９]+)）", ur"<br/>（\1）", defText)

# Update note ==================================================================
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from anki.hooks import addHook
from anki.notes import Note
from aqt import mw

def glossNote( f ):
    if f[ definitionField ]: return
    f[ definitionField ] = multi_lookup(f[ expressionField ], fetchDef, separator = "").lstrip('　・')

def setupMenu( ed ):
	a = QAction( 'Regenerate Sanseido definitions', ed )
	ed.connect( a, SIGNAL('triggered()'), lambda e=ed: onRegenGlosses( e ) )
	ed.form.menuEdit.addAction( a )

def onRegenGlosses( ed ):
	n = "Regenerate Sanseido definitions"
	ed.editor.saveNow()
	regenGlosses(ed, ed.selectedNotes() )   
	mw.requireReset()
	
def regenGlosses( ed, fids ):
	mw.progress.start( max=len( fids ) , immediate=True)
	for (i,fid) in enumerate( fids ):
		mw.progress.update( label='Generating Sanseido definitions...', value=i )
		f = mw.col.getNote(id=fid)
		try: glossNote( f )
		except:
			pass
			"""import traceback
			print 'definitions failed:'
			traceback.print_exc()"""
		try: f.flush()
		except:
			raise Exception()
			#sleep(10*random.random())
		ed.onRowChanged(f,f)
	mw.progress.finish()
	
addHook( 'browser.setupMenus', setupMenu )




