import appModuleHandler
import api
import controlTypes
from tones import beep
from logHandler import log
import oleacc

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if obj.IAccessibleRole==oleacc.ROLE_SYSTEM_OUTLINEITEM and obj.isFocusable and obj.lastChild and obj.lastChild.name and not obj.lastChild.isFocusable:
			obj.name=obj.lastChild.name
