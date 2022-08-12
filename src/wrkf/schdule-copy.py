import datetime 
# first row represents days of the week, with [0] representing nothing  

# NPR shows
""" 
BBC 
Morning Addition
Left, Right, and Center
Variable
Weekend Addition
Talk LA
Wait Wait... Don't Tell Me
1A
Fresh Air
Ted Radio Hour
Planet Money 
How I Built This
Milk Street Radio 
LA Considered
BBC Outside Source
This American Life
Think 
BBC
All Things Considered
Market Place
The Daily
Today, Explained
Louisiana Considered
Science Friday 
Louisiana Eats!
The Moth 
Radio Lab
Hidden Brain 
On the Media
Out To Lunch 
The Reading Life
Selected Shorts
American Routes
Center Stage
Hootenary Power
"""
schedule =  [['HR',  'M',   'T',   'W',   'TH',  'F',   'SA',  'SU'],
            ['0000', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0030', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0100', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0130', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0200', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0230', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0300', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0330', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0400', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0430', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 'bbc'],
            ['0500', 'ma',  'ma',  'ma',  'ma',  'ma',  'bbc', 'bbc'],
            ['0530', 'ma',  'ma',  'ma',  'ma',  'ma',  'bbc', 'bbc'],
            ['0600', 'ma',  'ma',  'ma',  'ma',  'ma',  'lr&c', 'variable'],
            ['0630', 'ma',  'ma',  'ma',  'ma',  'ma',  'lr&c', 'variable'],
            ['0700', 'ma',  'ma',  'ma',  'ma',  'ma',  'wa', 'variable'],
            ['0730', 'ma',  'ma',  'ma',  'ma',  'ma',  'wa', 'wa'],
            ['0800', 'ma',  'ma',  'ma',  'ma',  'ma',  'wa', 'wa'],
            ['0830', 'ma',  'ma',  'ma',  'ma',  'ma',  'wa', 'wa'], 
            ['0900', 'tl',  'tl',  'tl',  'tl',  'tl',  'wa', 'wa'],
            ['0930', 'tl',  'tl',  'tl',  'tl',  'tl',  'wa', 'wa'],
            ['1000', '1a',  '1a',  '1a',  '1a',  '1a',  'wwdtm', 'pm'],
            ['1030', '1a',  '1a',  '1a',  '1a',  '1a',  'wwdtm', 'hibt'],
            ['1100', 'fa',  'fa',  'fa',  'fa',  'fa',  'trh',  'msr'],
            ['1130', 'fa',  'fa',  'fa',  'fa',  'fa',  'trh',  'msr'],
            ['1200', 'lc',  'lc',  'lc',  'lc',  'lc',  'tal',  'wwdtm'],
            ['1230', 'lc',  'lc',  'lc',  'lc',  'lc',  'tal',  'wwdtm'],
            ['1300', 't',   't',   't',   't',   'sf',  'lae', 'tmrh'],
            ['1330', 't',   't',   't',   't',   'sf',  'lae', 'tmrh'],
            ['1400', 'bbc', 'bbc', 'bbc', 'bbc', 'sf',  'rl', 'tal'],
            ['1430', 'bbc', 'bbc', 'bbc', 'bbc', 'sf', 'rl', 'tam'],
            ['1500', 'atc', 'atc', 'atc', 'atc', 'atc', 'hb', 'otm'],
            ['1530', 'atc', 'atc', 'atc', 'atc', 'atc', 'hb', 'otm'],
            ['1600', 'atc', 'atc', 'atc', 'atc', 'atc', 'atc', 'atc'],
            ['1630', 'atc', 'atc', 'atc', 'atc', 'atc', 'tmrh', 'otl'],
            ['1700', 'atc', 'atc', 'atc', 'atc', 'atc',],
            ['1730', 'atc', 'atc', 'atc', 'atc', 'atc',],
            ['1800', 'atc', 'atc', 'atc', 'atc', 'atc',],
            ['1830', 'mp',  'mp',  'mp',  'mp',  'mp',],
            ['1900'],
            ['1930'],
            ['2000'],
            ['2030'],
            ['2100'],
            ['2130'],
            ['2200'],
            ['2230'],
            ['2300'],
            ['2330']]



date = datetime.datetime.now()

day = date.strftime("%A")
hour = date.strftime("%H")
minute = date.strftime("%M")














