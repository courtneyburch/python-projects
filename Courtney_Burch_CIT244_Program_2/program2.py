#COURTNEY BURCH CIT 244 PROGRAM 2

import wx

class MyFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title='Shipping Calculator'):
		super(MyFrame, self).__init__(parent, id, title = title, size = (600, 600))
		self.panel = wx.Panel(self)

		# text inputs for Name, Address
		self.name = wx.TextCtrl(self.panel, pos = (30, 30), size = (220, -1))
		self.label = wx.StaticText(self.panel, id = -1, pos = (250, 30), label = 'Name')

		self.address_1 = wx.TextCtrl(self.panel, pos = (30, 60), size = (220, -1))
		self.label = wx.StaticText(self.panel, id = -1, pos = (250, 60), label = 'Address')

		self.address_2 = wx.TextCtrl(self.panel, pos = (30, 90), size = (220, -1))
		self.label = wx.StaticText(self.panel, id = -1, pos = (250, 90), label = 'City, State, Zip')

		#radio buttons for Weight
		self.weight_label = wx.StaticText(self.panel, label = "Weight", pos = (50, 150))
		self.weight_a = wx.RadioButton(self.panel, label = "0 - 1.9 pounds: $5.00", style = wx.RB_GROUP, pos = (30, 180))
		self.weight_b = wx.RadioButton(self.panel, label = "2 - 4.9 pounds: $8.00", pos = (30, 210))
		self.weight_c = wx.RadioButton(self.panel, label = "over 5 pounds: $12.25", pos = (30, 240))

		#radio buttons for Speed
		self.weight_speed = wx.StaticText(self.panel, label = "Shipping Speed", pos = (240, 150))
		self.speed_a = wx.RadioButton(self.panel, label = "Overland: $2.75", style = wx.RB_GROUP, pos = (220, 180))
		self.speed_b = wx.RadioButton(self.panel, label = "3-day Air: $6.15", pos = (220, 210))
		self.speed_c = wx.RadioButton(self.panel, label = "2-day Air: $10.70", pos = (220, 240))
		self.speed_d = wx.RadioButton(self.panel, label = "Overnight: $15.50", pos = (220, 270))

		#check boxes for extra items
		self.extras = wx.StaticText(self.panel, label = "Extras", pos = (400, 150))
		self.padding = wx.CheckBox(self.panel, -1, label = "Extra Padding $4.00", pos=(380, 180))
		self.gift_wrap = wx.CheckBox(self.panel, -1, label = "Gift Wrapping $6.00", pos=(380, 210))

		#Calculate Total button and event
		self.calc_button = wx.Button(self.panel, label="Calculate Total", pos = (40, 330))
		self.calc_button.Bind(wx.EVT_BUTTON, self.calcTotal)

		#Clear form button and event
		self.clear_button = wx.Button(self.panel, label="Clear Form", pos = (200, 330))
		self.clear_button.Bind(wx.EVT_BUTTON, self.clearForm)

		#lables for summary, address and total
		self.summary_address_label = wx.StaticText(self.panel, label = "Shipping To:", pos = (40, 400))
		self.summary_address = wx.StaticText(self.panel, label = '', pos = (40, 430))
		self.summary_total_label = wx.StaticText(self.panel, label = "Total:", pos = (200, 400))
		self.summary_total = wx.StaticText(self.panel, label = '', pos = (240, 400))

		self.status_bar = self.CreateStatusBar()
		self.status_bar.SetStatusText('')

	def calcTotal(self, event):
		cost = 0.00
		if self.weight_a.GetValue():
			cost = 5.00
		elif self.weight_b.GetValue():
			cost = 8.00
		else:
			cost = 12.25

		if self.speed_a.GetValue():
			cost += 2.75
		elif self.speed_b.GetValue():
			cost += 6.15
		elif self.speed_c.GetValue():
			cost += 10.70
		else: 
			cost += 15.00

		if self.padding.GetValue():
			cost += 4.00
		elif self.gift_wrap.GetValue():
			cost += 6.00

		#format the cost for display	
		cost = f"${cost}"

		#format the shipping address for display
		shipping_name = self.name.GetValue()
		shipping_address_1 = self.address_1.GetValue()
		shipping_address_2 = self.address_2.GetValue()
		shipping_summary = f"{shipping_name}\n{shipping_address_1}\n{shipping_address_2}"

		#display the address and cost
		self.summary_address.SetLabel(shipping_summary)
		self.summary_total.SetLabel(cost)


	def clearForm(self, event):
		self.name.SetValue('')
		self.address_1.SetValue('')
		self.address_2.SetValue('')
		self.weight_a.SetValue(1)
		self.speed_a.SetValue(1)
		self.padding.SetValue(0)
		self.gift_wrap.SetValue(0)
		self.summary_address.SetLabel('')
		self.summary_total.SetLabel('')
	

if __name__ == "__main__":
	app = wx.App()
	fr = MyFrame(None)
	fr.Show()
	app.MainLoop()