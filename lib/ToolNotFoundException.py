
class ToolNotFoundException(Exception):

	def __init__(self, tool):
		self.tool = tool
		super().__init__(self.tool)