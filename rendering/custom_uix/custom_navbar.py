from kivy.uix.stacklayout import StackLayout
from rendering.styles.css_manager import CSSManager


class CustomNavbar(StackLayout):
	local_styles = {
		'navbar_light': {'canvas_color': (1, 1, 1, 0.8)},
		'navbar_dark': {
			'canvas_colour': (0, 0, 0, 0.8),
			'color': (0,1,0,1)
		}
	}

	def __init__(self, **kwargs):
		super(CustomNavbar, self).__init__(**kwargs)
		self.style_classes = []
		self.css = CSSManager(self)

	def on_load(self, app, window):
		window.bind(on_resize=self.resize)

	def update_styles(self):
		for style_class in self.style_classes:
			for style, value in self.local_styles[style_class].items():
				self.css.add_style(style, value)

	def resize(self, *args):
		print(self.name)
		self.resize_navbar()
		widget_sizes = 0
		gap_widget = None
		extra_widgets_overflow = 0
		for child in self.children:
			try:
				if child.gap_widget:
					gap_widget = child
					continue
			except AttributeError:
				if gap_widget is None:
					extra_widgets_overflow += child.width
				widget_sizes += child.width

		gap_widget_size = self.width - widget_sizes
		if gap_widget_size >= 0:
			gap_widget.width = gap_widget_size
		else:
			# TODO Make the thing here for that drop down navbar
			pass
		print('Gap Widget Width =', self.width, '-', widget_sizes, '=', gap_widget.width)

	def resize_navbar(self):
		self.size = self.parent.width, 50
		self.pos = self.parent.pos[0], self.parent.height - self.height + self.parent.pos[1]
