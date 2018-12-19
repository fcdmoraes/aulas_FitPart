import blpapi

class Session():
	def __init__(self):
		pass

	def start(self, ip, port):
		self.options = blpapi.SessionOptions()
		self.options.setServerHost(ip)
		self.options.setServerPort(port)

		self.session = blpapi.Session(self.options)
		self.session.start()

	def request(self, securities, fields, stardate, enddate):
		self.refDataService = self.session.getService("//blp/refdata")
		request = self.refDataService.createRequest("HistoricalDataRequest")
		request.getElement("securities").appendValue(securities)
		request.getElement("fields").appendValue(fields)
		request.set("startDate", startdate)
		request.set("endDate", enddate)

		self.session.sendRequest(request)

		while True:
			ev = self.session.nextEvent(500)
			for msg in ev:
				print(msg)

			if ev.eventType() == blpapi.Event.RESPONSE:
				break
