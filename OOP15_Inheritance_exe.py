#lanjutan dari sebelumnya
from OOP15_Inheritance import HeroIntelligent,HeroStrenght

dudung = HeroIntelligent('dudung')
maman = HeroStrenght('maman')

dudung.show_info()
maman.show_info()

dudung.gainExp = 200
maman.gainExp = 250

dudung.show_info()
maman.show_info()