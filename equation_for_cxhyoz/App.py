from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from equation_for_cxhyoz import Reaction
from kivy.properties import StringProperty

class Gui(Widget):
    c = ObjectProperty(None)
    h = ObjectProperty(None)
    o = ObjectProperty(None)

    
    carbondioxide = StringProperty('12')
    oxygen = StringProperty('12')
    water = StringProperty('11')
    lost_to_water = StringProperty('22.607')
    lost_to_CO2 = StringProperty('77.3935')


    def preconditions_check(self):
        c = self.c.text
        h = self.h.text
        o = self.o.text
        
        if(c):
            if(h):
                if(o):
                    c = float(c)
                    h = float(h)
                    o = float(o)

                    reaction = Reaction(c,h,o)
                    output = reaction.balanced_reaction()
                    self.carbondioxide = str(output.get("carbondioxide"))
                    self.oxygen = str(output.get("oxygen"))
                    self.water = str(output.get("water"))
                    self.lost_to_CO2 = str(output.get("lost_to_CO2"))
                    self.lost_to_water = str(output.get("lost_to_water"))

    
class MyApp(App):
    def build(self):
        self.title = "Jesse we need to cook 💀"
        return Gui()

if __name__ == '__main__':
    MyApp().run()
