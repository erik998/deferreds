from twisted.internet import reactor, defer

class HeadlineRetriever(object):

	def processHeadline(self, headline):
		if len(headline) > 50:
			self.d.errback("The headline {0} is too long!".format(headline))
		else:
			self.d.callback(headline)

	def _toHTML(self, result):
		return "<h1>{0}</h1>".format(result)

	def getHeadline(self, input):
		self.d = defer.Deferred()
		reactor.callLater(1, self.processHeadline, input)
		self.d.addCallback(self._toHTML)
		return self.d

def printData(result):
	print result
	reactor.stop()

def printError(failure):
	print failure
	reactor.stop()

h = HeadlineRetriever()
d = h.getHeadline("Breaking New: Erik lands a job!")
d.addCallbacks(printData, printError)

reactor.run()