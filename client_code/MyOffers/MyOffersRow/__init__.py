from ._anvil_designer import MyOffersRowTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MyOffersRow(MyOffersRowTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run when the form opens.

    def delete_row_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.item.delete()
        self.remove_from_parent()

    def show_notes_click(self, **event_args):
        """This method is called when the link is clicked"""
        text = "\nNOTES:\n\n" + self.item['notes']
        alert(text)



