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
import os

###########################################################################
## Class MyFrame1
###########################################################################
class MyDiag(wx.MessageDialog):
	def __init__( self, parent,msg ):	
		wx.MessageDialog.__init__(self,parent,msg,'info',wx.OK)
		self.SetSize(0, 0, 200, 200, wx.SIZE_AUTO)
		
class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CodeClub Review Tool", pos = wx.DefaultPosition, size = wx.Size( 280,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		username    = repo_conf.get_option_value('remote','username')
		password    = repo_conf.get_option_value('remote','password')
		repo_path   = repo_conf.get_option_value('local','repository')
		output_path = repo_conf.get_option_value('local','output')
				
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
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
		self.m_open_path.Bind( wx.EVT_BUTTON, self.OpenDstPath )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def GenerateSourceCode( self, event ):
		username = self.m_username.GetValue()
		password = self.m_password.GetValue()
		repo_path = self.m_rep_path.GetValue()
		dst_path = self.m_output_path.GetValue()
		ret = copy_file.copy_file('head^','head', repo_path, dst_path)
		if(0 == ret):
			loginfo = repo_conf.LogInfo(username,password,repo_path,dst_path)
			repo_conf.set_cfg(loginfo)
			diag = MyDiag(self,'export file success!')
		else:
			diag = MyDiag(self,'export file fail!')
		diag.ShowModal()
		event.Skip()
	
	def OpenDstPath( self, event ):
		dst_path = self.m_output_path.GetValue()
		os.system("start explorer "+dst_path)
		event.Skip()
