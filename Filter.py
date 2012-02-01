import sublime, sublime_plugin

class FilterCommand(sublime_plugin.WindowCommand):

    def run(self):
        # open an input box for some user input
        self.window.show_input_panel("Please enter a filter:", '', self.filterText, None, None)
        pass

    def filterText(self, text):
    	fold_regions = []
    	index = 0
        # Get the current active view
    	activeView = self.window.active_view()
        # Find all places where the text can be found
    	for foundRegion in activeView.find_all(text):
    		line = activeView.line(foundRegion)
    		region = sublime.Region(index, line.begin())
    		index = line.end() + 1
    		fold_regions.append(region)

        # Last region will be form last line found to end of file
    	lastRegion = sublime.Region(index, activeView.size())
    	fold_regions.append(lastRegion)

        # Clear selection
    	activeView.sel().clear()

        # Reverse the list of region for folding from end of file
    	fold_regions.reverse()

        # Fold all filtered regions
    	for region in fold_regions:
    		activeView.fold(region)