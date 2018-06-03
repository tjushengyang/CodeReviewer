# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import repo_conf
import copy_file

###########################################################################
## Class MyFrame1
###########################################################################
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CodeClub Review Tool", pos = wx.DefaultPosition, size = wx.Size( 280,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		username    = repo_conf.get_option_value('remote','username')
		password    = repo_conf.get_option_value('remote','password')
		repo_path   = repo_conf.get_option_value('local','repository')
		output_path = repo_conf.get_option_value('local','output')
				
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_s_login = wx.StaticText( self, wx.ID_ANY, u"Login CodeClub", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_login.Wrap( -1 )
		bSizer2.Add( self.m_s_login, 0, wx.ALL, 5 )
		
		self.m_s_username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_username.Wrap( -1 )
		bSizer2.Add( self.m_s_username, 0, wx.ALL, 5 )
		
		self.m_username = wx.TextCtrl( self, wx.ID_ANY, username, wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.m_username.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.m_username, 0, wx.ALL, 5 )
		
		self.m_s_password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_password.Wrap( -1 )
		bSizer2.Add( self.m_s_password, 0, wx.ALL, 5 )
		
		self.m_password = wx.TextCtrl( self, wx.ID_ANY, password, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		bSizer2.Add( self.m_password, 0, wx.ALL, 5 )
		
		self.m_s_mr_url = wx.StaticText( self, wx.ID_ANY, u"Mr URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_mr_url.Wrap( -1 )
		bSizer2.Add( self.m_s_mr_url, 0, wx.ALL, 5 )
		
		self.m_mr_url = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer2.Add( self.m_mr_url, 0, wx.ALL, 5 )
		
		self.m_s_rep_path = wx.StaticText( self, wx.ID_ANY, u"Repository Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_rep_path.Wrap( -1 )
		bSizer2.Add( self.m_s_rep_path, 0, wx.ALL, 5 )
		
		self.m_rep_path = wx.TextCtrl( self, wx.ID_ANY, repo_path, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer2.Add( self.m_rep_path, 0, wx.ALL, 5 )
		
		self.m_s_output_path = wx.StaticText( self, wx.ID_ANY, u"Output Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_output_path.Wrap( -1 )
		bSizer2.Add( self.m_s_output_path, 0, wx.ALL, 5 )
		
		self.m_output_path = wx.TextCtrl( self, wx.ID_ANY, output_path, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer2.Add( self.m_output_path, 0, wx.ALL, 5 )
		
		self.m_generate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_generate, 0, wx.ALL, 5 )
		
		self.m_open_path = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_open_path, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_generate.Bind( wx.EVT_BUTTON, self.GenerateSourceCode )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def GenerateSourceCode( self, event ):
		repo_path = self.m_rep_path.GetValue()
		dst_path = self.m_output_path.GetValue()
		copy_file.copy_file('head^','head', repo_path, dst_path)
		event.Skip()
	

